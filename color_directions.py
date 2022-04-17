RED = ('red', (1, 1, -1))
GREEN = ('green', (-1, 1, 1))
BLUE = ('blue', (1, -1, 1))
YELLOW = ('yellow', (-1, -1, -1))

tetra_colors = (RED, GREEN, BLUE, YELLOW)

ANTI_RED = ('anti-red', (-1, -1, 1))
ANTI_GREEN = ('anti-green', (1, -1, -1))
ANTI_BLUE = ('anti-blue', (-1, 1, -1))
ANTI_YELLOW = ('anti-yellow', (1, 1, 1))

octa_colors = (ANTI_YELLOW, RED, ANTI_BLUE, GREEN, ANTI_RED, BLUE, ANTI_GREEN, YELLOW)

RGB = ('rgb', ANTI_YELLOW[1])
RGY = ('rgy', ANTI_BLUE[1])
GBY = ('gby', ANTI_RED[1])
RBY = ('rby', ANTI_GREEN[1])

vertex_colors = (RGB, RGY, GBY, RBY)
