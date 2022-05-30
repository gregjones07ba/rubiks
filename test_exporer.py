import unittest

from explorer import Explorer

from rubik import Rubik
from cell import Cell
from color_direction import *
from relative_director import RelativeDirector

class TestExplorer(unittest.TestCase):
    def setUp(self):
        pyraminx = self.__initialize_rubik()
        self.test_obj = Explorer(pyraminx, (2, 0, 0), ANTI_RED.vector)

    def __initialize_rubik(self):
        rubik = Rubik(Cell.tetra_factory, Cell.octa_factory)
        rb = rubik.get_cell(2, 0, 0)
        rb_r = rb.wall_with_direction(RED.vector)
        rb_r.description = 'no remarkable features'
        rb_r.door = True
        rb_g = rb.wall_with_direction(GREEN.vector)
        rb_g.description = 'a bas relief of a dream phoenix'
        rb_b = rb.wall_with_direction(BLUE.vector)
        rb_b.description = 'a lion statue'
        rb_y = rb.wall_with_direction(YELLOW.vector)
        rb_y.description = 'a bas relief of a sun phoenix'
        return rubik

    def test_describe_room_gives_relative_wall_descriptions(self):
        actual_description = self.test_obj.describe()
        actual_left = actual_description[0]
        self.assertEqual(actual_left.relative_directions, [RelativeDirector.Directions.LEFT])
        self.assertEqual(actual_left.description, 'a lion statue')
        actual_right = actual_description[1]
        self.assertEqual(actual_right.relative_directions, [RelativeDirector.Directions.RIGHT])
        self.assertEqual(actual_right.description, 'a bas relief of a dream phoenix')
        actual_back = actual_description[2]
        self.assertEqual(actual_back.relative_directions, [RelativeDirector.Directions.BACK])
        self.assertEqual(actual_back.description, 'no remarkable features')
        self.assertEqual(actual_back.door_state, Rubik.DoorState.DOOR)
        actual_down = actual_description[3]
        self.assertEqual(actual_down.relative_directions, [RelativeDirector.Directions.DOWN])
        self.assertEqual(actual_down.description, 'a bas relief of a sun phoenix')

if __name__ == '__main__':
    unittest.main()
