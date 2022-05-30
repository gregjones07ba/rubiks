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
            tuple(RED.vector): [RelativeDirector.Directions.BACK]
        }
        self.assertEquals(actual_direction_map, expected_direction_map)

    def test_simplify_directions_simplifies_singleton_blue_to_left(self):
        from_vector = ANTI_RED.vector
        direction_list = [BLUE.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(BLUE.vector): [RelativeDirector.Directions.LEFT]
        }
        self.assertEquals(actual_direction_map, expected_direction_map)
        
    def test_simplify_directions_simplifies_yellow_to_down_with_blue(self):
        from_vector = ANTI_RED.vector
        direction_list = [BLUE.vector, YELLOW.vector]
        direction_set = self.__vector_keys(direction_list)
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        expected_direction_map = {
            tuple(BLUE.vector): [RelativeDirector.Directions.LEFT],
            tuple(YELLOW.vector): [RelativeDirector.Directions.DOWN]
        }
        self.assertEquals(actual_direction_map, expected_direction_map)
        
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
            tuple(RED.vector): [RelativeDirector.Directions.BACK],
            tuple(BLUE.vector): [RelativeDirector.Directions.LEFT],
            tuple(GREEN.vector): [RelativeDirector.Directions.RIGHT],
            tuple(YELLOW.vector): [RelativeDirector.Directions.DOWN]
        }
        self.assertEquals(actual_direction_map, expected_direction_map)

    def test_simplify_directions_simplifies_anti_green_to_forward_right_when_blue_and_anti_blue_present(self):
        from_vector = RED.vector
        direction_list = [ANTI_GREEN.vector, BLUE.vector, ANTI_BLUE.vector]
        direction_set = set(map(tuple, direction_list))
        actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
        self.assertEquals(actual_direction_map[tuple(ANTI_GREEN.vector)],
                          [RelativeDirector.Directions.RIGHT, RelativeDirector.Directions.FORWARD])

    # def test_simplify_directions_simplifies_octahedron_directions_from_antired(self):
    #     from_vector = RED.vector
    #     direction_list = [RED.vector, ANTI_GREEN.vector, BLUE.vector, ANTI_RED.vector, GREEN.vector, ANTI_BLUE.vector, ANTI_YELLOW.vector, YELLOW.vector]
    #     direction_set = set(map(tuple, direction_list))
    #     actual_direction_map = self.test_obj.simplify_directions(from_vector, direction_set)
    #     expected_direction_map = {
    #         tuple(RED.vector): [RelativeDirector.Directions.FORWARD],
    #         tuple(ANTI_GREEN.vector): [RelativeDirector.Directions.RIGHT, RelativeDirector.Directions.FORWARD],
    #         tuple(BLUE.vector): [RelativeDirector.Directions.RIGHT, RelativeDirector.Directions.BACK],
    #         tuple(ANTI_RED.vector): [RelativeDirector.Directions.BACK],
    #         tuple(GREEN.vector): [RelativeDirector.Directions.LEFT, RelativeDirector.Directions.BACK],
    #         tuple(ANTI_BLUE.vector): [RelativeDirector.Directions.LEFT, RelativeDirector.Directions.FORWARD],
    #         tuple(ANTI_YELLOW.vector): [RelativeDirector.Directions.UP],
    #         tuple(YELLOW.vector): [RelativeDirector.Directions.DOWN]
    #     }
    #     self.assertEquals(actual_direction_map, expected_direction_map)
        
if __name__ == '__main__':
    unittest.main()
