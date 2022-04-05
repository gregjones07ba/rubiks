import unittest

from rubik import Rubik
from tetra_cell import TetraCell
from octa_cell import OctaCell

class TestRubik(unittest.TestCase):
    def setUp(self):
        self.rubik = Rubik(TetraCell.factory, OctaCell.factory)
    
    def test_rotate(self):
        gb = self.rubik.get_cell(0, 0, 2)
        gb.walls[0].description = "Boo!"
        self.rubik.rotate(0)
        gb_again = self.rubik.get_cell(2, 0, 0)
        self.assertEqual(gb_again.walls[0].description, "Boo!")

if __name__ == '__main__':
    unittest.main()
