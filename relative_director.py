from enum import Enum

from numpy import array

Z = array((0, 0, 1))
class RelativeDirector:
    def __init__(self, vertical=Z):
        self.vertical = vertical

    class Directions(Enum):
        BACK = -2
        FORWARD = 2

    def get_relative_directions(self, from_vector, to_vector):
        return (
            None,
            self.get_back_or_forward(from_vector, to_vector),
            None
        )

    def get_back_or_forward(self, from_vector, to_vector):
        dot_product = from_vector.dot(to_vector)
        return (self.Directions.FORWARD
                if dot_product > 0
                else self.Directions.BACK)
