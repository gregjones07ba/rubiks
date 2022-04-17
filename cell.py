from numpy import array

from wall import Wall
from color_directions import tetra_colors, octa_colors

class Cell:
    def tetra_factory(x, y, z):
        c = Cell(x, y, z)
        c.__walls = [Wall(color, direction) for color, direction in tetra_colors]
        return c

    def octa_factory(x, y, z):
        c = Cell(x, y, z)
        c.__walls = [Wall(color, direction) for color, direction in octa_colors]
        return c

    def __init__(self, x, y, z):
        self.coords = array((x, y, z))
        self.rotation = array(
            ((1, 0, 0),
             (0, 1, 0),
             (0, 0, 1))) # identity

    def get_walls(self):
        return self.__walls
