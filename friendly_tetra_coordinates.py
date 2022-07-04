from friendly_coordinates import FriendlyCoordinates

from numpy import array

class FriendlyTetraCoordinates(FriendlyCoordinates):
    def __init__(self,
                 vertical = array((1.0/3.0, 1.0/3.0, 1.0/3.0)),
                 vertical_offset = 1.0,
                 depth = array((-1.0/3.0, -1.0/3.0, 1.0/3.0)),
                 depth_offset = 1.0,
                 horizontal = array((-1.0/2.0, 1.0/2.0, 0.0)),
                 horizontal_offset = 0.0):
        super().__init__(vertical=vertical,
                         vertical_offset=vertical_offset,
                         depth=depth,
                         depth_offset=depth_offset,
                         horizontal=horizontal,
                         horizontal_offset=horizontal_offset)
