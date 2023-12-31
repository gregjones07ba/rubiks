import unittest

from numpy import array

from explorer import Explorer

from rubik import Rubik
from cell import Cell
from color_direction import *
from relative_director import RelativeDirector
from action import Action

class TestExplorer(unittest.TestCase):
    def setUp(self):
        pyraminx = self.__initialize_rubik()
        self.test_obj = Explorer(pyraminx, array((2, 0, 0)), ANTI_RED.vector)

    def __initialize_rubik(self):
        rubik = Rubik(Cell.tetra_factory, Cell.octa_factory)
        self.rb = rubik.get_cell(2, 0, 0)
        self.rb_r = self.rb.wall_with_direction(RED.vector)
        self.rb_r.description = 'no remarkable features'
        self.rb_r.door = True
        self.rb.name = 'rb'
        self.rb_g = self.rb.wall_with_direction(GREEN.vector)
        self.rb_g.description = 'a bas relief of a dream phoenix'
        self.rb_b = self.rb.wall_with_direction(BLUE.vector)
        self.rb_b.description = 'a lion statue'
        self.rb_y = self.rb.wall_with_direction(YELLOW.vector)
        self.rb_y.description = 'a bas relief of a sun phoenix'
        self.rb_y.door = True
        self.rgb_octa = rubik.get_cell(1, 1, 1)
        self.rgb_octa_ag = self.rgb_octa.wall_with_direction(ANTI_GREEN.vector)
        self.rgb_octa_ay = self.rgb_octa.wall_with_direction(ANTI_YELLOW.vector)
        self.rgb_octa_y = self.rgb_octa.wall_with_direction(YELLOW.vector)
        self.rgb_octa_y.description = 'a mosaic of a merman'
        self.rgb_octa_r = self.rgb_octa.wall_with_direction(RED.vector)
        self.rgb_octa_r.description = 'a fresco of a tree'
        self.rby_octa = rubik.get_cell(1, -1, -1)
        self.rby_octa_ay = self.rby_octa.wall_with_direction(ANTI_YELLOW.vector)
        self.rby_octa_ay.door = True
        self.rgb = rubik.get_cell(2, 2, 2)
        self.rgb_y = self.rgb.wall_with_direction(YELLOW.vector)
        self.rgb_y.door = True
        self.rgb.custom_actions.append(Action("rotate", lambda: rubik.rotate(0)))
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
        self.rgb_octa_ag.door = True
        self.rb_b.door = True
        
        actual_description = self.test_obj.get_options()

        actual_left = actual_description[0]
        self.assertEqual(actual_left.name, "1")
        self.assertEqual(actual_left.option_type, Explorer.Option.OptionType.GO)
        self.assertEqual(actual_left.relative_directions, [RelativeDirector.Direction.LEFT])

        self.assertEqual(len(actual_description), 8)

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

        self.assertEqual(len(actual_description), 6)

    def test_executing_go_moves_to_next_room(self):
        options = self.test_obj.get_options()
        self.assertEqual(options[1].relative_directions, [RelativeDirector.Direction.DOWN])
        options[1].execute()
        self.assertEqual(tuple(self.test_obj.location), (1, -1, -1))
        self.assertEqual(tuple(self.test_obj.direction), tuple(ANTI_RED.vector))

    def test_executing_go_right_moves_and_changes_direction(self):
        self.rb_g.door = True
        self.rgb_octa_ag.door = True

        options = self.test_obj.get_options()
        self.assertEqual(options[0].relative_directions, [RelativeDirector.Direction.RIGHT])
        options[0].execute()

        self.assertEqual(tuple(self.test_obj.direction), tuple(GREEN.vector))

    def test_executing_go_up_doesnt_change_direction(self):
        self.rb_g.door = True
        self.rgb_octa_ag.door = True
        self.rgb_octa_ay.door = True
        
        options = self.test_obj.get_options()
        self.assertEqual(options[0].relative_directions, [RelativeDirector.Direction.RIGHT])
        options[0].execute()

        options = self.test_obj.get_options()
        self.assertEqual(options[1].relative_directions, [RelativeDirector.Direction.UP])
        options[1].execute()

        self.assertEqual(tuple(self.test_obj.direction), tuple(GREEN.vector))

    def test_offers_custom_option(self):
        self.rb_g.door = True
        self.rgb_octa_ag.door = True
        self.rgb_octa_ay.door = True
        
        options = self.test_obj.get_options()
        self.assertEqual(options[0].relative_directions, [RelativeDirector.Direction.RIGHT])
        options[0].execute()

        options = self.test_obj.get_options()
        self.assertEqual(options[1].relative_directions, [RelativeDirector.Direction.UP])
        options[1].execute()

        options = self.test_obj.get_options()
        self.assertEqual(options[5].option_type, Explorer.Option.OptionType.CUSTOM)
        self.assertEqual(options[5].name, "6")
        self.assertEqual(options[5].description, "rotate")
        options[5].execute()

        options = self.test_obj.get_options()
        self.assertEqual(options[0].relative_directions, [RelativeDirector.Direction.DOWN])
        options[0].execute()

        options = self.test_obj.get_options()
        self.assertEqual(options[0].relative_directions, [RelativeDirector.Direction.RIGHT, RelativeDirector.Direction.FORWARD])

    def test_locate_gives_friendly_location(self):
        location = self.test_obj.locate()
        self.assertEqual(location, (-1, 0, 1))

    def test_name_gives_cell_name_at_location(self):
        name = self.test_obj.name()
        self.assertEqual(name, 'rb')

    def test_direct_gives_friendly_direction(self):
        dir = self.test_obj.direct()
        self.assertEqual(dir, "ANTI-RED")

    def test_direct_gives_different_direction_after_turn(self):
        self.rb_g.door = True
        self.rgb_octa_ag.door = True
        options = self.test_obj.get_options()
        options[0].execute()
        dir = self.test_obj.direct()
        self.assertEqual(dir, "GREEN")

    def test_get_options_offers_look(self):
        self.rb_g.door = True
        self.rgb_octa_ag.door = True
        self.rb_b.door = True
        
        actual_options = self.test_obj.get_options()

        actual_look_right = actual_options[5]
        self.assertEqual(actual_look_right.name, "6")
        self.assertEqual(actual_look_right.option_type, Explorer.Option.OptionType.LOOK)
        self.assertEqual(actual_look_right.relative_directions, [RelativeDirector.Direction.RIGHT])

        next_room_description = actual_look_right.execute()

        self.assertEqual(tuple(self.test_obj.direction), tuple(GREEN.vector))
        
        next_room_down = next_room_description[7]
        self.assertEqual(next_room_down.relative_directions, [RelativeDirector.Direction.DOWN])
        self.assertEqual(next_room_down.description, 'a mosaic of a merman')

        next_room_right = next_room_description[3]
        self.assertEqual(next_room_right.relative_directions, [RelativeDirector.Direction.RIGHT, RelativeDirector.Direction.BACK])
        self.assertEqual(next_room_right.description, 'a fresco of a tree')
        
        self.assertEqual(len(actual_options), 8)

    def test_get_options_offers_look_to_face_wall_without_door(self):
        self.rb_g.door = True
        self.rb_b.door = True
        
        actual_options = self.test_obj.get_options()

        actual_look_right = actual_options[4]
        self.assertEqual(actual_look_right.name, "5")
        self.assertEqual(actual_look_right.option_type, Explorer.Option.OptionType.LOOK)
        self.assertEqual(actual_look_right.relative_directions, [RelativeDirector.Direction.RIGHT])

        next_room_description = actual_look_right.execute()

        self.assertEqual(tuple(self.test_obj.direction), tuple(GREEN.vector))
        
        next_room_right = next_room_description[2]
        self.assertEqual(next_room_right.relative_directions, [RelativeDirector.Direction.FORWARD])
        self.assertEqual(next_room_right.description, 'a bas relief of a dream phoenix')
        
        self.assertEqual(len(actual_options), 7)
       
if __name__ == '__main__':
    unittest.main()
