import unittest

from numpy import array

from friendly_tetra_coordinates import FriendlyTetraCoordinates

class TestFriendlyTetraCoordinates(unittest.TestCase):
    def setUp(self):
        self.test_obj = FriendlyTetraCoordinates()

    def test_friendly_coords_returns_2_0_0_for_rgy(self):
        location = array((-2, 2, -2))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (2, 0, 0)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_0_0_2_for_rgb(self):
        location = array((2, 2, 2))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (0, 0, 2)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_n2_0_0_for_rby(self):
        location = array((2, -2, -2))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (-2, 0, 0)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_0_0_1_for_rgb_tetra(self):
        location = array((1, 1, 1))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (0, 0, 1)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_n1_0_0_for_rby_tetra(self):
        location = array((1, -1, -1))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (-1, 0, 0)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_0_2_0_for_gby(self):
        location = array((-2, -2, 2))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (0, 2, 0)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_0_1_0_for_gby_tetra(self):
        location = array((-1, -1, 1))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (0, 1, 0)
        self.assertEquals(actual_coords, expected_coords)

    def test_friendly_coords_returns_n1_1_0_for_by(self):
        location = array((0, -2, 0))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (-1, 1, 0)
        self.assertEquals(actual_coords, expected_coords)

if __name__ == '__main__':
    unittest.main()
