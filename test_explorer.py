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
        self.rb = rubik.get_cell(2, 0, 0)
        self.rb_r = self.rb.wall_with_direction(RED.vector)
        self.rb_r.description = 'no remarkable features'
        self.rb_r.door = True
        self.rb_g = self.rb.wall_with_direction(GREEN.vector)
        self.rb_g.description = 'a bas relief of a dream phoenix'
        self.rb_b = self.rb.wall_with_direction(BLUE.vector)
        self.rb_b.description = 'a lion statue'
        self.rb_y = self.rb.wall_with_direction(YELLOW.vector)
        self.rb_y.description = 'a bas relief of a sun phoenix'
        self.rb_y.door = True
        self.rbg_octa = rubik.get_cell(1, 1, 1)
        self.rbg_octa_ag = self.rbg_octa.wall_with_direction(ANTI_GREEN.vector)
        self.rby_octa = rubik.get_cell(1, -1, -1)
        self.rby_octa_ay = self.rby_octa.wall_with_direction(ANTI_YELLOW.vector)
        self.rby_octa_ay.door = True
        return rubik

    def test_describe_room_gives_relative_wall_descriptions(self):
        actual_description = self.test_obj.describe()
        actual_left = actual_description[0]
        self.assertEqual(actual_left.relative_directions, [RelativeDirector.Direction.LEFT])
        self.assertEqual(actual_left.description, 'a lion statue')
        actual_right = actual_description[1]
        self.assertEqual(actual_right.relative_directions, [RelativeDirector.Direction.RIGHT])
        self.assertEqual(actual_right.description, 'a bas relief of a dream phoenix')
        actual_back = actual_description[2]
        self.assertEqual(actual_back.relative_directions, [RelativeDirector.Direction.BACK])
        self.assertEqual(actual_back.description, 'no remarkable features')
        self.assertEqual(actual_back.door_state, Rubik.DoorState.DOOR)
        actual_down = actual_description[3]
        self.assertEqual(actual_down.relative_directions, [RelativeDirector.Direction.DOWN])
        self.assertEqual(actual_down.description, 'a bas relief of a sun phoenix')
        self.assertEqual(actual_down.door_state, Rubik.DoorState.DOOR)

    def test_get_options_offers_movement(self):
        self.rb_g.door = True
        self.rbg_octa_ag.door = True
        self.rb_b.door = True
        
        actual_description = self.test_obj.get_options()

        actual_left = actual_description[0]
        self.assertEqual(actual_left.name, "1")
        self.assertEqual(actual_left.option_type, Explorer.Option.OptionType.GO)
        self.assertEqual(actual_left.relative_directions, [RelativeDirector.Direction.LEFT])

        self.assertEqual(len(actual_description), 4)

    def test_get_options_offers_movement_only_through_open_doors(self):
        actual_description = self.test_obj.get_options()

        actual_back = actual_description[0]
        self.assertEqual(actual_back.name, "1")
        self.assertEqual(actual_back.option_type, Explorer.Option.OptionType.GO)
        self.assertEqual(actual_back.relative_directions, [RelativeDirector.Direction.BACK])
        actual_down = actual_description[1]
        self.assertEqual(actual_down.name, "2")
        self.assertEqual(actual_down.option_type, Explorer.Option.OptionType.GO)
        self.assertEqual(actual_down.relative_directions, [RelativeDirector.Direction.DOWN])

        self.assertEqual(len(actual_description), 2)

    def test_executing_go_moves_to_next_room(self):
        options = self.test_obj.get_options()
        self.assertEqual(options[1].relative_directions, [RelativeDirector.Direction.DOWN])
        options[1].execute()
        self.assertEqual(tuple(self.test_obj.location), (1, -1, -1))
        self.assertEqual(tuple(self.test_obj.direction), tuple(ANTI_RED.vector))

    def test_excuting_go_right_moves_and_changes_direction(self):
        self.rb_g.door = True
        self.rbg_octa_ag.door = True

        options = self.test_obj.get_options()
        options[0].execute()

        self.assertEqual(tuple(self.test_obj.direction), tuple(GREEN.vector))
        

if __name__ == '__main__':
    unittest.main()
