from numpy import array

from sun_temple import create_pyraminx, configure_initial
from explore import explore
from color_direction import *

def main():
    pyraminx = create_pyraminx()
    configure_initial(pyraminx)
    explore(pyraminx, array((2, 0, 0)), ANTI_RED.vector, review=True)

if __name__ == '__main__':
    main()
