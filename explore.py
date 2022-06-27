from explorer import Explorer
from color_direction import *
from relative_director import RelativeDirector
from rubik import Rubik

class ExploreInteract:
    HR_LEN = 10
    
    def __init__(self, rubik, initial_location, initial_direction, vertical):
        self.rubik = rubik
        self.explorer = Explorer(rubik, initial_location, initial_direction, vertical)
        self.options = []

    def step(self):
        self.options = self.explorer.get_options()
        self.__print_hr()
        print()
        self.__advise()
        print()
        return self.__execute(self.__read_command())

    def __print_hr(self):
        print('=' * self.HR_LEN)

    def __advise(self):
        self.__describe()
        print()
        self.__show_options()

    def __describe(self):
        description = self.explorer.describe()
        for wall_description in description:
            self.__describe_wall(wall_description)

    def __describe_wall(self, wall_description):
        description = ['{direction}, you see a wall with {description}.'.format(
            direction = self.__describe_direction(wall_description.relative_directions),
            description = wall_description.description
        )]
        self.__add_door_description(description, wall_description.door_state)
        print(self.__capitalize(' '.join(description)))

    def __describe_direction(self, relative_directions):
        if RelativeDirector.Direction.BACK in relative_directions:
            return self.__describe_with_longitudinal(relative_directions, RelativeDirector.Direction.BACK, 'behind you')
        elif RelativeDirector.Direction.FORWARD in relative_directions:
            return self.__describe_with_longitudinal(relative_directions, RelativeDirector.Direction.FORWARD, 'ahead')
        elif RelativeDirector.Direction.LEFT in relative_directions:
            return self.__describe_with_transverse(relative_directions, 'left')
        elif RelativeDirector.Direction.RIGHT in relative_directions:
            return self.__describe_with_transverse(relative_directions, 'right')
        elif RelativeDirector.Direction.DOWN in relative_directions:
            return 'below you'
        else:
            return 'above you'

    def __describe_with_longitudinal(self, relative_directions, first_direction, first_direction_description):
        remaining_directions = relative_directions[:]
        remaining_directions.remove(first_direction)
        if remaining_directions:
            return '{first} and {rest}'.format(
                first = first_direction_description,
                rest = self.__describe_direction(remaining_directions)
            )
        else:
            return first_direction_description

    def __describe_with_transverse(self, relative_directions, first_direction_description):
        if RelativeDirector.Direction.UP in relative_directions:
            vertical_adjective = 'upper '
        elif RelativeDirector.Direction.DOWN in relative_directions:
            vertical_adjective = 'lower '
        else:
            vertical_adjective = ''
        return 'to the {adj}{noun}'.format(
            adj = vertical_adjective,
            noun = first_direction_description
        )

    def __add_door_description(self, description, door_state):
        if door_state == Rubik.DoorState.DOOR:
            description.append("There is a door.")
        elif door_state == Rubik.DoorState.OBSTRUCTED:
            description.append("There is a door, but it is obstructed.")

    def __capitalize(self, s):
        return '{first}{rest}'.format(
            first = s[0].upper(),
            rest = s[1:]
        )

    def __show_options(self):
        for option in self.options:
            self.__show_option(option)

    def __show_option(self, option):
        print('{index}. {option}'.format(
            index = option.name,
            option = self.__describe_option(option)
        ))

    def __describe_option(self, option):
        return self.__describe_go_option(option)

    def __describe_go_option(self, option):
        return 'GO {direction}'.format(
            direction = self.__describe_movement_directions(option.relative_directions)
        )

    def __describe_movement_directions(self, relative_directions):
        return ' and '.join(
            [ self.__describe_movement_direction(relative_direction)
              for relative_direction in relative_directions ]
        )

    DIR_MAP = {
        RelativeDirector.Direction.RIGHT: 'right',
        RelativeDirector.Direction.LEFT: 'left',
        RelativeDirector.Direction.BACK: 'back',
        RelativeDirector.Direction.FORWARD: 'forward',
        RelativeDirector.Direction.DOWN: 'down',
        RelativeDirector.Direction.UP: 'up'
    }

    def __describe_movement_direction(self, relative_direction):
        return self.DIR_MAP[relative_direction]

    def __read_command(self):
        return input('> ').strip()

    def __execute(self, command):
        selected_options = [ option
                             for option in self.options
                             if option.name == command ]
        if selected_options:
            selected_options[0].execute()
            return True
        elif command in ['q', 'quit', 'exit']:
            return False
        else:
            print("Unrecognized command")

    def run(self):
        while(self.step()):
            pass

def explore(rubik, initial_location, initial_direction, vertical=RGB.vector):
    interact = ExploreInteract(rubik, initial_location, initial_direction, vertical)
    interact.run()
