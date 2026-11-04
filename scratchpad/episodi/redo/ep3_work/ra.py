import math, random
from reg import card
from rl import *
from common import hid, tx, star_gold

def full(p, H, hz, gs, tone='day', sun=None, seed=1, tower=None, clouds=((.22, .32, .85), (.72, .22, .7), (.5, .48, .5)), shore_on=True, ripples=16, gcol=('#cdb68a', '#a98d62'), boats=True, birds=True):
    d1, b1 = sky_scene(p, 215, hz, tone, sun, seed, clouds, tower, birds, boats)
    d2, b2 = water_scene(p, 215, hz, gs if shore_on else H, tone, sun, seed, ripples)
    d = d1 + d2 + lit_defs(p)
    b = b1 + b2
    if shore_on:
        d3, b3 = shore(p, 215, H, gs, seed + 1, gcol[0], gcol[1])
        d += d3
        b += b3
    return d, b

def finish(p, H, d, b, vs=.3, after=()):
    vd, vr = vignette(p, 215, H, vs)
    return H, d + vd, ''.join(b) + vr + ''.join(after)

@card(1)
def c1(p):
    H = 120
    d, b = full(p, H, 56, 94, 'day', (170, 24, 8), 3, tower=186)
    b += [B.smoke(176, 58, 34, 7, '#9a9aa4', 0.55)]
    b += [sail(60, 60, .9), sail(120, 58, .7)]
    b += [reedbed2(0, 78, 100, 44, 5, 1.2), reedbed2(140, 215, 101, 40, 8, 1.2)]
    b += [C(104, 56, 46, '#ffe9a0', stroke='none', opacity=.28)]
    b += [shadow(104, 112, 36, 6, .35)]
    b += [lit(p, leo(104, 73, 0.82, wing='small', ra=(40, -26), mouth='smile'))]
    b += [PLn('M40 116 q10 -3 18 0', '#9c8560', 2)]
    b += [sparkle4(60, 40, 4), sparkle4(150, 50, 3), sparkle4(80, 80, 3)]
    b += [reedbed2(0, 30, 119, 26, 21, .9, False), reedbed2(185, 215, 119, 24, 22, .9, False)]
    b += [A.tuft(30, 112, 1.0), A.tuft(185, 114, 1.0)]
    H, d, body = finish(p, H, d, b)
    return H, d, body, ''

@card(3)
def c3(p):
    H = 120
    d, b = full(p, H, 52, 96, 'day', (36, 20, 7), 5, tower=170)
    b += [reedbed2(0, 56, 100, 48, 3, 1.2), reedbed2(160, 215, 100, 46, 9, 1.2)]
    b += [C(107, 50, 40, '#ffe9a0', stroke='none', opacity=.22)]
    b += [shadow(107, 113, 24, 4.5, .35)]
    b += [lit(p, B.elena(107, 58, 0.86, expr='smile', ra=(30, 22)), B.basket(131, 83, 0.62, 'fish'))]
    b += [reedbed2(0, 24, 119, 26, 21, .9, False), reedbed2(190, 215, 119, 26, 22, .9, False)]
    H, d, body = finish(p, H, d, b)
    return H, d, body, ''

@card(2)
def c2(p):
    H = 175
    d, b = full(p, H, 60, 126, 'day', (40, 22, 8), 4, tower=196)
    b += [sail(80, 62, 1.0), sail(150, 63, .8), sail(30, 61, .7)]
    b += [reedbed2(0, 44, 128, 48, 2, 1.2), reedbed2(176, 215, 128, 48, 6, 1.2)]
    # mooring posts and rope
    b += [post(8, 86, 112), post(206, 84, 110)]
    # far small boats
    b += [boat2(6, 92, 56), boat2(158, 88, 52)]
    b += [lit(p, B.bundle(24, 92, 0.8), B.bundle(176, 88, 0.8))]
    # main boat
    b += [lit(p, B.bundle(66, 112, 1.1), B.bundle(142, 112, 1.0), B.basket(152, 114, 0.7, 'fish'))]
    b += [lit(p, B.papa(107, 76, 0.5, expr='smile', la=(-34, 24), ra=(34, 26)))]
    b += [lit(p, B.bundle(120, 114, 0.9))]
    b += [boat2(50, 112, 112)]
    b += [rope(8, 90, 52, 116, 6), rope(206, 88, 162, 114, 6)]
    # drying net and barrels on shore
    b += [post(2, 130, 160, 0, 4), post(22, 134, 160, 0, 4), net(3, 134, 19, 18)]
    b += [barrel(206, 150, .8), barrel(196, 156, .7)]
    # families on shore
    folk = [(24, 150, .95, '#b8a070', False, 'bundle', '#5a4030'), (52, 164, 1.0, '#9a9a5a', False, 'basket', '#5a4030'),
            (84, 152, .9, '#a77a5a', False, 'bundle', '#3a2a20'), (150, 152, .95, '#8a9ab0', True, 'bundle', '#5a4030'),
            (184, 166, 1.0, '#b8a070', True, 'basket', '#5a4030'), (112, 168, .7, '#c9a070', False, 'bundle', '#3a2a20')]
    for (x, y, s, c, fl, ca, hr) in sorted(folk, key=lambda t: t[1]):
        b += [shadow(x, y + 1, 10 * s, 2.4, .35), lit(p, B.refugee(x, y, s, c, fl, ca, hr))]
    b += [A.tuft(16, 172, 1.0), A.tuft(200, 174, 1.0), A.tuft(125, 150, 0.8)]
    for (x, y) in [(60, 142), (96, 160), (132, 143), (170, 172)]:
        b += [PLn('M%s %s l3 1 M%s %s l3 1' % (f(x), f(y), f(x + 6), f(y + 3)), '#8c7552', 1.3, .6)]
    H, d, body = finish(p, H, d, b, .28, [hid(78, 125, 8)])
    return H, d, body, ''

