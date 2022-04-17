from numpy import array

class Wall:
    def __init__(self, color, direction):
        self.__door = False
        self.__description = ""
        self.__color = color
        self.__direction = array(direction)

    def with_direction(self, direction):
        w = Wall(self.color, direction)
        w.door = self.door
        w.description = self.description
