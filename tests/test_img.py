from pathlib import Path

import pytest

from pycbf.img import Img


def test_create_handle():
    Img()


def test_no_field():
    i = Img()
    with pytest.raises(KeyError):
        i.get_field("Name")


def test_get_number():
    i = Img()
    assert i.get_number("sadasdasd") == 0.0


@pytest.fixture
def mar_image():
    # return (
    #     dials_data("image_examples", pathlib=True)
    #     / "DESY_BW7B"
    #     / "mar345_01_001.mar2300"
    # )
    mar_image_locations = [
        "/dls/science/groups/scisoft/DIALS/repositories/git-reference/dials_regression/image_examples/DESY_BW7B/mar345_01_001.mar2300",
        "/Users/nickd/dials/regression/dials_regression/image_examples/DESY_BW7B/mar345_01_001.mar2300",
    ]
    for path in mar_image_locations:
        if Path(path).is_file():
            return path
    pytest.skip("No mar345 file found")


def test_regression_image(mar_image):
    with open(mar_image, "rb") as f:
        img = Img()
        hi = img.read_mar345header(f)
        img.read_mar345data(f, hi)


def test_image_reading(mar_image):
    # Currently, problems building numpy on mac-arm, so don't require
    np = pytest.importorskip("numpy")

    img = np.asarray(Img.read_mar345(mar_image))
    assert img.shape == (2300, 2300)
    assert img[img == 0].sum() == 1131017
