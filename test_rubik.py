import unittest

from rubik import Rubik
from tetra_cell import TetraCell
from octa_cell import OctaCell

class TestRubik(unittest.TestCase):
    def setUp(self):
        self.rubik = Rubik(TetraCell.factory, OctaCell.factory)
    
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
        rb_again = self.rubik.get_cell(0, 2, 0)
        self.assertEqual(rb_again.walls[0].description, "rb")
        rg_again = self.rubik.get_cell(0, 0, 2)
        self.assertEqual(rg_again.walls[0].description, "rg")
        gby_again = self.rubik.get_cell(-2, -2, 2)
        self.assertEqual(gby_again.walls[0].description, "gby")
        center_again = self.rubik.get_cell(0, 0, 0)
        self.assertEqual(center_again.walls[0].description, "center")
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

if __name__ == '__main__':
    unittest.main()
