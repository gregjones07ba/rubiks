from enum import Enum, auto

from relative_director import RelativeDirector
from color_direction import RGB
from utils import vectors_equal

from rubik import Rubik

class Explorer:
    def __init__(self, dungeon, initial_location, initial_direction, vertical=RGB.vector):
        self.dungeon = dungeon
        self.location = initial_location
        self.direction = initial_direction
        self.vertical = vertical
        self.relative_director = RelativeDirector(self.vertical)

    class WallDescription:
        def __init__(self, direction, relative_directions, description, door_state):
            self.direction = direction
            self.relative_directions = relative_directions
            self.description = description
            self.door_state = door_state

    def describe(self):
        room_description = self.dungeon.describe_cell(*self.location)
        direction_set = self.__get_direction_set(room_description)
        direction_map = self.relative_director.simplify_directions(self.direction, direction_set)
        description = [
            self.WallDescription(
                wall_description.direction,
                direction_map[tuple(wall_description.direction)],
                wall_description.description,
                wall_description.door_state
            )
            for wall_description in room_description
        ]
        return self.__sorted_description(description)
        
    def __get_direction_set(self, description):
        return set(tuple(wall_description.direction)
            for wall_description in description)

    def __sorted_description(self, description):
        class SortableRelativeDirectionSet:
            def __init__(self, relative_direction_set):
                self.__dset = relative_direction_set

            def __compare_directions(relative_directions_1, relative_directions_2):
                min_length = min(len(relative_directions_1.__dset), len(relative_directions_2.__dset))
                for i in range(min_length):
                    relative_direction_1 = relative_directions_1.__dset[i]
                    relative_direction_2 = relative_directions_2.__dset[i]
                    if abs(relative_direction_1.value) < abs(relative_direction_2.value):
                        return -1
                    elif abs(relative_direction_1.value) > abs(relative_direction_2.value):
                        return 1
                    elif relative_direction_1.value < relative_direction_2.value:
                        return 1
                    elif relative_direction_1.value > relative_direction_2.value:
                        return -1

                if len(relative_directions_1.__dset) < len(relative_directions_2.__dset):
                    return -1
                elif len(relative_directions_1.__dset) > len(relative_directions_2.__dset):
                    return 1
                else:
                    return 0

            def __lt__(self, other):
                return self.__compare_directions(other) < 0

            def __gt__(self, other):
                return self.__compare_directions(other) > 0

            def __eq__(self, other):
                return self.__compare_directions(other) == 0

            def __le__(self, other):
                return self.__compare_directions(other) <= 0

            def __ge__(self, other):
                return self.__compare_directions(other) >= 0

            def __ne__(self, other):
                return self.__compare_directions(other) != 0
                
        return sorted(description, key=lambda wall_description: SortableRelativeDirectionSet(wall_description.relative_directions))

    class Option:
        class OptionType(Enum):
            GO = auto()
            
        def __init__(self, name, option_type, relative_directions, action):
            self.name = name
            self.option_type = option_type
            self.relative_directions = relative_directions
            self.action = action

        def __str__(self):
            return '{t} {dirs}'.format(t=self.option_type, dirs=self.relative_directions)

        def execute(self):
            (self.action)()

    def get_options(self):
        def make_go_option(direction):
            def go_option():
                self.location = self.location + direction
                if not self.is_vertical(direction):
                    self.direction = direction
                
            return go_option
        
        walls = self.describe()
        return [self.Option(str(i + 1),
                            self.Option.OptionType.GO,
                            wall.relative_directions,
                            make_go_option(wall.direction))
                for i, wall in enumerate(
                        wall
                        for wall in walls
                        if wall.door_state == Rubik.DoorState.DOOR
                )]

    def is_vertical(self, direction):
        return (vectors_equal(direction, self.vertical) or
                vectors_equal(direction, -self.vertical))
