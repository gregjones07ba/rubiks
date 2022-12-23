from numpy import array

from sun_temple import create_pyraminx, configure_initial
from explore import explore
from color_direction import *
from argparse import ArgumentParser

def __create_parser():
    parser = ArgumentParser(description='Explore the sun temple')
    parser.add_argument(
        '-r', '--review',
        default=False,
        action='store_true',
        help='Show action history'
    )
    return parser

def __parse_args():
    parser = __create_parser()
    return parser.parse_args()

def main():
    args = __parse_args()
    pyraminx = create_pyraminx()
    configure_initial(pyraminx)
    explore(pyraminx, array((2, 0, 0)), ANTI_RED.vector, review=args.review)

if __name__ == '__main__':
    main()
