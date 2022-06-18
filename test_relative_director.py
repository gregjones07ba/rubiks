import unittest

from relative_director import RelativeDirector

from color_direction import *

class TestRelativeDirector(unittest.TestCase):
    def setUp(self):
        self.test_obj = RelativeDirector(vertical=RGB.vector)
    
    def test_back(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, RED.vector)
        self.assertEqual(actual_directions[1], RelativeDirector.Direction.BACK)

    def test_forward(self):
        actual_directions = self.test_obj.get_relative_directions(RED.vector, RED.vector)
        self.assertEqual(actual_directions[1], RelativeDirector.Direction.FORWARD)

    def test_left(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, BLUE.vector)
        self.assertEqual(actual_directions[0], RelativeDirector.Direction.LEFT)

    def test_right(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, GREEN.vector)
        self.assertEqual(actual_directions[0], RelativeDirector.Direction.RIGHT)

    def test_down(self):
        actual_directions = self.test_obj.get_relative_directions(ANTI_RED.vector, YELLOW.vector)
        self.assertEqual(actual_directions[2], RelativeDirector.Direction.DOWN)

    def test_up(self):
        actual_directions = self.test_obj.get_relative_directions(RED.vector, ANTI_YELLOW.vector)
        self.assertEqual(actual_directions[2], RelativeDirector.Direction.UP)

    def test_floor_is_not_back_from_red(self):
        actual_directions = self.test_obj.get_relative_directions(RED.vector, YELLOW.vector)
        expected_directions = (None, None, RelativeDirector.Direction.DOWN)
        self.assertEqual(actual_directions, expected_directions)

    def test_floor_is_not_up_or_down_when_vertical_is_horizontal(self):
        self.test_obj.vertical = array((1, 1, -2))
        actual_directions = self.test_obj.get_relative_directions(RED.vector, YELLOW.vector)
        expected_directions = (None, RelativeDirector.Direction.BACK, None)
        self.assertEqual(actual_directions, expected_directions)

    def test_simplify_directions_simplifies_empty_directions(self):
        from_vector = ANTI_RED.vector
        direction_set = set()
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        self.assertEqual(actual_direction_map, {})

    def test_simplify_directions_simplifies_singleton_direction(self):
        from_vector = ANTI_RED.vector
        direction_list = [RED.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(RED.vector): [RelativeDirector.Direction.BACK]
        }
        self.assertEqual(actual_direction_map, expected_direction_map)

    def test_simplify_directions_simplifies_singleton_blue_to_left(self):
        from_vector = ANTI_RED.vector
        direction_list = [BLUE.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(BLUE.vector): [RelativeDirector.Direction.LEFT]
        }
        self.assertEqual(actual_direction_map, expected_direction_map)
        
    def test_simplify_directions_simplifies_yellow_to_down_with_blue(self):
        from_vector = ANTI_RED.vector
        direction_list = [BLUE.vector, YELLOW.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(BLUE.vector): [RelativeDirector.Direction.LEFT],
            tuple(YELLOW.vector): [RelativeDirector.Direction.DOWN]
        }
        self.assertEqual(actual_direction_map, expected_direction_map)
        
    def __vector_keys(self, vector_list):
        return set(self.__vector_key(vector) for vector in vector_list)

    def __vector_key(self, vector):
        return tuple(vector)

    def test_simplify_directions_simplifies_tetrahedron_directions_from_red(self):
        from_vector = ANTI_RED.vector
        direction_list = [RED.vector, BLUE.vector, GREEN.vector, YELLOW.vector]
        direction_set = set(map(tuple, direction_list))
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(RED.vector): [RelativeDirector.Direction.BACK],
            tuple(BLUE.vector): [RelativeDirector.Direction.LEFT],
            tuple(GREEN.vector): [RelativeDirector.Direction.RIGHT],
            tuple(YELLOW.vector): [RelativeDirector.Direction.DOWN]
        }
        self.assertEqual(actual_direction_map, expected_direction_map)

    def test_simplify_directions_simplifies_anti_green_to_forward_right_when_blue_and_anti_blue_present(self):
        from_vector = RED.vector
        direction_list = [ANTI_GREEN.vector, BLUE.vector, ANTI_BLUE.vector]
        direction_set = set(map(tuple, direction_list))
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        self.assertEqual(actual_direction_map[tuple(ANTI_GREEN.vector)],
                          [RelativeDirector.Direction.RIGHT, RelativeDirector.Direction.FORWARD])

    def test_simplify_directions_simplifies_red_to_forward_when_anti_green_and_blue_present(self):
        from_vector = RED.vector
        direction_list = [RED.vector, ANTI_GREEN.vector, BLUE.vector]
        direction_set = set(map(tuple, direction_list))
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        self.assertEqual(actual_direction_map[tuple(RED.vector)],
                          [RelativeDirector.Direction.FORWARD])

    def test_simplify_directions_simplifies_octahedron_directions_from_red(self):
        self.maxDiff = None
        from_vector = RED.vector
        direction_list = [RED.vector, ANTI_GREEN.vector, BLUE.vector, ANTI_RED.vector, GREEN.vector, ANTI_BLUE.vector, ANTI_YELLOW.vector, YELLOW.vector]
        direction_set = set(map(tuple, direction_list))
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(RED.vector): [RelativeDirector.Direction.FORWARD],
            tuple(ANTI_GREEN.vector): [RelativeDirector.Direction.RIGHT, RelativeDirector.Direction.FORWARD],
            tuple(BLUE.vector): [RelativeDirector.Direction.RIGHT, RelativeDirector.Direction.BACK],
            tuple(ANTI_RED.vector): [RelativeDirector.Direction.BACK],
            tuple(GREEN.vector): [RelativeDirector.Direction.LEFT, RelativeDirector.Direction.BACK],
            tuple(ANTI_BLUE.vector): [RelativeDirector.Direction.LEFT, RelativeDirector.Direction.FORWARD],
            tuple(ANTI_YELLOW.vector): [RelativeDirector.Direction.UP],
            tuple(YELLOW.vector): [RelativeDirector.Direction.DOWN]
        }
        self.assertEqual(actual_direction_map, expected_direction_map)
        
if __name__ == '__main__':
    unittest.main()
