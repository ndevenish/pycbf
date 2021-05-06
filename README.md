# `pycbf` - CBFlib for python

This repository builds the `pycbf` portion of [CBFlib] only, as a
binary wheel installable through `pip install pycbf`.

In order to do this, it has some limitations compared to the full build of CBFlib:

- No HDF5 bindings
- No (custom) libTiff bindings
- No CBF regex capabilities

[cbflib]: https://github.com/yayahjb/cbflib
