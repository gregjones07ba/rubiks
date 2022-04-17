from numpy import array

class Wall:
    def __init__(self, color, direction):
        self.door = False
        self.description = ""
        self.color = color
        self.direction = array(direction)
