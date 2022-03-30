class Rubik:
    """Currently supports pyraminx tetrahedron only"""
    def __init__(self, new_cell_factory):
        self.new_cell_factory = new_cell_factory
        self.populate_cells()

    def create_cells(self, new_cell_factory):
        self.cells = []
        self.add_cells([
            (2, 2, 2),
            (2, 0, 0),
            (1, 1, 1),
            (0, 2, 0),
            (0, 0, 2),
            (2, -2, -1),
            (1, -1, -1),
            (0, 0, -2),
            (-1, 1, -1),
            (-2, 2, -2),
            (0, 0, 0),
            (0, -2, 0),
            (-1, -1, 1),
            (-2, 0, 0),
            (-2, -2, 2)
            ])

    def add_cells(self, l):
        for cell in l:
            self.add_cell(cell)

    def add_cell(self, x, y, z):
        self.cells.append(self.new_cell_factory(x, y, z))

    def create_rotations(self):
        self.rotations = []
        self.add_rotations(self, [
            ((0, 1, 0),
             (1, 0, 0),
             (0, 0, 1)),
            None,
            None,
            ((0, -1, 0),
             (-1, 0, 0),
             (0, 0, 1))
            ])

    def add_rotations(self, matrices):
        for matrix in matrices:
            self.add_rotation(matrix)

    def add_rotation(self, matrix):
        self.rotations.append(matrix)
