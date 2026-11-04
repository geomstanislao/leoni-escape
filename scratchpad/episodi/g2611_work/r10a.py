from h10 import *


def sad_leo_overlay(x, y, s):
    b = [P('M-17 -35 L-5 -40 M17 -35 L5 -40', 'none', stroke_width=2.6),
         P('M-6 -7 Q0 -13 6 -7', 'none', stroke_width=2.2),
         P('M-12 -22 Q-9 -14 -12 -10 Q-15 -14 -12 -22 Z', '#bfe3f2', stroke_width=1.3),
         C(-12.6, -15.5, 1, '#ffffff', stroke='none')]
    return ink(*b, transform=xf(x, y, s))


def sandwich2(x, y, s=1, rot=0):
    b = []
    b.append(E(0, 21, 42, 5, '#2a1a10', stroke='none', opacity=.25))
    b.append(P('M-38 8 L38 8 Q39 21 26 21 L-26 21 Q-39 21 -38 8 Z', '#dba04e'))
    b.append(P('M-30 14 Q0 19 30 14', 'none', stroke='#f3cf8a', stroke_width=1.6))
    b.append(P('M-40 4 Q-30 10 -20 5 Q-10 11 0 5 Q10 11 20 5 Q30 10 40 4 L38 9 L-38 9 Z', '#f08a8a'))
    b.append(P('M-41 -2 L41 -2 L41 5 L-41 5 Z M30 5 L41 5 L36 14 Z', '#f6cc4a'))
    b.append(P('M-41 -2 L41 -2', 'none', stroke='#fff0a0', stroke_width=1.6))
    b.append(P('M-41 -2 Q-34 -9 -27 -3 Q-20 -10 -13 -3 Q-6 -10 1 -3 Q8 -10 15 -3 Q22 -10 29 -3 Q36 -9 41 -2 L41 -1 L-41 -1 Z', '#76b24a'))
    b.append(P('M-36 -5 Q-30 -8 -26 -4 M-8 -6 Q-2 -9 3 -5 M20 -6 Q25 -9 30 -5', 'none', stroke='#a8d46a', stroke_width=1.4))
    b.append(C(-33, -3, 4.2, '#d9392e') + C(33, -3, 4.2, '#d9392e'))
    b.append(P('M-39 -4 Q-42 -36 0 -38 Q42 -36 39 -4 Z', '#e8b25e'))
    b.append(P('M-33 -8 Q-34 -28 -10 -33', 'none', stroke='#fbe2a0', stroke_width=3, opacity=.9))
    b.append(P('M24 -34 Q38 -30 39 -4 L28 -4 Q32 -24 24 -34 Z', '#c98a3a', stroke='none', opacity=.55))
    for (cx, cy, r) in [(-16, -26, 1), (-4, -30, -20), (10, -28, 15), (22, -22, 40), (-26, -18, 70), (4, -20, 5), (-12, -14, 25), (16, -14, -10)]:
        b.append(E(cx, cy, 2.3, 1.2, '#fff4d2', stroke='none', transform='rotate(%s %s %s)' % (f(r), f(cx), f(cy))))
    return ink(*b, transform=T_(x, y, s, rot), sw=2.4)


def cheese_tri(x, y, s=1):
    return ink(P('M0 0 L18 -3 L18 6 L0 6 Z', '#f6cc4a'), C(11, 1, 1.4, '#e0a92a', stroke='none'), C(5, 3, 1, '#e0a92a', stroke='none'), transform=T_(x, y, s), sw=1.6)


