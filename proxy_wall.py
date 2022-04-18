class ProxyWall:
    def __init__(self, wall, direction):
        self.__wall = wall
        self.direction = direction

    @property
    def door(self):
        return self.__wall.door

    @door.setter
    def door(self, value):
        self.__wall.door = value

    @property
    def description(self):
        return self.__wall.description

    @description.setter
    def description(self, value):
        self.__wall.description = value

    @property
    def color(self):
        return self.__wall.color

    @color.setter
    def color(self, value):
        self.__wall.color = value
