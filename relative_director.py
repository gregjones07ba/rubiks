from enum import Enum

from numpy import array, cross
from itertools import chain, combinations

Z = array((0, 0, 1))
class RelativeDirector:
    def __init__(self, vertical=Z):
        self.vertical = vertical

    class Directions(Enum):
        RIGHT = -1
        LEFT = 1
        BACK = -2
        FORWARD = 2
        DOWN = -3
        UP = 3

    def get_relative_directions(self, from_vector, to_vector):
        return (
            self.get_left_or_right(from_vector, to_vector),
            self.get_back_or_forward(from_vector, to_vector),
            self.get_down_or_up(to_vector)
        )

    def get_left_or_right(self, from_vector, to_vector):
        cross_product = cross(from_vector, to_vector)
        dot_vertical = cross_product.dot(self.vertical)
        if dot_vertical == 0:
            return None
        return (self.Directions.LEFT
                if dot_vertical > 0
                else self.Directions.RIGHT)

    def get_back_or_forward(self, from_vector, to_vector):
        dot_product = from_vector.dot(to_vector)
        return (self.Directions.FORWARD
                if dot_product > 0
                else self.Directions.BACK)

    def get_down_or_up(self, to_vector):
        dot_vertical = to_vector.dot(self.vertical)
        return (self.Directions.UP
                if dot_vertical > 0
                else self.Directions.DOWN)

    def simplify_directions(self, from_vector, direction_set):
        all_relative_directions_map = self.__get_all_relative_directions_map(from_vector, direction_set)
        return {
            direction: self.__simplify_direction(from_vector, direction, all_relative_directions_map)
            for direction in direction_set
        }

    def __get_all_relative_directions_map(self, from_vector, direction_set):
        return {
            direction:
            self.get_relative_directions(from_vector, array(direction))
            for direction in direction_set
        }

    def __simplify_direction(self, from_vector, direction, all_relative_directions_map):
        relative_directions = all_relative_directions_map[direction]
        for indices in self.__axis_subsets(len(relative_directions)):
            relative_direction_set = self.__project(relative_directions, indices)
            if self.__use_relative_direction_set(relative_direction_set, indices, all_relative_directions_map.values()):
                return self.__remove_unspecified(relative_direction_set)

    def __axis_subsets(self, num_indices):
        all_indices = range(num_indices)
        return chain.from_iterable(combinations(all_indices, length)
                                   for length in range(1, num_indices + 1))

    def __project(self, l, indices):
        return [l[i] for i in indices]

    def __use_relative_direction_set(self, relative_direction_set, indices, all_relative_direction_sets):
        return (self.__direction_exists(relative_direction_set) and
                self.__direction_is_unique(relative_direction_set, indices, all_relative_direction_sets))

    def __direction_exists(self, relative_direction_set):
        return not all(relative_direction is None for relative_direction in relative_direction_set)

    def __direction_is_unique(self, relative_direction_set, indices, all_relative_direction_sets):
        return self.__freq_of_direction(relative_direction_set, indices, all_relative_direction_sets) == 1

    def __freq_of_direction(self, relative_direction_set, indices, all_relative_direction_sets):
        return len([1
                    for other_relative_directions in all_relative_direction_sets
                    if self.__match_on_indices(other_relative_directions, relative_direction_set, indices)
        ]) 

    def __match_on_indices(self, relative_directions, relative_direction_set, indices):
        return self.__project(relative_directions, indices) == relative_direction_set

    def __remove_unspecified(self, relative_direction_set):
        return [relative_direction
                for relative_direction in relative_direction_set
                if relative_direction]
