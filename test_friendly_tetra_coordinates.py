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

if __name__ == '__main__':
    unittest.main()