def backpack(x, yb, col, dark, light, item, tag, p):
    b = []
    b.append(E(0, 3, 40, 6, '#2a1a10', stroke='none', opacity=.3))
    b.append(P('M-31 0 Q-36 -30 -27 -54 L27 -54 Q36 -30 31 0 Q0 7 -31 0 Z', U(p + 'bp' + tag)))
    b.append(E(0, -54, 27, 8, dark))
    b.append(E(0, -53, 22, 5.5, '#2a1a10', stroke='none', opacity=.55))
    if item == 'nb':
        b.append(G(
            P('M-30 -48 L-2 -52 L-2 -86 L-32 -80 Z', '#fffdf4'), P('M30 -48 L2 -52 L2 -86 L32 -80 Z', '#fffdf4'),
            P('M-29 -56 L-3 -60 M-29 -62 L-3 -66 M-29 -68 L-3 -72 M-29 -74 L-3 -78', 'none', stroke='#8fb8e0', stroke_width=1.1),
            P('M29 -56 L3 -60 M29 -62 L3 -66 M29 -68 L3 -72', 'none', stroke='#8fb8e0', stroke_width=1.1),
            P('M8 -74 L14 -80 L20 -73', 'none', stroke='#d9392e', stroke_width=2),
            P('M0 -52 L0 -86', 'none', stroke_width=1.6), P('M-32 -80 L-2 -86 L-2 -85 L-32 -79', 'none', stroke='#d8cfb8', stroke_width=1.2),
            P('M-32 -80 L-30 -48 M32 -80 L30 -48', 'none', stroke='#e4dcc6', stroke_width=2.2)))
    else:
        b.append(G(sandwich2(0, -53, .56)))
    b.append(P('M-27 -54 Q0 -45 27 -54 L26 -49 Q0 -40 -26 -49 Z', U(p + 'bp' + tag)))
    b.append(P('M-27 -54 Q0 -45 27 -54', 'none', stroke=OUT, stroke_width=1.6))
    b.append(P('M-27 -22 Q0 -17 27 -22 L26 -2 Q0 3 -26 -2 Z', dark))
    b.append(P('M-27 -22 Q0 -17 27 -22', 'none', stroke=light, stroke_width=1.6))
    b.append(P('M-21 -13 Q0 -9 21 -13', 'none', stroke='#2a1a10', stroke_width=1.2, stroke_dasharray='2 2.4', opacity=.7))
    b.append(R(-7, -24, 14, 11, '#e9c46a', rx=2.5))
    b.append(R(-4, -21, 8, 5, '#a87a22', rx=1.5, stroke_width=1.2))
    b.append(P('M-18 -50 Q-22 -30 -19 -6 M18 -50 Q22 -30 19 -6', 'none', stroke=dark, stroke_width=5))
    b.append(P('M-18 -50 Q-22 -30 -19 -6 M18 -50 Q22 -30 19 -6', 'none', stroke=light, stroke_width=1.5, opacity=.8))
    b.append(P('M-30 -34 Q-36 -22 -30 -10', 'none', stroke=light, stroke_width=2.4, opacity=.6))
    return ink(*b, transform=T_(x, yb, 1), sw=2.2)


