import math, random
from reg import card
from rl import *
from common import hid, tx, star_gold
import helpers as Hh
from helpers import pool, rake, crystal, wood_sign, bez, bric_top, sand_dots, WOOD, SANDY
from ra import finish


def bric_top2(x, y, r=1.0):
    return G(E(x + 2.2, y + 4.2, 6.4 * r, 2.6 * r, '#1d4a62', stroke='none', opacity=.35), bric_top(x, y, r))


@card(9)
def c9(p):
    H = 180
    ch_out, ch_in = '#2f6f8e', '#6fc0dc'
    mid = ((107, 150), (112, 115), (102, 85), (107, 50))
    lef = ((107, 150), (80, 148), (40, 125), (40, 80))
    rig = ((107, 150), (134, 148), (174, 125), (174, 80))

    def pth(c):
        return 'M%s %s C%s %s %s %s %s %s' % (c[0][0], c[0][1], c[1][0], c[1][1], c[2][0], c[2][1], c[3][0], c[3][1])
    d = LGd(p + 'mf', [(0, '#d3cda4'), (1, '#b9b184')], 0, 0, 1, 1) + LGd(p + 'sh', [(0, '#fbeeb0'), (1, '#e3c970')]) + LGd(p + 'is', [(0, '#a9c668'), (1, '#6f9a44')]) + LGd(p + 'bt', [(0, '#c98a4e'), (1, '#8e5a2a')], 0, 0, 1, 0) + lit_defs(p)
    b = [R(0, 0, 215, H, U(p + 'mf'), stroke='none')]
    rnd = random.Random(11)
    # mudflat texture (no digits, no confusion)
    for i in range(40):
        mx, my = rnd.uniform(4, 205), rnd.uniform(4, 176)
        b.append(P('M%s %s q5 -2 10 0' % (f(mx), f(my)), 'none', stroke='#a89f74', stroke_width=1.3, stroke_linecap='round', opacity=.8))
    for i in range(24):
        b.append(E(rnd.uniform(0, 215), rnd.uniform(0, 180), rnd.uniform(6, 16), rnd.uniform(1.5, 3), '#8f885f', stroke='none', opacity=.22))
    # reed/grass clumps at map edges (seen from above)
    for (cx, cy) in [(8, 100), (10, 128), (205, 100), (203, 130), (8, 60), (207, 62), (22, 150), (190, 150)]:
        b.append(G(*[PLn('M%s %s l%s %s' % (f(cx), f(cy), f(5 * math.cos(a)), f(5 * math.sin(a))), '#6f8a46', 1.6) for a in (0, 1.1, 2.2, 3.3, 4.4, 5.5)]))
    # shallow halo then channels
    for c in (lef, rig, mid):
        b.append(P(pth(c), 'none', stroke='#a9d8e2', stroke_width=29, stroke_linecap='round', opacity=.55))
    for c in (lef, rig, mid):
        b.append(P(pth(c), 'none', stroke=ch_out, stroke_width=22, stroke_linecap='round'))
    for c in (lef, rig, mid):
        b.append(P(pth(c), 'none', stroke=ch_in, stroke_width=17, stroke_linecap='round'))
    for c in (lef, rig, mid):
        b.append(P(pth(c), 'none', stroke='#4aa0c4', stroke_width=7, stroke_linecap='round', opacity=.45))
    for c in (lef, rig, mid):
        b.append(P(pth(c), 'none', stroke='#ffffff', stroke_width=1.4, stroke_dasharray='4 6', opacity=0.8))
    # shoals
    for (cx, cy, sd) in [(40, 74, 3), (174, 74, 5)]:
        b.append(E(cx + 2, cy + 3, 26, 14, '#6b5a2a', stroke='none', opacity=.25))
        b.append(E(cx, cy, 24, 13, U(p + 'sh'), stroke='#a8802c', stroke_width=2, stroke_dasharray='4 2.5'))
        b.append(E(cx - 4, cy - 4, 14, 5, '#ffffff', stroke='none', opacity=.35))
        b.append(sand_dots(cx, cy, 21, 10, sd, 16, '#9a7424'))
        b.append(P('M%s %s q5 -3 10 0 M%s %s q5 -3 10 0' % (f(cx - 14), f(cy - 3), f(cx + 2), f(cy + 5)), 'none', stroke='#c9a64a', stroke_width=1.6, stroke_linecap='round'))
    # briccole: middle route
    for t in (0.22, 0.34, 0.46, 0.58, 0.7, 0.82, 0.92):
        x, y, nx, ny = bez(*mid, t)
        for sgn in (-1, 1):
            b.append(bric_top2(x + sgn * nx * 14, y + sgn * ny * 14))
    # left route: briccole only at the start
    for t in (0.4, 0.52):
        x, y, nx, ny = bez(*lef, t)
        for sgn in (-1, 1):
            b.append(bric_top2(x + sgn * nx * 14, y + sgn * ny * 14))
    # islands
    for (cx, num) in [(40, 21), (107, 26), (174, 29)]:
        b.append(E(cx, 34, 31, 21, '#3a5a68', stroke='none', opacity=.3))
        b.append(E(cx, 31, 29, 21, '#a9926a', stroke=OUT, stroke_width=2.2))
        b.append(E(cx, 29, 25, 17, U(p + 'is'), stroke='none'))
        b.append(E(cx - 6, 24, 12, 6, '#c4dc86', stroke='none', opacity=.5))
        for k in (-18, 16):
            b.append(P('M%s 40 q-1 -7 -4 -11 M%s 40 q1 -7 4 -11' % (f(cx + k), f(cx + k)), 'none', stroke='#4a6a2a', stroke_width=1.8, stroke_linecap='round'))
        for (bx, by) in [(cx - 22, 30), (cx + 22, 29), (cx + 18, 40), (cx - 16, 41)]:
            b.append(C(bx, by, 3.6, '#4f7f36', stroke=OUT, stroke_width=1.2))
            b.append(C(bx - 1, by - 1, 1.4, '#8ab85a', stroke='none'))
        b.append(wood_sign(cx - 15, 12, 30, 19, num, 13, 8))
    # boat (top view)
    b.append(E(109, 160, 14, 18, '#1d4a62', stroke='none', opacity=.3))
    b.append(P('M107 142 Q121 158 107 174 Q93 158 107 142 Z', U(p + 'bt'), stroke=OUT, stroke_width=2.2, stroke_linejoin='round'))
    b.append(P('M101 156 L113 156 M101 162 L113 162', 'none', stroke='#7a4a22', stroke_width=1.6))
    b.append(P('M107 146 L107 172', 'none', stroke='#e0b27a', stroke_width=1, opacity=.7))
    b.append(P('M96 154 L84 160 M118 154 L130 160', 'none', stroke=OUT, stroke_width=2.4, stroke_linecap='round'))
    b.append(E(83, 161, 4, 2, '#b98a55', stroke=OUT, stroke_width=1.3, transform='rotate(-20 83 161)'))
    b.append(E(131, 161, 4, 2, '#b98a55', stroke=OUT, stroke_width=1.3, transform='rotate(20 131 161)'))
    b.append(P('M100 176 q4 3 8 0 q4 -3 8 0', 'none', stroke='#ffffff', stroke_width=1.4, opacity=.8))
    # legend
    b.append(R(5, 164, 60, 14, '#fffdf0', rx=4, stroke='none', opacity=.55))
    b.append(R(150, 164, 60, 14, '#fffdf0', rx=4, stroke='none', opacity=.55))
    b.append(bric_top(12, 172, 0.95))
    b.append(tx('briccole', 22, 175, 8.5, '#2a1a10', 'start'))
    b.append(E(158, 172, 8, 5, SANDY, stroke='#a8802c', stroke_width=1.4, stroke_dasharray='3 2'))
    b.append(tx('secca', 169, 175, 8.5, '#2a1a10', 'start'))
    H, d, body = finish(p, H, d, b, .18)
    return H, d, body, ''


