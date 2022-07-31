from numpy import array

from wall import Wall
from proxy_wall import ProxyWall
from color_direction import tetra_colors, octa_colors

class Cell:
    def tetra_factory(x, y, z):
        c = Cell(x, y, z)
        c.__walls = [Wall(color.name, color.vector) for color in tetra_colors]
        return c

    def octa_factory(x, y, z):
        c = Cell(x, y, z)
        c.__walls = [Wall(color.name, color.vector) for color in octa_colors]
        return c

    def __init__(self, x, y, z):
        self.coords = array((x, y, z))
        self.rotation = array(
            ((1, 0, 0),
             (0, 1, 0),
             (0, 0, 1))) # identity
        self.custom_actions = []
        self.name = "Unnamed cell"

    def rotate(self, rotation):
        self.rotation = rotation.dot(self.rotation)

    @property
    def walls(self):
        return [ProxyWall(wall, self.rotation.dot(wall.direction)) for wall in self.__walls]

    def wall_with_direction(self, direction):
        try:
            return next(
                filter(
                    lambda wall: (wall.direction == direction).all(),
                    self.walls
                ),
            )
        except StopIteration:
            raise ValueError("No such wall")
