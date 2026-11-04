import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep3a')
from lib3 import *


def venice_card(x, y, w, h):
    b = [R(x, y, w, h, '#fbfaf4', stroke=OUT, stroke_width=2.2)]
    ix, iy, iw, ih = x + 4, y + 4, w - 8, h - 8
    b.append(R(ix, iy, iw, ih, '#bfe3f2', stroke='none'))
    b.append(R(ix, iy + ih * 0.62, iw, ih * 0.38, '#4a9aa8', stroke='none'))
    cols = ['#e8b58a', '#d98a6a', '#efd7a0', '#c9806a', '#e8c9a0']
    bw = iw / 5.0
    for i in range(5):
        hh = ih * (0.30 + 0.07 * ((i * 3) % 3))
        b.append(R(ix + i * bw, iy + ih * 0.62 - hh, bw, hh, cols[i], stroke=OUT, stroke_width=1.2))
        b.append(R(ix + i * bw + bw * 0.25, iy + ih * 0.62 - hh + 5, bw * 0.2, 6, '#6b4428', stroke='none'))
        b.append(R(ix + i * bw + bw * 0.6, iy + ih * 0.62 - hh + 5, bw * 0.2, 6, '#6b4428', stroke='none'))
    b.append(P('M%s %s Q%s %s %s %s L%s %s Q%s %s %s %s Z' % (f(ix + iw * 0.3), f(iy + ih * 0.82), f(ix + iw * 0.4), f(iy + ih * 0.9), f(ix + iw * 0.5), f(iy + ih * 0.84), f(ix + iw * 0.58), f(iy + ih * 0.84), f(ix + iw * 0.66), f(iy + ih * 0.8), f(ix + iw * 0.72), f(iy + ih * 0.76)), '#2a1a10', stroke=OUT, stroke_width=1))
    b.append(C(x + w / 2.0, y - 1, 3.2, '#e2573a', stroke_width=1.5))
    return G(*b)


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 738, 330
    b = []
    defs = gid_defs(('e3t1g1', 'v', [(0, '#7fc4ee', 1), (1, '#d7eefa', 1)]),
                    ('e3t1g2', 'r', [(0, '#fff0b0', 0.85), (1, '#ffd36e', 0)]))
    b.append(R(0, 0, W, H, '#dfe6e4'))
    b.append(R(0, 250, W, 80, '#c49a6a'))
    b.append(L(0, 250, W, 250, '#8b6a45', 3))
    for i in range(0, 760, 70):
        b.append(L(i, 250, i - 34, 330, '#a97f52', 1.5))
    # window with afternoon sky
    b.append(R(22, 48, 132, 108, 'url(#e3t1g1)', stroke=OUT, stroke_width=3))
    b.append(cloud(60, 84, 0.6, 0.95) + cloud(118, 112, 0.5, 0.9))
    b.append(C(132, 74, 11, '#fff0a8', stroke='none'))
    b.append(P('M22 156 L22 138 Q50 126 78 140 Q108 126 154 138 L154 156 Z', '#8fbf7a', stroke='none'))
    b.append(L(88, 48, 88, 156, OUT, 3) + L(22, 102, 154, 102, OUT, 3))
    b.append(R(14, 156, 148, 8, '#efe0c2', stroke=OUT, stroke_width=2.5))
    b.append(P('M10 44 L22 44 L22 164 L10 164 Z', '#6fa3c9', stroke=OUT, stroke_width=2))
    b.append(P('M154 44 L166 44 L166 164 L154 164 Z', '#6fa3c9', stroke=OUT, stroke_width=2))
    # bed
    b.append(R(0, 196, 176, 40, '#e6d8c0', stroke=OUT, stroke_width=2.5, rx=4))
    b.append(R(0, 222, 186, 40, '#e2573a', stroke=OUT, stroke_width=2.5, rx=6))
    b.append(R(8, 202, 58, 24, '#fbfaf4', stroke=OUT, stroke_width=2.2, rx=8))
    b.append(P('M72 232 L186 232', stroke='#f08a72', stroke_width=3))
    b.append(R(168, 256, 10, 12, '#8b5a35', stroke=OUT, stroke_width=2))
    # postcard of Venice on wall
    b.append(venice_card(608, 54, 88, 66))
    # desk with lamp
    b.append(R(580, 214, 158, 12, '#b9783f', stroke=OUT, stroke_width=2.5))
    b.append(R(588, 226, 140, 40, '#a06a3c', stroke=OUT, stroke_width=2.5))
    b.append(R(598, 234, 56, 26, '#8b5a35', stroke=OUT, stroke_width=1.8, rx=2))
    b.append(R(662, 234, 56, 26, '#8b5a35', stroke=OUT, stroke_width=1.8, rx=2))
    b.append(R(592, 266, 12, 30, '#8b5a35', stroke=OUT, stroke_width=2))
    b.append(P('M690 214 L694 186 L700 186 L704 214 Z', '#6e4a2c', stroke=OUT, stroke_width=2))
    b.append(P('M678 188 L688 164 L710 164 L720 188 Z', '#f2c043', stroke=OUT, stroke_width=2.4))
    b.append(R(614, 200, 40, 14, '#4f74a8', stroke=OUT, stroke_width=1.8) + R(618, 190, 34, 10, '#e2573a', stroke=OUT, stroke_width=1.8))
    # rug
    b.append(E(340, 312, 300, 24, '#6fa3c9', stroke=OUT, stroke_width=2.5))
    b.append(E(340, 312, 270, 17, 'none', stroke='#fbfaf4', stroke_width=2.5))
    # kids
    b.append(sofia(190, 241, 1.15, la=(-16, 14), ra=(16, 14), expr='wow', look=3))
    b.append(toni(472, 259, 1.1, la=(-24, 4), ra=(24, 4), expr='wow', look=-3))
    b.append(nico(330, 248, 1.2, la=(-22, 16), ra=(30, -4), expr='smile', pack=True))
    b.append(C(368, 238, 30, 'url(#e3t1g2)', stroke='none'))
    b.append(coin(368, 239, 10, -10))
    b.append(star(392, 214, 5) + star(350, 212, 4) + star(376, 262, 4))
    ov = cap('Una settimana dopo.') + abal('La moneta di Tito… si sta scaldando!', 262, 20, 300, 'bl', 17, 12)
    return panel(W, H, ''.join(b), 'La camera di Nico di pomeriggio, con la cartolina di Venezia appesa al muro: Nico mostra a Sofia e Toni una piccola moneta di bronzo', ov, bg='#dfe6e4', height=330, defs=defs)


