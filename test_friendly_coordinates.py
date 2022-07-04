import unittest

from numpy import array

from friendly_coordinates import FriendlyCoordinates

class TestFriendlyCoordinates(unittest.TestCase):
    def setUp(self):
        self.test_obj = FriendlyCoordinates(
            vertical = array((1.0/3.0, 1.0/3.0, 1.0/3.0)),
            vertical_offset = 1.0,
            depth = array((-1.0/3.0, -1.0/3.0, 1.0/3.0)),
            depth_offset = 1.0,
            horizontal = array((-1.0/2.0, 1.0/2.0, 0.0)),
            horizontal_offset = 0.0
        )

    def test_friendly_coords_returns_2_0_0_for_rgy(self):
        location = array((-2, 2, -2))
        actual_coords = self.test_obj.friendly_coords(location)
        expected_coords = (2, 0, 0)
        self.assertEquals(actual_coords, expected_coords)

if __name__ == '__main__':
    unittest.main()
