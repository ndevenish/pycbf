from pathlib import Path

import pycbf
import pytest

DATA_DIR = Path(__file__).parent.parent / "data"


def test_2():
    cbf = pycbf.cbf_handle_struct()
    cbf.read_file(str(DATA_DIR / "adscconverted.cbf"), 0)
    cbf.select_datablock(0)
    g = cbf.construct_goniometer()
    print(("Rotation axis is", g.get_rotation_axis()))
    d = cbf.construct_detector(0)
    print(("Beam center is", d.get_beam_center()))

def test2_asbytefilename():
    cbf = pycbf.cbf_handle_struct()
    cbf.read_file(str(DATA_DIR / "adscconverted.cbf").encode(), 0)
    cbf.select_datablock(0)
    g = cbf.construct_goniometer()
    print(("Rotation axis is", g.get_rotation_axis()))
    assert g.get_rotation_axis() == pytest.approx([1, 0, 0])
    d = cbf.construct_detector(0)
    print(("Beam center is", d.get_beam_center()))
    assert d.get_beam_center() == pytest.approx([1535.5, 1535.5, 157.52387, -157.52387])
