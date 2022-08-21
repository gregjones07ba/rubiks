from rubik import Rubik
from cell import Cell
from color_direction import *
from action import Action

def create_pyraminx():
    pyraminx = Rubik(Cell.tetra_factory, Cell.octa_factory)

    rgb = pyraminx.get_cell(2, 2, 2)
    rgb_y = rgb.wall_with_direction(YELLOW.vector)
    rgb_y.door = True
    rgb.custom_actions += [__create_ccw_rotation(pyraminx, 0),
                           __create_cw_rotation(pyraminx, 0)]
    rgb.name = '1.rgb'

    rb = pyraminx.get_cell(2, 0, 0)
    rb_g = rb.wall_with_direction(GREEN.vector)
    rb_g.door = True
    rb_y = rb.wall_with_direction(YELLOW.vector)
    rb_y.description = "a triangular glass case enclosing a gold nyanka with key 1 in its chest"
    rb.name = '2.rb'

    rgb_octa = pyraminx.get_cell(1, 1, 1)
    rgb_octa_ay = rgb_octa.wall_with_direction(ANTI_YELLOW.vector)
    rgb_octa_ay.door = True
    rgb_octa_ab = rgb_octa.wall_with_direction(ANTI_BLUE.vector)
    rgb_octa_ab.door = True
    rgb_octa_ar = rgb_octa.wall_with_direction(ANTI_RED.vector)
    rgb_octa_ar.door = True
    rgb_octa_ag = rgb_octa.wall_with_direction(ANTI_GREEN.vector)
    rgb_octa_ag.door = True
    rgb_octa.name = '3.rgb8'

    rg = pyraminx.get_cell(0, 2, 0)
    rg_b = rg.wall_with_direction(BLUE.vector)
    rg_b.door = True
    rg_y = rg.wall_with_direction(YELLOW.vector)
    rg_y.door = True
    rg.name = '4.rg'

    gb = pyraminx.get_cell(0, 0, 2)
    gb_r = gb.wall_with_direction(RED.vector)
    gb_r.door = True
    gb_y = gb.wall_with_direction(YELLOW.vector)
    gb_y.door = True
    gb.name = '5.gb'

    rby = pyraminx.get_cell(2, -2, -2)
    rby_g = rby.wall_with_direction(GREEN.vector)
    rby_g.door = True
    rby.custom_actions += [__create_ccw_rotation(pyraminx, 3),
                           __create_cw_rotation(pyraminx, 3)]
    rby.name = '6.rby'

    rby_octa = pyraminx.get_cell(1, -1, -1)
    rby_octa_ay = rby_octa.wall_with_direction(ANTI_YELLOW.vector)
    rby_octa_ay.door = True
    rby_octa_ab = rby_octa.wall_with_direction(ANTI_BLUE.vector)
    rby_octa_ab.door = True
    rby_octa_ar = rby_octa.wall_with_direction(ANTI_RED.vector)
    rby_octa_ar.door = True
    rby_octa_ag = rby_octa.wall_with_direction(ANTI_GREEN.vector)
    rby_octa_ag.door = True
    rby_octa.name = '7.rby8'

    ry = pyraminx.get_cell(0, 0, -2)
    ry_g = ry.wall_with_direction(GREEN.vector)
    ry_g.door = True
    ry_b = ry.wall_with_direction(BLUE.vector)
    ry_b.door = True
    ry.name = '8.ry'

    rgy_octa = pyraminx.get_cell(-1, 1, -1)
    rgy_octa_ay = rgy_octa.wall_with_direction(ANTI_YELLOW.vector)
    rgy_octa_ay.door = True
    rgy_octa_ab = rgy_octa.wall_with_direction(ANTI_BLUE.vector)
    rgy_octa_ab.door = True
    rgy_octa_ag = rgy_octa.wall_with_direction(ANTI_GREEN.vector)
    rgy_octa_ag.door = True
    rgy_octa.name = '9.rgy8'

    rgy = pyraminx.get_cell(-2, 2, -2)
    rgy_b = rgy.wall_with_direction(BLUE.vector)
    rgy_b.door = True
    rgy.custom_actions += [__create_ccw_rotation(pyraminx, 1),
                           __create_cw_rotation(pyraminx, 1)]
    rgy.name = '10.rgy'

    core = pyraminx.get_cell(0, 0, 0)
    core.name = '11.core'

    by = pyraminx.get_cell(0, -2, 0)
    by_r = by.wall_with_direction(RED.vector)
    by_r.door = True
    by_g = by.wall_with_direction(GREEN.vector)
    by_g.door = True
    by.name = '12.by'

    gby_octa = pyraminx.get_cell(-1, -1, 1)
    gby_octa_ab = gby_octa.wall_with_direction(ANTI_BLUE.vector)
    gby_octa_ab.door = True
    gby_octa_ar = gby_octa.wall_with_direction(ANTI_RED.vector)
    gby_octa_ar.door = True
    gby_octa_ag = gby_octa.wall_with_direction(ANTI_GREEN.vector)
    gby_octa_ag.door = True
    gby_octa.name = '13.gby8'

    gy = pyraminx.get_cell(-2, 0, 0)
    gy_g = gy.wall_with_direction(GREEN.vector)
    gy_g.description = "a rectangular door with its base on the yellow face"
    gy_b = gy.wall_with_direction(BLUE.vector)
    gy_b.door = True
    gy.name = '14.gy'

    gby = pyraminx.get_cell(-2, -2, 2)
    gby_r = gby.wall_with_direction(RED.vector)
    gby_r.door = True
    gby.custom_actions += [__create_ccw_rotation(pyraminx, 2),
                           __create_cw_rotation(pyraminx, 2)]
    gby.name = '15.gby'
    
    return pyraminx

def __create_ccw_rotation(pyraminx, index):
    def rotate_ccw():
        pyraminx.rotate(index)

    return Action("rotate ccw", rotate_ccw)

def __create_cw_rotation(pyraminx, index):
    def rotate_cw():
        for i in range(2):
            pyraminx.rotate(index)

    return Action("rotate cw", rotate_cw)

def configure_initial(pyraminx):
    pyraminx.rotate(0)
    pyraminx.rotate(0)
    pyraminx.rotate(1)
    pyraminx.rotate(1)
    pyraminx.rotate(2)
    pyraminx.rotate(2)
    pyraminx.rotate(3)

