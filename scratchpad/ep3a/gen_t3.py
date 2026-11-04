import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep3a')
from lib3 import *

SKYS = [(0, '#8cc8ec', 1), (0.8, '#d7ecf0', 1), (1, '#f6efd2', 1)]
WATS = [(0, '#8ccbc8', 1), (1, '#3f8f9a', 1)]
MUTED = ['#8f9a6a', '#d1a85a', '#b89a7a', '#a8806a', '#9a8f7a', '#7f8a9a']


def scatter_ripples(x0, y0, x1, y1, n, seed, col='#ffffff', op=0.5):
    r = random.Random(seed)
    return G(*[ripple(x0 + r.random() * (x1 - x0), y0 + r.random() * (y1 - y0), 40 + r.random() * 70, col, op, 2.2) for _ in range(n)])


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 738, 340
    b = []
    defs = gid_defs(('e3t3g1', 'v', SKYS), ('e3t3g2', 'v', WATS))
    b.append(R(0, 0, W, 160, 'url(#e3t3g1)'))
    b.append(cloud(110, 40, 1.0, 0.9) + cloud(430, 60, 0.8, 0.9) + cloud(640, 34, 0.9, 0.9))
    b.append(R(0, 150, W, 190, 'url(#e3t3g2)'))
    b.append(L(0, 150, W, 150, OUT, 2))
    # far barene
    b.append(mound(90, 154, 200, 12, '#c2ae7e', '#8fa860') + mound(330, 153, 160, 10, '#c2ae7e', '#8fa860') + mound(600, 154, 240, 14, '#c2ae7e', '#8fa860'))
    b.append(reeds(60, 152, 6, 22, 21, 24) + reeds(330, 151, 5, 20, 22, 20) + reeds(560, 152, 6, 22, 23, 24) + reeds(660, 153, 5, 20, 24, 20))
    b.append(mound(180, 200, 130, 22, '#b9a878', '#8fa860') + mound(660, 206, 150, 26, '#b9a878', '#8fa860'))
    b.append(reeds(150, 200, 8, 40, 25, 30) + reeds(210, 202, 6, 34, 26, 18) + reeds(640, 206, 8, 44, 27, 30) + reeds(700, 208, 7, 38, 28, 22))
    b.append(scatter_ripples(0, 215, 738, 330, 14, 3))
    # reed bed foreground-left
    b.append(reeds(40, 330, 9, 95, 29, 34) + reeds(110, 336, 6, 70, 30, 24))
    # boat with the family
    GY = 262
    b.append(E(430, 306, 190, 9, '#2f7f8a', stroke='none', opacity=0.4))
    b.append(papa(318, GY - 40 * 0.95, 0.95, la=(-30, 30), ra=(34, 24), expr='smile'))
    b.append(nico(372, GY - 20 * 0.85, 0.85, la=(-24, 14), ra=(24, 14), expr='smile', pack=False))
    b.append(toni(424, GY - 19 * 0.8, 0.8, la=(-22, 10), ra=(22, 10), expr='worry', look=-2))
    b.append(sofia(474, GY - 17 * 0.85, 0.85, la=(-20, 14), ra=(20, 14), expr='wow'))
    b.append(elena(526, GY - 19 * 0.85, 0.85, la=(-24, 12), ra=(36, -26), expr='happy'))
    b.append(boat(425, GY, 320, 36))
    b.append(oar(342, 246, 284, 296, 34) + oar(300, 250, 258, 294, 30))
    b.append(ripple(250, 306, 90, '#ffffff', 0.6, 2.4) + ripple(540, 306, 100, '#ffffff', 0.5, 2.4) + ripple(330, 312, 190, '#ffffff', 0.4, 2.4))
    # egrets, gulls
    b.append(egret(190, 112, 1.2, True, False, "up") + egret(290, 100, 1.0, True, False, 'down') + egret(610, 104, 1.1, True, True, 'up'))
    b.append(egret(700, 190, 0.9, False, True) + egret(172, 188, 0.8, False, False))
    b.append(gull(380, 90, 0.9) + gull(420, 112, 0.7) + gull(120, 130, 0.8))
    ov = cap('La laguna: acqua bassa, canneti e tante piccole isole.', 520)
    return panel(W, H, ''.join(b), 'Una barca attraversa la calma laguna tra canneti e piccole isole basse, mentre le garzette volano nel cielo', ov, bg='#8ccbc8', height=340, defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 362, 300
    b = []
    defs = gid_defs(('e3t3g3', 'v', SKYS), ('e3t3g4', 'v', WATS))
    b.append(R(0, 0, W, 140, 'url(#e3t3g3)'))
    b.append(cloud(250, 36, 0.7, 0.9) + cloud(60, 60, 0.6, 0.85))
    b.append(R(0, 134, W, 166, 'url(#e3t3g4)'))
    b.append(L(0, 134, W, 134, OUT, 2))
    b.append(mound(300, 138, 120, 10, '#c2ae7e', '#8fa860') + mound(60, 138, 100, 8, '#c2ae7e', '#8fa860'))
    b.append(reeds(290, 138, 6, 24, 31, 22) + reeds(60, 138, 5, 20, 32, 18))
    b.append(egret(332, 168, 0.8, False, True))
    b.append(scatter_ripples(0, 160, 362, 290, 8, 4))
    GY = 250
    b.append(papa(112, GY - 40 * 1.2, 1.2, la=(-30, 30), ra=(34, 26), expr='smile', look=2))
    b.append(nico(250, GY - 24 * 1.2, 1.2, la=(-30, 26), ra=(24, 18), expr='det', pack=False))
    b.append(boat(181, GY, 330, 40))
    b.append(oar(72, 238, 26, 286, 36))
    b.append(oar(286, 250, 334, 290, 36))
    b.append(ripple(8, 292, 70, '#ffffff', 0.6, 2.4) + ripple(300, 296, 56, '#ffffff', 0.6, 2.4) + ripple(100, 296, 160, '#ffffff', 0.4, 2.4))
    ov = abal('Qui l\'acqua è bassa: le grandi navi non possono entrare.', 40, 8, 310, 'bl', 15, 10)
    return panel(W, H, ''.join(b), 'Papà rema e Nico lo aiuta con un secondo remo', ov, bg='#8ccbc8', height=300, defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 362, 300
    b = []
    defs = gid_defs(('e3t3g5', 'v', SKYS), ('e3t3g6', 'v', WATS))
    b.append(R(0, 0, W, 130, 'url(#e3t3g5)'))
    b.append(cloud(300, 40, 0.7, 0.9))
    b.append(R(0, 124, W, 176, 'url(#e3t3g6)'))
    b.append(L(0, 124, W, 124, OUT, 2))
    b.append(mound(310, 128, 110, 9, '#c2ae7e', '#8fa860'))
    b.append(reeds(310, 128, 5, 22, 33, 18))
    b.append(scatter_ripples(0, 150, 362, 290, 7, 5))
    b.append(E(318, 252, 26, 8, 'none', stroke='#ffffff', stroke_width=2.4, opacity=0.8) + E(318, 252, 14, 4, 'none', stroke='#ffffff', stroke_width=2.2, opacity=0.8))
    b.append(toni(126, 228, 1.6, rot=12, la=(-26, 12), ra=(30, 22), expr='worry', look=3))
    b.append(boat(150, 262, 330, 60))
    b.append(ripple(260, 296, 100, '#ffffff', 0.45, 2.4))
    ov = abal('E noi dove dormiamo? Sull\'acqua?', 50, 8, 270, 'bl', 16, 10)
    return panel(W, H, ''.join(b), 'Toni si sporge dalla barca e guarda preoccupato l\'acqua', ov, bg='#8ccbc8', height=300, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4(H):
    W = 738
    b = []
    defs = gid_defs(('e3t3g7', 'v', SKYS), ('e3t3g8', 'v', WATS), ('e3t3g9', 'v', [(0, '#c9b27c', 1), (1, '#a8946a', 1)]))
    b.append(R(0, 0, W, 170, 'url(#e3t3g7)'))
    b.append(cloud(90, 44, 0.9, 0.9) + cloud(620, 50, 0.8, 0.9))
    b.append(R(0, 160, W, H - 160, 'url(#e3t3g8)'))
    b.append(L(0, 160, W, 160, OUT, 2))
    b.append(mound(100, 164, 180, 10, '#c2ae7e', '#8fa860') + reeds(80, 163, 5, 20, 41, 22))
    b.append(scatter_ripples(0, 190, 380, H - 6, 10, 6))
    # the island
    b.append(P('M356 %s Q352 300 396 266 Q440 240 520 238 L738 234 L738 %s Z' % (f(H), f(H)), 'url(#e3t3g9)', stroke=OUT, stroke_width=2.5))
    b.append(P('M398 268 Q440 244 520 242 L738 238', stroke='#8fa860', stroke_width=7, stroke_linecap='round'))
    for (x, y) in [(430, 300), (500, 262), (600, 252), (700, 262), (470, 346), (660, 350)]:
        b.append(tuft(x, y, 0.9))
    # huts, poles, platform
    b.append(hut(650, 298, 0.95))
    b.append(R(500, 286, 90, 8, '#c99a62', stroke=OUT, stroke_width=2))
    for px in (506, 542, 584):
        b.append(pole(px, 288, 316, 7))
    b.append(pole(470, 262, 292, 7) + pole(606, 266, 296, 6))
    b.append(refugee(520, 285, 1.0, MUTED[0], carry='bundle'))
    b.append(refugee(560, 286, 1.0, MUTED[1], carry='none'))
    b.append(refugee(455, 318, 1.1, MUTED[3], carry='sack'))
    b.append(refugee(405, 336, 1.2, MUTED[2], carry='basket'))
    b.append(bundle(520, 320, 1.3) + bundle(556, 322, 1.2, '#a8806a'))
    b.append(boat(600, 346, 110, 20))
    b.append(nonna(706, 338, 1.0, la=(-18, 14), ra=(26, -28), expr='smile'))
    # our boat arriving
    GY = 300
    b.append(E(190, GY + 38, 160, 9, '#2f7f8a', stroke='none', opacity=0.4))
    b.append(papa(70, GY - 40 * 1.1, 1.1, la=(-30, 30), ra=(34, 24), expr='smile'))
    b.append(toni(130, GY - 22 * 1.0, 1.0, la=(-22, 8), ra=(22, 8), expr='wow', look=3))
    b.append(sofia(186, GY - 18 * 1.0, 1.0, la=(-20, 14), ra=(20, 14), expr='wow', look=3))
    b.append(nico(240, GY - 22 * 1.0, 1.0, la=(-22, 14), ra=(24, 14), expr='smile', pack=False))
    b.append(elena(296, GY - 24 * 1.1, 1.1, la=(-24, 12), ra=(46, -16), expr='happy', look=2))
    b.append(boat(185, GY, 320, 38))
    b.append(oar(40, 290, -4, 338, 34))
    b.append(ripple(20, 346, 100, '#ffffff', 0.55, 2.4) + ripple(240, 350, 110, '#ffffff', 0.5, 2.4))
    b.append(egret(560, 90, 1.1, True, True, 'up') + egret(620, 56, 0.9, True, False, 'down') + gull(330, 100, 0.9) + gull(360, 118, 0.7))
    b.append(reeds(30, H + 6, 8, 70, 42, 30))
    ov = abal('Ecco la nostra nuova casa!', 250, 12, 270, 'bl', 18, 12)
    return panel(W, H, ''.join(b), 'La barca arriva a una piccola isola dove altre famiglie stanno già cominciando a costruire; Elena indica la loro nuova casa', ov, bg='#8ccbc8', flex=True, defs=defs)


FH = 1012 - 340 - 300
rows = [p1(), row2(p2(), p3(), height=300), p4(FH)]
write(OUTD + 'Ep3_Tavola3.dc.html', page('Ep. 3 Tavola 3 – La laguna', rows, 3))
print('ok', FH)
