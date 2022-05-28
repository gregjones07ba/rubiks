import unittest

from relative_director import RelativeDirector

from color_direction import *

class TestRelativeDirector(unittest.TestCase):
    def setUp(self):
        self.test_obj = RelativeDirector(vertical=RGB.vector)
    
    def test_back(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, RED.vector)
        self.assertEqual(actual_directions[1], RelativeDirector.Directions.BACK)

if __name__ == '__main__':
    unittest.main()
