from numpy import array

class ColorDirection:
    def __init__(self, name, vector):
        self.name = name
        self.vector = array(vector)

    def alias(self, alias_name):
        return ColorDirection(alias_name, self.vector)

RED = ColorDirection('red', (1, 1, -1))
GREEN = ColorDirection('green', (-1, 1, 1))
BLUE = ColorDirection('blue', (1, -1, 1))
YELLOW = ColorDirection('yellow', (-1, -1, -1))

tetra_colors = (RED, GREEN, BLUE, YELLOW)

ANTI_RED = ColorDirection('anti-red', (-1, -1, 1))
ANTI_GREEN = ColorDirection('anti-green', (1, -1, -1))
ANTI_BLUE = ColorDirection('anti-blue', (-1, 1, -1))
ANTI_YELLOW = ColorDirection('anti-yellow', (1, 1, 1))

octa_colors = (ANTI_YELLOW, RED, ANTI_BLUE, GREEN, ANTI_RED, BLUE, ANTI_GREEN, YELLOW)

RGB = ANTI_YELLOW.alias('rgb')
RGY = ANTI_BLUE.alias('rgy')
GBY = ANTI_RED.alias('gby')
RBY = ANTI_GREEN.alias('rby')

vertex_colors = (RGB, RGY, GBY, RBY)
