from gp import *
import r10a

CARDS = {}


def card(n):
    def deco(fn):
        CARDS[n] = fn
        return fn
    return deco


def crate(x, y, w=26, h=18, seed=1):
    rnd = random.Random(seed)
    b = [R(x, y - h, w, h, '#b98a55', stroke_width=1.6)]
    for k in range(1, 3):
        b.append(L(x, y - h + k * h / 3.0, x + w, y - h + k * h / 3.0, '#6b4426', 1, opacity=.8))
    b.append(L(x + 2, y - h, x + 2, y, '#e4b27a', 1.2, opacity=.6))
    for i in range(7):
        sx = x + 2 + i * (w - 4) / 6.0
        b.append(PLn('M%s %s L%s %s' % (f(sx), f(y - h), f(sx + rnd.uniform(-5, 5)), f(y - h - rnd.uniform(5, 9))), '#f0cf6a', 1.5))
    b.append(PLn('M%s %s l-4 3 M%s %s l4 2' % (f(x), f(y - h * .4), f(x + w), f(y - h * .6)), '#f0cf6a', 1.4))
    return ink(*b, sw=1.5)


def bridge_arch(x1, x2, yd, yw, p):
    w = x2 - x1
    b = [P('M%s %s L%s %s L%s %s Q%s %s %s %s Z' % (f(x1), f(yw), f(x1), f(yd), f(x2), f(yd), f(x2), f(yw), f(x2), f(yw)), '#d9c7a0', stroke_width=1.8)]
    b = [P('M%s %s L%s %s L%s %s L%s %s Z' % (f(x1), f(yw), f(x1), f(yd), f(x2), f(yd), f(x2), f(yw)), '#d9c7a0', stroke_width=1.8)]
    cx = (x1 + x2) / 2.0
    b.append(P('M%s %s Q%s %s %s %s Z' % (f(cx - w * .3), f(yw), f(cx), f(yd + (yw - yd) * .15), f(cx + w * .3), f(yw)), '#3f7a96', stroke_width=1.6))
    b.append(P('M%s %s Q%s %s %s %s' % (f(cx - w * .3 - 3), f(yw), f(cx), f(yd + (yw - yd) * .02), f(cx + w * .3 + 3), f(yw)), 'none', stroke='#a89874', stroke_width=2))
    b.append(R(x1 - 2, yd - 3, w + 4, 3.5, '#efe1c0', stroke_width=1.4))
    for k in range(0, int(w / 7) + 1):
        b.append(L(x1 + k * 7, yd - 3, x1 + k * 7, yd - 9, '#a89874', 1.6))
    b.append(L(x1, yd - 9, x2, yd - 9, '#a89874', 1.6))
    b.append(R(x1, yw - 3, w, 3, '#2a1a10', stroke='none', opacity=.15))
    return ink(*b, sw=1.5)


def shop_house(x, yb, w, h, seed, roof):
    b = [bhouse(x, yb, w, h, seed, roof, True, False, False)]
    # shop window with glassware + awning
    sx = x + w * .12
    b.append(ink(R(sx, yb - h * .5, w * .42, h * .32, '#ffe9b0', stroke_width=1.3), sw=1.3))
    b.append(cup(sx + w * .1, yb - h * .2, .6, '#cfe9f0'))
    b.append(goblet(sx + w * .22, yb - h * .2, .42))
    b.append(cup(sx + w * .34, yb - h * .2, .55, '#d8f0d0'))
    b.append(ink(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(sx - 2), f(yb - h * .5), f(sx + w * .42 + 2), f(yb - h * .5), f(sx + w * .42 + 4), f(yb - h * .58), f(sx - 4), f(yb - h * .58)), '#d9472f'), sw=1.3))
    dx = x + w * .62
    b.append(ink(P('M%s %s L%s %s Q%s %s %s %s L%s %s Z' % (f(dx), f(yb), f(dx), f(yb - h * .4), f(dx + 5), f(yb - h * .52), f(dx + 10), f(yb - h * .4), f(dx + 10), f(yb)), '#5a3a22'), sw=1.3))
    return G(*b)


