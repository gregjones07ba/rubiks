from enum import Enum

from numpy import array, cross

Z = array((0, 0, 1))
class RelativeDirector:
    def __init__(self, vertical=Z):
        self.vertical = vertical

    class Directions(Enum):
        RIGHT = -1
        LEFT = 1
        BACK = -2
        FORWARD = 2

    def get_relative_directions(self, from_vector, to_vector):
        return (
            self.get_left_or_right(from_vector, to_vector),
            self.get_back_or_forward(from_vector, to_vector),
            None
        )

    def get_left_or_right(self, from_vector, to_vector):
        cross_product = cross(from_vector, to_vector)
        dot_vertical = cross_product.dot(self.vertical)
        return (self.Directions.LEFT
                if dot_vertical > 0
                else self.Directions.RIGHT)

    def get_back_or_forward(self, from_vector, to_vector):
        dot_product = from_vector.dot(to_vector)
        return (self.Directions.FORWARD
                if dot_product > 0
                else self.Directions.BACK)