def pool2(p, x, y, w, h, mode, seed=1, cs=1.0):
    s = [E(x + w / 2, y + h + 4, w * .55, 4, '#6b5530', stroke='none', opacity=.3), pool(x, y, w, h, mode, seed, cs)]
    # wooden rim detail
    s.append(PLn('M%s %s L%s %s' % (f(x + 3), f(y + 2), f(x + w - 3), f(y + 2)), '#d9b078', 1.4, .7))
    s.append(PLn('M%s %s L%s %s' % (f(x + 2), f(y + 3), f(x + 2), f(y + h - 3)), '#d9b078', 1.2, .6))
    for k in range(1, 4):
        s.append(PLn('M%s %s l0 3 M%s %s l0 -3' % (f(x + w * k / 4), f(y), f(x + w * k / 4), f(y + h)), '#6b4a2a', 1.2, .8))
    # inner shadow (top-left light)
    s.append(R(x + 4, y + 4, w - 8, 6, '#1f3a4a', rx=2, stroke='none', opacity=.16))
    s.append(R(x + 4, y + 4, 5, h - 8, '#1f3a4a', rx=2, stroke='none', opacity=.10))
    if mode == 'water':
        s.append(PLn('M%s %s l8 -2' % (f(x + w - 18), f(y + h - 12)), '#ffffff', 1.6, .9))
        s.append(E(x + w - 14, y + 12, 8, 3, '#ffffff', stroke='none', opacity=.3))
    if mode == 'half':
        s.append(E(x + 14, y + 14, 11, 4, '#fff6c0', stroke='none', opacity=.35))
    return G(*s)


