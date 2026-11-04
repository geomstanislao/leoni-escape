from h10 import *
from r10a import sandwich2


def boot(x, yb, s=1, flip=False, tag='', p=''):
    b = []
    b.append(P('M-15 -80 L15 -80 L16 -28 Q17 -15 30 -12 Q52 -9 52 1 L52 10 L-19 10 L-19 -8 Q-16 -30 -15 -80 Z', U(p + 'by' + tag)))
    b.append(P('M4 -78 L15 -78 L16 -28 Q17 -15 30 -12 Q52 -9 52 1 L40 1 Q28 -4 10 -12 Z', '#d89a1c', stroke='none', opacity=.5))
    b.append(P('M-16 -80 L16 -80 L16 -68 L-16 -68 Z', '#f08a24'))
    b.append(P('M-16 -68 L16 -68', 'none', stroke='#b85a10', stroke_width=1.2))
    b.append(P('M-12 -64 Q-13 -40 -12 -24', 'none', stroke='#fff6c0', stroke_width=3.4, opacity=.95))
    b.append(P('M-8 -22 Q-10 -12 -6 -6', 'none', stroke='#fff6c0', stroke_width=2, opacity=.8))
    b.append(P('M-16 -80 Q-24 -80 -23 -72 L-16 -72', '#f08a24'))
    b.append(P('M16 -80 Q24 -80 23 -72 L16 -72', '#f08a24'))
    b.append(P('M-21 4 Q-19 10 -17 10 L52 10 L52 2 Q50 -3 44 -5 L40 -3 Q-8 -2 -21 4 Z', '#6a4a30'))
    b.append(P('M-21 4 L52 4', 'none', stroke='#8a6a4a', stroke_width=1.2))
    for k in range(6):
        b.append(P('M%s 6 L%s 9.5' % (f(-14 + k * 11), f(-14 + k * 11)), 'none', stroke='#2a1a10', stroke_width=1.6))
    b.append(P('M22 -8 Q40 -8 49 -2', 'none', stroke='#fff6c0', stroke_width=2, opacity=.8))
    return ink(*b, transform='translate(%s %s) scale(%s %s)' % (f(x), f(yb), f(-s if flip else s), f(s)), sw=2.2 / max(s, .4) if False else 2.4)


def splash(x, y, s=1, col='#e4f6fa'):
    b = [P('M-12 0 Q-10 -10 -7 -4 Q-5 -16 -1 -5 Q2 -18 5 -5 Q8 -12 10 -3 Q13 -6 14 0 Z', col, stroke=OUT, stroke_width=1.2),
         C(-14, -8, 1.8, col, stroke=OUT, stroke_width=.9), C(16, -9, 1.6, col, stroke=OUT, stroke_width=.9), C(1, -22, 1.7, col, stroke=OUT, stroke_width=.9)]
    return G(*b, transform=T_(x, y, s))


def cat(x, y, s=1, flip=False):
    b = []
    b.append(P('M16 2 Q40 4 38 -18 Q36 -28 28 -24', 'none', stroke=OUT, stroke_width=8))
    b.append(P('M16 2 Q40 4 38 -18 Q36 -28 28 -24', 'none', stroke='#e08a3a', stroke_width=5))
    b.append(P('M30 -4 L34 -6 M35 -14 L39 -14 M34 -22 L37 -25', 'none', stroke='#a85a1c', stroke_width=1.6))
    b.append(P('M-18 4 Q-24 -16 -10 -32 L10 -32 Q24 -16 18 4 Z', '#e8943c'))
    b.append(P('M-8 4 Q-12 -10 -4 -26 L4 -26 Q12 -10 8 4 Z', '#fbe3c0', stroke='none'))
    b.append(P('M-18 -10 L-10 -12 M-17 -2 L-9 -4 M18 -10 L10 -12 M17 -2 L9 -4', 'none', stroke='#a85a1c', stroke_width=1.8))
    b.append(E(-6, 4, 5, 3, '#e8943c') + E(6, 4, 5, 3, '#e8943c'))
    b.append(C(0, -40, 15, '#e8943c'))
    b.append(P('M-14 -48 L-13 -64 L-3 -54 Z', '#e8943c') + P('M14 -48 L13 -64 L3 -54 Z', '#e8943c'))
    b.append(P('M-11.5 -52 L-11 -60 L-6 -55 Z', '#f2a0a0', stroke='none') + P('M11.5 -52 L11 -60 L6 -55 Z', '#f2a0a0', stroke='none'))
    b.append(P('M-4 -52 L-2 -46 M4 -52 L2 -46 M0 -54 L0 -49', 'none', stroke='#a85a1c', stroke_width=1.8))
    b.append(E(0, -34, 8, 5.5, '#fbe3c0', stroke='none'))
    b.append(E(-6, -41, 2.8, 3.6, '#2a1a10', stroke='none') + E(6, -41, 2.8, 3.6, '#2a1a10', stroke='none'))
    b.append(C(-5.2, -42.4, 1, '#ffffff', stroke='none') + C(6.8, -42.4, 1, '#ffffff', stroke='none'))
    b.append(P('M-2.4 -37 L2.4 -37 L0 -34.6 Z', '#e07a8a', stroke_width=1))
    b.append(P('M0 -34.6 Q-3 -31 -6 -33 M0 -34.6 Q3 -31 6 -33', 'none', stroke_width=1.2))
    b.append(P('M-10 -35 L-22 -37 M-10 -32 L-22 -31 M10 -35 L22 -37 M10 -32 L22 -31', 'none', stroke='#ffffff', stroke_width=.9))
    return ink(*b, transform=xf(x, y, s, 0, flip), sw=2)