# ---------------------------------------------------------------- panel 2: coin close-up
def p2():
    W, H = 362, 290
    b = []
    defs = gid_defs(('e3t1g4', 'r', [(0, '#fff6cf', 1), (0.45, '#ffd36e', 0.7), (1, '#f4b942', 0)]),
                    ('e3t1g5', 'v', [(0, '#5a3424', 1), (1, '#2e1a10', 1)]))
    b.append(R(0, 0, W, H, 'url(#e3t1g5)'))
    b.append(C(181, 128, 200, 'url(#e3t1g4)', stroke='none'))
    rays = []
    for k in range(20):
        a = 2 * math.pi * k / 20
        rays.append(L(181 + 100 * math.cos(a), 128 + 100 * math.sin(a), 181 + 330 * math.cos(a), 128 + 330 * math.sin(a), '#ffe08a', 4, stroke_linecap='round'))
    b.append(G(*rays, opacity=0.6))
    # open palm
    b.append(INK(limb(98, 262, 62, 214, SK, 24, hand=None), limb(120, 246, 98, 192, SK, 22, hand=None), limb(262, 262, 296, 220, SK, 24, hand=None),
                 limb(240, 246, 258, 196, SK, 22, hand=None), P('M70 290 Q76 232 181 226 Q290 232 296 290 Z', SK),
                 P('M120 258 Q181 240 242 258', stroke='#e0b896', stroke_width=2)))
    b.append(coin(181, 138, 70, -6))
    for (x, y, r) in [(52, 60, 9), (310, 54, 11), (36, 150, 7), (326, 168, 8), (110, 24, 6), (250, 22, 7), (181, 34, 8)]:
        b.append(star(x, y, r, '#fff6cf'))
    b.append(G(star(84, 108, 5, '#ffe08a'), star(284, 108, 5, '#ffe08a'), star(238, 68, 4, '#ffe08a')))
    return panel(W, H, ''.join(b), 'Primo piano della piccola moneta di bronzo che brilla d\'oro nel palmo della mano di Nico', '', bg='#2e1a10', defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 362, 290
    b = []
    defs = gid_defs(('e3t1g6', 'r', [(0, '#fff6cf', 1), (0.5, '#ffe9a3', 0.7), (1, '#ffd36e', 0)]),
                    ('e3t1g7', 'v', [(0, '#f6c76a', 1), (1, '#fbe7a6', 1)]))
    b.append(R(0, 0, W, H, 'url(#e3t1g7)'))
    b.append(P('M200 282 L250 282 L372 -10 L50 -10 Z', '#fff6cf', opacity=0.55, stroke='none'))
    b.append(C(225, 170, 150, 'url(#e3t1g6)', stroke='none'))
    for k in range(14):
        a = math.pi * (1.05 + 0.9 * k / 13.0)
        b.append(L(225 + 90 * math.cos(a), 170 + 90 * math.sin(a), 225 + 260 * math.cos(a), 170 + 260 * math.sin(a), '#f0a92e', 3, opacity=0.5, stroke_linecap='round'))
    b.append(coin(225, 292, 24, 0))
    b.append(leo(225, 190, 1.05, wing='small', la=(-46, -8), ra=(46, -8), eyes='proud'))
    b.append(toni(52, 306, 1.1, la=(-24, -4), ra=(36, -52), expr='happy'))
    b.append(sandwich(95, 246, 1.15, -10))
    for (x, y, r) in [(320, 90, 8), (336, 210, 7), (170, 100, 6), (300, 250, 6), (140, 210, 5)]:
        b.append(star(x, y, r, '#fff6cf'))
    ov = abal('Pax tibi! Oggi andiamo dove nasce Venezia.', 150, 4, 206, 'bl', 15, 10) + abal('Stavolta la merenda me la porto io!', 6, 104, 140, 'bl', 14, 10)
    return panel(W, H, ''.join(b), 'Leo esce dalla luce dorata della moneta mentre Toni alza un panino', ov, bg='#f6c76a', defs=defs)


# ---------------------------------------------------------------- panel 4: swirl
def p4():
    W, H = 738, 392
    cx, cy = 530, 196
    defs = gid_defs(('e3t1g8', 'r', [(0, '#ffffff', 1), (0.35, '#ffe9a3', 0.95), (1, '#f4b942', 0)]),
                    ('e3t1g9', 'v', [(0, '#f8c660', 1), (1, '#fde8a8', 1)]))
    b = [swirl_sky(W, H, cx, cy, 'e3t1g8', 'e3t1g9')]
    b.append(nico(150, 262, 1.25, rot=38, la=(-30, -30), ra=(30, -22), expr='wow'))
    b.append(sofia(292, 248, 1.15, rot=48, la=(-30, -26), ra=(28, -30), expr='wow'))
    b.append(toni(408, 228, 1.0, rot=62, la=(-34, -22), ra=(30, -28), expr='wow'))
    b.append(sandwich(372, 250, 0.9, 40))
    b.append(leo(560, 190, 0.85, rot=58, wing='open', la=(-34, -10), ra=(34, -16), eyes='open'))
    for (x, y, r) in [(220, 120, 8), (350, 330, 9), (440, 90, 7), (650, 320, 8), (680, 80, 9), (90, 150, 6), (600, 360, 6), (200, 350, 7)]:
        b.append(star(x, y, r, '#fff6cf'))
    ov = sfx('FWOOSH!', 24, 14, 84, -8)
    return panel(W, H, ''.join(b), 'Un vortice dorato risucchia Nico, Sofia, Toni e Leo con linee di velocità', ov, bg='#f8c660', flex=True, defs=defs)


rows = [p1(), row2(p2(), p3(), height=290), p4()]
write(OUTD + 'Ep3_Tavola1.dc.html', page('Ep. 3 Tavola 1 – La moneta', rows, 1))
print('ok')
