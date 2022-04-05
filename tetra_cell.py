from cell import Cell
from wall import Wall

class TetraCell(Cell):
    def factory(x, y, z):
        return TetraCell(x, y, z)
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.walls = [Wall() for i in range(4)]
