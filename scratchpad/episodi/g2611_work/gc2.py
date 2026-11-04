from gc1 import *


def becco_g(p, x, y, s=1, flip=False, wings='down', gob=True, gs=None, legs_on=True):
    b = [becco(x, y, s, 0, flip, wings, False, legs_on)]
    if gob:
        gs = gs or s * 1.5
        bx = x + (46 if flip else -44) * s
        b.append(goblet(bx, y - 36 * s, gs, 0))
    return G(*b)


def head_shake(x, y, s=1):
    return ''.join([PLn('M%s %s q-8 8 0 16' % (f(x - 24 * s), f(y - 8 * s)), '#3b2416', 2.2),
                    PLn('M%s %s q-5 6 0 12' % (f(x - 31 * s), f(y - 5 * s)), '#3b2416', 1.8),
                    PLn('M%s %s q8 8 0 16' % (f(x + 24 * s), f(y - 8 * s)), '#3b2416', 2.2),
                    PLn('M%s %s q5 6 0 12' % (f(x + 31 * s), f(y - 5 * s)), '#3b2416', 1.8)])


def interior(p, H, ytab, seed=2, gx=30, gy=80, gr=70):
    d = lit_defs(p) + glow_def(p + 'gl')
    dd, wb = room_wall(p, H, 0, ytab, '#a9644a', '#6e3a22', seed)
    d += dd
    b = [wb, C(gx, gy, gr, U(p + 'gl'), stroke='none', opacity=.45)]
    return d, b


def sandpile(x, y, w, h):
    return ink(P('M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z' % (f(x - w), f(y), f(x - w * .8), f(y - h * .3), f(x - w * .3), f(y - h), f(x), f(y - h), f(x + w * .3), f(y - h), f(x + w * .8), f(y - h * .3), f(x + w), f(y)), '#f1d57a'),
               P('M%s %s Q%s %s %s %s' % (f(x - w * .7), f(y - h * .25), f(x - w * .4), f(y - h * .8), f(x - w * .1), f(y - h * .92)), 'none', stroke='#fff0b4', stroke_width=2.4, opacity=.9),
               *[E(x + w * a_, y - h * b_, 1.2, .8, '#b88a2c', stroke='none') for (a_, b_) in [(-.4, .3), (.1, .5), (.5, .25), (-.1, .15), (.3, .7), (-.6, .12), (.7, .1)]], sw=2)


def scoop(x, y, rot=0):
    return ink(P('M0 0 L26 -4', 'none', stroke='#6b4426', stroke_width=4), P('M0 0 L26 -4', 'none', stroke='#c99a62', stroke_width=2),
               P('M-10 -4 Q-14 4 -2 6 L4 0 Z', '#c99a62'), transform=T_(x, y, 1, rot), sw=1.4)


