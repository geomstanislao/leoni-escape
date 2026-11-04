import math, random
from reg import card
from rl import *
from common import hid, tx, star_gold
import helpers as Hh
from helpers import pool, rake, clothbag, crystal, wood_sign, mud_poles, bric_side, sand_dots, bez, bric_top, WOOD, SANDY
from ra import finish


def objbg(p, H, fy, tone=('#f3e6c4', '#e2cf9f'), floor=('#d9c08a', '#b89a62'), seed=1, planks=True, glow=(107, 60, 90)):
    rnd = random.Random(seed)
    d = LGd(p + 'bg', [(0, tone[0]), (1, tone[1])]) + LGd(p + 'fl', [(0, floor[0]), (1, floor[1])]) + RGd(p + 'gw', [(0, '#fff6d0', .9), (1, '#fff6d0', 0)])
    b = [R(0, 0, 215, H, U(p + 'bg'), stroke='none')]
    b.append(C(glow[0], glow[1], glow[2], U(p + 'gw'), stroke='none'))
    # soft wall pattern: faint dots
    for i in range(26):
        b.append(C(rnd.uniform(4, 211), rnd.uniform(4, fy - 6), rnd.uniform(.8, 1.8), '#ffffff', stroke='none', opacity=.35))
    b.append(P('M0 %s Q107 %s 215 %s L215 %s L0 %s Z' % (fy, fy - 6, fy, H, H), U(p + 'fl'), stroke='none'))
    if planks:
        for k, y in enumerate([fy + 8, fy + 18, fy + 29]):
            if y < H:
                b.append(PLn('M0 %s Q107 %s 215 %s' % (y, y - 4, y), '#8a6a3a', 1, .35))
        for k in range(8):
            x = k * 30 + 8
            b.append(PLn('M%s %s l-4 %s' % (x, fy + 4, H - fy), '#8a6a3a', 1, .2))
    b.append(PLn('M0 %s Q107 %s 215 %s' % (fy, fy - 6, fy), '#ffffff', 1.5, .5))
    return d, b


def sparkle_set(pts):
    return [sparkle4(x, y, r) for (x, y, r) in pts]


