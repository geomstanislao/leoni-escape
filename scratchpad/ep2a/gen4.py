import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'
OCHRE, OLIVE, TERRA, WHITE = '#d1a85a', '#9a9a5a', '#c8683f', '#efe6d0'
SKYSTOPS = [(0, '#7ec6ea', 1), (1, '#d8eef3', 1)]


def feather(x, y, rot=0, sc=1):
    return G(P('M0 0 Q16 -9 42 -3 Q26 9 0 0 Z', '#b9bcc2'), P('M0 0 L40 -3', stroke='#8a8d94', stroke_width=1.6),
             P('M10 -1 L16 5 M18 -2 L24 4 M26 -3 L31 2', stroke='#8a8d94', stroke_width=1.2),
             stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round',
             transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def crumb(x, y, r=3.5):
    return C(x, y, r, '#e6c88a', stroke=OUT, stroke_width=1.5)


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 362, 320
    defs = gid_defs(('e2t4g1', 'v', SKYSTOPS))
    b = [R(0, 0, W, 150, 'url(#e2t4g1)')]
    b.append(house(-10, 165, 150, 120, '#e8d5b0', TERRA))
    b.append(house(150, 165, 120, 80, '#d9c29a', '#b85a36', door=False))
    b.append(house(262, 165, 110, 100, '#efe0c2', TERRA))
    b.append(paving(0, 160, W, 160, 22, 44, '#cdbf9f', '#a89874', 51))
    b.append(L(0, 160, W, 160, OUT, 2.5))
    b.append(toni(105, 228, 1.5, bend=55, target=(84, 52), expr='wow', look=2))
    b.append(feather(222, 305, -8, 1.0))
    for (x, y, r) in [(262, 296, 3.5), (284, 303, 3), (303, 295, 3.5), (324, 301, 3), (344, 297, 2.6), (272, 310, 2)]:
        b.append(crumb(x, y, r))
    ov = balloon('Una piuma grigia… e briciole di pane!', 8, 6, 270, 88, 'bl', 17, 16)
    return panel(W, H, ''.join(b), 'Toni si china sulle pietre della strada: una piuma grigia e una scia di briciole di pane', ov, bg='#e8d5b0', defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 362, 320
    defs = gid_defs(('e2t4g2', 'v', SKYSTOPS))
    b = [R(0, 0, W, 150, 'url(#e2t4g2)')]
    b.append(house(-10, 170, 160, 130, '#efe0c2', TERRA))
    b.append(house(230, 170, 140, 110, '#e0c9a0', '#b85a36'))
    b.append(paving(0, 165, W, 155, 22, 44, '#cdbf9f', '#a89874', 61))
    b.append(L(0, 165, W, 165, OUT, 2.5))
    b.append(nico(100, 312 - 62 * 1.5, 1.5, la=(-30, -4), ra=(32, -10), expr='wow', look=4))
    b.append(sofia(262, 312 - 72 * 1.5, 1.5, la=(-32, -10), ra=(30, -4), expr='wow', look=-4))
    b.append(P('M150 118 L162 106 M158 134 L174 130 M212 118 L200 106 M204 134 L188 130', stroke=OUT, stroke_width=3, stroke_linecap='round'))
    ov = balloon('Becco!', 36, 8, 124, 62, 'br', 24, 8) + balloon('Becco!', 206, 8, 124, 62, 'bl', 24, 8)
    return panel(W, H, ''.join(b), 'Nico e Sofia si guardano con la stessa espressione sorpresa e dicono Becco', ov, bg='#e8d5b0', defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 738, 340
    defs = gid_defs(('e2t4g3', 'v', [(0, '#6fc0ea', 1), (1, '#e6f2f0', 1)]))
    b = [R(0, 0, W, H, 'url(#e2t4g3)')]
    b.append(cloud(110, 60, 1.0) + cloud(300, 36, 0.7) + cloud(640, 90, 0.9))
    # distant roofs
    b.append(P('M0 250 L0 210 L60 210 L90 190 L170 190 L200 214 L250 214 L250 250 Z', '#b9783f', stroke=OUT, stroke_width=2, opacity=0.9))
    b.append(R(120, 160, 18, 34, '#a8502e', stroke=OUT, stroke_width=2))
    # main roof slope
    slope_y = lambda x: 300 + (150 - 300) * (x + 10) / 748.0
    b.append(P('M-10 300 L738 150 L738 340 L-10 340 Z', '#c8683f', stroke=OUT, stroke_width=3))
    for k in range(1, 8):
        off = k * 24
        b.append(L(-10, 300 + off, 738, 150 + off, '#a14f2c', 2))
    for k in range(0, 8):
        off = k * 24
        for x in range(0, 740, 36):
            xx = x + (k % 2) * 18
            y0 = slope_y(xx) + off
            b.append(L(xx, y0, xx + 1, y0 + 24 - 2, '#a14f2c', 1.3))
    b.append(P('M-10 296 L738 146 L738 158 L-10 308 Z', '#e0875a', stroke=OUT, stroke_width=2.5))
    # Becco
    bx = 420
    by = slope_y(bx) + 12
    b.append(becco(bx, by - 52 * 1.5, 1.5, rot=-4, bundle=True))
    for (x, y) in [(300, 120), (560, 60)]:
        b.append(star(x, y, 6, '#f4b942'))
    ov = balloon('Rotoli? Perfetti per farci il nido!', 470, 16, 252, 78, 'bl', 18, 14)
    return panel(W, H, ''.join(b), 'Becco in piedi su un tetto di tegole rosse stringe tre rotoli legati con lo spago', ov, bg='#bfe3f2', height=340, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4():
    W, H = 738, 352
    defs = gid_defs(('e2t4g4', 'v', [(0, '#6fc0ea', 1), (1, '#f1f4e6', 1)]), ('e2t4g5', 'v', [(0, '#6fc3c9', 1), (1, '#2f8590', 1)]))
    b = [R(0, 0, W, 250, 'url(#e2t4g4)')]
    b.append(cloud(200, 50, 0.9) + cloud(520, 30, 0.7))
    b.append(P('M300 230 Q420 205 540 222 Q640 206 738 220 L738 250 L300 250 Z', '#a9bc98', stroke='none'))
    # port in the distance (right)
    b.append(R(330, 214, 408, 40, 'url(#e2t4g5)'))
    for (x, y, w) in [(380, 226, 60), (520, 232, 70), (650, 226, 60)]:
        b.append(P('M%s %s Q%s %s %s %s' % (f(x), f(y), f(x + w / 2.0), f(y - 4), f(x + w), f(y)), stroke='#d8f1ee', stroke_width=2, opacity=0.7))
    b.append(house(640, 218, 90, 60, '#e0c9a0', '#b85a36', door=True, win=False))
    b.append(barge(420, 214, 110, True, 0.7, 21))
    b.append(barge(560, 224, 100, True, 0.7, 22))
    b.append(amphora(620, 226, 0.8) + amphora(634, 226, 0.8) + amphora(627, 206, 0.8) + sack(600, 226, 0.8))
    # left town
    b.append(house(-10, 245, 150, 100, '#e8d5b0', TERRA))
    b.append(house(140, 245, 110, 70, '#d9c29a', '#b85a36', door=False))
    b.append(house(240, 245, 100, 84, '#efe0c2', TERRA, door=False))
    b.append(cypress(350, 248, 56, 14))
    b.append(paving(0, 245, W, 107, 20, 42, '#cdbf9f', '#a89874', 71))
    b.append(L(0, 245, W, 245, OUT, 2.5))
    # Becco flying away (faces right)
    for k in range(4):
        b.append(L(440 - k * 8, 130 + k * 14, 500 - k * 8, 118 + k * 14, '#ffffff', 4, stroke_linecap='round', opacity=0.8))
    b.append(becco(570, 120, 1.4, rot=-8, flip=True, wings='up', bundle=True))
    # kids pointing
    g = 340
    s = 1.15
    b.append(nico(90, g - 62 * s, s, la=(-24, 16), ra=(40, -36), expr='wow', look=3))
    b.append(sofia(190, g - 72 * s, s, la=(-24, 14), ra=(38, -36), expr='wow', look=3))
    b.append(toni(285, g - 72 * s, s, la=(-30, -4), ra=(36, -30), expr='wow', look=3))
    b.append(tito(385, g - 63 * s * 1.05, s, la=(-24, 16), ra=(38, -34), expr='worry', look=3))
    ov = balloon('Va verso il porto sul fiume!', 20, 8, 262, 72, 'bl', 18, 14)
    return panel(W, H, ''.join(b), 'Becco vola via con i rotoli verso il porto sul fiume mentre Nico, Sofia, Toni e Tito indicano', ov, bg='#bfe3f2', flex=True, defs=defs)


rows = [row2(p1(), p2(), height=320), p3(), p4()]
write(OUTD + 'Ep2_Tavola4.dc.html', page('Ep. 2 Tavola 4 – Le tracce', rows, 4))
print('ok')
