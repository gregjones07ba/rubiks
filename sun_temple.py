from rubik import Rubik
from cell import Cell
from color_direction import *

def create_pyraminx():
    pyraminx = Rubik(Cell.tetra_factory, Cell.octa_factory)

    rgb = pyraminx.get_cell(2, 2, 2)
    rgb_y = rgb.wall_with_direction(YELLOW.vector)
    rgb_y.door = True

    rb = pyraminx.get_cell(2, 0, 0)
    rb_r = rb.wall_with_direction(RED.vector)
    rb_r.door = True
    rb_y = rb.wall_with_direction(YELLOW.vector)
    rb_y.door = True

    rgb_octa = pyraminx.get_cell(1, 1, 1)
    rgb_octa_ag = rgb_octa.wall_with_direction(ANTI_GREEN.vector)
    rgb_octa_ag.door = True
    rgb_octa_ab = rgb_octa.wall_with_direction(ANTI_BLUE.vector)
    rgb_octa_ab.door = True
    rgb_octa_ar = rgb_octa.wall_with_direction(ANTI_RED.vector)
    rgb_octa_ar.door = True

    rg = pyraminx.get_cell(0, 2, 0)
    rg_y = rg.wall_with_direction(YELLOW.vector)
    rg_y.door = True
    rg_b = rg.wall_with_direction(BLUE.vector)
    rg_b.door = True

    gb = pyraminx.get_cell(0, 0, 2)
    gb_y = gb.wall_with_direction(YELLOW.vector)
    gb_y.door = True
    gb_r = gb.wall_with_direction(RED.vector)
    gb_r.door = True

    rby = pyraminx.get_cell(2, -2, -2)
    rby_g = rby.wall_with_direction(GREEN.vector)
    rby_g.door = True

    rby_octa = pyraminx.get_cell(1, -1, -1)
    rby_octa_ay = rby_octa.wall_with_direction(ANTI_YELLOW.vector)
    rby_octa_ay.door = True
    rby_octa_ag = rby_octa.wall_with_direction(ANTI_GREEN.vector)
    rby_octa_ag.door = True
    rby_octa_ar = rby_octa.wall_with_direction(ANTI_RED.vector)
    rby_octa_ar.door = True

    ry = pyraminx.get_cell(0, 0, -2)

    rgy_octa = pyraminx.get_cell(-1, 1, -1)
    rgy_octa_ag = rgy_octa.wall_with_direction(ANTI_GREEN.vector)
    rgy_octa_ag.door = True
    rgy_octa_ab = rgy_octa.wall_with_direction(ANTI_BLUE.vector)
    rgy_octa_ab.door = True

    rgy = pyraminx.get_cell(-2, 2, -2)
    rgy_b = rgy.wall_with_direction(BLUE.vector)
    rgy_b.door = True

    core = pyraminx.get_cell(0, 0, 0)

    by = pyraminx.get_cell(0, -2, 0)
    by_g = by.wall_with_direction(BLUE.vector)
    by_g.door = True
    by_r = by.wall_with_direction(RED.vector)
    by_r.door = True

    gby_octa = pyraminx.get_cell(-1, -1, 1)
    gby_octa_ay = gby_octa.wall_with_direction(ANTI_YELLOW.vector)
    gby_octa_ay.door = True

    gy = pyraminx.get_cell(-2, 0, 0)

    gby = pyraminx.get_cell(-2, -2, 2)
    
    return pyraminx

