from numpy import array
from math import floor

class FriendlyCoordinates:
    def __init__(self,
                 vertical = array((0.0, 0.0, 1.0)),
                 vertical_offset = 0.0,
                 depth = array((0.0, 1.0, 0.0)),
                 depth_offset = 0.0,
                 horizontal = array((1.0, 0.0, 0.0)),
                 horizontal_offset = 0.0):
        self.vertical = vertical
        self.vertical_offset = vertical_offset
        self.depth = depth
        self.depth_offset = depth_offset
        self.horizontal = horizontal
        self.horizontal_offset = horizontal_offset

    def friendly_coords(self, location):
        return (
            self.__calc_horiz(location),
            self.__calc_depth(location),
            self.__calc_vert(location)
        )

    def __calc_horiz(self, location):
        return self.__project(location, self.horizontal, self.horizontal_offset)

    def __calc_depth(self, location):
        return self.__project(location, self.depth, self.depth_offset)

    def __calc_vert(self, location):
        return self.__project(location, self.vertical, self.vertical_offset)

    def __project(self, location, direction, offset):
        return floor(location.dot(direction) + offset)
