from pathlib import Path

import pycbf


def test_2():
    obj = pycbf.cbf_handle_struct()
    obj.read_file(str(Path(__file__).parent.parent / "adscconverted.cbf"), 0)
    obj.select_datablock(0)
    g = obj.construct_goniometer()
    print(("Rotation axis is", g.get_rotation_axis()))
    d = obj.construct_detector(0)
    print(("Beam center is", d.get_beam_center()))