def brick_wall(x, y, w, h, c1='#c9825a', c2='#a8603e', seed=1, plaster=True):
    rnd = random.Random(seed)
    b = [R(x, y, w, h, c1, stroke='none')]
    rows = int(h / 7)
    for r_ in range(rows + 1):
        yy = y + r_ * 7
        b.append(L(x, yy, x + w, yy, c2, .9, opacity=.6))
        off = 6 if r_ % 2 else 0
        for c_ in range(int(w / 12) + 1):
            xx = x + off + c_ * 12
            if x < xx < x + w:
                b.append(L(xx, yy, xx, min(yy + 7, y + h), c2, .8, opacity=.5))
    if plaster:
        for k in range(3):
            px = x + rnd.uniform(0, w * .7)
            py = y + rnd.uniform(0, h * .6)
            b.append(P('M%s %s q8 -4 14 1 q4 8 -3 12 q-10 3 -14 -4 Z' % (f(px), f(py)), '#e8cfa8', stroke='none', opacity=.75))
    return G(*b)


# ------------------------------------------------------------------ 9
@card(9)
def c9(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#f6ead2'), (1, '#f3e0b6')])
    b = [R(0, 0, 215, 120, U(p + 'sk'), stroke='none')]
    # back wall with Doge's palace arches and a lion column
    dd, pal = ducale(p, -4, 150, 84, 50, 4, 'a')
    d += dd
    b += [pal]
    ddp, pv = paving_persp(p, 84, 120, 215, '#e1d3b0', '#bda97e', 107, 40, 5, 4, 11)
    d += ddp
    b += [pv]
    # column of San Todaro / lion on the right
    b += [shadow(204, 112, 14, 3, .3)]
    b += [ink(R(195, 112, 20, 5, '#e3dcc8'), R(199, 40, 12, 72, '#f1e8d0'), P('M205 40 L205 112', 'none', stroke='#c9b88c', stroke_width=1, opacity=.8), R(196, 34, 18, 7, '#e9e2cf'), sw=1.4)]
    b += [R(0, 0, 215, 120, '#fff2b8', stroke='none', opacity=0)]
    b += [lion_wing_emblem(205, 27, .75)]
    b += [shadow(86, 112, 28, 4, .3)]
    b += [lit(p, becco2(86, 74, .64, hat='bigcorno', wings='down', beak='closed'))]
    b += [T('text', 'GRRR', x=168, y=66, text_anchor='middle', font_family='Bangers', font_weight=700, font_size=17, fill='#a8322a', stroke='none', transform='rotate(-8 168 66)')]
    b += [P('M146 80 q6 -6 12 0 q6 6 12 0 q6 -6 12 0', 'none', stroke='#a8322a', stroke_width=2, stroke_linecap='round'),
          P('M146 92 q6 -6 12 0 q6 6 12 0', 'none', stroke='#a8322a', stroke_width=2, stroke_linecap='round')]
    b += [sparkle4(30, 60, 3), sparkle4(130, 40, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 21
@card(21)
def c21(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#a8dcf2'), (1, '#f8efd0')])
    b = [R(0, 0, 215, 90, U(p + 'sk'), stroke='none'), cloud2(60, 16, .6), cloud2(170, 12, .55)]
    dd, pal = ducale(p, -6, 221, 76, 44, 6, 'a')
    d += dd
    b += [pal]
    ddp, pv = paving_persp(p, 76, 120, 215, '#e7dab8', '#bda97e', 107, 36, 6, 5, 11)
    d += ddp
    b += [pv]
    # Becco munching the sandwich
    b += [shadow(66, 111, 24, 3.5, .3)]
    b += [lit(p, becco2(66, 66, .7, hat='captain', wings='down', beak='open'))]
    b += [ink(sandwich2(26, 34, .3, -18), sw=1)]
    for (cx, cy) in [(38, 28), (42, 38), (20, 46), (32, 50), (46, 46)]:
        b += [E(cx, cy, 1.5, 1, '#e8b25e', stroke='none')]
    b += [P('M34 20 l-4 -5 M41 22 l1 -7 M17 24 l-6 -3', 'none', stroke='#3b2416', stroke_width=1.4, stroke_linecap='round')]
    # rolling corno + motion lines
    b += [PLn('M92 100 l-16 0 M94 106 l-20 0 M90 112 l-12 0', '#7a5a3a', 1.6, .8)]
    b += [shadow(108, 112, 18, 3, .3)]
    b += [corno(112, 106, .82, -78)]
    b += [PLn('M104 92 q-4 -6 -10 -8', '#7a5a3a', 1.4, .7)]
    # kids
    b += [shadow(168, 111, 12, 2.4, .3), shadow(200, 111, 12, 2.4, .3)]
    b += [lit(p, nico(168, 76, .6, expr='wow', la=(-24, -10), ra=(24, 16), pack=False, flip=True))]
    b += [lit(p, sofia(200, 73, .6, expr='smile', la=(-24, 16), ra=(24, 8), flip=True))]
    b += [sparkle4(130, 70, 2.6)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 30
@card(30)
def c30(p):
    H = 160
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#8fd0ee'), (.6, '#d0e8f0'), (1, '#f8efd0')])
    b = [R(0, 0, 215, 110, U(p + 'sk'), stroke='none'), cloud2(44, 18, .6), cloud2(160, 24, .55), cloud2(110, 10, .4)]
    dd, bas = basilica(p, 22, 138, 104, 66)
    d += dd
    b += [bas]
    b += [campanile(178, 104, 94, 15)]
    # procuratie hint to the right
    b += [R(188, 74, 28, 30, '#e8dcc0', stroke=OUT, stroke_width=1.4)]
    for i in range(3):
        b += [P(pointed(190 + i * 9, 196 + i * 9, 92, 84, 104), '#4a3426', stroke=OUT, stroke_width=1)]
    ddp, pv = paving_persp(p, 104, 160, 215, '#e1d3b0', '#bda97e', 107, 70, 8, 6, 12)
    d += ddp
    b += [pv]
    # flags on the building, and a pole
    b += [flagpole(26, 70, 40, 0, 28, 18, 2.4, 'it'), flagpole(142, 80, 46, 0, 30, 19, 2.4, 'it'), flagpole(204, 108, 52, 0, -28, 18, 2.4, 'it')]
    b += [pennant_line(30, 46, 176, 24, 11, ('#3a9a58', '#fbf8ee', '#d9392e'), 6, 6)]
    # pigeons
    for (px, py) in [(52, 112), (150, 112), (112, 110)]:
        b += [ink(E(px, py, 4.4, 2.8, '#b6bcc4'), C(px + 4, py - 2, 1.9, '#9aa0aa'), P('M%s %s l2 .6' % (f(px + 5.6), f(py - 2)), 'none', stroke='#f08a24', stroke_width=1), sw=.8)]
    # crowd (back to front)
    box = (104, 130, 34, 24)
    people = [
        (20, 142, .52, '#c9a040', '#3a2a20', 'up', None, None),
        (66, 140, .5, '#8a5a3a', '#4a2a1a', 'one', None, ballot(26, -42, 1.7)),
        (186, 142, .5, '#d9794a', '#2a1a10', 'up', None, None),
        (92, 148, .55, '#6a8ab8', '#2a1a10', 'one', 'cap', ballot(26, -42, 1.7)),
        (150, 146, .55, '#7a9a5a', '#5a3a20', 'up', None, None),
        (42, 156, .58, '#4f9a5a', '#2a1a10', 'up', 'cap', None),
        (172, 156, .58, '#9a5aa0', '#3a2a20', 'one', None, ballot(26, -42, 1.7)),
        (202, 154, .56, '#c0392b', '#4a2a1a', 'up', None, None),
    ]
    caps = '#c0392b'
    for (x, feet, s, sh, hr, arms, hat, hold) in people:
        y = feet - 57 * s
        b += [shadow(x, feet, 10 * s + 2, 2, .3), lit(p, fig(x, y, s, sh, caps if hat == 'cap' else hr, arms=arms, hat=hat, hold=hold))]
    # ballot box
    b += [shadow(121, 156, 22, 3, .3)]
    b += [ink(R(104, 130, 34, 24, '#9a6a3c'), R(101, 126, 40, 6, '#7a4e26'), R(112, 128, 18, 3, '#2a1a10'), P('M104 134 L138 134', 'none', stroke='#c99a62', stroke_width=1.2), sw=1.8)]
    b += [ballot(121, 120, 1.0, -8)]
    b += [T('text', 'SÌ', x=121, y=148, text_anchor='middle', font_family='Comic Neue', font_weight=700, font_size=11, fill='#ffffff', stroke='none')]
    # confetti
    for (cx, cy, c_) in [(30, 90, '#3a9a58'), (60, 80, '#d9392e'), (84, 96, '#ffffff'), (100, 76, '#3a9a58'), (130, 92, '#d9392e'), (150, 70, '#ffffff'), (166, 98, '#3a9a58'), (190, 86, '#d9392e'), (120, 60, '#3a9a58'), (76, 60, '#ffffff'), (46, 100, '#d9392e'), (206, 100, '#ffffff')]:
        b += [P('M%s %s l3 1 l-1 3 l-3 -1 Z' % (f(cx), f(cy)), c_, stroke=OUT, stroke_width=.6)]
    H, d, body = finish(p, H, d, b, .24)
    return H, d, body, ''


# ------------------------------------------------------------------ 40
@card(40)
def c40(p):
    H = 175
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#7cc4ec'), (1, '#cfe9ee')]) + LGd(p + 'wt', [(0, '#a9d9e4'), (1, '#5fa8c4')])
    d += LGd(p + 'by', [(0, '#f8d24e'), (1, '#e6a824')], 0, 0, 1, 0) + LGd(p + 'mw', [(0, '#7fc0d6'), (1, '#4f98b8')])
    b = [R(0, 0, 215, 30, U(p + 'sk'), stroke='none')]
    b += [cloud2(40, 9, .45, .85), cloud2(160, 7, .4, .8)]
    b += [R(0, 14, 215, 32, U(p + 'mw'), stroke='none')]
    b += [P('M0 14 L215 14', 'none', stroke='#5f94ad', stroke_width=1, opacity=.8)]
    for (x, y, w) in [(8, 40, 30), (100, 22, 24), (60, 42, 26), (150, 36, 30), (130, 20, 18), (30, 24, 20)]:
        b += [PLn('M%s %s q%s -2.4 %s 0 q%s 2.4 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.3, .7)]
    # MOSE gates rising from the sea
    for k in range(7):
        gx = 10 + k * 13.5
        gy = 38 - k * 2.3
        sc_ = 1.0 - k * .06
        b += [ink(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(gx), f(gy), f(gx + 9 * sc_), f(gy), f(gx + 17 * sc_), f(gy - 24 * sc_), f(gx + 8 * sc_), f(gy - 24 * sc_)), U(p + 'by')),
                  P('M%s %s L%s %s' % (f(gx + 3 * sc_), f(gy - 3), f(gx + 10 * sc_), f(gy - 21 * sc_)), 'none', stroke='#fff6c0', stroke_width=1.6),
                  P('M%s %s L%s %s' % (f(gx + 8 * sc_), f(gy - 24 * sc_), f(gx + 17 * sc_), f(gy - 24 * sc_)), 'none', stroke='#b07a12', stroke_width=1.4), sw=1.3),
              PLn('M%s %s q4 -3 8 0 q4 3 8 0' % (f(gx - 4), f(gy + 1.4)), '#ffffff', 1.8, .95)]
    # city: procuratie arcade, basilica, campanile
    dd, pal = ducale(p, -2, 106, 100, 40, 5, 'a', crenel=False)
    d += dd
    b += [pal]
    dd2, bas = basilica(p, 104, 168, 100, 50)
    d += dd2
    b += [bas, campanile(192, 100, 90, 14)]
    b += [R(168, 66, 22, 34, '#e8dcc0', stroke=OUT, stroke_width=1.4)]
    for i in range(2):
        b += [P(pointed(170 + i * 10, 178 + i * 10, 90, 80, 100), '#4a3426', stroke=OUT, stroke_width=1)]
    # flooded square: water with reflections
    b += [R(0, 100, 215, 18, U(p + 'wt'), stroke='none')]
    b += [R(0, 100, 215, 4, '#2a1a10', stroke='none', opacity=.15)]
    for (x, y, w) in [(120, 108, 30), (160, 112, 24), (20, 114, 26), (80, 112, 28)]:
        b += [PLn('M%s %s q%s -2.6 %s 0 q%s 2.6 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.4, .75)]
    # wooden walkway (passerella)
    b += [ink(R(0, 96, 215, 6, '#c79a62'), sw=1.6)]
    b += [R(0, 96, 215, 1.8, '#e4b27a', stroke='none')]
    for xx in range(8, 215, 36):
        b += [ink(R(xx, 102, 4, 10, '#8a5a30'), R(xx - 3, 111, 10, 2.6, '#6b4426'), sw=1.1)]
    for xx in range(0, 215, 14):
        b += [L(xx, 96, xx, 102, '#8a5a30', .8, opacity=.7)]
    # people on the walkway
    ppl = [(24, '#d9392e', '#3a2a20'), (60, '#3a6ab8', '#7a4a26'), (96, '#3a9a58', '#2a1a10'), (134, '#e0a02a', '#5a3a20')]
    for (x, sh, hr) in ppl:
        b += [lit(p, fig(x, 70, .47, sh, hr, arms='down', pants='#4a5a7a', shoe='#f4c64e'))]
    # bottom-left: stone wall with step and boots
    b += [R(0, 118, 105, 57, '#d8c9a4', stroke='none')]
    b += [P('M0 118 L105 118', 'none', stroke=OUT, stroke_width=1.4)]
    b += [brick_wall(0, 118, 105, 36, '#e3d3ae', '#b9a67c', 3, False)]
    for xx in (0, 35, 70, 105):
        b += [R(xx - 1.5, 118, 3, 36, '#fbf3de', stroke=OUT, stroke_width=.9)]
    b += [P('M10 124 L10 150 M72 124 L72 150', 'none', stroke='#b9a67c', stroke_width=.8)]
    b += [ink(R(0, 150, 105, 12, '#efe3c4'), R(0, 162, 105, 13, '#c9b88c'), sw=1.4)]
    b += [R(0, 150, 105, 2.4, '#fffaf0', stroke='none', opacity=.8)]
    b += [R(0, 168, 105, 7, '#5fa8c4', stroke='none', opacity=.85)]
    b += [PLn('M8 171 q4 -2 8 0 q4 2 8 0 M60 172 q4 -2 8 0', '#ffffff', 1.4, .8)]
    # boots on the step
    b += [shadow(40, 151, 26, 3, .3)]
    b += [lit(p, boot(14, 150, .5, False, '', p), boot(46, 150, .5, False, '', p))]
    # right: alley with houses and water
    b += [R(108, 118, 107, 57, U(p + 'wt'), stroke='none')]
    b += [R(105, 118, 5, 57, '#d8c9a4', stroke=OUT, stroke_width=1.3)]
    b += [brick_wall(110, 118, 105, 24, '#caa078', '#a07048', 7)]
    # house left
    b += [ink(R(110, 118, 34, 45, '#d98a6a'), R(114, 126, 10, 14, '#4a3a34'), R(115.5, 127.5, 7, 11, '#8fc9d8'), L(119, 126, 119, 140, OUT, 1), R(112, 142, 14, 2.4, '#e3d3ae'), sw=1.4)]
    b += [ink(R(130, 128, 10, 16, '#9a6a3c'), P('M130 134 L140 134', 'none', stroke='#6a4426', stroke_width=1), sw=1.2)]
    # house right with arch
    b += [ink(R(184, 120, 31, 48, '#e6c680'), P(pointed(190, 208, 140, 126, 168), '#4a3a34'), R(192, 124, 8, 10, '#8fc9d8'), R(204, 124, 8, 10, '#8fc9d8'), sw=1.4)]
    # distant bridge
    b += [ink(P('M146 140 Q172 122 184 140 L184 146 L146 146 Z', '#e3d3ae'), P('M152 146 Q165 134 178 146 Z', '#3a5a6a'), sw=1.3)]
    b += [R(108, 145, 107, 30, U(p + 'wt'), stroke='none', opacity=.97)]
    b += [R(108, 145, 107, 3, '#2a1a10', stroke='none', opacity=.12)]
    for (x, y, w) in [(112, 152, 28), (150, 148, 24), (186, 156, 22), (120, 168, 30), (176, 170, 28), (140, 160, 18)]:
        b += [PLn('M%s %s q%s -2.6 %s 0 q%s 2.6 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#e4f3f6', 1.5, .9)]
    b += [P('M114 150 L140 150 M190 150 L206 150', 'none', stroke='#c0583a', stroke_width=2, opacity=.25)]
    b += [hid(27, 142, 7), hid(162, 158, 8)]
    b += [sparkle4(60, 124, 3), sparkle4(100, 150, 2.6)]
    H, d, body = finish(p, H, d, b, .24)
    return H, d, body, ''


# ------------------------------------------------------------------ 7
@card(7)
def c7(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#a8dcf2'), (1, '#e4f4f4')]) + LGd(p + 'by', [(0, '#f8d24e'), (1, '#e6a824')], 0, 0, 1, 0)
    d += LGd(p + 'wt', [(0, '#a9d9e4'), (1, '#6fb0cc')])
    b = [R(0, 0, 215, 120, U(p + 'sk'), stroke='none'), cloud2(38, 20, .6), cloud2(170, 16, .5)]
    # distant skyline
    b += [P('M0 70 L0 62 L16 62 L16 56 L30 56 L30 64 L46 64 Q50 50 56 64 L70 64 L70 58 L92 58 Q98 44 104 58 L130 58 L130 50 L136 50 L136 58 L160 58 L160 64 L215 64 L215 70 Z', '#b9c9d0', stroke='none', opacity=.7)]
    b += [campanile(176, 74, 42, 8)]
    ddp, pv = paving_persp(p, 74, 120, 215, '#e7dab8', '#bda97e', 107, 40, 9, 4, 11)
    d += ddp
    b += [pv]
    # puddle
    b += [E(108, 106, 98, 11, U(p + 'wt'), stroke=OUT, stroke_width=1.6), E(108, 105, 90, 8, '#ffffff', stroke='none', opacity=.18)]
    b += [P('M40 104 q8 -3 16 0 M150 108 q8 -3 16 0 M100 110 q6 -2 12 0', 'none', stroke='#ffffff', stroke_width=1.6, stroke_linecap='round', opacity=.9)]
    # boots + reflections
    b += [E(70, 108, 28, 3.6, '#c9a020', stroke='none', opacity=.3), E(152, 108, 28, 3.6, '#c9a020', stroke='none', opacity=.3)]
    b += [lit(p, boot(56, 104, 1.0, False, '', p), boot(136, 104, 1.0, False, '', p))]
    b += [splash(60, 106, 1.1), splash(140, 108, 1.1), splash(104, 112, .8)]
    for (cx, cy) in [(22, 38), (196, 52), (108, 20)]:
        b += [sparkle4(cx, cy, 4)]
    b += [P('M96 14 l0 8 M118 10 l0 6 M44 54 l-4 6 M176 30 l4 6', 'none', stroke='#4f98b8', stroke_width=1.6, stroke_linecap='round', opacity=.8)]
    H, d, body = finish(p, H, d, b, .24)
    return H, d, body, ''


# ------------------------------------------------------------------ 8
@card(8)
def c8(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#8fd0ee'), (1, '#e8f4ee')]) + LGd(p + 'wt', [(0, '#a9d9e4'), (1, '#5fa8c4')])
    d += LGd(p + 'wlL', [(0, '#e8b48a'), (1, '#c9825a')], 0, 0, 1, 0) + LGd(p + 'wlR', [(0, '#d9a070'), (1, '#b07048')], 0, 0, 1, 0)
    b = [R(0, 0, 215, 120, U(p + 'sk'), stroke='none')]
    b += [cloud2(120, 14, .5, .9)]
    # distant end of the alley: small bridge and house
    b += [ink(R(78, 36, 60, 38, '#e6d0a0'), P(pointed(96, 120, 70, 50, 74), '#3a5a6a'), R(84, 40, 7, 9, '#8fc9d8'), R(124, 40, 7, 9, '#8fc9d8'), sw=1.4)]
    b += [ink(P('M60 74 Q108 48 156 74 L156 80 L60 80 Z', '#d8c9a4'), P('M74 80 Q108 58 142 80 Z', '#3a5a6a'), sw=1.5)]
    b += [L(66, 74, 150, 74, '#fbf3de', 1.4, opacity=.7)]
    # side walls in perspective
    b += [ink(P('M0 0 L58 18 L58 82 L0 96 Z', U(p + 'wlL')), sw=1.8), ink(P('M215 0 L158 18 L158 82 L215 96 Z', U(p + 'wlR')), sw=1.8)]
    # brick texture lines
    for k in range(1, 9):
        t = k / 9.0
        b += [L(0, 96 * t, 58, 18 + 64 * t, '#9a5a3a', .8, opacity=.5), L(215, 96 * t, 158, 18 + 64 * t, '#8a5030', .8, opacity=.5)]
    for k in range(1, 5):
        b += [L(14 * k, 96 * 0 + 2 + k * 2, 14 * k, 92 - k * 1.5, '#9a5a3a', .6, opacity=.3)]
    # windows / shutters left & right
    b += [ink(P('M14 28 L34 33 L34 58 L14 58 Z', '#3a4a52'), P('M8 26 L16 28 L16 60 L8 60 Z', '#4f9a6a'), P('M34 33 L42 35 L42 58 L34 58 Z', '#4f9a6a'), sw=1.3)]
    b += [ink(P('M201 28 L181 33 L181 58 L201 58 Z', '#3a4a52'), P('M207 26 L199 28 L199 60 L207 60 Z', '#4f9a6a'), P('M181 33 L173 35 L173 58 L181 58 Z', '#4f9a6a'), sw=1.3)]
    b += [ink(P('M188 70 L172 62 L172 80 L188 84 Z', '#6a4426'), sw=1.3)]
    # laundry line
    b += [PLn('M0 14 Q108 36 215 12', '#6a4a30', 1.1)]
    for (x, col) in [(40, '#fbf8ee'), (70, '#d9392e'), (110, '#f4c64e'), (150, '#6a8ab8'), (182, '#fbf8ee')]:
        yy = 14 + (22 * (1 - ((x - 107.5) / 107.5) ** 2))
        b += [P('M%s %s l10 0 l-1 11 l-8 0 Z' % (f(x - 5), f(yy + 1)), col, stroke=OUT, stroke_width=.9)]
    # water floor, calm with reflections
    b += [P('M0 96 L58 82 L158 82 L215 96 L215 120 L0 120 Z', U(p + 'wt'), stroke=OUT, stroke_width=1.6)]
    b += [P('M64 84 L108 84 L108 110 L40 110 Z', '#e6a878', stroke='none', opacity=.28), P('M152 84 L112 84 L112 110 L172 110 Z', '#d99060', stroke='none', opacity=.25)]
    b += [R(98, 84, 20, 18, '#e6d0a0', stroke='none', opacity=.3)]
    for (x, y, w) in [(70, 92, 26), (120, 90, 30), (150, 100, 28), (90, 104, 30), (176, 108, 24), (30, 108, 26), (120, 112, 28)]:
        b += [PLn('M%s %s q%s -2.6 %s 0 q%s 2.6 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.5, .85)]
    # stone step with cat at left
    b += [ink(P('M0 78 L36 82 L36 120 L0 120 Z', '#d8c9a4'), P('M0 78 L36 82 L36 90 L0 86 Z', '#efe3c4'), sw=1.6)]
    b += [R(0, 100, 36, 2, '#b9a67c', stroke='none', opacity=.7), R(0, 112, 36, 8, '#5fa8c4', stroke='none', opacity=.9)]
    b += [PLn('M2 114 q4 -2 8 0 q4 2 8 0', '#ffffff', 1.4, .9)]
    b += [shadow(16, 85, 14, 2, .3)]
    b += [lit(p, cat(15, 84, .62))]
    # mooring pole
    b += [ink(R(196, 62, 7, 56, '#f4efe0'), R(196, 70, 7, 6, '#3a6ab8'), R(196, 84, 7, 6, '#3a6ab8'), R(196, 98, 7, 6, '#3a6ab8'), sw=1.4)]
    b += [sparkle4(120, 60, 3), sparkle4(60, 60, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 15
@card(15)
def c15(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#6fb4e0'), (.5, '#f3dc9c'), (1, '#f9d8a0')]) + LGd(p + 'wt', [(0, '#f8e0aa'), (.4, '#a9d3d8'), (1, '#4f98b8')])
    d += RGd(p + 'gl', [(0, '#fff8d0', 1), (1, '#fff8d0', 0)])
    b = [R(0, 0, 215, 120, U(p + 'sk'), stroke='none')]
    for k in range(10):
        a = -math.pi + k * math.pi / 9
        b += [P('M118 32 L%s %s L%s %s Z' % (f(118 + 150 * math.cos(a - .05)), f(32 + 150 * math.sin(a - .05)), f(118 + 150 * math.cos(a + .05)), f(32 + 150 * math.sin(a + .05))), '#fff3b8', stroke='none', opacity=.28)]
    b += [cloud2(40, 18, .6, .9, '#f6d9b0'), cloud2(180, 40, .5, .85, '#f6d9b0')]
    dd, bas = basilica(p, 36, 160, 84, 54)
    d += dd
    b += [bas, campanile(184, 84, 76, 12)]
    dd2, pal = ducale(p, 140, 215, 84, 26, 3, 'a', crenel=False)
    d += dd2
    b += [pal] if False else []
    # flooded square water
    b += [R(0, 82, 215, 38, U(p + 'wt'), stroke='none')]
    b += [R(0, 82, 215, 3, '#2a1a10', stroke='none', opacity=.14)]
    b += [P('M56 84 L146 84 L146 100 L56 100 Z', '#e8c890', stroke='none', opacity=.25)]
    for (x, y, w) in [(10, 92, 30), (90, 96, 34), (160, 94, 36), (60, 108, 32), (130, 112, 30), (20, 112, 26), (180, 110, 28)]:
        b += [PLn('M%s %s q%s -2.8 %s 0 q%s 2.8 %s 0' % (f(x), f(y), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.6, .9)]
    # gondola pole with Becco
    b += [ink(R(14, 72, 9, 42, '#f4efe0'), R(14, 82, 9, 6, '#3a6ab8'), R(14, 96, 9, 6, '#3a6ab8'), E(18.5, 72, 4.5, 1.6, '#c99a62'), sw=1.4)]
    b += [E(19, 113, 12, 2.4, '#2a5a78', stroke='none', opacity=.35), PLn('M6 113 q6 -3 12 0 q6 3 12 0', '#ffffff', 1.6, .9)]
    b += [lit(p, becco2(19, 44, .46, hat='captain', wings='wave', legs_on=True))]
    # lion flag
    b += [flagpole(196, 112, 14, 0, 18, 30, 3, 'lion')]
    # kids with boots splashing
    kids = [(64, 74, 'nico'), (104, 70, 'sofia'), (142, 78, 'toni')]
    b += [splash(64, 106, 1.3), splash(104, 108, 1.3), splash(142, 110, 1.3)]
    b += [lit(p, nico(64, 78, .55, expr='happy', la=(-30, -14), ra=(30, -14), pack=False), kid_boots(64, 78, .55, 'nico'))]
    b += [lit(p, sofia(104, 70, .55, expr='happy', la=(-30, -12), ra=(30, -12)), kid_boots(104, 70, .55, 'sofia'))]
    b += [lit(p, toni(142, 80, .52, expr='happy', la=(-34, -26), ra=(34, -26)), kid_boots(142, 80, .52, 'toni'))]
    b += [splash(52, 110, .6), splash(118, 112, .6), splash(156, 108, .55)]
    # Leo flying with glowing halo
    b += [C(118, 30, 34, U(p + 'gl'), stroke='none')]
    b += [lit(p, leo(118, 31, .48, wing='open', la=(-34, -6), ra=(34, -6), mouth='smile'))]
    b += [sparkle4(80, 20, 3.5), sparkle4(160, 14, 3.5), sparkle4(100, 54, 2.6), sparkle4(30, 78, 3), sparkle4(200, 76, 3)]
    H, d, body = finish(p, H, d, b, .22)
    return H, d, body, ''
