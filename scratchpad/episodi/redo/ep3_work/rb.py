import math, random
from reg import card
from rl import *
from common import hid, tx, star_gold
from helpers import pool, rake, clothbag, crystal, wood_sign, mud_poles
from ra import full, finish

@card(30)
def c30(p):
    H = 175
    d, b = full(p, H, 70, 108, 'day', (176, 30, 9), 17, tower=190, ripples=14)
    b += [reedbed2(0, 34, 112, 40, 3, 1.2), reedbed2(80, 112, 110, 34, 12, 1.0)]
    b += [reedbed2(190, 215, 112, 30, 15, .9)]
    # little hut far on the shore
    b += [shadow(150, 111, 20, 2.5, .25)]
    # pole pile left, with shadow
    b += [shadow(46, 154, 46, 5, .32)]
    b += [lit(p, A.log_pile(46, 152, 80, 4, -6, 1.0))]
    for (x, y) in [(18, 142), (30, 128), (22, 114)]:
        b += [PLn('M%s %s l10 -2' % (f(x + 4), f(y + 2)), '#d9a96e', 1.2, .6)]
    # Becco with mallet
    bx, by, bs, br = 118, 46, 0.42, -8
    b += [shadow(118, 118, 14, 2.2, .18)]
    b += [lit(p, A.becco_mallet(bx, by, bs, br, False, 'up'))]
    b += [PLn('M140 40 q6 -3 12 0 M146 52 q6 -3 12 0 M84 36 q-6 -3 -12 0', '#ffffff', 1.8, .8)]
    # grandmother + pools
    b += [shadow(174, 142, 24, 4, .35)]
    b += [lit(p, pool(88, 138, 30, 22, 'crystal', 1, 0.6), pool(120, 138, 30, 22, 'water'))]
    b += [lit(p, B.nonna(174, 108, 0.86, expr='smile', la=(-22, 16), ra=(22, 16)))]
    b += [A.tuft(70, 130, .9), A.tuft(196, 150, .9), A.tuft(10, 166, 1.0)]
    hx, hy = A.wpt(bx, by, bs, br, -2, 10)
    nx, ny = 174, 108 + 32 * 0.86 * 0.95
    H, d, body = finish(p, H, d, b, .26, [hid(hx, hy, 12), hid(46, 128, 40), hid(nx, ny, 31)])
    return H, d, body, ''

