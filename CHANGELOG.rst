Pycbf 0.9.6.5 (2022-03-23)
==========================

Bugfixes
--------

- Fix incorrect sdist packaging. (#22)


Pycbf 0.9.6.4 (2022-03-22)
==========================

Features
--------

- Use dials-data release for test data, instead of experimental branch. (#17)
- Added PEP-484 type hints for ``pycbf.Img``, and mark as typing-compatible. (#20)
- Windows is now a supported target. (#21)


Misc
----

- #18


Pycbf 0.9.6.3 (2021-05-26)
==========================

Bugfixes
--------

- Prevent source files from being scattered across site-packages (#14)


pycbf 0.9.6.2 (2021-05-18)
==========================

Features
--------

- Added initial bindings for ``libimg``. Only the methods required for minimal mar345 image reading have been implemented. (#1)
- Add python bindings ``read_buffer`` for ``cbf_read_buffered_file``, for loading files directly from bytes buffers. (#3)
- Functions that accept string arguments will now accept both ``bytes`` and ``str``, for easier transition away from ``SWIG_PYTHON_BYTE_CHAR``. (#4)
- The ``pycbf.cbf2str`` utility function has been added to convert CBF string returns to str, no matter what is used in the SWIG bindings. (#4)
- Add ``pycbf.HAS_SWIG_PYTHON_STRICT_BYTE_CHAR``, to tell if the module has been build with the ``SWIG_PYTHON_STRICT_BYTE_CHAR`` compile definition. (#10)


Deprecations and Removals
-------------------------

- Drop support for Python 2.7 (#5)
- Regeneration via nuweb literate sources is removed. The generated sources are now used as the original versions, which makes it much easier to add changes without building up stacks of patches. (#9)


Misc
----

- `dials-data <https://github.com/dials/data>`_ is now used for regression test data. (#6)
- A convenience script, ``make_release.sh``, has been added to aid release generation. (#11)


pycbf 0.9.6.1
=============

This was an unreleased internal commit.


pycbf 0.9.6.0 (2021-05-06)
==========================

- Regenerated SWIG bindings for Python 3 compatibility
- Compiled with `SWIG_PYTHON_STRICT_BYTE_CHAR`
- Initial release of separated pycbf from CBFlib

