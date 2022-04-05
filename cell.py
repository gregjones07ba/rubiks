from numpy import array

class Cell:
    def factory(x, y, z):
        return Cell(x, y, z)

    def __init__(self, x, y, z):
        self.coords = array((x, y, z))