# ------------------------------------------------------------------ 1
@card(1)
def c1(p):
    H = 120
    d = LGd(p + 'sk', [(0, '#7cc4ec'), (.55, '#bfe3f0'), (1, '#f8efd0')]) + lit_defs(p)
    b = [R(0, 0, 215, 100, U(p + 'sk'), stroke='none')]
    b += [cloud2(40, 17, .8), cloud2(150, 11, .65), cloud2(100, 30, .5)]
    b += [PLn('M120 18 q3 -4 6 0 q3 -4 6 0 M135 25 q3 -3 5 0 q3 -3 5 0', '#4a5560', 1.1, .7)]
    dd, pal = ducale(p, -6, 168, 98, 62, 6, 'a')
    d += dd
    b += [campanile(190, 98, 98, 15), pal]
    # sea strip on right
    b += [R(168, 90, 20, 8, '#6fb3c9', stroke='none', opacity=.7)]
    ddp, pv = paving_persp(p, 94, 120, 215, '#e7dab8', '#bda97e', 107, 60, 2, 5, 11)
    d += ddp
    b += [pv]
    b += [E(190, 100, 20, 2.6, '#2a1a10', stroke='none', opacity=.18)]
    # poles
    for px in (12, 202):
        b += [R(px - 2.2, 70, 4.4, 40, '#f4efe0', stroke=OUT, stroke_width=1.3), R(px - 2.2, 76, 4.4, 5, '#d9392e', stroke='none'), R(px - 2.2, 88, 4.4, 5, '#d9392e', stroke='none'), R(px - 2.2, 100, 4.4, 5, '#d9392e', stroke='none')]
    b += [flagpole(26, 106, 62, 0, 26, 17, 2, 'lion')]
    b += [C(107, 56, 44, '#fff2b8', stroke='none', opacity=.3)]
    b += [shadow(108, 111, 34, 6, .35)]
    b += [lit(p, leo(108, 66, .83, wing='small', ra=(40, -26), mouth='none')), sad_leo_overlay(108, 66, .83)]
    b += [sparkle4(150, 40, 3), sparkle4(66, 44, 3)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 2
@card(2)
def c2(p):
    H = 175
    d = lit_defs(p) + LGd(p + 'wl', [(0, '#f1e4c4'), (1, '#d9c79c')]) + LGd(p + 'ar', [(0, '#2a1a14'), (1, '#6e5040')])
    d += LGd(p + 'cl', [(0, '#c9b78a'), (.35, '#f6ecd0'), (.7, '#e6d6ac'), (1, '#a89468')], 0, 0, 1, 0)
    d += RGd(p + 'lg', [(0, '#fff6c8', .55), (1, '#fff6c8', 0)], .5, .5, .5)
    b = [R(0, 0, 215, 130, U(p + 'wl'), stroke='none')]
    # upper loggia: dark arches with depth
    b += [R(0, 4, 215, 4, '#fbf3de', stroke=OUT, stroke_width=1.2)]
    for i in range(7):
        a = 3 + i * 31
        c = a + 24
        b += [P(pointed(a, c, 36, 14, 54), U(p + 'ar'), stroke=OUT, stroke_width=1.3)]
        b += [P(pointed(a + 4, c - 4, 38, 20, 54), '#8a6c58', stroke='none', opacity=.5)]
        b += [R(a + 10, 40, 4, 14, '#3a2a20', stroke='none', opacity=.5)]
        b += [R(a + 24, 28, 7, 26, '#efe1c0', stroke=OUT, stroke_width=1.1)]
    b += [R(0, 54, 215, 6, '#e3d3ac', stroke=OUT, stroke_width=1.4)]
    for i in range(18):
        b += [C(6 + i * 12, 57, 1.6, '#a65e4a', stroke='none')]
    # wall with diamond stripes
    b += [R(0, 60, 215, 22, '#f0e2c4', stroke='none')]
    # lower arcades left & right
    for (x0, n) in [(0, 2), (150, 2)]:
        for i in range(n):
            a = x0 + 3 + i * 31
            c = a + 28
            b += [P(pointed(a, c, 96, 74, 124), U(p + 'ar'), stroke=OUT, stroke_width=1.3)]
            b += [P(pointed(a + 4, c - 4, 98, 82, 124), '#7a5e4c', stroke='none', opacity=.5)]
    b += [R(60, 60, 95, 64, '#eadcbc', stroke='none')]
    # central doorway (porta della Carta side) at the head of the stairs
    b += [R(70, 56, 70, 26, '#f1e4c8', stroke=OUT, stroke_width=1.5)]
    b += [P(pointed(92, 118, 74, 58, 82), '#4a3426', stroke=OUT, stroke_width=1.3), P(pointed(96, 114, 74, 62, 82), '#6e5040', stroke='none', opacity=.6)]
    # statues Mars & Neptune on plinths
    for sx in (74, 136):
        sflip = (sx == 136)
        b += [ink(R(sx - 7, 70, 14, 12, '#cfc7b4'), R(sx - 9, 68.5, 18, 3, '#e3dcc8'), sw=1.3)]
        b += [ink(P('M%s 70 L%s 48 L%s 48 L%s 70 Z' % (f(sx - 5), f(sx - 6), f(sx + 6), f(sx + 5)), '#ece7d9'), C(sx, 43, 5.2, '#ece7d9'),
                  P('M%s 46 L%s 66' % (f(sx + (8 if not sflip else -8)), f(sx + (8 if not sflip else -8))), 'none', stroke='#8b5a2b', stroke_width=2),
                  P('M%s 50 Q%s 56 %s 64' % (f(sx - 5), f(sx - 10), f(sx - 5)), 'none', stroke='#cfc7b4', stroke_width=2), sw=1.3),
              P('M%s 48 L%s 68' % (f(sx + 2), f(sx + 2)), 'none', stroke='#cfc7b4', stroke_width=1.6, opacity=.8)]
    # stairs (giants' staircase)
    for i in range(8):
        w_ = 44 + i * 6.2
        yy = 82 + i * 5.3
        b += [ink(R(107.5 - w_ / 2, yy, w_, 5.3, '#e9dcbc'), sw=1.2), R(107.5 - w_ / 2 + .8, yy + 4.4, w_ - 1.6, 1, '#b9a67c', stroke='none')]
    # balustrades
    b += [P('M85 82 L62 124 L72 124 L88 90 Z', U(p + 'cl'), stroke=OUT, stroke_width=1.3), P('M130 82 L153 124 L143 124 L127 90 Z', U(p + 'cl'), stroke=OUT, stroke_width=1.3)]
    b += [R(0, 124, 0, 0, 'none')] if False else []
    # light from left
    b += [P('M-10 0 L40 0 L110 130 L40 130 Z', U(p + 'lg'), stroke='none', opacity=.5)]
    dd, pv = paving_persp(p, 124, H, 215, '#dcccA6'.lower(), '#b29c70', 107, 72, 4, 8, 12)
    d += dd
    b += [pv]
    # checker inlay in paving
    for i in range(8):
        b += [P('M%s 128 L%s 128 L%s 134 L%s 134 Z' % (f(60 + i * 12.5), f(60 + (i + 1) * 12.5), f(58 + (i + 1) * 13), f(58 + i * 13)), '#c9b88c', stroke='none', opacity=.35 if i % 2 else 0)]
    # wellhead
    b += [shadow(110, 166, 16, 3, .3)]
    b += [ink(P('M99 150 Q99 164 103 166 L117 166 Q121 164 121 150 Z', '#b9743f'), E(110, 150, 11, 3.6, '#8a5a2b'), E(110, 150, 8, 2, '#2a1a10', stroke='none'),
              P('M101 156 L119 156', 'none', stroke='#e4a76a', stroke_width=1.2), sw=1.6)]
    # column with capital for Becco
    b += [shadow(171, 154, 20, 3, .32)]
    b += [ink(R(158, 147, 26, 7, '#e3dcc8'), R(161, 141, 20, 7, '#d8cfb8'),
              R(164, 98, 14, 44, U(p + 'cl')), P('M164 98 L164 142 M171 98 L171 142', 'none', stroke='#a89468', stroke_width=.9, opacity=.6),
              P('M160 98 Q160 90 171 90 Q182 90 182 98 Z', '#e9e2cf'), R(158, 97, 26, 4, '#f2ecd9'),
              P('M161 94 Q165 99 169 94 M173 94 Q177 99 181 94', 'none', stroke='#a89468', stroke_width=1), sw=1.4)]
    # Becco with the corno on the capital
    b += [lit(p, becco2(171, 69.5, .5, hat='corno', beak='closed'))]
    # old doge, sad, hatless
    b += [shadow(46, 158, 16, 3, .33)]
    b += [lit(p, doge(46, 122, .52, 'sad', True, la=(-22, 26), ra=(22, 26)))]
    b += [hid(46, 122, 5), hid(170, 73, 9)]
    b += [sparkle4(24, 20, 3.4), sparkle4(196, 50, 3)]
    H, d, body = finish(p, H, d, b, .28)
    return H, d, body, ''


# ------------------------------------------------------------------ 3
@card(3)
def c3(p):
    H = 120
    d = LGd(p + 'sk', [(0, '#6d86b8'), (.55, '#b9c4dc'), (1, '#f3d8b0')]) + lit_defs(p) + LGd(p + 'gd', [(0, '#a8977a'), (1, '#7a6a4e')])
    b = [R(0, 0, 215, 98, U(p + 'sk'), stroke='none')]
    b += [cloud2(36, 24, .9, .8, '#e8c8b0'), cloud2(176, 14, .7, .8, '#e8c8b0'), cloud2(120, 38, .6, .6, '#e8c8b0')]
    # distant hills and camp
    b += [P('M0 78 Q40 62 90 74 T170 68 T215 74 L215 100 L0 100 Z', '#8a9aa0', stroke='none', opacity=.7)]
    b += [P('M0 86 Q50 74 110 84 T215 80 L215 100 L0 100 Z', '#6f8a74', stroke='none')]
    for tx_ in (22, 60, 170, 198):
        b += [ink(P('M%s 92 L%s 80 L%s 92 Z' % (f(tx_ - 9), f(tx_), f(tx_ + 9)), '#efe3c8'), P('M%s 92 L%s 80 L%s 92 Z' % (f(tx_), f(tx_), f(tx_ + 9)), '#cdbd9a', stroke='none'), sw=1.1)]
    b += [R(0, 94, 215, 26, U(p + 'gd'), stroke='none')]
    b += [P('M0 96 Q60 92 110 96 T215 94', 'none', stroke='#d8c8a0', stroke_width=1.4, opacity=.6)]
    for i in range(8):
        b += [E(18 + i * 28, 104 + (i % 3) * 5, 10, 1.6, '#5a4a32', stroke='none', opacity=.3)]
    # smoke
    b += [B.smoke(150, 82, 40, 8, '#8f8f98', .5), B.smoke(40, 84, 36, 8, '#8f8f98', .45)]
    # french flags
    b += [flagpole(20, 100, 30, 0, 32, 22, 3, 'fr'), flagpole(192, 100, 30, 0, 32, 22, 3, 'fr')]
    # cannon right
    b += [ink(E(176, 108, 9, 9, '#8b5a2b'), C(176, 108, 3, '#3a2a20'), R(150, 98, 38, 9, '#5a5a62'), E(150, 102.5, 3, 4.5, '#2a2a30'), sw=1.6)]
    b += [P('M152 99 L184 99', 'none', stroke='#9a9aa4', stroke_width=1.2, opacity=.8)]
    b += [C(107, 50, 50, '#fff0c8', stroke='none', opacity=.22)]
    b += [shadow(107, 115, 44, 5, .3)]
    b += [lit(p, napoleon(107, 72, .92))]
    b += [sparkle4(60, 30, 3), sparkle4(158, 44, 3)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 4
@card(4)
def c4(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'wl', [(0, '#f6e8c6'), (1, '#e6d2a4')])
    d += LGd(p + 'bpy', [(0, '#f8cf5a'), (1, '#e0a22a')], 0, 0, 1, 0) + LGd(p + 'bpb', [(0, '#7a9ccc'), (1, '#4a6aa0')], 0, 0, 1, 0)
    b = [R(0, 0, 215, 74, U(p + 'wl'), stroke='none')]
    # window light + wooden floor
    b += [R(150, 6, 46, 50, '#cfe9f4', stroke=OUT, stroke_width=2), R(172.5, 6, 1.6, 50, OUT, stroke='none'), R(150, 30, 46, 1.6, OUT, stroke='none')]
    b += [P('M152 8 L172 8 L160 30 L152 30 Z', '#ffffff', stroke='none', opacity=.55)]
    b += [P('M150 56 L110 120 L60 120 L130 56 Z', '#fff6c8', stroke='none', opacity=.25)]
    b += [R(144, 56, 58, 4, '#c99a62', stroke=OUT, stroke_width=1.5)]
    # shelf skirting
    b += [R(0, 70, 215, 5, '#c9a878', stroke=OUT, stroke_width=1.4)]
    dd, wp = wood_planks(p, 0, 75, 215, 45, '#c79a62', '#9a6c3e', 30, 0)
    d += dd
    b += [wp]
    for i in range(0, 215, 30):
        b += [L(i, 75, i - 6 + i * .03, 120, '#4a3020', 1.1, opacity=.5)]
    b += [R(0, 75, 215, 4, '#000000', stroke='none', opacity=.14)]
    # backpacks
    b += [backpack(56, 104, '', '#caa020', '#fbe190', 'nb', 'y', p)]
    b += [backpack(158, 104, '', '#3a5a90', '#a8c4ec', 'sw', 'b', p)]
    b += [sparkle4(98, 40, 3.4), sparkle4(112, 70, 2.6), sparkle4(18, 36, 3)]
    # pencil + coin on the floor
    b += [ink(P('M92 112 L124 104', 'none', stroke_width=5), P('M92 112 L124 104', 'none', stroke='#e9c46a', stroke_width=3), P('M124 104 L130 102.5', 'none', stroke='#f2c9a0', stroke_width=3), sw=1.2)]
    H, d, body = finish(p, H, d, b, .28)
    return H, d, body, ''
