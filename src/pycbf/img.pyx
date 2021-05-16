# distutils: sources = cbflib/src/img.c
# distutils: include_dirs = cbflib/include
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# cython: c_string_encoding=utf8

import os
import sys

cimport cpython.buffer as buf
from cpython cimport Py_buffer
from cpython.object cimport PyObject_AsFileDescriptor
from cpython.ref cimport PyObject
from libc.stdio cimport FILE, fdopen, ftell

cimport pycbf.img as img

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

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

cdef class Img:
    cdef img.img_object * _img_handle;
    cdef int _active_views
    cdef Py_ssize_t shape[2]
    cdef Py_ssize_t strides[2]

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
        return img

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
        return self._active_views

    @property
    def fields(self):
        tags = {}
        cdef int index = 0
        cdef const char *tag
        cdef const char *data
        while img_get_next_field(self._img_handle, &tag, &data, &index) != ImageError.BAD_ARGUMENT:
            tags[tag.decode()] = data.decode()

        return tags

    @property
    def image(self):
        """Return the image data"""
        if self._img_handle.image == NULL:
            raise RuntimeError("No image data - cannot generate image data")
        if np == None:
            raise ImportError("Missing numpy. You can access image data as a memoryview.")

        return np.asarray(self)

    def __getbuffer__(self, Py_buffer *buffer, int flags):
        if self._img_handle.image == NULL:
            raise RuntimeError("No image data yet - cannot generate image data")
        assert not self._img_handle.rowmajor, "Rowmajor appears only used with SMV?"

        # Internally between flex/libimg:
        #       size1 == img_org_data[0] == cols, size2 == img_org_data[1] == rows
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
        buffer.suboffsets = NULL

        self._active_views += 1
        # print("Active Views:   ", self._active_views)

    def __releasebuffer__(self, Py_buffer *buffer):
        self._active_views -= 1
        # print("Decref Active Views: ", self._active_views)