@card(8)
def c8(p):
    H = 120
    d, b = full(p, H, 50, 100, 'day', (176, 22, 8), 7, tower=60)
    b += [reedbed2(0, 36, 104, 40, 4, 1.2), reedbed2(190, 215, 104, 34, 14, 1.0)]
    b += [post(150, 72, 102)]
    b += [lit(p, B.bundle(34, 70, 1.2, '#c9a85f'), B.bundle(62, 70, 1.3, '#b8a070'), B.bundle(92, 70, 1.2, '#c9a85f'), B.basket(112, 72, 0.8, 'fish'))]
    b += [boat2(14, 70, 124)]
    b += [rope(150, 78, 134, 76, 5)]
    b += [shadow(176, 107, 22, 4, .35)]
    b += [lit(p, B.papa(176, 66, 0.62, expr='worry', ra=(18, -54), la=(-34, 26)))]
    b += [barrel(130, 104, .8)]
    b += [A.tuft(150, 112, 0.9), A.tuft(205, 112, 0.9)]
    H, d, body = finish(p, H, d, b)
    return H, d, body, ''

@card(15)
def c15(p):
    H = 120
    d, b = full(p, H, 46, H, 'gold', (166, 36, 9), 9, tower=30, shore_on=False, ripples=20)
    b += [lit(p, B.egret(150, 26, 0.5, True, True), B.egret(188, 40, 0.42, True, False))]
    b += [reedbed2(0, 34, 106, 46, 2, 1.2), reedbed2(184, 215, 106, 42, 7, 1.2)]
    b += [lit(p, B.papa(52, 56, 0.4, expr='happy', la=(34, 14), ra=(40, 22)), B.refugee(74, 92, 0.55, '#9a9a5a', False, 'bundle'),
              B.elena(98, 57, 0.5, expr='smile'), B.refugee(120, 92, 0.5, '#a77a5a', False, 'basket', '#3a2a20'),
              B.nico(150, 58, 0.5, expr='happy', la=(-26, 18), ra=(30, 22), pack=False))]
    b += [boat2(24, 80, 156)]
    b += [A.oar(62, 74, 78, 112, 26), A.oar(158, 76, 174, 112, 26)]
    for (x, y, w) in [(14, 104, 40), (96, 112, 50), (170, 102, 34), (120, 100, 30)]:
        b += [A.ripple(x, y, w)]
    b += [PLn('M72 112 q5 3 10 0 M150 110 q5 3 10 0', '#ffffff', 2, .8)]
    b += [lily(10, 112, 1), lily(204, 114, 1.1)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''

@card(21)
def c21(p):
    H = 120
    d, b = full(p, H, 48, H, 'day', (30, 20, 7), 12, tower=100, shore_on=False, ripples=14)
    b += [reedbed2(170, 215, 70, 38, 3, 1.2)]
    sd = LGd(p + 'sd', [(0, '#f8e7a0'), (1, '#d4b660')])
    d += sd
    b += [P('M58 112 Q84 88 120 90 Q160 90 190 112 Z', U(p + 'sd'), stroke=OUT, stroke_width=2.2)]
    b += [P('M62 110 Q84 94 120 95 Q156 95 184 110', 'none', stroke='#ffffff', stroke_width=1.4, opacity=.6), sand_dots2(122, 104, 54, 8, 4, 22, '#a8802c')]
    b += [PLn('M56 114 q6 -2 12 0 M170 114 q6 -2 12 0 M120 116 q8 -2 16 0', '#ffffff', 2, .9)]
    boat = [B.bundle(78, 74, 1.1), B.bundle(104, 74, 1.2, '#b8a070'), B.bundle(128, 74, 1.0)]
    b += [lit(p, B.elena(150, 50, 0.38, expr='worry', la=(-24, 10), ra=(24, 10)))]
    b += [G(lit(p, *boat), boat2(48, 74, 112, False), transform='rotate(-7 104 90)')]
    b += [lit(p, B.papa(38, 62, 0.46, expr='worry', rot=10, la=(30, -2), ra=(40, 10)), B.nico(14, 74, 0.44, rot=10, la=(24, -4), ra=(30, 8), expr='worry', pack=False))]
    b += [PLn('M4 108 q8 -4 16 0 M30 110 q8 -4 16 0 M60 116 q8 -4 16 0', '#ffffff', 2)]
    b += [P('M44 100 l-8 6 M50 106 l-9 4', 'none', stroke=OUT, stroke_width=2.4, stroke_linecap='round')]
    for (x, y) in [(16, 98), (40, 112), (12, 112)]:
        b += [C(x, y, 1.6, '#ffffff', stroke='none', opacity=.8), C(x + 4, y - 3, 1, '#ffffff', stroke='none', opacity=.8)]
    H, d, body = finish(p, H, d, b)
    return H, d, body, ''

@card(29)
def c29(p):
    H = 120
    d, b = full(p, H, 46, 74, 'day', (178, 22, 8), 13, tower=36, gcol=('#8a6a48', '#5f4630'), ripples=8)
    b += [reedbed2(0, 44, 80, 38, 5, 1.2), reedbed2(150, 215, 78, 36, 9, 1.2)]
    # mud texture
    for (x, y, rx, ry) in [(30, 100, 20, 4), (100, 112, 24, 4), (190, 110, 18, 4), (60, 86, 14, 3), (130, 90, 12, 3)]:
        b += [E(x, y, rx, ry, '#4a3220', stroke='none', opacity=.28), E(x - 2, y - 1, rx * .6, ry * .4, '#a98a62', stroke='none', opacity=.35)]
    boat = [B.bundle(36, 64, 1.1), B.bundle(60, 64, 1.2, '#b8a070'), B.bundle(84, 64, 1.0)]
    b += [G(lit(p, *boat), boat2(14, 64, 100, False), transform='rotate(6 64 80)')]
    b += [E(64, 94, 52, 11, '#5a3d24', stroke=OUT, stroke_width=2), E(30, 88, 26, 7, '#6f4c30', stroke='none'), E(60, 92, 34, 5, '#8a6a48', stroke='none', opacity=.5),
          PLn('M30 96 q8 -2 16 0 M70 98 q8 -2 16 0', '#c9a67a', 1.4, .6)]
    b += [E(152, 100, 40, 11, '#5a3d24', stroke=OUT, stroke_width=2.2), E(152, 98, 30, 6, '#6f4c30', stroke='none'), E(146, 97, 18, 3, '#a98a62', stroke='none', opacity=.4)]
    b += [lit(p, B.toni(152, 66, 0.62, expr='happy', la=(-30, -34), ra=(30, -34)))]
    for (x, y, r) in [(116, 80, 3.5), (122, 70, 2.5), (190, 74, 3.5), (196, 84, 2.5), (112, 96, 3), (184, 98, 3)]:
        b += [C(x, y, r, '#5a3d24', stroke='none'), C(x - r * .3, y - r * .3, r * .35, '#a98a62', stroke='none', opacity=.6)]
    b += [PLn('M120 106 q8 -4 16 0 M178 112 q8 -4 16 0', '#3a2414', 2)]
    for (x, y) in [(10, 112), (84, 110), (140, 114), (208, 100)]:
        b += [A.tuft(x, y, .8)]
    H, d, body = finish(p, H, d, b, .32)
    return H, d, body, ''

@card(26)
def c26(p):
    H = 120
    d, b = full(p, H, 48, H, 'gold', (110, 34, 9), 15, tower=60, shore_on=False, ripples=16)
    md = LGd(p + 'md', [(0, '#c4ae84'), (1, '#8c744e')])
    d += md
    b += [A.mound(150, 112, 130, 40, '#a58f6a', '#8fa05c')]
    b += [P('M88 112 Q110 92 150 88 Q195 90 215 108 L215 112 Z', U(p + 'md'), stroke='none', opacity=.5)]
    b += [PLn('M90 110 Q120 98 150 96 Q190 96 212 108', '#ffffff', 1.8, .7)]
    b += [reedbed2(96, 134, 96, 34, 4, 1.1), reedbed2(176, 215, 98, 40, 6, 1.2)]
    b += [B.smoke(176, 70, 24, 6, '#9a9aa4', 0.4)]
    for (x, y, s, c, fl, ca, hr) in [(138, 90, .7, '#b8a070', False, 'bundle', '#5a4030'), (184, 92, .65, '#a77a5a', True, 'bundle', '#3a2a20'), (160, 94, .75, '#9a9a5a', True, 'basket', '#5a4030')]:
        b += [shadow(x, y + 1, 9 * s, 2.2, .35), lit(p, B.refugee(x, y, s, c, fl, ca, hr))]
    b += [lit(p, B.papa(40, 60, 0.4, expr='happy', la=(34, 14), ra=(40, 22)), B.nico(86, 62, 0.44, expr='happy', pack=False), B.elena(62, 62, 0.42, expr='smile'))]
    b += [boat2(10, 80, 110)]
    b += [A.oar(100, 82, 112, 110, 22)]
    for (x, y, w) in [(4, 108, 40), (60, 114, 40), (112, 112, 30)]:
        b += [A.ripple(x, y, w)]
    b += [lily(40, 112, 1), lily(200, 114, 1)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''
