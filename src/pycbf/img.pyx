# distutils: sources = cbflib/src/img.c
# distutils: include_dirs = cbflib/include
# cython: c_string_encoding=utf8

# img_set_dimensions
# img_set_tags
from cpython cimport array
from cpython.ref cimport PyObject
from libc.stdio cimport FILE, fdopen, ftell

cimport pycbf.img as img

# img_BAD_ARGUMENT
# img_BAD_OPEN

# img_columns and img_rows are defines
# img_columns
# img_rows

# img_get_number
# img_handle
# img_get_field
# img_read_mar345data
# img_read_mar345header



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

cdef class Img:
    cdef img.img_object * _img_handle;

    def __cinit__(self):
        self._img_handle = img.img_make_handle()

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


    def read_mar345header(self, object fileobject):
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
        return array.array('i', mardata)

    def read_mar345data(self, object fileobject, array.array org_data):
        cdef int fd = PyObject_AsFileDescriptor(fileobject)
        cdef FILE* file = fdopen(fd, "r")
        check_error(
            img.img_read_mar345data(self._img_handle, file, org_data.data.as_ints)
        )

    def set_dimensions(self, int columns, int rows):
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
    def image(self):
        pass

    @property
    def rowmajor(self):
        return self._img_handle.rowmajor
