import unittest

from numpy import array

from rubik import Rubik
from cell import Cell

from color_direction import *

class TestRubik(unittest.TestCase):
    def setUp(self):
        self.test_obj = Rubik(Cell.tetra_factory, Cell.octa_factory)
    
    def test_rotate_rgb(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = "gb"
        rb = self.test_obj.get_cell(2, 0, 0)
        rb.walls[0].description = "rb"
        rg = self.test_obj.get_cell(0, 2, 0)
        rg.walls[0].description = "rg"
        gby = self.test_obj.get_cell(-2, -2, 2)
        gby.walls[0].description = "gby"
        center = self.test_obj.get_cell(0, 0, 0)
        center.walls[0].description = "center"
        rgb_octa = self.test_obj.get_cell(1, 1, 1)
        rgb_octa.walls[0].description = "rgb_octa"
        rgb = self.test_obj.get_cell(2, 2, 2)
        rgb.walls[0].description = "rgb"
        gby_octa = self.test_obj.get_cell(-1, -1, 1)
        gby_octa.walls[0].description = "gby_octa"
        
        self.test_obj.rotate(0)

        gb_again = self.test_obj.get_cell(2, 0, 0)
        self.assertEqual(gb_again.walls[0].description, "gb")
        self.assertEqual(tuple(gb_again.walls[0].direction), (-1, 1, 1))
        rb_again = self.test_obj.get_cell(0, 2, 0)
        self.assertEqual(rb_again.walls[0].description, "rb")
        rg_again = self.test_obj.get_cell(0, 0, 2)
        self.assertEqual(rg_again.walls[0].description, "rg")
        gby_again = self.test_obj.get_cell(-2, -2, 2)
        self.assertEqual(gby_again.walls[0].description, "gby")
        self.assertEqual(tuple(gby_again.walls[0].direction), (1, 1, -1))
        center_again = self.test_obj.get_cell(0, 0, 0)
        self.assertEqual(center_again.walls[0].description, "center")
        self.assertEqual(tuple(center_again.walls[0].direction), (1, 1, 1))
        rgb_octa_again = self.test_obj.get_cell(1, 1, 1)
        self.assertEqual(rgb_octa_again.walls[0].description, "rgb_octa")
        rgb_again = self.test_obj.get_cell(2, 2, 2)
        self.assertEqual(rgb_again.walls[0].description, "rgb")
        gby_octa_again = self.test_obj.get_cell(-1, -1, 1)
        self.assertEqual(gby_octa_again.walls[0].description, "gby_octa")

    def test_rotate_rgy(self):
        rg = self.test_obj.get_cell(0, 2, 0)
        rg.walls[0].description = "rg"

        self.test_obj.rotate(1)

        rg_again = self.test_obj.get_cell(0, 0, -2)
        self.assertEqual(rg_again.walls[0].description, "rg")

    def test_rotate_gby(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = "gb"

        self.test_obj.rotate(2)

        gb_again = self.test_obj.get_cell(-2, 0, 0)
        self.assertEqual(gb_again.walls[0].description, "gb")

    def test_rotate_rby(self):
        rb = self.test_obj.get_cell(2, 0, 0)
        rb.walls[0].description = "rb"

        self.test_obj.rotate(3)

        rb_again = self.test_obj.get_cell(0, -2, 0)
        self.assertEqual(rb_again.walls[0].description, "rb")

    def test_describe_cell_no_doors(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'
        
        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_with_doors(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        rgb_octa = self.test_obj.get_cell(1, 1, 1)
        rgb_octa.walls[4].door = True
        
        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.DOOR),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_with_obstructed_door(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.OBSTRUCTED),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_with_obstructed_door_then_open_door(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        rgy_octa = self.test_obj.get_cell(-1, 1, -1)
        rgy_octa.walls[4].door = True
        
        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.OBSTRUCTED),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

        self.test_obj.rotate(2)
        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.DOOR),
            Rubik.WallDescription(YELLOW.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(GREEN.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(-2, 0, 0)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_with_trap_door(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[3].door = True

        gby_octa = self.test_obj.get_cell(-1, -1, 1)
        gby_octa.walls[0].door = True
        
        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_with_exterior_door(self):
        gb = self.test_obj.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[1].door = True

        expected_description = [
            Rubik.WallDescription(RED.vector, 'red', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(GREEN.vector, 'green', Rubik.DoorState.DOOR),
            Rubik.WallDescription(BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(YELLOW.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 2)
        self.assertEqual(actual_description, expected_description)

    def test_describe_cell_describes_center_tetra_with_roof_and_three_walls(self):
        gb = self.test_obj.get_cell(0, 0, 0)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'
        
        expected_description = [
            Rubik.WallDescription(ANTI_YELLOW.vector, 'red', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(ANTI_GREEN.vector, 'green', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(ANTI_BLUE.vector, 'blue', Rubik.DoorState.NO_DOOR),
            Rubik.WallDescription(ANTI_RED.vector, 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.test_obj.describe_cell(0, 0, 0)
        self.assertEqual(actual_description, expected_description)
        
if __name__ == '__main__':
    unittest.main()
