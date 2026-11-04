import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'
OCHRE, OLIVE, TERRA, WHITE = '#d1a85a', '#9a9a5a', '#c8683f', '#efe6d0'
SKYSTOPS = [(0, '#7ec6ea', 1), (1, '#d8eef3', 1)]


def street_bg(W, H, gid, horizon, houses):
    b = [R(0, 0, W, horizon, 'url(#%s)' % gid)]
    for h in houses:
        b.append(h)
    b.append(paving(0, horizon, W, H - horizon, 20, 40, '#cdbf9f', '#a89874', 21))
    b.append(L(0, horizon, W, horizon, OUT, 2.5))
    return b


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 362, 330
    defs = gid_defs(('e2t3g1', 'v', SKYSTOPS))
    b = street_bg(W, H, 'e2t3g1', 220, [house(-10, 230, 140, 130, '#e0c9a0', '#b85a36'), house(240, 230, 130, 110, '#efe0c2', TERRA), house(125, 230, 120, 70, '#d9c29a', TERRA, door=False)])
    b.append(pot(24, 252, 1.0))
    s = 1.7
    b.append(tito(181, 322 - 63 * s * 1.05, s, rot=-2, la=(-34, 8), ra=(4, -6), expr='dot', front=True))
    for (x, y, r) in [(60, 130, 5), (310, 140, 5)]:
        b.append(star(x, y, r, '#f4b942'))
    ov = balloon('Mi chiamo Tito Livio. Ho perso i rotoli dove scrivo le mie storie!', 8, 6, 346, 96, 'bl', 15, 14)
    return panel(W, H, ''.join(b), 'Tito Livio, un ragazzo in tunica chiara con i ricci neri, si presenta con la mano sul petto', ov, bg='#e8d5b0', defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 362, 330
    defs = gid_defs(('e2t3g2', 'v', SKYSTOPS))
    b = street_bg(W, H, 'e2t3g2', 230, [house(-10, 240, 150, 140, '#efe0c2', TERRA), house(220, 240, 150, 120, '#e0c9a0', '#b85a36')])
    b.append(roman(330, 262, 0.8, OCHRE))
    b.append(sofia(100, 322 - 72 * 1.35, 1.35, rot=-6, la=(-28, 2), ra=(22, -34), expr='wow', look=2))
    b.append(leo(268, 270, 1.2, wing='small', eyes='open', la=(-34, 22), shh=True))
    ov = balloon('Tito Livio? Quello che scriverà la storia di Roma?!', 30, 6, 215, 92, 'bl', 15, 14) + balloon('Shhh! Lui non lo sa ancora.', 215, 104, 141, 70, 'bl', 14, 12)
    return panel(W, H, ''.join(b), 'Sofia stupita sussurra a Leo, che si mette una zampa sulla bocca per farla tacere', ov, bg='#e8d5b0', defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 738, 290
    defs = gid_defs(('e2t3g3', 'v', SKYSTOPS))
    b = [R(0, 0, W, 200, 'url(#e2t3g3)')]
    b.append(cloud(120, 50, 0.8, 0.9) + cloud(640, 40, 0.7, 0.9))
    b.append(house(10, 215, 160, 130, '#e8d5b0', TERRA))
    b.append(house(184, 215, 120, 90, '#d9c29a', '#b85a36', door=False))
    b.append(cypress(326, 215, 64, 15))
    b.append(paving(0, 215, 340, 75, 18, 36, '#cdbf9f', '#a89874', 31))
    b.append(L(0, 215, 340, 215, OUT, 2.5))
    # steps
    b.append(R(340, 250, 398, 40, '#c9bea4', stroke=OUT, stroke_width=2.5))
    b.append(R(380, 250, 358, 30, '#c9bea4', stroke='none'))
    b.append(R(360, 280, 378, 10, '#b6aa8c', stroke=OUT, stroke_width=2))
    b.append(R(380, 250, 358, 30, '#d9cfb4', stroke=OUT, stroke_width=2.5))
    for x in range(400, 740, 60):
        b.append(L(x, 250, x, 280, '#a89874', 1.6))
    b.append(L(380, 250, 738, 250, '#efe6d0', 3))
    b.append(roman(200, 230, 0.9, OLIVE))
    b.append(roman(110, 232, 0.8, OCHRE, flip=True))
    b.append(tito(520, 250 - 40 * 1.575, 1.5, rot=5, la=(-10, 6), ra=(10, 8), expr='sad', front=True))
    ov = balloon('Domani dovevo leggerli al mio maestro…', 250, 8, 300, 72, 'br', 17, 16)
    return panel(W, H, ''.join(b), 'Tito triste seduto sui gradini di pietra con la testa china', ov, bg='#e8d5b0', height=290, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4():
    W, H = 738, 392
    defs = gid_defs(('e2t3g4', 'v', SKYSTOPS), ('e2t3g5', 'r', [(0, '#fff6cf', 0.9), (1, '#fff6cf', 0)]))
    b = [R(0, 0, W, 240, 'url(#e2t3g4)')]
    b.append(cloud(90, 40, 0.8, 0.9) + cloud(640, 50, 0.7, 0.9))
    b.append(house(-10, 245, 170, 150, '#efe0c2', TERRA))
    b.append(house(570, 245, 180, 140, '#e0c9a0', '#b85a36'))
    b.append(temple(250, 247, 160, 100))
    b.append(paving(0, 245, W, 147, 22, 44, '#cdbf9f', '#a89874', 41))
    b.append(L(0, 245, W, 245, OUT, 2.5))
    sl = []
    for k in range(18):
        a = 2 * math.pi * k / 18
        sl.append(L(330 + 120 * math.cos(a), 190 + 120 * math.sin(a), 330 + 480 * math.cos(a), 190 + 480 * math.sin(a), '#ffe08a', 4, stroke_linecap='round'))
    b.append(G(*sl, opacity=0.45))
    b.append(C(330, 190, 190, 'url(#e2t3g5)', stroke='none'))
    b.append(sofia(190, 254 - 30, 1.5, la=(-26, 6), ra=(26, 6), expr='smile'))
    b.append(toni(478, 262 - 8, 1.5, la=(-32, -10), ra=(30, 0), expr='dot'))
    b.append(tito(650, 296, 1.2, la=(-26, 10), ra=(26, 6), expr='smile'))
    b.append(nico(330, 246, 2.0, la=(-30, 10), ra=(28, -44), expr='det'))
    ov = balloon('Li ritroviamo noi!', 100, 10, 250, 70, 'br', 20, 12)
    return panel(W, H, ''.join(b), 'Nico decisissimo alza il pugno, con Sofia e Toni dietro di lui e Tito che spera', ov, bg='#bfe3f2', flex=True, defs=defs)


rows = [row2(p1(), p2(), height=330), p3(), p4()]
write(OUTD + 'Ep2_Tavola3.dc.html', page('Ep. 2 Tavola 3 – Tito', rows, 3))
print('ok')
