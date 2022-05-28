import unittest

from relative_director import RelativeDirector

from color_direction import *

class TestRelativeDirector(unittest.TestCase):
    def setUp(self):
        self.test_obj = RelativeDirector(vertical=RGB.vector)
    
    def test_back(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, RED.vector)
        self.assertEqual(actual_directions[1], RelativeDirector.Directions.BACK)

    def test_forward(self):
        actual_directions = self.test_obj.get_relative_directions(RED.vector, RED.vector)
        self.assertEqual(actual_directions[1], RelativeDirector.Directions.FORWARD)

    def test_left(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, BLUE.vector)
        self.assertEqual(actual_directions[0], RelativeDirector.Directions.LEFT)

    def test_right(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, GREEN.vector)
        self.assertEqual(actual_directions[0], RelativeDirector.Directions.RIGHT)

    def test_down(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, YELLOW.vector)
        self.assertEqual(actual_directions[2], RelativeDirector.Directions.DOWN)

    def test_up(self):
        actual_directions = self.test_obj.get_relative_directions(RED.vector, ANTI_YELLOW.vector)
        self.assertEqual(actual_directions[2], RelativeDirector.Directions.UP)

    def test_simplify_directions_simplifies_empty_directions(self):
        from_vector = ANTI_RED.vector
        direction_set = set()
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        self.assertEquals(actual_direction_map, {})

    def test_simplify_directions_simplifies_singleton_direction(self):
        from_vector = ANTI_RED.vector
        direction_list = [RED.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(RED.vector): RelativeDirector.Directions.BACK
        }
        self.assertEquals(actual_direction_map, expected_direction_map)

    def __vector_keys(self, vector_list):
        return set(self.__vector_key(vector) for vector in vector_list)

    def __vector_key(self, vector):
        return tuple(vector)

    # def test_simplify_directions_simplifies_tetrahedron_directions_from_red(self):
    #     from_vector = ANTI_RED.vector
    #     direction_list = [RED.vector, BLUE.vector, GREEN.vector, YELLOW.vector]
    #     direction_set = set(map(tuple, direction_list))
    #     actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
    #     expected_direction_map = {
    #         tuple(RED.vector): RelativeDirector.Directions.BACK,
    #         tuple(BLUE.vector): RelativeDirector.Directions.LEFT,
    #         tuple(GREEN.vector): RelativeDirector.Directions.GREEN,
    #         tuple(YELLOW.vector): RelativeDirector.Directions.DOWN
    #     }
    #     self.assertEquals(actual_direction_map, expected_direction_map)

if __name__ == '__main__':
    unittest.main()
