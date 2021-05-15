import pycbf

if pycbf.SWIG_PYTHON_STRICT_BYTE_CHAR:
    print("IS STRICT")

    def pycbfstr(string: str) -> bytes:
        """Shim to convert to representation of string natively handled by pycbf"""
        return string.encode()


else:

    def pycbfstr(string: str) -> str:
        """Shim to convert to representation of string natively handled by pycbf"""
        return string


def test_get_local_integer_byte_order():
    assert pycbf.get_local_integer_byte_order() == pycbfstr("little_endian")


def test_get_local_real_byte_order():
    assert pycbf.get_local_real_byte_order() == pycbfstr("little_endian")


def test_get_local_real_format():
    assert pycbf.get_local_real_format() == pycbfstr("ieee 754-1985")


def test_compute_cell_volume():
    assert pycbf.compute_cell_volume((2.0, 3.0, 4.0, 90.0, 90.0, 90.0)) == 24.0
