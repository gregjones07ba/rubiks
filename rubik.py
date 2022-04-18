from rotation import Rotation
from color_directions import RGB, RGY, GBY, RBY

class Rubik:
    """Currently supports pyraminx tetrahedron only"""
    def __init__(self, tetra_factory, octa_factory):
        self.tetra_factory = tetra_factory
        self.octa_factory = octa_factory
        self.__cell_map = {}
        self.__create_cells()
        self.__create_rotations()

    def get_cell(self, x, y, z):
        return self.__cell_map[(x, y, z)]

    def rotate(self, axis_index):
        for cell in self.__cells:
            if self.__should_rotate(cell, axis_index):
                cell.coords = self.__rotations[axis_index].matrix.dot(cell.coords)
                cell.rotate(self.__rotations[axis_index].matrix)
        for cell in self.__cells:
            self.__set_cell(cell)

    def describe_cell(self, x, y, z):
        return [self.describe_wall(x, y, z, wall)
                for wall in
                self.get_cell(x, y, z).walls]

    def describe_wall(self, x, y, z, wall):
        return (wall.direction, wall.description, '')

    def __should_rotate(self, cell, axis_index):
        return not self.__is_base(cell, axis_index)

    def __is_base(self, cell, axis_index):
        alignment = cell.coords.dot(self.__rotations[axis_index].vertex)
        return alignment <= 0

    def __create_cells(self):
        self.__cells = []
        tf = self.tetra_factory
        of = self.octa_factory
        cells = [
            tf(2, 2, 2),
            tf(2, 0, 0),
            of(1, 1, 1),
            tf(0, 2, 0),
            tf(0, 0, 2),
            tf(2, -2, -1),
            of(1, -1, -1),
            tf(0, 0, -2),
            of(-1, 1, -1),
            tf(-2, 2, -2),
            tf(0, 0, 0), #TODO: invert
            tf(0, -2, 0),
            of(-1, -1, 1),
            tf(-2, 0, 0),
            tf(-2, -2, 2)
        ]
        for cell in cells:
            self.__add_cell(cell)

    def __add_cell(self, cell):
        self.__cells.append(cell)
        self.__set_cell(cell)

    def __set_cell(self, cell):
        self.__cell_map[tuple(cell.coords)] = cell

    def __create_rotations(self):
        self.__rotations = []
        rotations =  [
            Rotation(
                RGB[1],
                ((0, 0, 1),
                 (1, 0, 0),
                 (0, 1, 0))
                ),
            Rotation(
                RGY[1],
                ((0, 0, 1),
                 (-1, 0, 0),
                 (0, -1, 0))
                ),
            Rotation(
                GBY[1],
                ((0, 0, -1),
                 (1, 0, 0),
                 (0, -1, 0))
                ),
            Rotation(
                RBY[1],
                ((0, 0, -1),
                 (-1, 0, 0),
                 (0, 1, 0))
                )
            ]
        self.__add_rotations(rotations)

    def __add_rotations(self, rotations):
        for rotation in rotations:
            self.__add_rotation(rotation)

    def __add_rotation(self, rotation):
        self.__rotations.append(rotation)
