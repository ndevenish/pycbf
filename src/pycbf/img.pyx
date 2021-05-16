# distutils: sources = cbflib/src/img.c
# distutils: include_dirs = cbflib/include
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# cython: c_string_encoding=utf8

import os
# img_set_dimensions
# img_set_tags
import sys

cimport cpython.buffer as buf
from cpython cimport Py_buffer
from cpython.ref cimport PyObject
from libc.stdio cimport FILE, fdopen, ftell

cimport pycbf.img as img

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

cdef extern from "Python.h":
    int PyObject_AsFileDescriptor(object fileobject) except -1

cdef check_error(int err):
    if err == 0:
        return
    elif err == ImageError.BAD_ARGUMENT:
        raise ValueError
    elif err == ImageError.BAD_ALLOC:
        raise MemoryError
    elif err == ImageError.BAD_OPEN:
        raise IOError("Bad open")
    elif err == ImageError.BAD_READ:
        raise IOError("Bad read")
    elif err == ImageError.BAD_FORMAT:
        raise RuntimeError("Bad Format")
    elif err == ImageError.BAD_FIELD:
        raise KeyError("Bad field")
    elif err == ImageError.BAD_WRITE:
        raise IOError("Bad Write")

cdef class ImageData:
    """Image Data class to help with refcounting the image array"""
    cdef Img image_container
    cdef img.img_object * _img_handle
    cdef Py_ssize_t shape[2]
    cdef Py_ssize_t strides[2]

    def __cinit__(self, Img image_container):
        self.image_container = image_container
        self._img_handle = image_container._img_handle


    def __getbuffer__(self, Py_buffer *buffer, int flags):
        # rows
        self.shape[0] = self._img_handle.size[1]
        self.strides[0] = sizeof(int)*self.shape[1]
        # cols
        self.shape[1] = self._img_handle.size[0]
        self.strides[1] = sizeof(int)

        # Note: self is automatically incref'd by cython
        buffer.obj = self
        buffer.buf = self._img_handle.image
        buffer.len = self.shape[0] * self.shape[1] * sizeof(int)
        buffer.itemsize = sizeof(int)
        buffer.ndim = 2

        buffer.format = "i"
        buffer.readonly = 0
        buffer.shape = self.shape
        buffer.strides = NULL
        # self.strides
        buffer.suboffsets = NULL
        self.image_container.active_views += 1

        print("Increasing ID to:", sys.getrefcount(self))
        print("Active Views:   ", self.image_container.active_views)

    def __releasebuffer__(self, Py_buffer *buffer):
        self.image_container.active_views -= 1
        print("Decref Active Views: ", self.image_container.active_views)

cdef class Img:
    cdef img.img_object * _img_handle;
    cdef int _active_views

    def __cinit__(self):
        self._img_handle = img.img_make_handle()
        self._active_views = 0

    def __dealloc__(self):
        if self._img_handle is not NULL:
            img.img_free_handle(self._img_handle)

    def get_field(self, str name):
        cdef const char * ret = img_get_field(self._img_handle, name);
        if ret == NULL:
            raise KeyError("No field named " + name)
        return ret.decode()

    def get_number(self, str name):
        return img.img_get_number(self._img_handle, name)

    @classmethod
    def read_mar345(cls, object filename):
        img = Img()
        strpath = os.fspath(filename)
        cdef char *filen = strpath
        check_error(img_read_mar345(img._img_handle, strpath))

    def read_mar345header(self, object fileobject):
        # Make sure that we don't rewire memory while references are handed out
        if self._active_views > 0:
            raise ValueError("Cannot reload data: There are unfreed references to the image data")
        cdef int mardata[4];
        cdef int fd = PyObject_AsFileDescriptor(fileobject)
        cdef FILE* file = fdopen(fd, "r")
        check_error(
            img.img_read_mar345header(self._img_handle, file, mardata)
        )
        # Restore the tell position - for some reason, on some versions
        # of python, the python fileobject changes 2 bytes for every byte
        # - Since the code we are replacing explicitly winds the file
        # back to the .tell() position, make that work here.
        fileobject.seek(ftell(file))
        return tuple(mardata)

    def read_mar345data(self, object fileobject, object org_data):
        # Make sure that we don't rewire memory while references are handed out
        if self._active_views > 0:
            raise ValueError("Cannot reload data: There are unfreed references to the image data")
        if len(org_data) != 4:
            raise ValueError("org_data appears to be in incorrect form for header data")
        cdef int[4] mardata = org_data
        cdef int fd = PyObject_AsFileDescriptor(fileobject)
        cdef FILE* file = fdopen(fd, "r")
        check_error(
            img.img_read_mar345data(self._img_handle, file, mardata)
        )

    def set_dimensions(self, int columns, int rows):
        if self._active_views > 0:
            raise ValueError("Cannot resize data: There are unfreed references to the image data")
        check_error(img.img_set_dimensions(self._img_handle, columns, rows))

    def set_tags(self, int number):
        check_error(img.img_set_tags(self._img_handle, number))

    @property
    def rows(self):
        return self._img_handle.size[1]

    @property
    def columns(self):
        return self._img_handle.size[0]

    @property
    def rowmajor(self):
        return self._img_handle.rowmajor

    def active_views(self):
        return self.active_views

    @property
    def fields(self):
        tags = {}
        cdef int index = 0
        cdef char *tag, *data;
        while img_get_next_field(self._img_handle, &tag, &data, &index) != ImageError.BAD_ARGUMENT:
            tags[tag.decode()] = data.decode()

        return tags

    @property
    def image(self):
        """Return the raw image data array pointer"""
        if self._img_handle.image == NULL:
            raise RuntimeError("No image data - cannot generate image data")
            return None
        if np == None:
            raise ImportError("Missing runtime dependency numpy - cannot generate image arrays")

        assert not self._img_handle.rowmajor, "Rowmajor appears only used with SMV?"

        # Work out the proper way to convert this data e.g. orientation:
        # Internally between flex/libimg:
        #       size1 == img_org_data[0] == cols, size2 == img_org_data[1] == rows
        # We constructed a flex array from:
        #       af::flex_int z(af::flex_grid<>((long)size1(), (long)size2()));
        # And wrote to the 2d-ized flex array with:
        #       begin[r * side + c] = img->image[r * side + c];
        # And inside libimg get_pixel(r, c):
        #       return img->image[r * img->size[1] + c];
        # Flex itself uses the lookup all[1, 2] => (r, c) / (row, col) ->:
        #        return r * all_[1] + c;

        # e.g....
        # rowmajor = False: Normal c-style e.g. what's normally called _Row Major_
        #   [[0,1,2],
        #    [3,4,5],
        #    [6,7,8]]
        # i.e. what the default numpy is. This matches flex, so we should
        # be able to convert without an issue.

        # cdef np.npy_intp shape[2];
        shape = (self._img_handle.size[1], self._img_handle.size[0])
        # shape[0] = self._img_handle.size[1]
        # shape[1] =  self._img_handle.size[0]
        print("Getting image")
        cdef int i = 0
        for y in range(3):
            for x in range(shape[0]):
                print("Setting", x, y, i)
                self._img_handle.image[y * self._img_handle.size[0] + x] = i
                i += 1

        print("ref", sys.getrefcount(self))
        imd = ImageData(self)

        return np.asarray(imd)