@card(32)
def c32(p):
    H = 160
    d = LGd(p + 'sk', [(0, '#6fc0ea'), (1, '#e8f4ee')]) + RGd(p + 'sun', [(0, '#fff2b8', 1), (1, '#fff2b8', 0)]) + LGd(p + 'gd', [(0, '#e6d3a0'), (1, '#c9b27c')]) + LGd(p + 'sea', [(0, '#a9dcec'), (1, '#5fb0cc')]) + lit_defs(p)
    b = [R(0, 0, 215, H, U(p + 'sk'), stroke='none')]
    for (cx, cy, cs) in [(100, 10, .7), (180, 6, .5)]:
        b.append(cloud2(cx, cy, cs))
    # far hills and horizon
    b.append(P('M0 36 Q30 24 70 32 T130 30 L130 42 L0 42 Z', '#a9c7b0', stroke='none', opacity=.8))
    # lagoon inlet at right (sea feeding the channel)
    b.append(R(120, 24, 95, 18, U(p + 'sea'), stroke='none'))
    b.append(P('M138 30 q5 -3 10 0 q5 3 10 0 M180 34 q5 -3 10 0 q5 3 10 0 M156 38 q5 -3 10 0 q5 3 10 0', 'none', stroke='#ffffff', stroke_width=1.8, stroke_linecap='round', opacity=.9))
    # ground
    b.append(R(0, 40, 215, 120, U(p + 'gd'), stroke='none'))
    b.append(P('M0 40 Q60 36 120 42 L215 42', 'none', stroke=OUT, stroke_width=2))
    rnd = random.Random(32)
    for i in range(30):
        b.append(E(rnd.uniform(0, 215), rnd.uniform(46, 158), rnd.uniform(6, 16), rnd.uniform(1.2, 2.6), '#a8905a', stroke='none', opacity=.3))
    for i in range(40):
        b.append(C(rnd.uniform(2, 213), rnd.uniform(46, 158), rnd.uniform(.6, 1.3), rnd.choice(['#f6edd0', '#a8905a', '#8c7552']), stroke='none', opacity=.7))
    # channel for pool 4 (same place)
    b += [R(166, 40, 20, 16, '#6fb8d2', stroke=OUT, stroke_width=1.8), R(167, 38, 18, 4, '#6fb8d2', stroke='none')]
    b += [R(169, 40, 14, 14, '#8cd0e4', stroke='none', opacity=.7)]
    for yy in (42, 49):
        b += [P('M171 %s l5 5 l5 -5' % f(yy), 'none', stroke='#ffffff', stroke_width=2, stroke_linecap='round')]
    # sun above first pool
    b += [C(36, 20, 30, U(p + 'sun'), stroke='none')]
    for k in range(10):
        a = k * math.pi / 5
        b += [L(36 + 12 * math.cos(a), 20 + 12 * math.sin(a), 36 + 19 * math.cos(a), 20 + 19 * math.sin(a), '#f2a900', 2.2, stroke_linecap='round')]
    b += [C(36, 20, 10, '#ffd23c', stroke=OUT, stroke_width=2), C(33, 17, 4, '#fff6c0', stroke='none', opacity=.7)]
    # heat shimmer over pool 1
    b += [PLn('M16 50 q4 -5 0 -10 q-4 -5 0 -10', '#ffffff', 1.4, .5), PLn('M56 50 q4 -5 0 -10', '#ffffff', 1.4, .5)]
    # pools (same layout)
    b += [lit(p, pool2(p, 6, 54, 60, 58, 'half', 1))]
    b += [lit(p, pool2(p, 77, 54, 60, 58, 'crystal', 2, 1.0))]
    b += [lit(p, pool2(p, 148, 54, 60, 58, 'water'))]
    b += [P('M170 56 q-6 6 -4 10 M182 56 q6 6 4 10', 'none', stroke='#ffffff', stroke_width=2, stroke_linecap='round'), C(176, 62, 3, '#ffffff', stroke=OUT, stroke_width=1)]
    b += [PLn('M158 66 q4 -3 8 0 M188 68 q4 -3 8 0', '#ffffff', 1.6, .9)]
    b += [lit(p, rake(104, 98, 52))]
    # salt mounds at the foot, sandy walkways between pools
    for (x, y, s_) in [(68, 118, 1.0), (140, 118, 1.0)]:
        b += [G(P('M-9 0 Q-6 -9 0 -10 Q6 -9 9 0 Z', '#ffffff', stroke=OUT, stroke_width=1.3), PLn('M-4 -3 l2 -3 M2 -6 l2 2', '#c8d6dc', 1), transform='translate(%s %s) scale(%s)' % (x, y, s_))]
    # signs
    for (cx, num) in [(36, 7), (107, 1), (178, 4)]:
        b += [E(cx, 150, 18, 3, '#6b5530', stroke='none', opacity=.3), wood_sign(cx - 16, 120, 32, 28, num, 22, 10)]
    H, d, body = finish(p, H, d, b, .2)
    return H, d, body, ''