def rio_bg(p, H, wl, scale=1.0, seed=3):
    """returns (defs, [body]) canal scene: sky, houses, bridge, water. wl = waterline y"""
    d = LGd(p + 'sky', [(0, '#6fb4e0'), (.55, '#bfe0e8'), (1, '#f9e3b4')]) + LGd(p + 'wat', [(0, '#a9d8e0'), (.5, '#6fb4cc'), (1, '#3f86a8')])
    d += T('clipPath', R(0, wl, 215, H - wl, '#000'), id=p + 'wc')
    b = [R(0, 0, 215, wl + 2, U(p + 'sky'), stroke='none')]
    b += [cloud2(40, wl * .22, .8), cloud2(160, wl * .15, .65)]
    # distant roofs / campanile
    b += [P('M0 %s L0 %s L30 %s L50 %s L80 %s L110 %s L140 %s L170 %s L215 %s L215 %s Z' % (f(wl), f(wl * .66), f(wl * .62), f(wl * .7), f(wl * .6), f(wl * .66), f(wl * .6), f(wl * .68), f(wl * .62), f(wl)), '#b9a29a', stroke='none', opacity=.75)]
    b += [R(104, wl * .3, 5, wl * .4, '#c99a82', stroke='none', opacity=.8), P('M103 %s L106.5 %s L110 %s Z' % (f(wl * .3), f(wl * .22), f(wl * .3)), '#a8452c', stroke='none', opacity=.8)]
    hh = wl * .66
    hs = [shop_house(0, wl, 56, hh, seed, '#a8452c'), shop_house(52, wl, 46, hh * .85, seed + 1, '#c4623c'),
          shop_house(125, wl, 44, hh * .8, seed + 2, '#b8523a'), shop_house(166, wl, 52, hh, seed + 3, '#a8452c')]
    # smoke
    sm = [B.smoke(14, wl - hh - 28, 26, 7, '#9a9aa4', .5), B.smoke(190, wl - hh - 28, 26, 7, '#9a9aa4', .5)]
    b += sm + [bridge_arch(92, 130, wl - hh * .3, wl, p)]
    b += hs
    # water
    b += [R(0, wl, 215, H - wl, U(p + 'wat'), stroke='none')]
    refl = G(*hs, transform='matrix(1 0 0 -.55 0 %s)' % f(wl * 1.55), opacity=.3)
    b += [G(refl, clip_path='url(#%s)' % (p + 'wc'))]
    b += [R(0, wl, 215, H - wl, U(p + 'wat'), stroke='none', opacity=.45)]
    rnd = random.Random(seed)
    for i in range(14):
        yy = rnd.uniform(wl + 4, H - 3)
        t = (yy - wl) / max(1, H - wl)
        w = 12 + 30 * t
        xx = rnd.uniform(-6, 210)
        b.append(PLn('M%s %s q%s -3 %s 0 q%s 3 %s 0' % (f(xx), f(yy), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.3 + t, .7))
    b += [L(0, wl, 215, wl, '#2a5a78', 1.2, opacity=.5)]
    return d, b


# ------------------------------------------------------------------ 1
@card(1)
def c1(p):
    H = 95
    d = lit_defs(p) + LGd(p + 'sky', [(0, '#6fb4e0'), (.6, '#f3dfb0'), (1, '#f9c88a')]) + LGd(p + 'wat', [(0, '#f1c88a'), (.4, '#8fc0cc'), (1, '#4a86a8')])
    d += LGd(p + 'qy', [(0, '#d8c9a4'), (1, '#a89874')]) + T('clipPath', R(0, 58, 215, 22, '#000'), id=p + 'wc')
    b = [R(0, 0, 215, 60, U(p + 'sky'), stroke='none')]
    b += [C(150, 24, 30, '#fff1b8', stroke='none', opacity=.35), cloud2(40, 14, .6), cloud2(170, 10, .5)]
    hs = [bhouse(-4, 60, 40, 24, 2, '#a8452c'), bhouse(36, 60, 34, 18, 5, '#c4623c'), bhouse(70, 60, 44, 26, 7, '#b8523a'),
          bhouse(118, 60, 36, 20, 4, '#a8452c'), bhouse(152, 60, 36, 26, 9, '#c4623c'), bhouse(186, 60, 40, 20, 1, '#a8452c')]
    b += [B.smoke(14, 8, 30, 8, '#8f8f98', .5), B.smoke(90, 4, 30, 8, '#8f8f98', .5), B.smoke(170, 2, 28, 8, '#8f8f98', .5)]
    b += hs
    b += [R(0, 58, 215, 22, U(p + 'wat'), stroke='none')]
    b += [G(G(*hs, transform='matrix(1 0 0 -.5 0 90)', opacity=.3), clip_path='url(#%s)' % (p + 'wc'))]
    b += [R(0, 58, 215, 22, U(p + 'wat'), stroke='none', opacity=.4)]
    for (x, y, w) in [(10, 66, 22), (60, 72, 28), (100, 64, 20), (150, 70, 26), (190, 66, 22), (125, 75, 18)]:
        b.append(PLn('M%s %s q%s -2.5 %s 0 q%s 2.5 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.3, .75))
    # small boat with crates
    b += [boat2(156, 62, 44, True)]
    b += [crate(166, 66, 12, 9, 2), crate(180, 66, 11, 8, 3)]
    # quay
    b += [R(0, 80, 215, 15, U(p + 'qy'), stroke='none'), L(0, 80, 215, 80, OUT, 2)]
    for k in range(0, 215, 22):
        b.append(L(k, 80, k - 3, 95, '#8c7552', 1, opacity=.6))
    b.append(R(0, 80, 215, 3, '#fff6dc', stroke='none', opacity=.7))
    b += [post(24, 70, 84, 0, 6), rope(24, 74, 60, 80, 4)]
    b += [shadow(107, 87, 22, 4, .35)]
    b += [lit(p, leo(107, 62, .5, wing='small', ra=(40, -26), mouth='smile'))]
    b += [sparkle4(70, 40, 3), sparkle4(150, 40, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 2
@card(2)
def c2(p):
    H = 160
    d = lit_defs(p) + glow_def(p + 'gl') + sky_def(p)
    dd, wb = room_wall(p, H, 0, 114, '#a9644a', '#6e3a22', 4)
    d += dd
    b = [wb]
    b += [C(100, 100, 96, U(p + 'gl'), stroke='none', opacity=.55)]
    # window
    b += [window_arch(160, 10, 32, 38, p)]
    # floor
    dw, fl = table_wood(p, 112, H)
    d += dw
    b += [fl]
    b += [E(100, 128, 70, 12, '#ff9a30', stroke='none', opacity=.3)]
    # wall shelves
    b += [shelf(6, 50, 62), shelf(6, 84, 62)]
    for i, cx in enumerate([14, 26, 38, 50, 62]):
        b.append(cup(cx, 50, .9 if i != 2 else 1.1))
    b += [goblet(16, 84, .8), cup(30, 84, 1.0, '#d8f0d0'), goblet(46, 84, .8), cup(60, 84, .9)]
    # bench + tools
    b += [bench(6, 144, 56, 24, p), pincers(22, 122, .9, -20), shears(46, 124, .9, 70)]
    b += [bucket(76, 154, .9), bucket(92, 158, .8)]
    # furnace
    df, fu = furnace(p, 100, 128, .95, tag='a')
    d += df
    b += [fu]
    # apprentice
    b += [shadow(172, 146, 18, 3.5, .4)]
    b += [blowpipe(204, 95, 126, 112.5, ('#ffd24a', '#fff6c0'), 5, p + 'gl')]
    b += [lit(p, man(172, 100, .75, kind='boy', la=(-30, 10), ra=(-12, 6), expr='smile', look=-2))]
    b += [blowpipe(165, 103.5, 150, 107)]
    b += [sparkle4(130, 48, 3, '#ffe9a0'), sparkle4(76, 46, 2.5, '#ffe9a0'), sparkle4(120, 20, 2.5, '#ffe9a0')]
    b += [hid(100, 128 - 70 * .95, 7), hid(176, 99, 13)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 3
@card(3)
def c3(p):
    H = 95
    d = lit_defs(p) + glow_def(p + 'gl') + sky_def(p)
    dd, wb = room_wall(p, H, 0, 74, '#a9644a', '#6e3a22', 6)
    d += dd
    b = [wb]
    b += [C(30, 36, 60, U(p + 'gl'), stroke='none', opacity=.35)]
    b += [window_arch(10, 8, 38, 50, p)]
    b += [P('M48 20 L152 30 L152 60 L48 58 Z', '#fff6c8', stroke='none', opacity=.3)]
    dw, fl = table_wood(p, 74, H)
    d += dw
    b += [fl]
    b += [shelf(150, 24, 60), goblet(162, 24, .7), cup(180, 24, .9), goblet(198, 24, .7)]
    b += [shadow(120, 90, 30, 5, .4)]
    g = goblet(0, 6, 1.5)
    b += [lit(p, man(120, 68, .8, la=(-26, 24), ra=(32, -36), expr='worry', hold_r=goblet(0, 6, 1.3)))]
    b += [sparkle4(150, 8, 4, '#ffffff'), sparkle4(166, 30, 3, '#ffffff'), sparkle4(138, 4, 2.4, '#ffffff')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 4
@card(4)
def c4(p):
    return r10a.c4(p)


# ------------------------------------------------------------------ 11
@card(11)
def c11(p):
    H = 70
    d = LGd(p + 'pg', [(0, '#fbf1d6'), (1, '#efdcae')])
    b = [R(0, 0, 215, H, U(p + 'pg'), stroke='none')]
    for yy in range(12, 70, 9):
        b.append(L(0, yy, 215, yy, '#a8c4e0', .8, opacity=.7))
    b.append(L(14, 0, 14, H, '#e08a7a', 1.1, opacity=.8))
    for yy in (10, 30, 50):
        b.append(C(6, yy, 2.6, '#8a7a5a', stroke='none') + C(5.4, yy - .6, 1, '#d8c8a0', stroke='none'))
    pen = '#4a3a2c'
    # sand heap
    b.append(P('M20 46 Q30 24 42 22 Q54 24 62 46 Z', '#f1d57a', stroke=pen, stroke_width=1.4, stroke_linejoin='round'))
    b.append(PLn('M28 40 Q34 28 40 26', '#fff0b4', 2, .9))
    for (a_, b_) in [(36, 40), (46, 38), (52, 43), (42, 32), (30, 44)]:
        b.append(C(a_, b_, .9, '#b88a2c', stroke='none'))
    b.append(tx('sabbia', 41, 58, 7, pen))
    # burning plants -> ash
    b.append(PLn('M82 46 Q80 32 76 20 M86 46 Q86 30 88 18 M90 46 Q94 34 100 22', '#8a7a3a', 1.8))
    b.append(PLn('M76 20 q-3 -4 -1 -7 M88 18 q3 -4 1 -7 M100 22 q4 -3 2 -7', '#8a7a3a', 1.4))
    b.append(P('M78 36 Q74 26 80 18 Q80 26 85 22 Q86 30 88 34 Q92 24 96 20 Q98 30 94 38 Z', '#f08a24', stroke=pen, stroke_width=1.1, stroke_linejoin='round'))
    b.append(P('M82 36 Q80 30 84 26 Q86 32 88 35 Q91 30 92 31 Q93 36 90 38 Z', '#ffe36a', stroke='none'))
    b.append(P('M72 48 Q84 40 100 48 Z', '#a2a5a8', stroke=pen, stroke_width=1.2, stroke_linejoin='round'))
    b.append(tx('cenere', 87, 58, 7, pen))
    # black stone
    b.append(P('M118 46 L116 34 L124 24 L136 22 L146 30 L148 46 Z', '#2d2c33', stroke=pen, stroke_width=1.4, stroke_linejoin='round'))
    b.append(PLn('M122 34 L128 28 L136 27', '#8a8a9c', 1.8, .9))
    b.append(tx('manganese', 132, 58, 7, pen))
    # arrow, glasses
    b.append(PLn('M154 36 L166 36 M162 32 L166 36 L162 40', '#d9472f', 2))
    b.append(ink(P('M172 22 L192 22 Q192 38 182 40 Q172 38 172 22 Z', '#9ad07a', opacity=.9), L(182, 40, 182, 48, OUT, 1.6), E(182, 50, 7, 2, '#9ad07a'), sw=1.3))
    b.append(PLn('M175 25 Q175 33 179 37', '#ffffff', 1.6, .9))
    b.append(ink(P('M196 22 L214 22 Q214 38 205 40 Q196 38 196 22 Z', '#e8f6fa', opacity=.8), L(205, 40, 205, 48, OUT, 1.6), E(205, 50, 6.5, 2, '#e8f6fa'), sw=1.3))
    b.append(PLn('M199 25 Q199 33 202 37', '#ffffff', 1.6, .9))
    b.append(sparkle4(207, 18, 3, '#ffffff'))
    H, d, body = finish(p, H, d, b, .2)
    return H, d, body, ''


# ------------------------------------------------------------------ 12
@card(12)
def c12(p):
    H = 120
    d = lit_defs(p) + glow_def(p + 'gl')
    dd, wb = room_wall(p, H, 0, 62, '#a9644a', '#6e3a22', 8)
    d += dd
    b = [wb, C(20, 40, 70, U(p + 'gl'), stroke='none', opacity=.45)]
    b += [shelf(140, 30, 66), cup(150, 30, 1), goblet(168, 30, .8), cup(190, 30, 1.1, '#d8f0d0')]
    dw, fl = table_wood(p, 62, H)
    d += dw
    b += [fl]
    d += T('pattern', R(0, 0, 14, 14, '#fbf3e0', stroke='none') + R(0, 0, 7, 7, '#5a86b8', stroke='none') + R(7, 7, 7, 7, '#5a86b8', stroke='none'), id=p + 'ck', width=14, height=14, patternUnits='userSpaceOnUse')
    b += [ink(P('M26 98 L50 66 L168 66 L196 98 Z', U(p + 'ck')), sw=1.8)]
    b += [pincers(46, 76, .8, 30), shears(188, 78, .8, -50)]
    b += [E(108, 98, 78, 6, '#2a1a10', stroke='none', opacity=.25)]
    b += [C(108, 70, 62, U(p + 'gl'), stroke='none', opacity=.5)]
    b += [lit(p, sandwich2(108, 80, 1.3))]
    b += [cheese_t(50, 100), cheese_t(158, 102)]
    for (cx, cy) in [(48, 90), (172, 92), (76, 104), (150, 108), (128, 108), (90, 106)]:
        b += [E(cx, cy, 1.6, 1, '#e8b25e', stroke='none')]
    b += [sparkle4(30, 56, 3), sparkle4(188, 56, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 13
def scrap(x, y, rot=0):
    return ink(P('M-5 -4 L3 -5 L5 0 L2 4 L-4 3 Z', '#ffffff'), PLn('M0 -5 L0 -10', OUT, 1), transform=T_(x, y, 1, rot), sw=1)


@card(13)
def c13(p):
    H = 100
    d = lit_defs(p) + glow_def(p + 'gl')
    dd, wb = room_wall(p, H, 0, 84, '#a9644a', '#6e3a22', 9)
    d += dd
    b = [wb, C(30, 80, 70, U(p + 'gl'), stroke='none', opacity=.45)]
    dw, fl = table_wood(p, 84, H)
    d += dw
    b += [fl]
    b += [shelf(100, 46, 112), shelf(100, 74, 112), cup(114, 74, .8), cup(128, 74, .8), goblet(196, 74, .7), cup(180, 74, .8)]
    jd = ''
    for (x, tg, ct) in [(132, 'a', sand_heap()), (160, 'b', ash_heap()), (190, 'c', lumps())]:
        dj, j = jar(p, x, 46, .6, ct, tg)
        d += dj
        b += [j, scrap(x - 5, 22, 20 + (x % 30))]
    b += [shadow(60, 100, 24, 4, .4)]
    pipe = blowpipe(2, 8, -10, -104)
    b += [lit(p, man(62, 58, .78, kind='boy', la=(-30, 22), ra=(50, -12), expr='smile', look=3, hold_l=pipe))]
    b += [sparkle4(104, 28, 3), sparkle4(176, 14, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 20
@card(20)
def c20(p):
    H = 150
    d = glow_def(p + 'gl')
    dd, wb = room_wall(p, H, 0, 112, '#a9644a', '#6e3a22', 11)
    d += dd
    b = [wb, C(107, 70, 110, U(p + 'gl'), stroke='none', opacity=.4)]
    d += LGd(p + 'sh', [(0, '#d9a96e'), (1, '#b98a55')]) + LGd(p + 'sf', [(0, '#a8703f'), (1, '#6b4426')])
    b += [P('M0 112 L215 112 L215 123 L0 123 Z', U(p + 'sh'), stroke=OUT, stroke_width=2)]
    b += [R(0, 123, 215, 27, U(p + 'sf'), stroke=OUT, stroke_width=2)]
    for k in range(0, 215, 36):
        b.append(L(k, 123, k, 150, '#4a3020', 1, opacity=.5))
    b += [PLn('M4 126 L211 126', '#e4b27a', 1.4, .6)]
    for (x, tg, ct, num) in [(40, 'a', sand_heap(), 31), (107, 'b', ash_heap(), 35), (175, 'c', lumps(), 38)]:
        b.append(E(x + 6, 115, 32, 4, '#1f1008', stroke='none', opacity=.3))
        dj, j = jar(p, x, 114, 1.22, ct, tg)
        d += dj
        b += [j]
    for (x, n) in [(40, 31), (107, 35), (175, 38)]:
        b += [label(x, 137, 44, 20, n, 17)]
    for (fx, fy, r) in [(76, 118, 70), (142, 117, -40), (206, 117, 20), (8, 118, -70), (90, 119, 100)]:
        b += [feather(fx, fy, 15, r, '#9a9da6')]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''
