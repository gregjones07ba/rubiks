from explorer import Explorer
from color_direction import *
from relative_director import RelativeDirector
from rubik import Rubik

class ExploreInteract:
    HR_LEN = 10
    DATA_FILE_PATH = 'rubik_history.txt'
    GOD_PREFIX = 'g:'
    
    def __init__(self, rubik, initial_location, initial_direction, vertical, review):
        self.rubik = rubik
        self.explorer = Explorer(self.rubik, initial_location, initial_direction, vertical)
        self.review = review
        self.options = []
        self.in_file = None
        self.out_file = None
        self.__suppress_show = False

    def __try_load(self):
        try:
            self.__load()
        except FileNotFoundError:
            pass

    def __load(self):
        with open(self.DATA_FILE_PATH, 'r') as self.in_file:
            while(self.__load_step()):
                pass
            self.in_file.close()
        self.in_file = None

    def __load_step(self):
        raw_line = self.in_file.readline()
        if raw_line:
            line = raw_line.strip()
            self.options = self.explorer.get_options()
            self.__execute(line)
            return True
        else:
            return False

    def __interact(self):
        with open(self.DATA_FILE_PATH, 'a') as self.out_file:
            while(self.__step()):
                pass
            self.out_file.close()
        self.out_file = None

    def __step(self):
        self.options = self.explorer.get_options()
        self.__maybe_show()
        return self.__act()

    def __maybe_show(self):
        if not self.__suppress_show:
            self.__show()
        self.__suppress_show = False
        
    def __show(self):
        self.__print_hr()
        print()
        self.__advise()
        print()

    def __print_hr(self):
        print('=' * self.HR_LEN)

    def __advise(self):
        self.__describe()
        print()
        self.__show_options()

    def __describe(self):
        self.__name_location()
        self.__describe_location()
        self.__describe_facing()
        self.__describe_room()

    def __name_location(self):
        print('Cell {name}'.format(
            name=self.explorer.name()
        ))

    def __describe_location(self):
        location = self.explorer.locate()
        print('File {file} | Rank {rank} | Tier {tier}'.format(
            file=location[0],
            rank=location[1],
            tier=location[2]
        ))

    def __describe_facing(self):
        dir = self.explorer.direct()
        if dir:
            print('Facing {dir}'.format(
                dir=dir
            ))

    def __describe_room(self):
        self.__describe_walls(self.explorer.describe())

    def __describe_walls(self, description):
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
        if option.option_type == Explorer.Option.OptionType.GO:
            return self.__describe_go_option(option)
        elif option.option_type == Explorer.Option.OptionType.LOOK:
            return self.__describe_look_option(option)
        else:
            return self.__describe_custom_option(option)

    def __describe_go_option(self, option):
        return 'GO {direction}'.format(
            direction = self.__describe_movement_directions(option.relative_directions)
        )

    def __describe_look_option(self, option):
        return 'LOOK {direction}'.format(
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

    def __describe_custom_option(self, option):
        if option.description == "rotate ccw":
            return "Rotate CCW"
        elif option.description == "rotate cw":
            return "Rotate CW"
        else:
            raise ValueError("Unrecognized option")

    def __act(self):
        command = self.__read_command()
        if self.__execute(command):
            self.__record_command(command)
            return True
        else:
            return False

    def __read_command(self):
        try:
            return input('> ').strip()
        except EOFError:
            return 'q'

    def __record_command(self, command):
        self.out_file.write('{command}\n'.format(command=command))

    def __execute(self, command):
        selected_options = [ option
                             for option in self.options
                             if option.name == command ]
        if selected_options:
            if self.review:
                print('{num}. {desc}'.format(num=selected_options[0].name, desc=self.__describe_option(selected_options[0])))
            result = selected_options[0].execute()
            if result:
                self.__show_result(result)
                self.__suppress_show = True
            return True
        elif command in ['q', 'quit', 'exit']:
            return False
        elif command in ['d', 'describe']:
            # no-op; description will be printed in next step
            return True
        elif command.startswith(self.GOD_PREFIX):
            if self.review:
                print(command)
            exec(command[len(self.GOD_PREFIX):])
            return True
        else:
            print("Unrecognized command")
            return True

    def __show_result(self, result):
        self.__describe_walls(result)

    def run(self):
        self.__try_load()
        self.__suppress_show = False
        self.__interact()

    # god mode commands
    def goto(self, x, y, z):
        self.explorer.location = array((x, y, z))

    def tag(self, tag):
        cell = self.explorer.dungeon.get_cell(*tuple(self.explorer.location))
        wall = cell.wall_with_direction(self.explorer.direction)
        wall.description += " t: " + tag

def explore(rubik, initial_location, initial_direction, vertical=RGB.vector, review=False):
    interact = ExploreInteract(rubik, initial_location, initial_direction, vertical, review)
    interact.run()