@card(40)
def c40(p):
    H = 120
    d, b = objbg(p, H, 92, ('#efdfb8', '#d9c08c'), ('#c9ad7c', '#9c805a'), 3, True, (107, 56, 90))
    b += [shadow(107, 102, 88, 8, .35), shadow(112, 100, 70, 4, .2)]
    # straw/sawdust bits
    rnd = random.Random(4)
    for i in range(18):
        x = rnd.uniform(10, 205); y = rnd.uniform(96, 117)
        b += [PLn('M%s %s l%s %s' % (f(x), f(y), f(rnd.uniform(3, 7)), f(rnd.uniform(-1, 1))), '#d9bf70', 1.3, .8)]
    spec_p = [(-3, 20, 150, -3), (4, 34, 150, 2), (-4, 48, 152, -1), (2, 62, 148, 3), (-2, 76, 150, 0)]
    pls = []
    for (xo, yo, ln, rot) in spec_p:
        pls.append(mud_poles(104 + xo * 3, 16 + yo, ln, rot, w=13))
    b += [lit(p, *pls)]
    # bark highlights and knots
    for (xo, yo, ln, rot) in spec_p:
        x, y = 104 + xo * 3, 16 + yo
        b += [G(PLn('M%s -4 L%s -4' % (f(-ln / 2 + 14), f(ln / 2 - 50)), '#e6c28a', 1.3, .6), E(-ln / 2 + 40, 1, 2, 1.2, '#6b3e1c', stroke='none', opacity=.7), E(ln / 6, -1, 1.6, 1, '#6b3e1c', stroke='none', opacity=.6),
                 transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))]
    # rope tie
    b += [P('M80 22 Q76 62 80 104', 'none', stroke='#7a5a30', stroke_width=3.2, stroke_linecap='round'), P('M80 22 Q76 62 80 104', 'none', stroke='#d9b878', stroke_width=1.2, stroke_dasharray='3 2.5', stroke_linecap='round')]
    b += [sparkle4(30, 30, 4), sparkle4(188, 40, 3.5), sparkle4(174, 14, 3)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


@card(10)
def c10(p):
    H = 120
    d, b = objbg(p, H, 98, ('#f0e0b8', '#dcc48f'), ('#cdb080', '#a58a5e'), 5, True, (100, 62, 88))
    b += [shadow(98, 108, 62, 6, .38)]
    d += LGd(p + 'mh', [(0, '#c99058'), (.5, '#a8703f'), (1, '#7a4a26')], 0, 0, 1, 1) + LGd(p + 'mw', [(0, '#a06a3a'), (.5, '#c9985e'), (1, '#7a4a26')], 0, 0, 1, 0)
    m = [R(-3.5, -52, 7, 56, U(p + 'mw'), stroke=OUT, stroke_width=2.2, rx=2), PLn('M-1 -48 L-1 0', '#e6c28a', 1, .6),
         R(-20, -76, 40, 28, U(p + 'mh'), stroke=OUT, stroke_width=2.2, rx=4),
         PLn('M-12 -76 L-12 -48 M12 -76 L12 -48', '#6e4020', 2.2), PLn('M-17 -66 L17 -66', '#e6c28a', 1.6, .8),
         PLn('M-17 -70 q6 -2 12 0 q6 2 12 0 q6 -2 8 0', '#6e4020', .9, .7), PLn('M-17 -58 q6 2 12 0 q6 -2 12 0 q6 2 8 0', '#6e4020', .9, .7),
         R(-19, -75, 38, 4, '#ffffff', stroke='none', rx=2, opacity=.25), E(0, -50, 4.2, 1.4, '#3b2416', stroke='none', opacity=.4), C(-15, -62, 1.2, '#4a2c16', stroke='none')]
    b += [lit(p, G(*m, stroke_linejoin='round', stroke_linecap='round', transform='translate(78 108) rotate(62) scale(1.2)'))]
    b += [star_gold(176, 34, 6, '#fff6cf'), star_gold(34, 30, 5, '#fff6cf'), sparkle4(150, 70, 4), sparkle4(50, 70, 3), sparkle4(120, 20, 3)]
    rnd = random.Random(6)
    for i in range(10):
        x = rnd.uniform(120, 200); y = rnd.uniform(102, 116)
        b += [PLn('M%s %s l5 -1' % (f(x), f(y)), '#d9bf70', 1.2, .7)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


@card(16)
def c16(p):
    H = 120
    d, b = objbg(p, H, 98, ('#f2e6c8', '#e0cc9c'), ('#d4bd8c', '#a98f62'), 7, True, (107, 56, 90))
    b += [shadow(107, 104, 62, 7, .38)]
    d += LGd(p + 'cb', [(0, '#f4e9c8'), (1, '#cdb88a')], 0, 0, 1, 0)
    b += [lit(p, clothbag(107, 62, 1.18))]
    # cloth weave + highlights over bag
    b += [G(PLn('M-26 24 Q-24 4 -14 -8', '#ffffff', 2, .5), PLn('M-30 30 Q-34 10 -22 -6', '#ffffff', 1.2, .4), E(-8, 10, 6, 18, '#ffffff', stroke='none', opacity=.14), E(20, 20, 10, 20, '#8a6a3a', stroke='none', opacity=.12),
            transform='translate(107 62) scale(1.18)')]
    for (x, y, k) in [(52, 106, 1.3), (66, 111, 1.0), (152, 108, 1.3), (168, 104, 1.0), (140, 113, 0.9), (86, 112, .8), (126, 114, .8)]:
        b += [lit(p, crystal(x, y, k)), E(x + 3, y + 5 * k, 5 * k, 1.4, '#3b2416', stroke='none', opacity=.2)]
    b += [star_gold(34, 34, 6, '#fff6cf'), star_gold(184, 40, 7, '#fff6cf'), star_gold(172, 76, 4, '#fff6cf'), sparkle4(80, 24, 4), sparkle4(150, 20, 3), sparkle4(22, 70, 3)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


@card(7)
def c7(p):
    H = 120
    d, b = objbg(p, H, 100, ('#f6e8c4', '#e8d3a0'), ('#d8c08c', '#b09462'), 9, True, (116, 60, 80))
    d += rgrad_def(p + 'gl', '#ffe27a', 1)
    # light rays
    for k in range(12):
        a = -math.pi / 2 + (k - 5.5) * .24
        b.append(P('M122 64 L%s %s L%s %s Z' % (f(122 + 120 * math.cos(a - .04)), f(64 + 120 * math.sin(a - .04)), f(122 + 120 * math.cos(a + .04)), f(64 + 120 * math.sin(a + .04))), '#fff1b0', stroke='none', opacity=.18))
    b += [C(116, 60, 64, 'url(#%sgl)' % p, stroke='none')]
    b += [shadow(48, 108, 26, 4, .35), shadow(138, 108, 20, 3, .3)]
    b += [lit(p, leo(48, 74, 0.64, wing='small', ra=(54, -6), mouth='smile'))]
    d += LGd(p + 'ox', [(0, '#ffb04a'), (1, '#e07a1c')], 0, 0, 1, 0)
    oar = [P('M0 -62 L0 -52', 'none', stroke=OUT, stroke_width=3), C(0, -68, 7, 'none', stroke='#9aa0a8', stroke_width=3), C(0, -68, 7, 'none', stroke='#e6eaee', stroke_width=1, stroke_dasharray='6 30'),
           C(-3, -52, 4, 'none', stroke='#9aa0a8', stroke_width=2.4),
           R(-4, -48, 8, 68, U(p + 'ox'), rx=3), P('M-10 14 Q-12 40 0 50 Q12 40 10 14 Z', '#f5a03c'), P('M0 16 L0 46', 'none', stroke='#c9701c', stroke_width=1.2, opacity=.7),
           P('M-4 -44 L-4 14', 'none', stroke='#ffe08a', stroke_width=1.8), P('M-7 20 Q-9 36 -3 44', 'none', stroke='#ffe08a', stroke_width=1.4, opacity=.8)]
    b += [lit(p, G(*oar, stroke=OUT, stroke_width=2.4, stroke_linejoin='round', stroke_linecap='round', transform='translate(122 64) rotate(24)'))]
    for (sx, sy, sr) in [(92, 22, 6), (170, 32, 7), (176, 92, 5), (86, 100, 5), (150, 14, 4)]:
        b += [star_gold(sx, sy, sr)]
    b += [sparkle4(110, 30, 4), sparkle4(144, 50, 4), sparkle4(100, 80, 3), sparkle4(188, 62, 3), sparkle4(130, 100, 3)]
    H, d, body = finish(p, H, d, b, .28)
    return H, d, body, ''


@card(4)
def c4(p):
    H = 120
    d = LGd(p + 'tb', [(0, '#e8c995'), (1, '#c9a064')]) + LGd(p + 'bg', [(0, '#f6e8c0'), (1, '#e3cc98')], 0, 0, 1, 1) + LGd(p + 'pk', [(0, '#f6e5bd'), (1, '#d4bd8a')], 0, 0, 1, 0) + LGd(p + 'ct', [(0, '#4f9a90'), (1, '#2f6a62')]) + lit_defs(p) + RGd(p + 'gw', [(0, '#fff6d0', .8), (1, '#fff6d0', 0)])
    b = [R(0, 0, 215, H, U(p + 'tb'), stroke='none')]
    rnd = random.Random(12)
    for y in (16, 38, 60, 82, 104):
        b.append(PLn('M0 %s Q107 %s 215 %s' % (y, y - 3, y), '#8a6a3a', 1.2, .4))
    for i in range(40):
        x = rnd.uniform(0, 215); y = rnd.uniform(0, 120)
        b.append(PLn('M%s %s l%s 0' % (f(x), f(y), f(rnd.uniform(8, 22))), '#9a7440', .8, .35))
    b.append(C(107, 55, 90, U(p + 'gw'), stroke='none'))
    b += [P('M0 104 Q107 96 215 104 L215 120 L0 120 Z', '#a8803f', stroke='none', opacity=.25)]
    # Nico backpack
    b += [shadow(47, 106, 46, 6, .4)]
    bag = [R(8, 32, 78, 68, U(p + 'pk'), rx=14, stroke=OUT, stroke_width=2.4),
           P('M10 70 Q8 90 22 98 L72 98 Q84 90 84 72 Q50 82 10 70 Z', '#c9b080', stroke='none', opacity=.5),
           E(47, 36, 37, 9, '#5a4630', stroke=OUT, stroke_width=2.2), E(47, 38, 30, 6, '#3d2e1e', stroke='none'), P('M20 36 Q47 44 74 36', 'none', stroke='#8a6a46', stroke_width=1.2),
           P('M14 56 Q47 66 80 56', 'none', stroke='#b8a47a', stroke_width=2),
           R(20, 64, 54, 30, '#e6d3a6', rx=8, stroke=OUT, stroke_width=2), P('M24 70 L70 70', 'none', stroke='#b8a47a', stroke_width=1.6, stroke_dasharray='3 2'),
           P('M24 90 L70 90', 'none', stroke='#b8a47a', stroke_width=1, stroke_dasharray='2 2', opacity=.7),
           C(58, 71, 3.2, 'none', stroke='#6a6e76', stroke_width=2), R(56, 73, 4, 3, '#6a6e76'), C(58, 80, 2.6, 'none', stroke='#6a6e76', stroke_width=1.8),
           PLn('M15 40 Q12 60 14 78', '#ffffff', 2, .5), R(10, 94, 12, 8, '#b8a47a', rx=2, stroke=OUT, stroke_width=1.4), R(72, 94, 12, 8, '#b8a47a', rx=2, stroke=OUT, stroke_width=1.4)]
    b += [lit(p, *bag)]
    ok = [P('M58 83 L66 108', 'none', stroke=OUT, stroke_width=7, stroke_linecap='round'), P('M58 83 L66 108', 'none', stroke='#f08a24', stroke_width=4, stroke_linecap='round'),
          P('M59 85 L65 104', 'none', stroke='#ffd08a', stroke_width=1.2, stroke_linecap='round'),
          E(68, 112, 5.5, 8.5, '#f08a24', stroke=OUT, stroke_width=2, transform='rotate(14 68 112)'), E(67, 110, 1.8, 4, '#ffd08a', stroke='none', transform='rotate(14 68 112)')]
    b += [lit(p, *ok)]
    # Sofia notebook
    b += [shadow(156, 114, 52, 5, .4)]
    b += [E(156, 78, 44, 12, U(p + 'ct'), stroke=OUT, stroke_width=2.2)]
    nb = [R(104, 14, 50, 78, '#fffdf5', rx=2, stroke=OUT, stroke_width=2), R(154, 14, 52, 78, '#fffdf5', rx=2, stroke=OUT, stroke_width=2),
          R(150, 14, 8, 78, '#d9d2bc', stroke='none', opacity=.5), PLn('M154 14 L154 92', '#8a8470', 1.2, .8)]
    for yy in (24, 32, 40, 48, 56, 64, 72):
        nb += [L(110, yy, 148 - (yy % 3) * 6, yy, '#b8bcc4', 1.6)]
    for xx in (110, 120, 130, 140):
        nb += [C(xx, 18, 1.5, '#6a6e76', stroke='none')]
    nb += [P('M160 62 q5 -3 10 0 q5 3 10 0 q5 -3 10 0 q5 3 10 0', 'none', stroke='#4f74a8', stroke_width=1.6, stroke_linecap='round')]
    nb += [bric_side(166, 60, 18, '#4a3a2a', 2.2, '#8a6a3a'), bric_side(185, 54, 18, '#4a3a2a', 2.2, '#8a6a3a'), bric_side(166, 38, 15, '#4a3a2a', 2, '#8a6a3a'), bric_side(188, 32, 15, '#4a3a2a', 2, '#8a6a3a')]
    nb += [P('M174 30 q4 6 -2 14 q-4 8 2 16 M182 24 q4 6 -2 12', 'none', stroke='#4f74a8', stroke_width=1.1, stroke_dasharray='2 2', opacity=.8)]
    b += [lit(p, *nb)]
    b += [P('M110 96 Q156 108 202 96 L204 114 Q204 118 198 118 L110 118 Q106 118 106 114 Z', U(p + 'ct'), stroke=OUT, stroke_width=2.2, stroke_linejoin='round')]
    b += [R(132, 100, 48, 14, '#4a9086', rx=5, stroke=OUT, stroke_width=1.8), PLn('M112 100 Q156 110 200 100', '#8ad0c4', 1.4, .6)]
    # pencil
    b += [G(R(0, 0, 40, 4.5, '#e8b83a', stroke=OUT, stroke_width=1.4, rx=1), P('M40 0 L47 2.2 L40 4.5 Z', '#f0d7a8', stroke=OUT, stroke_width=1.2), P('M44 1.2 L47 2.2 L44 3.3 Z', '#3b2416', stroke='none'), R(0, 0, 6, 4.5, '#d9604a', stroke=OUT, stroke_width=1.2),
            transform='translate(96 104) rotate(-12)')]
    b += [sparkle4(98, 12, 3), sparkle4(8, 18, 3)]
    H, d, body = finish(p, H, d, b, .28)
    return H, d, body, ''


@card(11)
def c11(p):
    H = 110
    d = LGd(p + 'ds', [(0, '#d8bd8e'), (1, '#b89868')]) + LGd(p + 'pp', [(0, '#fffef8'), (1, '#f4eedc')], 0, 0, 1, 1) + lit_defs(p)
    b = [R(0, 0, 215, H, U(p + 'ds'), stroke='none')]
    rnd = random.Random(21)
    for y in (14, 40, 66, 92):
        b.append(PLn('M0 %s Q107 %s 215 %s' % (y, y - 3, y), '#8a6a3a', 1, .3))
    b += [R(13, 9, 195, 98, '#3b2416', rx=3, stroke='none', opacity=.25)]
    b += [R(10, 6, 195, 98, U(p + 'pp'), rx=3, stroke=OUT, stroke_width=2)]
    b += [R(10, 6, 12, 98, '#e8e0c8', stroke='none', opacity=.7), PLn('M26 8 L26 102', '#e08a8a', 1.2, .8)]
    for k in range(6):
        b += [C(15, 14 + k * 15, 3.2, '#8a6a3a', stroke=OUT, stroke_width=1.2), C(14.2, 13.2 + k * 15, 1, '#e6c88a', stroke='none')]
    for yy in range(18, 100, 9):
        b += [L(28, yy, 203, yy, '#dfe6ee', 1)]
    # channel
    b += [P('M44 98 C72 80 70 58 104 48 C140 38 150 24 190 14', 'none', stroke='#c9e4f2', stroke_width=30, stroke_linecap='round', opacity=.6)]
    b += [P('M44 98 C72 80 70 58 104 48 C140 38 150 24 190 14', 'none', stroke='#a9d3e8', stroke_width=26, stroke_linecap='round'),
          P('M44 98 C72 80 70 58 104 48 C140 38 150 24 190 14', 'none', stroke='#8cc0dc', stroke_width=14, stroke_linecap='round', opacity=.5),
          P('M44 98 C72 80 70 58 104 48 C140 38 150 24 190 14', 'none', stroke='#4f74a8', stroke_width=1.4, stroke_dasharray='4 3')]
    for (x, y) in [(46, 82), (62, 64), (92, 38), (126, 26), (168, 12)]:
        b += [P('M%s %s q4 -3 8 0 q4 3 8 0' % (f(x), f(y)), 'none', stroke='#4f74a8', stroke_width=1.3, stroke_linecap='round')]
    s1 = ((44, 98), (72, 80), (70, 58), (104, 48))
    s2 = ((104, 48), (140, 38), (150, 24), (190, 14))
    first = None
    br = []
    for (seg, ts) in ((s1, (0.2, 0.55, 0.9)), (s2, (0.35, 0.7, 1.0))):
        for t in ts:
            x, y, nx, ny = bez(*seg, t)
            for sgn in (-1, 1):
                gx, gy2 = x + sgn * nx * 17, y + sgn * ny * 17
                if first is None and gx < x:
                    first = (gx, gy2)
                br.append(E(gx + 2, gy2 + 8, 7, 2, '#3b2416', stroke='none', opacity=.25))
                br.append(bric_side(gx, gy2 + 7, 14, '#4a3a2a', 2.1, '#c8483a'))
    b += br
    # shoal
    d += LGd(p + 'sh', [(0, '#fbeeb0'), (1, '#e3c970')])
    b += [E(176, 84, 22, 9, U(p + 'sh'), stroke='#8a6a3a', stroke_width=1.3, stroke_dasharray='3 2'), sand_dots(176, 84, 20, 8, 2, 14), PLn('M160 88 q6 -2 12 0 M182 80 q6 -2 12 0', '#c9a64a', 1.2, .8)]
    b += [tx('secca', 176, 101, 8.5, '#6a4a2a')]
    b += [tx('briccole', 58, 22, 11, '#a8322a')]
    b += [P('M56 27 Q%s %s %s %s' % (f(first[0]), f(first[1] - 26), f(first[0] + 2), f(first[1] - 12)), 'none', stroke='#a8322a', stroke_width=1.4, stroke_linecap='round'), P('M%s %s l-3 -7 M%s %s l5 -5' % (f(first[0] + 2), f(first[1] - 12), f(first[0] + 2), f(first[1] - 12)), 'none', stroke='#a8322a', stroke_width=1.4, stroke_linecap='round')]
    # pencil and page curl
    b += [P('M205 104 Q196 104 195 95 Q205 97 205 104 Z', '#e8dfc4', stroke=OUT, stroke_width=1.2)]
    b += [G(R(0, 0, 44, 5, '#e05a3a', stroke=OUT, stroke_width=1.4, rx=1), P('M44 0 L52 2.5 L44 5 Z', '#f0d7a8', stroke=OUT, stroke_width=1.2), P('M49 1.4 L52 2.5 L49 3.6 Z', '#3b2416', stroke='none'),
            R(0, 0, 7, 5, '#c9ccd2', stroke=OUT, stroke_width=1.2), transform='translate(120 94) rotate(-6)')] if False else []
    H, d, body = finish(p, H, d, b, .22)
    return H, d, body, ''
