# distutils: sources = cbflib/src/img.c
# distutils: include_dirs = cbflib/include

cimport img

# img_BAD_ARGUMENT
# img_BAD_OPEN

# img_columns and img_rows are defines
# img_columns
# img_rows

# img_get_field
# img_get_number
# img_handle
# img_org_data
# img_read_mar
# img_set_dimensions
# img_set_tags


cdef class Img:
    cdef img.img_object * _img_handle;

    def __cinit__(self):
        self._img_handle = img.img_make_handle()

    def __dealloc__(self):
        if self._img_handle is not NULL:
            img.img_free_handle(self._img_handle)

    def get_field(self, str name):
        return img_get_field(self._img_handle, name)

    # cpdef img_object * _img_make_handle():
    #     return img.img_make_handle()