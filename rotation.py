from numpy import array

class Rotation:
    def __init__(self, vertex, matrix):
        self.vertex = array(vertex)
        self.matrix = array(matrix)