def wrong_card(p, kind):
    H = 120
    d, b = interior(p, H, 84, 12 + (kind == 'ash'))
    b += [window_arch(160, 8, 30, 40, p)]
    d += sky_def(p)
    dw, fl = table_wood(p, 84, H)
    d += dw
    b += [C(108, 70, 80, U(p + 'gl'), stroke='none', opacity=.2)]
    b += [lit(p, man(70, 58, .8, la=(-32, -20), ra=(24, 22), expr='sad', look=2))]
    b += [head_shake(70, 40 + 0, .8)]
    b += [fl]
    if kind == 'sand':
        b += [E(150, 108, 46, 6, '#1f1008', stroke='none', opacity=.3), sandpile(150, 106, 40, 36), scoop(100, 104, -12)]
    else:
        dj, j = jar(p, 150, 108, 1.2, ash_heap(), 'a')
        d += dj
        b += [E(152, 108, 30, 4, '#1f1008', stroke='none', opacity=.3), j]
        b += [E(110, 104, 8, 2, '#a2a5a8', stroke=OUT, stroke_width=1.2)]
    b += [sparkle4(30, 30, 3, '#ffe9a0')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


CARDS[31] = lambda p: wrong_card(p, 'sand')
CARDS[35] = lambda p: wrong_card(p, 'ash')


# ------------------------------------------------------------------ 38
@card(38)
def c38(p):
    H = 110
    d, b = interior(p, H, 88, 14, 108, 70, 80)
    df, fu = furnace(p, 108, 96, .62, tag='b')
    d += df
    dw, fl = table_wood(p, 88, H)
    d += dw
    b += [C(108, 70, 74, U(p + 'gl'), stroke='none', opacity=.5), fu, fl]
    lump = ink(P('M-8 -2 L-9 -10 L-3 -17 L6 -18 L11 -10 L9 -1 Z', '#2d2c33'), PLn('M-5 -9 L0 -14 L6 -14', '#9a9aac', 1.8, .95), sw=1.5, transform='translate(0 -4)')
    b += [shadow(56, 108, 22, 4, .4), shadow(160, 108, 22, 4, .4)]
    b += [lit(p, man(56, 62, .74, la=(-28, 22), ra=(32, -34), expr='happy', hold_r=lump))]
    b += [lit(p, man(160, 62, .72, kind='boy', la=(-8, 4), ra=(8, 4), expr='happy'))]
    b += [PLn('M140 54 l-6 -4 M142 62 l-8 0 M180 54 l6 -4 M178 62 l8 0', '#3b2416', 1.8)]
    b += [sparkle4(80, 22, 4, '#ffffff'), sparkle4(92, 14, 2.6, '#ffffff'), sparkle4(30, 50, 3, '#ffe9a0'), sparkle4(196, 30, 3, '#ffe9a0')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 16
@card(16)
def c16(p):
    H = 120
    d, b = interior(p, H, 80, 16, 107, 60, 80)
    d += sky_def(p)
    b += [window_arch(18, 8, 30, 40, p)]
    b += [P('M48 20 L120 40 L120 80 L48 50 Z', '#fff6c8', stroke='none', opacity=.25)]
    dw, fl = table_wood(p, 80, H)
    d += dw
    b += [fl, E(107, 108, 56, 7, '#1f1008', stroke='none', opacity=.35)]
    dj, j = jar(p, 107, 112, 1.42, lumps(), 'm')
    d += dj
    b += [j]
    for (x, y, r) in [(44, 98, 0), (62, 106, 30), (160, 100, 10), (176, 108, -20)]:
        b += [ink(P('M-7 0 L-8 -7 L-2 -12 L6 -11 L9 -4 L7 2 Z', '#2d2c33'), PLn('M-4 -6 L1 -10 L5 -9', '#9a9aac', 1.6, .95), transform=T_(x, y, 1, r), sw=1.5)]
    b += [scoop(175, 92, 8)]
    b += [sparkle4(70, 30, 4, '#ffffff'), sparkle4(150, 24, 3, '#ffffff'), sparkle4(186, 60, 2.6, '#ffe9a0')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 7
@card(7)
def c7(p):
    H = 120
    d = lit_defs(p) + glow_def(p + 'gl')
    dd, wb = room_wall(p, H, 0, 102, '#8f5238', '#5a2c1a', 18)
    d += dd
    b = [wb, C(107, 60, 105, U(p + 'gl'), stroke='none', opacity=.6)]
    dw, fl = table_wood(p, 102, H)
    d += dw
    b += [fl, E(107, 112, 70, 9, '#ff9a30', stroke='none', opacity=.35)]
    df, fu = furnace(p, 107, 112, 1.1, tag='c', big=True)
    d += df
    b += [fu]
    b += [bucket(28, 112, 1.0), pincers(176, 100, 1.0, 10)]
    for k, (x, a) in enumerate([(12, 4), (20, 6), (194, -4), (202, -6)]):
        b.append(blowpipe(x, 108, x + a * 2, 18))
    rnd = random.Random(4)
    for i in range(14):
        b.append(C(rnd.uniform(40, 175), rnd.uniform(8, 100), rnd.uniform(.8, 1.8), '#ffd24a', stroke='none', opacity=.9))
    b += [sparkle4(70, 30, 3, '#ffe9a0'), sparkle4(150, 22, 3, '#ffe9a0')]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 23
@card(23)
def c23(p):
    H = 120
    d = lit_defs(p) + glow_def(p + 'gl') + sky_def(p)
    dd, wb = room_wall(p, H, 0, 98, '#a9644a', '#6e3a22', 21)
    d += dd
    b = [wb, C(48, 90, 70, U(p + 'gl'), stroke='none', opacity=.5)]
    b += [window_arch(150, 6, 44, 46, p)]
    dw, fl = table_wood(p, 98, H)
    d += dw
    b += [fl]
    b += [shelf(120, 66, 90), goblet(134, 66, .7), goblet(176, 66, .7), cup(192, 66, .9)]
    b += [lit(p, becco_g(p, 176, 30, .34, False, 'up', True, .55))]
    b += [sparkle4(156, 18, 3, '#ffffff'), sparkle4(196, 14, 3, '#ffffff')]
    df, fu = furnace(p, 40, 116, .8, tag='d')
    d += df
    b += [fu]
    b += [blowpipe(134, 56, 66, 84.5, ('#fffbe8', '#ffffff'), 6.5, p + 'gl')]
    b += [shadow(100, 110, 20, 4, .4)]
    b += [lit(p, man(100, 64, .62, la=(-24, 20), ra=(-10, 14), expr='wow'))]
    b += [blowpipe(94, 70.5, 85, 74.5)]
    b += [sparkle4(66, 70, 4, '#ffffff'), sparkle4(58, 78, 2.6, '#ffffff'), sparkle4(74, 76, 2.6, '#ffffff')]
    kids = [lit(p, leo(128, 104, .27, ra=(34, -26), mouth='oh')),
            lit(p, nico(150, 92, .34, la=(-26, -30), ra=(26, -30), expr='wow')),
            lit(p, sofia(176, 92, .34, la=(-20, -6), ra=(20, -6), expr='wow')),
            lit(p, toni(199, 92, .34, la=(-30, -32), ra=(30, -32), expr='wow'))]
    b += kids
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 40
@card(40)
def c40(p):
    H = 150
    d = lit_defs(p)
    dd, bg = rio_bg(p, H, 88, 1.0, 3)
    d += dd
    b = bg
    b += [boat2(8, 104, 104), boat2(120, 100, 48)]
    b += [crate(20, 114, 22, 16, 1), crate(44, 114, 24, 18, 2), crate(68, 114, 22, 14, 3), crate(32, 100, 22, 14, 4), crate(56, 98, 22, 14, 5), crate(130, 108, 16, 12, 6), crate(146, 108, 14, 10, 7)]
    # pole
    d += T('pattern', R(0, 0, 12, 12, '#ffffff', stroke='none') + P('M0 12 L12 0 L12 6 L6 12 Z M0 6 L6 0 L0 0 Z', '#d9472f', stroke='none'), id=p + 'ps', width=12, height=12, patternUnits='userSpaceOnUse', patternTransform='rotate(0)')
    b += [ink(R(172, 110, 12, 40, '#d9472f', stroke_width=1.8), R(172, 110, 12, 6, '#ffffff', stroke='none'), R(172, 122, 12, 6, '#ffffff', stroke='none'), R(172, 134, 12, 6, '#ffffff', stroke='none'), E(178, 110, 6, 2, '#c99a62', stroke_width=1.6), sw=1.8)]
    b += [PLn('M168 124 q5 -3 10 0 q5 3 10 0', '#ffffff', 1.6, .9)]
    b += [lit(p, becco_g(p, 178, 80, .55, False, 'down', True, .8))]
    b += [hid(178, 80 + 16 * .55, 14)]
    b += [sparkle4(150, 50, 3, '#ffffff')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 14
@card(14)
def c14(p):
    H = 120
    d = lit_defs(p)
    dd, bg = rio_bg(p, H, 70, 1.0, 5)
    d += dd
    b = bg
    b += [boat2(130, 82, 70)]
    b += [crate(142, 90, 18, 14, 1), crate(162, 90, 18, 14, 2)]
    b += [ink(R(96, 90, 14, 30, '#d9472f', stroke_width=1.8), R(96, 90, 14, 5, '#ffffff', stroke='none'), R(96, 100, 14, 5, '#ffffff', stroke='none'), R(96, 110, 14, 5, '#ffffff', stroke='none'), E(103, 90, 7, 2.2, '#c99a62', stroke_width=1.6), sw=1.8)]
    b += [lit(p, becco_g(p, 103, 60, .62, False, 'down', True, 1.0))]
    b += [PLn('M78 76 q-5 4 0 8 q5 4 0 8', '#3b2416', 2) , PLn('M128 76 q5 4 0 8 q-5 4 0 8', '#3b2416', 2)]
    b += [tx('GRRR', 52, 88, 11, '#a8322a', font='Bangers', weight=400)]
    b += [sparkle4(60, 30, 3, '#ffffff')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 26
def old_book(x, y, s=1, rot=0):
    b = [E(0, 6, 22, 4, '#1f1008', stroke='none', opacity=.3),
         P('M-18 -8 L18 -8 L20 4 L-20 4 Z', '#f1e2b8'), P('M-20 4 L20 4 L20 8 L-20 8 Z', '#d9c08a'),
         P('M-18 -8 L18 -8 L16 -12 L-16 -12 Z', '#7a4a26'),
         P('M-18 -8 L-20 -12 L-20 8 L-18 4 Z', '#5a3418'),
         PLn('M-14 -2 L14 -2 M-14 1 L10 1', '#c9a96a', 1, .9),
         C(10, -1, 5.5, '#c8352a', stroke_width=1.5), P('M7 -1 L10 -4 L13 -1 L10 2 Z', '#f4c64e', stroke='none'),
         P('M10 4 L8 10 M10 4 L13 9', 'none', stroke='#c8352a', stroke_width=2)]
    return ink(*b, transform=T_(x, y, s, rot), sw=1.5)


@card(26)
def c26(p):
    H = 120
    d = lit_defs(p)
    dd, bg = rio_bg(p, H, 66, 1.0, 6)
    d += dd
    b = bg
    d += LGd(p + 'qy', [(0, '#d8c9a4'), (1, '#a89874')])
    b += [R(0, 88, 215, 32, U(p + 'qy'), stroke='none'), L(0, 88, 215, 88, OUT, 2), R(0, 88, 215, 3, '#fff6dc', stroke='none', opacity=.7)]
    for k in range(0, 215, 24):
        b.append(L(k, 88, k - 4, 120, '#8c7552', 1, opacity=.6))
    b += [crate(170, 100, 28, 22, 3), crate(176, 80, 26, 20, 4)]
    b += [ink(R(34, 82, 13, 22, '#d9472f', stroke_width=1.8), R(34, 82, 13, 5, '#ffffff', stroke='none'), R(34, 92, 13, 5, '#ffffff', stroke='none'), E(40.5, 82, 6.5, 2, '#c99a62', stroke_width=1.6), sw=1.8)]
    b += [shadow(110, 112, 22, 4, .35)]
    b += [lit(p, becco(40, 52, .52, 0, False, 'up', False, True))]
    b += [lit(p, sandwich2(26, 46, .34, -10))]
    for (cx, cy) in [(14, 56), (18, 64), (30, 62), (8, 46)]:
        b.append(E(cx, cy, 1.5, 1, '#e8b25e', stroke='none'))
    b += [lit(p, sofia(112, 60, .55, la=(-12, 12), ra=(12, 12), expr='happy'))]
    b += [goblet(112, 60 + 12 * .55 + 7, .8)]
    b += [PLn('M112 8 l0 14 M104 10 l1 10 M120 10 l-1 10', '#ffffff', 2, .9), sparkle4(98, 24, 3, '#ffffff'), sparkle4(128, 22, 3, '#ffffff')]
    b += [lit(p, old_book(150, 110, 1.1, -8))]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 50 / 1311
def parchment(p, x, y, w, h, ytxt, big=True, rot=0, lines=True):
    d = LGd(p + 'pc', [(0, '#fbf0cc'), (.6, '#f2deaa'), (1, '#e2c78a')])
    b = [E(w / 2, h + 4, w * .5, 5, '#1f1008', stroke='none', opacity=.3)]
    b.append(P('M2 0 L%s 0 Q%s %s %s %s Q%s %s %s %s L2 %s Q-3 %s 2 0 Z' % (f(w - 2), f(w + 4), f(h * .25), f(w - 2), f(h * .5), f(w - 6), f(h * .75), f(w - 2), f(h), f(h), f(h * .5)), U(p + 'pc'), stroke_width=2))
    b.append(P('M-4 -3 Q%s -9 %s -3 L%s 6 Q%s 1 -4 6 Z' % (f(w / 2), f(w + 4), f(w + 4), f(w / 2)), '#e8d19a', stroke_width=1.8))
    b.append(P('M-4 %s Q%s %s %s %s L%s %s Q%s %s -4 %s Z' % (f(h - 4), f(w / 2), f(h - 10), f(w + 4), f(h - 4), f(w + 4), f(h + 4), f(w / 2), f(h + 9), f(h + 4)), '#e8d19a', stroke_width=1.8))
    b.append(R(5, 8, w - 10, h - 16, 'none', stroke='#a8802c', stroke_width=1.2, opacity=.6))
    if lines:
        for k, yy in enumerate([h * .15, h * .22]):
            b.append(PLn('M%s %s q4 -3 8 0 q4 3 8 0 q4 -3 8 0 q4 3 8 0 q4 -3 8 0 q4 3 8 0' % (f(w * .2), f(yy + 6)), '#6b4a22', 1.4, .7))
        for k in range(3):
            yy = h * (.72 + k * .06)
            b.append(PLn('M%s %s l%s 0' % (f(w * .12), f(yy), f(w * .5 - k * 6)), '#6b4a22', 1.4, .55))
    # text
    sz1, sz2 = (16, 25) if big else (11, 19)
    b.append(tx('ANNO', w / 2, ytxt, sz1, '#3b2416', font='Georgia, serif', weight=700, textLength=f(sz1 * 2.7), lengthAdjust='spacingAndGlyphs'))
    b.append(tx('MCCXCI', w / 2, ytxt + sz2 * .95, sz2, '#3b2416', font='Georgia, serif', weight=700, textLength=f(sz2 * 3.5), lengthAdjust='spacingAndGlyphs'))
    # seal
    sx, sy = 24, h - 19
    b.append(P('M%s %s l-5 14 l5 -3 l5 3 Z' % (f(sx - 2), f(sy + 8)), '#c8352a', stroke_width=1.4))
    b.append(C(sx, sy, 11 if big else 8, '#b8261e', stroke_width=1.8))
    b.append(C(sx, sy, 8 if big else 5.5, 'none', stroke='#8a1812', stroke_width=1))
    b.append(P('M%s %s q-6 -6 -9 -2 q4 0 6 4 M%s %s q6 -6 9 -2 q-4 0 -6 4 M%s %s l0 8' % (f(sx), f(sy - 1), f(sx), f(sy - 1), f(sx), f(sy - 2)), 'none', stroke='#f4c64e', stroke_width=1.3))
    return d, ink(*b, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)), sw=1.8)


@card(50)
def c50(p):
    H = 120
    d, b = interior(p, H, 100, 30, 150, 60, 90)
    dw, fl = table_wood(p, 100, H)
    d += dw
    b += [fl]
    dp, pc = parchment(p, 70, 8, 138, 96, 44, True, 1)
    d += dp
    b += [pc]
    b += [shadow(30, 112, 20, 4, .4)]
    b += [lit(p, man(30, 64, .6, la=(-22, 24), ra=(52, -6), expr='smile', look=3))]
    b += [sparkle4(60, 14, 3, '#ffffff'), sparkle4(210, 16, 3, '#ffffff')]
    H, d, body = finish(p, H, d, b, .22)
    return H, d, body, ''


@card(1311)
def c1311(p):
    H = 120
    d, b = interior(p, H, 100, 31, 150, 60, 90)
    dw, fl = table_wood(p, 100, H)
    d += dw
    b += [fl]
    dp, pc = parchment(p, 108, 18, 98, 78, 33, False, -3)
    d += dp
    b += [pc]
    b += [shadow(58, 112, 26, 4, .4)]
    b += [lit(p, leo(58, 66, .66, mouth='smile'), sad_leo_overlay(58, 66, .66))]
    b += [head_shake(58, 66 - 28 * .66, .66)]
    H, d, body = finish(p, H, d, b, .22)
    return H, d, body, ''


# ------------------------------------------------------------------ 1291
@card(1291)
def c1291(p):
    H = 100
    d, b = interior(p, H, 74, 40, 107, 56, 90)
    d += sky_def(p)
    df, fu = furnace(p, 107, 80, .66, tag='e')
    d += df
    b += [C(107, 50, 70, U(p + 'gl'), stroke='none', opacity=.5), fu]
    b += [window_arch(170, 4, 34, 36, p)]
    b += [lit(p, becco(188, 30, .26, 0, False, 'down', False, False))]
    b += [PLn('M181 14 l5 3 M200 14 l-4 3', '#3b2416', 1.4)]
    dw, fl = table_wood(p, 76, H)
    d += dw
    figs = [lit(p, man(28, 52, .46, kind='boy', la=(-20, 22), ra=(26, -26), expr='happy')),
            lit(p, man(62, 52, .46, la=(-22, 22), ra=(26, -26), expr='happy')),
            lit(p, nico(100, 52, .33, la=(-24, 16), ra=(26, -34), expr='happy')),
            lit(p, sofia(134, 52, .33, la=(-24, 16), ra=(26, -34), expr='happy')),
            lit(p, toni(166, 52, .33, la=(-28, -20), ra=(30, -38), expr='happy')),
            lit(p, leo(200, 62, .26, ra=(34, -30), mouth='smile'))]
    b += figs
    b += [fl]
    for (x, gy) in [(28 + 26 * .46, 52 - 26 * .46), (62 + 26 * .46, 52 - 26 * .46), (100 + 26 * .33, 52 - 34 * .33), (134 + 26 * .33, 52 - 34 * .33), (166 + 30 * .33, 52 - 38 * .33)]:
        b += [goblet(x, gy + 5, .6)]
    b += [goblet(200 + 34 * .26, 62 - 30 * .26 + 3, .5)]
    for (x, y, c) in [(30, 90, '#d9472f'), (44, 94, '#4f74a8'), (58, 89, '#e9c46a'), (72, 95, '#5f9a5a'), (92, 91, '#8a5fb0'), (110, 96, '#d9472f'), (126, 90, '#4f9ad0'), (142, 95, '#e39a3b'), (158, 90, '#5f9a5a'), (172, 96, '#c85a9a'), (190, 92, '#4f74a8')]:
        b += [glass_bead(x, y, 4, c)]
    b += [sparkle4(80, 40, 3, '#ffffff'), sparkle4(150, 24, 3, '#ffffff')]
    H, d, body = finish(p, H, d, b, .22)
    return H, d, body, ''
