import re
from distutils.core import Extension
from pathlib import Path, PurePath
from typing import Any, Dict

# import skbuild
# import skbuild.constants

extensions = [
    Extension(
        "pycbf._cbflib",
        sources=["pycbf_wrap.c"],
        include_dirs=[str(PurePath(__file__).parent / "cbflib" / "include")],
    )
]


def build(setup_kwargs: Dict[str, Any]) -> None:
    # print("Build C Extensions Here")
    # Rewrite the cbf.h file to not require hdf5

    # Rewrite cbf.h so that it doesn't require HDF5.h (it doesn't need it)
    cbf_h = Path(__file__).parent.joinpath("cbflib", "include", "cbf.h")
    cbf_h_data = cbf_h.read_bytes()
    cbf_h_data_rw = re.sub(
        b'^#include "hdf5.h"', b'// #include "hdf5.h"', cbf_h_data, flags=re.MULTILINE
    )
    if cbf_h_data != cbf_h_data_rw:
        cbf_h.write_bytes(cbf_h_data_rw)

    setup_kwargs.update({"ext_modules": extensions})


if __name__ == "__main__":
    build()
