import unittest

from numpy import array

from rubik import Rubik
from cell import Cell

from color_directions import *

class TestRubik(unittest.TestCase):
    def setUp(self):
        self.rubik = Rubik(Cell.tetra_factory, Cell.octa_factory)
    
    def test_rotate_rgb(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = "gb"
        rb = self.rubik.get_cell(2, 0, 0)
        rb.walls[0].description = "rb"
        rg = self.rubik.get_cell(0, 2, 0)
        rg.walls[0].description = "rg"
        gby = self.rubik.get_cell(-2, -2, 2)
        gby.walls[0].description = "gby"
        center = self.rubik.get_cell(0, 0, 0)
        center.walls[0].description = "center"
        rgb_octa = self.rubik.get_cell(1, 1, 1)
        rgb_octa.walls[0].description = "rgb_octa"
        rgb = self.rubik.get_cell(2, 2, 2)
        rgb.walls[0].description = "rgb"
        gby_octa = self.rubik.get_cell(-1, -1, 1)
        gby_octa.walls[0].description = "gby_octa"
        
        self.rubik.rotate(0)

        gb_again = self.rubik.get_cell(2, 0, 0)
        self.assertEqual(gb_again.walls[0].description, "gb")
        self.assertEqual(tuple(gb_again.walls[0].direction), (-1, 1, 1))
        rb_again = self.rubik.get_cell(0, 2, 0)
        self.assertEqual(rb_again.walls[0].description, "rb")
        rg_again = self.rubik.get_cell(0, 0, 2)
        self.assertEqual(rg_again.walls[0].description, "rg")
        gby_again = self.rubik.get_cell(-2, -2, 2)
        self.assertEqual(gby_again.walls[0].description, "gby")
        self.assertEqual(tuple(gby_again.walls[0].direction), (1, 1, -1))
        center_again = self.rubik.get_cell(0, 0, 0)
        self.assertEqual(center_again.walls[0].description, "center")
        self.assertEqual(tuple(center_again.walls[0].direction), (1, 1, -1))
        rgb_octa_again = self.rubik.get_cell(1, 1, 1)
        self.assertEqual(rgb_octa_again.walls[0].description, "rgb_octa")
        rgb_again = self.rubik.get_cell(2, 2, 2)
        self.assertEqual(rgb_again.walls[0].description, "rgb")
        gby_octa_again = self.rubik.get_cell(-1, -1, 1)
        self.assertEqual(gby_octa_again.walls[0].description, "gby_octa")

    def test_rotate_rgy(self):
        rg = self.rubik.get_cell(0, 2, 0)
        rg.walls[0].description = "rg"

        self.rubik.rotate(1)

        rg_again = self.rubik.get_cell(0, 0, -2)
        self.assertEqual(rg_again.walls[0].description, "rg")

    def test_rotate_gby(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = "gb"

        self.rubik.rotate(2)

        gb_again = self.rubik.get_cell(-2, 0, 0)
        self.assertEqual(gb_again.walls[0].description, "gb")

    def test_rotate_rby(self):
        rb = self.rubik.get_cell(2, 0, 0)
        rb.walls[0].description = "rb"

        self.rubik.rotate(3)

        rb_again = self.rubik.get_cell(0, -2, 0)
        self.assertEqual(rb_again.walls[0].description, "rb")

    def test_describe_cell_no_doors(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'
        
        expected_description = [
            (RED[1], 'red', Rubik.DoorState.NO_DOOR),
            (GREEN[1], 'green', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def test_describe_cell_with_doors(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        rgb_octa = self.rubik.get_cell(1, 1, 1)
        rgb_octa.walls[4].door = True
        
        expected_description = [
            (RED[1], 'red', Rubik.DoorState.DOOR),
            (GREEN[1], 'green', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def test_describe_cell_with_obstructed_door(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        expected_description = [
            (RED[1], 'red', Rubik.DoorState.OBSTRUCTED),
            (GREEN[1], 'green', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def test_describe_cell_with_obstructed_door_then_open_door(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[0].door = True

        rgy_octa = self.rubik.get_cell(-1, 1, -1)
        rgy_octa.walls[4].door = True
        
        expected_description = [
            (RED[1], 'red', Rubik.DoorState.OBSTRUCTED),
            (GREEN[1], 'green', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

        self.rubik.rotate(2)
        expected_description = [
            (RED[1], 'red', Rubik.DoorState.DOOR),
            (YELLOW[1], 'green', Rubik.DoorState.NO_DOOR),
            (GREEN[1], 'blue', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(-2, 0, 0)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def test_describe_cell_with_trap_door(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[3].door = True

        gby_octa = self.rubik.get_cell(-1, -1, 1)
        gby_octa.walls[0].door = True
        
        expected_description = [
            (RED[1], 'red', Rubik.DoorState.NO_DOOR),
            (GREEN[1], 'green', Rubik.DoorState.NO_DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def test_describe_cell_with_exterior_door(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = 'red'
        gb.walls[1].description = 'green'
        gb.walls[2].description = 'blue'
        gb.walls[3].description = 'yellow'

        gb.walls[1].door = True

        expected_description = [
            (RED[1], 'red', Rubik.DoorState.NO_DOOR),
            (GREEN[1], 'green', Rubik.DoorState.DOOR),
            (BLUE[1], 'blue', Rubik.DoorState.NO_DOOR),
            (YELLOW[1], 'yellow', Rubik.DoorState.NO_DOOR)
        ]
        actual_description = self.rubik.describe_cell(0, 0, 2)
        self.__assert_descriptions_equal(actual_description, expected_description)

    def __assert_descriptions_equal(self, actual_description, expected_description):
        actual_description_simplified = list(map(lambda wall: (tuple(wall[0]), wall[1], wall[2]), actual_description))
        self.assertEqual(actual_description_simplified, expected_description)
        
if __name__ == '__main__':
    unittest.main()
