#cython: language_level=3

from libc.stdio cimport FILE


cdef extern from "cbflib/include/img.h":
    ctypedef struct img_object:
        pass

    img_object *img_make_handle()
    int img_free_handle(img_object* img)

    int img_swap_i4(int i4)
    float img_float_i4(int i4, int VAX)
    int img_read_i4(FILE *file, int *i4)
    int img_read_smvheader(img_object * img, FILE *file)
    int img_read_smvdata(img_object * img, FILE *file)
    int img_read_smv(img_object * img, const char *name)
    int img_write_smv(img_object *img, const char *name, unsigned int bits)
    int img_read_mar300header(img_object * img, FILE *file, int *org_data)
    int img_read_mar300data(img_object * img, FILE *file, int *org_data)
    int img_read_mar300(img_object * img, const char *name)
    int img_read_mar345header(img_object * img, FILE *file, int *org_data)
    int img_read_mar345data(img_object * img, FILE *file, int *org_data)
    int img_read_mar345(img_object * img, const char *name)
    int img_get_tags(img_object * img)
    int img_delete_fieldnumber(img_object * img, int x)

    int img_read(img_object * img, const char *name)
    int img_delete_field(img_object * img, const char *tag)
    const char *img_get_field(img_object * img, const char *tag)
    int img_get_next_field(img_object * img, const char **tag, const char **data,
                        int *index)
    int img_set_field(img_object * img, const char *tag, const char *data)
    double img_get_number(img_object * img, const char *tag)
    int img_set_number(img_object * img, const char *tag, const char *format,
                    double data)
    int img_get_pixel(img_object * img, int x, int y)
    int img_set_pixel(img_object * img, int x, int y, int data)
    int img_set_dimensions(img_object * img, int columns, int rows)
    int img_get_dimension(img_object * img, int dimension)