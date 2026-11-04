import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'

OCHRE, OLIVE, TERRA, WHITE = '#d1a85a', '#9a9a5a', '#c8683f', '#efe6d0'


def sky(W, H, gid):
    return R(0, 0, W, H, 'url(#%s)' % gid)


SKYSTOPS = [(0, '#6fc0ea', 1), (0.7, '#bfe3f2', 1), (1, '#fbefc8', 1)]


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 738, 400
    b = []
    defs = gid_defs(('e2t2g1', 'v', SKYSTOPS), ('e2t2g2', 'v', [(0, '#6fc3c9', 1), (1, '#2f8590', 1)]),
                    ('e2t2g3', 'r', [(0, '#fff6cf', 1), (1, '#fff6cf', 0)]))
    b.append(R(0, 0, W, 300, 'url(#e2t2g1)'))
    b.append(C(630, 70, 80, 'url(#e2t2g3)', stroke='none'))
    b.append(C(630, 70, 30, '#fff3b0', stroke='none'))
    b.append(cloud(120, 60, 1.0) + cloud(420, 40, 0.8) + cloud(560, 120, 0.7))
    b.append(P('M0 235 Q120 205 250 228 Q380 200 520 226 Q640 206 738 226 L738 270 L0 270 Z', '#a9bc98', stroke='none'))
    # far town
    far = [(220, 50, 40, '#e8d5b0'), (270, 56, 52, '#d9c29a'), (326, 62, 44, '#efe0c2'), (392, 50, 38, '#e0c9a0'),
           (446, 64, 54, '#e8d5b0'), (514, 56, 42, '#d9c29a'), (574, 62, 50, '#efe0c2'), (640, 54, 40, '#e0c9a0')]
    for (x, w, h, wall) in far:
        b.append(house(x, 266, w, h, wall, TERRA, door=False, win=False))
    b.append(temple(34, 268, 150, 106))
    b.append(cypress(210, 268, 58, 14) + cypress(702, 268, 64, 16) + cypress(224, 268, 40, 12))
    # water
    b.append(R(0, 296, W, 104, 'url(#e2t2g2)'))
    for (x, y, w) in [(210, 316, 90), (380, 330, 120), (540, 312, 80), (110, 350, 100), (620, 360, 110), (320, 372, 90)]:
        b.append(P('M%s %s Q%s %s %s %s' % (f(x), f(y), f(x + w / 2.0), f(y - 5), f(x + w), f(y)), stroke='#d8f1ee', stroke_width=2.4, opacity=0.6, stroke_linecap='round'))
    # bridge
    b.append(bridge(176, 600, 266, 12, 322, 5))
    # banks with houses
    b.append(P('M0 290 Q70 284 150 300 L170 330 L120 400 L0 400 Z', '#b9a77d', stroke=OUT, stroke_width=2.4))
    b.append(P('M738 292 Q680 286 620 304 L606 334 L650 400 L738 400 Z', '#b9a77d', stroke=OUT, stroke_width=2.4))
    b.append(house(0, 318, 96, 82, '#e8d5b0', TERRA, door=True))
    b.append(house(92, 324, 70, 60, '#d9c29a', '#b85a36'))
    b.append(house(622, 322, 116, 90, '#efe0c2', TERRA))
    b.append(house(570, 332, 56, 50, '#e0c9a0', '#b85a36', door=False, win=False))
    # barges
    b.append(barge(200, 338, 150, True, 1.0, 11))
    b.append(barge(390, 356, 170, True, 1.0, 12))
    b.append(roman(470, 346, 1.0, OLIVE, arms='up'))
    b.append(L(478, 262, 492, 362, '#8b5a35', 4))
    b.append(barge(320, 316, 100, False, 0.8, 13))
    # quay
    b.append(paving(0, 372, W, 28, 14, 30, '#cdbf9f', '#a89874', 4))
    b.append(L(0, 372, W, 372, OUT, 2.5))
    b.append(amphora(40, 398, 1.1) + amphora(66, 398, 1.1, '#b8683a') + sack(98, 398, 1.1))
    b.append(sack(660, 398, 1.1) + amphora(692, 398, 1.1) + amphora(716, 398, 1.1, '#d08a52'))
    for (x, y) in [(300, 30), (500, 18), (680, 140)]:
        pass
    ov = caption('Patavium, oggi Padova. Circa 2.000 anni fa.')
    return panel(W, H, ''.join(b), 'Patavium romana lungo il fiume: ponte di pietra ad archi, barconi carichi di anfore, tetti di tegole e un tempio sullo sfondo', ov, bg='#bfe3f2', height=400, defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 738, 290
    b = []
    defs = gid_defs(('e2t2g4', 'v', [(0, '#7ec6ea', 1), (1, '#d8eef3', 1)]))
    b.append(R(0, 0, W, 170, 'url(#e2t2g4)'))
    b.append(cloud(380, 36, 0.7, 0.9) + cloud(640, 60, 0.6, 0.9))
    b.append(temple(300, 172, 150, 90))
    b.append(cypress(480, 172, 70, 16))
    b.append(house(0, 176, 110, 100, '#e8d5b0', TERRA))
    b.append(house(112, 176, 130, 78, '#d9c29a', '#b85a36'))
    b.append(house(246, 176, 56, 56, '#efe0c2', TERRA, door=False, win=False))
    b.append(house(520, 176, 110, 90, '#efe0c2', TERRA))
    b.append(house(632, 176, 106, 112, '#e0c9a0', '#b85a36'))
    b.append(paving(0, 170, W, 120, 20, 40, '#cdbf9f', '#a89874', 7))
    b.append(L(0, 170, W, 170, OUT, 2.5))
    b.append(pot(118, 200, 1.0) + pot(512, 202, 1.0) + pot(628, 204, 1.1))
    # background Romans
    b.append(roman(52, 232, 1.15, OCHRE))
    b.append(roman(200, 226, 1.0, OLIVE, flip=True))
    b.append(roman(470, 232, 1.1, WHITE, arms='carry'))
    b.append(roman(588, 228, 1.1, TERRA, flip=True))
    b.append(roman(690, 240, 1.25, OCHRE, arms='up'))
    b.append(roman(430, 222, 0.9, OLIVE))
    # kids + Leo
    g = 288
    s = 1.15
    b.append(nico(150, g - 62 * s, s, la=(-34, -6), ra=(34, -6), expr='wow', look=-2))
    b.append(sofia(250, g - 72 * s, s, la=(-14, -24), ra=(14, -24), expr='wow', look=1))
    b.append(toni(345, g - 72 * s, s, la=(-34, -14), ra=(34, -14), expr='wow', look=2))
    b.append(leo(520, g - 49 * 1.1, 1.1, wing='small', eyes='open', la=(-34, 16), ra=(36, -12)))
    ov = balloon('Questa sarebbe Padova?!', 96, 8, 214, 62, 'bl', 16, 12) + balloon('Si chiamava Patavium. I Veneti ora sono amici dei Romani.', 400, 8, 322, 92, 'bl', 16, 14)
    return panel(W, H, ''.join(b), 'Nico, Sofia, Toni e Leo a bocca aperta in una strada lastricata di Patavium piena di Romani in tunica', ov, bg='#7ec6ea', height=290, defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 362, 322
    b = []
    defs = gid_defs(('e2t2g5', 'v', [(0, '#7ec6ea', 1), (1, '#d8eef3', 1)]))
    b.append(R(0, 0, W, 130, 'url(#e2t2g5)'))
    b.append(R(0, 80, W, 140, '#e8d5b0'))
    b.append(L(0, 80, W, 80, OUT, 2.5))
    b.append(roof(-10, 80, 382, 40, TERRA))
    b.append(R(20, 100, 24, 40, '#3a2a22', stroke=OUT, stroke_width=2) + R(318, 100, 24, 40, '#3a2a22', stroke=OUT, stroke_width=2))
    b.append(paving(0, 215, W, 107, 18, 36, '#cdbf9f', '#a89874', 9))
    b.append(L(0, 215, W, 215, OUT, 2.5))
    b.append(stall(96, 238, 210, 100))
    b.append(pot(40, 232, 1.0) + pot(330, 234, 1.0))
    b.append(sofia(70, 312 - 72 * 1.1, 1.1, la=(-24, 6), ra=(40, -26), expr='happy'))
    b.append(leo(306, 312 - 49, 1.05, wing='small', eyes='proud', la=(-34, 20), ra=(40, -8)))
    ov = balloon('Guardate quanta lana!', 8, 6, 150, 62, 'bl', 16, 10) + balloon('La lana di Patavium era famosa fino a Roma.', 150, 70, 206, 80, 'br', 15, 14)
    return panel(W, H, ''.join(b), 'Una bancarella con tessuti di lana ripiegati in tanti colori; Sofia e Leo ammirano la merce', ov, bg='#e8d5b0', flex=True, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4():
    W, H = 362, 322
    b = []
    defs = gid_defs(('e2t2g6', 'v', [(0, '#7ec6ea', 1), (1, '#d8eef3', 1)]))
    b.append(R(0, 0, W, 140, 'url(#e2t2g6)'))
    b.append(house(-10, 190, 130, 130, '#e0c9a0', '#b85a36'))
    b.append(house(240, 190, 130, 112, '#efe0c2', TERRA))
    b.append(house(120, 190, 120, 70, '#d9c29a', TERRA, door=False))
    b.append(paving(0, 188, W, 134, 20, 40, '#cdbf9f', '#a89874', 12))
    b.append(L(0, 188, W, 188, OUT, 2.5))
    b.append(tito(100, 312 - 63 * 1.5 * 1.05, 1.5, rot=8, run=14, la=(-34, -30), ra=(34, -26), expr='worry'))
    b.append(nico(262, 312 - 62 * 1.5, 1.5, rot=-12, la=(-36, -22), ra=(36, 4), expr='wow', look=-2))
    # bump burst
    bx, by = 185, 190
    pts = []
    for k in range(16):
        a = 2 * math.pi * k / 16
        r = 26 if k % 2 == 0 else 13
        pts.append('%s %s' % (f(bx + r * math.cos(a)), f(by + r * math.sin(a))))
    b.append(P('M' + ' L'.join(pts) + ' Z', '#ffe08a', stroke=OUT, stroke_width=2.5))
    b.append(star(150, 120, 6, '#f4b942') + star(228, 128, 7, '#f4b942'))
    ov = balloon('Scusate! Avete visto i miei rotoli?', 22, 6, 230, 82, 'bl', 17, 12)
    return panel(W, H, ''.join(b), 'Tito, un ragazzo con la tunica chiara, corre preoccupato e urta Nico in strada', ov, bg='#e8d5b0', flex=True, defs=defs)


rows = [p1(), p2(), row2(p3(), p4(), flex=True)]
write(OUTD + 'Ep2_Tavola2.dc.html', page('Ep. 2 Tavola 2 – Patavium', rows, 2))
print('ok')