@card(12)
def c12(p):
    H = 120
    d, b = full(p, H, 48, H, 'day', (176, 24, 9), 19, tower=190, shore_on=False, ripples=18)
    b += [reedbed2(0, 24, 110, 34, 4, 1.0), reedbed2(190, 215, 110, 34, 5, 1.0)]
    # stump in the water with reflection
    b += [E(94, 122, 36, 4, '#2a5a78', stroke='none', opacity=.35)]
    b += [R(72, 98, 44, 26, '#8b5e3a', stroke=OUT, stroke_width=2.4), E(94, 98, 22, 5, '#b98a55', stroke=OUT, stroke_width=2),
          P('M80 106 L80 120 M94 104 L94 120 M108 106 L108 120', 'none', stroke='#6a4426', stroke_width=1.4),
          PLn('M76 100 L76 118', '#d9a96e', 1.4, .6), E(94, 98, 12, 2.4, '#d9b068', stroke='none', opacity=.7),
          PLn('M82 98 a12 3 0 0 0 24 0', '#8a5f36', 1)]
    b += [PLn('M68 120 q6 -3 12 0 M108 121 q6 -3 12 0', '#ffffff', 2, .9)]
    b += [lit(p, A.mallet(128, 98, 0.8, 14))]
    b += [lit(p, becco(94, 62, 0.64, wings='down'))]
    b += [A.ripple(10, 112, 46), A.ripple(150, 110, 44)]
    b += [star_gold(176, 30, 7), star_gold(24, 24, 5), sparkle4(60, 40, 4), sparkle4(140, 62, 3), sparkle4(130, 22, 3)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''

@card(31)
def c31(p):
    H = 120
    d, b = full(p, H, 48, 90, 'day', (166, 24, 8), 21, tower=188, ripples=12)
    b += [reedbed2(0, 34, 94, 36, 3, 1.2)]
    b += [shadow(70, 114, 26, 4.5, .35)]
    b += [lit(p, pool(116, 92, 36, 22, 'crystal', 3, 0.7), pool(158, 92, 36, 22, 'water'))]
    b += [lit(p, B.nonna(70, 62, 0.86, expr='smile', la=(-22, 18), ra=(40, 8)))]
    b += [A.tuft(104, 112, .9), A.tuft(205, 115, .9), A.tuft(20, 112, .9)]
    b += [sparkle4(150, 88, 3, '#ffffff', .9), sparkle4(130, 98, 2.5, '#ffffff', .9)]
    H, d, body = finish(p, H, d, b)
    return H, d, body, ''

@card(41)
def c41(p):
    H = 120
    d, b = full(p, H, 46, 94, 'gold', (108, 38, 9), 23, tower=190, ripples=12)
    b += [reedbed2(0, 28, 98, 36, 3, 1.1), reedbed2(190, 215, 98, 36, 8, 1.1)]
    b += [shadow(60, 114, 24, 4, .35), shadow(154, 114, 22, 4, .35), shadow(107, 100, 16, 3, .3)]
    b += [lit(p, B.nonna(60, 62, 0.82, expr='smile', la=(-22, 18), ra=(44, 4)))]
    b += [lit(p, sofia(154, 60, 0.72, expr='happy', la=(-44, 4), ra=(24, 16)))]
    b += [lit(p, clothbag(107, 82, 0.52))]
    b += [star_gold(96, 40, 5), star_gold(120, 36, 4), star_gold(110, 52, 3), sparkle4(86, 62, 3), sparkle4(130, 60, 3)]
    b += [A.tuft(104, 112, .9), A.tuft(36, 114, .9)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''

@card(28)
def c28(p):
    H = 120
    d, b = full(p, H, 46, H, 'day', (110, 22, 9), 27, tower=196, shore_on=False, ripples=18)
    b += [E(33, 122, 24, 3, '#2a5a78', stroke='none', opacity=.35), E(86, 122, 30, 3, '#2a5a78', stroke='none', opacity=.35)]
    b += [R(18, 84, 30, 36, '#8b5e3a', stroke=OUT, stroke_width=2.4), E(33, 84, 15, 4, '#b98a55', stroke=OUT, stroke_width=2),
          PLn('M22 88 L22 118', '#d9a96e', 1.4, .6), PLn('M26 90 l0 28 M40 90 l0 28', '#6a4426', 1.2, .7)]
    b += [R(66, 90, 40, 30, '#b98a55', stroke=OUT, stroke_width=2.4), P('M66 100 L106 100 M66 110 L106 110', 'none', stroke='#8a5f36', stroke_width=1.4),
          PLn('M70 94 L70 118', '#e0b27a', 1.2, .6)]
    b += [R(62, 84, 48, 7, '#d9b068', rx=3, stroke=OUT, stroke_width=2)]
    b += [lit(p, B.fish(86, 80, 1.1, 0))]
    b += [lit(p, becco(33, 56, 0.5, flip=True, wings='up'))]
    for (x, y) in [(60, 58), (64, 62), (68, 64), (71, 69), (75, 70), (78, 74), (83, 71), (66, 70), (74, 76), (89, 73)]:
        b += [C(x, y, 1.6, '#ffffff', stroke=OUT, stroke_width=0.8)]
    b += [lit(p, A.sackbag(50, 68, 0.45, '#e8d9b0'))]
    b += [lit(p, A.mallet(136, 8, 0.46, 150))]
    b += [PLn('M124 4 l-2 10 M146 2 l-2 10 M112 14 l-2 8', '#ffffff', 2)]
    b += [lit(p, B.nico(176, 66, 0.62, expr='wow', la=(-22, -46), ra=(22, -46), pack=False))]
    b += [A.ripple(100, 112, 40), A.ripple(150, 108, 30)]
    b += [PLn('M160 114 q6 -3 12 0 M10 112 q6 -3 12 0', '#ffffff', 2, .8), lily(200, 114, 1.1)]
    H, d, body = finish(p, H, d, b, .28)
    return H, d, body, ''

@card(50)
def c50(p):
    H = 120
    d, b = full(p, H, 68, H, 'sunset', (150, 66, 20), 29, tower=None, shore_on=False, ripples=22, clouds=((.2, .3, .8), (.62, .18, .7), (.9, .42, .6)), boats=False)
    # stars
    for (x, y) in [(20, 12), (60, 22), (100, 8), (190, 14), (170, 28), (130, 20), (40, 36)]:
        b += [B.bstar(x, y, 2.6)]
    b += [B.far_huts([92, 99], 74, 0.4, True)]
    for (x, y, w) in [(8, 104, 36), (60, 112, 40), (120, 108, 34), (170, 114, 36)]:
        b += [A.ripple(x, y, w, '#ffe2a0', 0.6)]
    # warm reflection of hut glow on water
    b += [E(54, 108, 36, 4, '#ffd36a', stroke='none', opacity=.3), E(150, 108, 40, 3, '#ffd36a', stroke='none', opacity=.25)]
    b += [lit(p, B.stilt_hut(16, 92, 116, 70, 40, 196, True, 30))]
    fy = 90
    for (fn, x, s, kw) in [(B.papa, 112, .27, dict(expr='smile')), (B.nonna, 131, .32, dict(expr='smile')), (B.elena, 150, .32, dict(expr='happy')),
                           (nico, 168, .32, dict(expr='happy', pack=False)), (sofia, 185, .32, dict(expr='happy')), (toni, 201, .32, dict(expr='happy', la=(-24, -8), ra=(24, -8)))]:
        pass
    b += [lit(p, B.papa(112, fy - 85 * 0.27, 0.27, expr='smile'), B.nonna(131, fy - 66 * 0.32 * 0.95, 0.32, expr='smile'), B.elena(150, fy - 67 * 0.32, 0.32, expr='happy'),
              nico(168, fy - 63 * 0.32, 0.32, expr='happy', pack=False), sofia(185, fy - 72 * 0.32, 0.32, expr='happy'),
              toni(201, fy - 59 * 0.32, 0.32, expr='happy', la=(-24, -8), ra=(24, -8)))]
    b += [R(104, 76, 108, 4, '#c99a62', stroke=OUT, stroke_width=1.8), R(110, 80, 3, 10, '#8b5e3a', stroke='none'), R(204, 80, 3, 10, '#8b5e3a', stroke='none')]
    b += [PLn('M108 77.5 L208 77.5', '#e8c88a', 1, .8)]
    for (x, col) in [(124, '#e8c07a'), (150, '#cf4a3a'), (176, '#e8c07a'), (196, '#9fb4c4')]:
        b += [E(x, 75, 7, 3, col, stroke=OUT, stroke_width=1.2), E(x - 1.5, 74.2, 3.5, 1, '#ffffff', stroke='none', opacity=.5)]
    b += [PLn('M104 95 L212 95', '#ffd88a', 1.2, .5)]
    # lanterns glow on deck
    b += [C(107, 70, 16, '#ffd36a', stroke='none', opacity=.14)]
    b += [C(51, 14, 18, '#ffd36a', stroke='none', opacity=.5)]
    b += [lit(p, leo(51, 26, 0.3, wing='small', mouth='smile'))]
    b += [sparkle4(80, 24, 3), sparkle4(30, 40, 2.5), sparkle4(176, 54, 3)]
    H, d, body = finish(p, H, d, b, .34)
    return H, d, body, ''
