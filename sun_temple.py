from rubik import Rubik
from cell import Cell
from color_direction import *
from action import Action

def create_pyraminx():
    pyraminx = Rubik(Cell.tetra_factory, Cell.octa_factory)

    rgb = pyraminx.get_cell(2, 2, 2)
    rgb_r = rgb.wall_with_direction(RED.vector)
    rgb_r.description = 'the right wing of the sun phoenix like rays of gold'
    rgb_g = rgb.wall_with_direction(GREEN.vector)
    rgb_g.description = 'the head of the sun phoenix'
    rgb_b = rgb.wall_with_direction(BLUE.vector)
    rgb_b.description = 'the left wing of the sun phoenix like rays of gold'
    rgb_y = rgb.wall_with_direction(YELLOW.vector)
    rgb_y.door = True
    rgb_y.description = 'a wheel at the center, made of dark glass studded with clear crystals'
    rgb.custom_actions += [__create_ccw_rotation(pyraminx, 0),
                           __create_cw_rotation(pyraminx, 0)]
    rgb.name = '1.rgb'

    rb = pyraminx.get_cell(2, 0, 0)
    rb_r = rb.wall_with_direction(RED.vector)
    rb_r.description = 'a mural of the Stone Mother squatting at the base of a great tree'
    rb_g = rb.wall_with_direction(GREEN.vector)
    rb_g.door = True
    rb_g.description = 'a mural of the Sun Phoenix, flying over a golden tower that straddles the door'
    rb_b = rb.wall_with_direction(BLUE.vector)
    rb_b.description = 'a mural of the Thunder Phoenix, perched atop a silver tower'
    rb_y = rb.wall_with_direction(YELLOW.vector)
    rb_y.description = 'a drow child tossing the Snake key sitting on one of three stone pillars on the edge of a circular mosaic of Tiamat enclosed by rough waters t: 8'
    rb.name = '2.rb'

    rgb_octa = pyraminx.get_cell(1, 1, 1)
    rgb_octa_ay = rgb_octa.wall_with_direction(ANTI_YELLOW.vector)
    rgb_octa_ay.door = True
    rgb_octa_ay.description  = 'a rainbow staircase leading to each other door. Its surface of dark glass. There is a door with an indentation in the shape of a 6-pointed asterisk'
    rgb_octa_ab = rgb_octa.wall_with_direction(ANTI_BLUE.vector)
    rgb_octa_ab.door = True
    rgb_octa_ab.description = 'a surface of obsidian'
    rgb_octa_ar = rgb_octa.wall_with_direction(ANTI_RED.vector)
    rgb_octa_ar.door = True
    rgb_octa_ar.description = 'a surface of obsidian'
    rgb_octa_ag = rgb_octa.wall_with_direction(ANTI_GREEN.vector)
    rgb_octa_ag.door = True
    rgb_octa_ag.description = 'a surface of obsidian'
    rgb_octa_r = rgb_octa.wall_with_direction(RED.vector)
    rgb_octa_r.description = 'a platinum comet inlaid in obsidian'
    rgb_octa_g = rgb_octa.wall_with_direction(GREEN.vector)
    rgb_octa_g.description = 'a silver moon inlaid in obsidian'
    rgb_octa_b = rgb_octa.wall_with_direction(BLUE.vector)
    rgb_octa_b.description = 'the Milky Way inlaid in mother of pearl'
    rgb_octa_y = rgb_octa.wall_with_direction(YELLOW.vector)
    rgb_octa_y.description = 'a mosaic map of the earth. There is a pyramid with a coin slot and a lever. t: 10'
    rgb_octa.name = '3.rgb8'

    rg = pyraminx.get_cell(0, 2, 0)
    rg_r = rg.wall_with_direction(RED.vector)
    rg_r.description = 'a mural of Tiamat, flanked by diverse aberrations'
    rg_g = rg.wall_with_direction(GREEN.vector)
    rg_g.description = 'a mural of the three Elder Phoenixes, flanked by an army of diverse lesser phoenixes'
    rg_b = rg.wall_with_direction(BLUE.vector)
    rg_b.door = True
    rg_y = rg.wall_with_direction(YELLOW.vector)
    rg_y.door = True
    rg_y.description = 'a mosaic of the ocean meeting the sky. There are nyankas with the Spider key t: 9'
    rg.name = '4.rg'

    gb = pyraminx.get_cell(0, 0, 2)
    gb_r = gb.wall_with_direction(RED.vector)
    gb_r.door = True
    gb_g = gb.wall_with_direction(GREEN.vector)
    gb_g.description = 'a mural of the three Elder Phoenixes, charging in a phalanx toward the opposite wall'
    gb_b = gb.wall_with_direction(BLUE.vector)
    gb_b.description = 'a mural of Tiamat fleeing'
    gb_y = gb.wall_with_direction(YELLOW.vector)
    gb_y.description = 'a mosaic of the waters receding in an arc against Tiamat, her tentacles trying to hold them back'
    gb_y.door = True
    gb.name = '5.gb'

    rby = pyraminx.get_cell(2, -2, -2)
    rby_g = rby.wall_with_direction(GREEN.vector)
    rby_g.door = True
    rby_y = rby.wall_with_direction(YELLOW.vector)
    rby_y.description = 'a wheel in the far corner t: 2'
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
    rby_octa_ag.description = 'a door with an indentation in the shape of an 8-pointed asterisk. Above it is a window of ice revealing a rapier behind it. Clear crystal stairs to each other door'
    rby_octa_y = rby_octa.wall_with_direction(YELLOW.vector)
    rby_octa_y.description = 'angular arches of clear crystal t: 6'
    rby_octa.name = '7.rby8'

    ry = pyraminx.get_cell(0, 0, -2)
    ry_r = ry.wall_with_direction(RED.vector)
    ry_r.description = 'a rectangular door. A semisphere with a map of Gord'
    ry_g = ry.wall_with_direction(GREEN.vector)
    ry_g.door = True
    ry_g.description = 'the right half of a colossal granite sculpture of a flightless bird seated'
    ry_b = ry.wall_with_direction(BLUE.vector)
    ry_b.door = True
    ry_b.description = 'the left half of a colossal granite sculpture of a flightless bird seated'
    ry_y = ry.wall_with_direction(YELLOW.vector)
    ry_y.description = 'irregular, natural stone slabs. There are nyankas with the Frog key t: 11'
    ry.name = '8.ry'

    rgy_octa = pyraminx.get_cell(-1, 1, -1)
    rgy_octa_ay = rgy_octa.wall_with_direction(ANTI_YELLOW.vector)
    rgy_octa_ay.door = True
    rgy_octa_ay.description = 'a staircase leading to the side door and a sculpture of a flower'
    rgy_octa_ab = rgy_octa.wall_with_direction(ANTI_BLUE.vector)
    rgy_octa_ab.door = True
    rgy_octa_ab.description = 'a door with an indentation in the shape of a 2-pointed asterisk'
    rgy_octa_ag = rgy_octa.wall_with_direction(ANTI_GREEN.vector)
    rgy_octa_ag.door = True
    rgy_octa_ag.description = 'a staircase leading to the side door'
    rgy_octa_r = rgy_octa.wall_with_direction(RED.vector)
    rgy_octa_r.description = 'a glowing red globe'
    rgy_octa_g = rgy_octa.wall_with_direction(GREEN.vector)
    rgy_octa_g.description = 'a glowing green globe'
    rgy_octa_y = rgy_octa.wall_with_direction(YELLOW.vector)
    rgy_octa_y.description = 'limestone columns carved into naturalistic shapes of tree trunks, branches, and roots. The room is full of water'
    rgy_octa.name = '9.rgy8'

    rgy = pyraminx.get_cell(-2, 2, -2)
    rgy_b = rgy.wall_with_direction(BLUE.vector)
    rgy_b.door = True
    rgy_y = rgy.wall_with_direction(YELLOW.vector)
    rgy_y.description = 'a wheel in the far corner'
    rgy.custom_actions += [__create_ccw_rotation(pyraminx, 1),
                           __create_cw_rotation(pyraminx, 1)]
    rgy.name = '10.rgy'

    core = pyraminx.get_cell(0, 0, 0)
    core.name = '11.core'

    by = pyraminx.get_cell(0, -2, 0)
    by_r = by.wall_with_direction(RED.vector)
    by_r.door = True
    by_r.description = 'the right wing of a phoenix made of branching purple veins in white marble'
    by_g = by.wall_with_direction(GREEN.vector)
    by_g.door = True
    by_g.description = 'the left wing of a phoenix made of branching purple veins in white marble'
    by_b = by.wall_with_direction(BLUE.vector)
    by_b.description = 'a rectangular door. A semisphere with a map of Solasta'
    by_y = by.wall_with_direction(YELLOW.vector)
    by_y.description = 'slabs of meteoritic iron. There are nyankas with the Lizard key, and the aboleth will try to sneak attack. The room is full of water'
    by.name = '12.by'

    gby_octa = pyraminx.get_cell(-1, -1, 1)
    gby_octa_ab = gby_octa.wall_with_direction(ANTI_BLUE.vector)
    gby_octa_ab.door = True
    gby_octa_ab.description = 'a staircase leading to the side door'
    gby_octa_ar = gby_octa.wall_with_direction(ANTI_RED.vector)
    gby_octa_ar.door = True
    gby_octa_ar.description = 'a door with an indentation in the shape of a 4-pointed asterisk'
    gby_octa_ag = gby_octa.wall_with_direction(ANTI_GREEN.vector)
    gby_octa_ag.door = True
    gby_octa_ag.description = 'a staircase leading to the side door'
    gby_octa_ay = gby_octa.wall_with_direction(ANTI_YELLOW.vector)
    gby_octa_ay.description = 'three bells hung from the corners. A chest suspended in a bell in the center of the room'
    gby_octa_y = gby_octa.wall_with_direction(YELLOW.vector)
    gby_octa_y.description = 'delicate gothic arches of purple porphyry supporting the staircases. The room is full of water'
    gby_octa.name = '13.gby8'

    gy = pyraminx.get_cell(-2, 0, 0)
    gy_r = gy.wall_with_direction(RED.vector)
    gy_r.description = 'the left horn of a crescent moon'
    gy_g = gy.wall_with_direction(GREEN.vector)
    gy_g.description = 'a rectangular door. A semisphere with a map of an unknown continent'
    gy_b = gy.wall_with_direction(BLUE.vector)
    gy_b.door = True
    gy_b.description = 'the right horn of a crescent moon'
    gy_y = gy.wall_with_direction(YELLOW.vector)
    gy_y.description = 'slabs of black lava rock t: 5'
    gy.name = '14.gy'

    gby = pyraminx.get_cell(-2, -2, 2)
    gby_r = gby.wall_with_direction(RED.vector)
    gby_r.door = True
    gby_y = gby.wall_with_direction(YELLOW.vector)
    gby_y.description = 'a wheel in the far corner'
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

