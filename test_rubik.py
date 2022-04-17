import unittest

from rubik import Rubik
from cell import Cell

class TestRubik(unittest.TestCase):
    def setUp(self):
        self.rubik = Rubik(Cell.tetra_factory, Cell.octa_factory)
    
    def test_rotate_rgb(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.get_walls()[0].description = "gb"
        rb = self.rubik.get_cell(2, 0, 0)
        rb.get_walls()[0].description = "rb"
        rg = self.rubik.get_cell(0, 2, 0)
        rg.get_walls()[0].description = "rg"
        gby = self.rubik.get_cell(-2, -2, 2)
        gby.get_walls()[0].description = "gby"
        center = self.rubik.get_cell(0, 0, 0)
        center.get_walls()[0].description = "center"
        rgb_octa = self.rubik.get_cell(1, 1, 1)
        rgb_octa.get_walls()[0].description = "rgb_octa"
        rgb = self.rubik.get_cell(2, 2, 2)
        rgb.get_walls()[0].description = "rgb"
        gby_octa = self.rubik.get_cell(-1, -1, 1)
        gby_octa.get_walls()[0].description = "gby_octa"
        
        self.rubik.rotate(0)

        gb_again = self.rubik.get_cell(2, 0, 0)
        self.assertEqual(gb_again.get_walls()[0].description, "gb")
        rb_again = self.rubik.get_cell(0, 2, 0)
        self.assertEqual(rb_again.get_walls()[0].description, "rb")
        rg_again = self.rubik.get_cell(0, 0, 2)
        self.assertEqual(rg_again.get_walls()[0].description, "rg")
        gby_again = self.rubik.get_cell(-2, -2, 2)
        self.assertEqual(gby_again.get_walls()[0].description, "gby")
        center_again = self.rubik.get_cell(0, 0, 0)
        self.assertEqual(center_again.get_walls()[0].description, "center")
        rgb_octa_again = self.rubik.get_cell(1, 1, 1)
        self.assertEqual(rgb_octa_again.get_walls()[0].description, "rgb_octa")
        rgb_again = self.rubik.get_cell(2, 2, 2)
        self.assertEqual(rgb_again.get_walls()[0].description, "rgb")
        gby_octa_again = self.rubik.get_cell(-1, -1, 1)
        self.assertEqual(gby_octa_again.get_walls()[0].description, "gby_octa")

    def test_rotate_rgy(self):
        rg = self.rubik.get_cell(0, 2, 0)
        rg.get_walls()[0].description = "rg"

        self.rubik.rotate(1)

        rg_again = self.rubik.get_cell(0, 0, -2)
        self.assertEqual(rg_again.get_walls()[0].description, "rg")

    def test_rotate_gby(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.get_walls()[0].description = "gb"

        self.rubik.rotate(2)

        gb_again = self.rubik.get_cell(-2, 0, 0)
        self.assertEqual(gb_again.get_walls()[0].description, "gb")

    def test_rotate_rby(self):
        rb = self.rubik.get_cell(2, 0, 0)
        rb.get_walls()[0].description = "rb"

        self.rubik.rotate(3)

        rb_again = self.rubik.get_cell(0, -2, 0)
        self.assertEqual(rb_again.get_walls()[0].description, "rb")

if __name__ == '__main__':
    unittest.main()
