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
        img.read_mar345header(f)
        img.read_mar345data(f)


class Mar345Adaptor:
    def __init__(self, filename):
        self.filename = filename

        self._read_header = False
        self._read_data = False
        self._data_position = None
        self._metadata = None
        self._img = Img()
        self._img.set_tags(0)
        self._img.set_dimensions(0, 0)

    def read_header(self):
        if self._read_header:
            return
        with open(self.filename, "rb") as f:
            self._metadata = self._img.read_mar345header(f)
            self._data_position = f.tell()
        detector = self._img.get_field("DETECTOR")
        if "mar" not in detector.lower() or "345" not in detector.lower():
            raise RuntimeError(
                f"Detector type other than mar345 from mar345 reader ({detector})"
            )

    def read_data(self):
        if self._read_data:
            return
        self.read_header()
        with open(self.filename, "rb") as f:
            f.seek(self._data_position)
            self._img.read_mar345data(f, self._metadata)

    def rawdata(self):
        self.read_data()
        raise NotImplementedError

    def columns(self):
        return self._img.columns

    def rows(self):
        return self._img.rows

    def size1(self):
        self.read_header()
        return self._metadata[0]

    def size2(self):
        self.read_header()
        return self._metadata[2]

    def pixel_size(self):
        self.read_header()
        return self._img.get_number("PIXEL SIZE")

    def wavelength(self):
        self.read_header()
        return self._img.get_number("WAVELENGTH")

    def distance(self):
        self.read_header()
        return self._img.get_number("DISTANCE")

    def gain(self):
        return 1.55

    def overload(self):
        # Determined from a single image.
        return 249862

    def osc_range(self):
        self.read_header()
        return self._img.get_number("OSCILLATION RANGE")

    def osc_start(self):
        self.read_header()
        return self._img.get_number("PHI")

    def twotheta(self):
        self.read_header()
        return self._img.get_number("TWOTHETA")

    def exposure_time(self):
        self.read_header()
        return self._img.get_number("EXPOSURE_TIME")


def beam_center_slow(adaptor):
    return adaptor.size1() * adaptor.pixel_size() / 2.0


def beam_center_fast(adaptor):
    return adaptor.size2() * adaptor.pixel_size() / 2.0


def test_adaptor(mar_image):
    mar = Mar345Adaptor(mar_image)

    meta = {
        "SIZE1": mar.size1(),
        "SIZE2": mar.size2(),
        "CCD_IMAGE_SATURATION": mar.overload(),
        "PIXEL_SIZE": mar.pixel_size(),
        "OSC_START": mar.osc_start(),
        "DISTANCE": mar.distance(),
        "WAVELENGTH": mar.wavelength(),
        "BEAM_CENTER_X": beam_center_slow(mar),
        "BEAM_CENTER_Y": beam_center_fast(mar),
        "OSC_RANGE": mar.osc_range(),
        "TWOTHETA": mar.twotheta(),
        "DETECTOR_SN": 0,
    }
