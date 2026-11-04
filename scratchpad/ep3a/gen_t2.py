import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep3a')
from lib3 import *

SKYS = [(0, '#8cc8ec', 1), (0.8, '#d7ecf0', 1), (1, '#f6efd2', 1)]
WATS = [(0, '#8ccbc8', 1), (1, '#4fa0a8', 1)]
MUTED = ['#8f9a6a', '#d1a85a', '#b89a7a', '#a8806a', '#9a8f7a', '#7f8a9a']


def far_horizon_reeds(y, x0, x1, seed):
    r = random.Random(seed)
    s = []
    x = x0
    while x < x1:
        s.append(reeds(x, y, 3, 16 + r.random() * 10, int(x), 8))
        x += 30 + r.random() * 30
    return G(*s)


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 738, 360
    b = []
    defs = gid_defs(('e3t2g1', 'v', SKYS), ('e3t2g2', 'v', WATS))
    b.append(R(0, 0, W, 160, 'url(#e3t2g1)'))
    b.append(cloud(300, 60, 1.0, 0.9) + cloud(600, 40, 0.8, 0.9) + cloud(150, 120, 0.7, 0.8))
    b.append(R(0, 148, W, 212, '#a8c783'))
    # water of the lagoon
    b.append(P('M430 150 L738 150 L738 274 Q640 270 560 256 Q480 216 430 150 Z', 'url(#e3t2g2)', stroke='none'))
    b.append(P('M430 150 Q480 216 560 256 Q640 270 738 274', stroke=OUT, stroke_width=2.5))
    for (x, y, w) in [(480, 168, 70), (590, 180, 90), (650, 216, 70), (540, 200, 60), (690, 160, 40)]:
        b.append(ripple(x, y, w, '#ffffff', 0.55, 2))
    b.append(mound(600, 154, 80, 8, '#c2ae7e', '#8fa860') + mound(700, 156, 60, 7, '#c2ae7e', '#8fa860'))
    b.append(far_horizon_reeds(152, 40, 400, 3))
    # fields
    for k, yy in enumerate([178, 200, 230]):
        b.append(P('M0 %s Q200 %s 420 %s' % (f(yy), f(yy - 6), f(yy - 8)), stroke='#92b56e', stroke_width=2, opacity=0.7))
    # trees
    for (x, yb, h) in [(60, 168, 40), (130, 164, 34), (250, 160, 28), (330, 158, 24), (380, 156, 20)]:
        b.append(G(R(x - 2, yb - 14, 4, 14, '#6e4a2c', stroke_width=1.5), E(x, yb - 14 - h / 2.0, h * 0.32, h / 2.0, '#6f9a52', stroke_width=2), stroke=OUT))
    # smoke far away
    b.append(smoke(180, 152, 54) + smoke(236, 153, 44))
    # road
    road = 'M-20 342 Q200 318 400 286 Q520 268 612 262'
    b.append(P(road, stroke=OUT, stroke_width=60, stroke_linecap='round'))
    b.append(P(road, stroke='#dcc088', stroke_width=54, stroke_linecap='round'))
    b.append(P('M-20 336 Q200 312 400 280 Q520 262 612 256', stroke='#c9a96a', stroke_width=3, opacity=0.8))
    b.append(P('M-20 350 Q200 326 400 294 Q520 276 612 270', stroke='#c9a96a', stroke_width=3, opacity=0.8))
    # jetty & boats
    b.append(R(596, 246, 92, 12, '#c99a62', stroke=OUT, stroke_width=2.2))
    for px in (610, 650, 684):
        b.append(pole(px, 252, 276, 7))
    b.append(boat(700, 252, 100, 18))
    b.append(refugee(690, 244, 0.7, '#8f9a6a', carry='bundle'))
    b.append(boat(560, 214, 96, 18))
    b.append(bundle(545, 214, 0.9) + bundle(575, 214, 0.9, '#a8806a'))
    b.append(boat(650, 196, 80, 15))
    b.append(refugee(650, 190, 0.6, '#b89a7a', carry='none'))
    # people on the road (far to near)
    ppl = [(530, 272, 0.8, 'none', 2), (480, 281, 0.85, 'sack', 1), (432, 290, 0.95, 'bundle', 3), (380, 298, 1.1, 'basket', 5),
           (318, 308, 1.25, 'hood', 4), (112, 346, 1.25, 'none', 1), (50, 352, 1.6, 'bundle', 0)]
    b.append(cart(232, 322, 1.1))
    for (x, y, sc, carry, ci) in ppl:
        b.append(refugee(x, y, sc, MUTED[ci], carry=carry))
    b.append(refugee(150, 334, 1.1, '#9a8f7a', carry='bundle'))
    b.append(refugee(612, 266, 0.8, '#d1a85a', carry='bundle'))
    for x in range(10, 738, 74):
        b.append(tuft(x, 358, 1.0, '#6f9a52'))
    ov = cap('Altino, anno 452. Si dice che sta arrivando Attila, re degli Unni.', 540)
    return panel(W, H, ''.join(b), 'Una strada di campagna al margine della laguna: famiglie con fagotti e carretti camminano verso le barche, mentre in lontananza sale un sottile filo di fumo', ov, bg='#a8c783', height=360, defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 738, 250
    b = []
    defs = gid_defs(('e3t2g3', 'v', SKYS), ('e3t2g4', 'v', WATS))
    b.append(R(0, 0, W, 120, 'url(#e3t2g3)'))
    b.append(cloud(120, 40, 0.8, 0.9) + cloud(560, 28, 0.7, 0.9))
    b.append(R(0, 110, W, 140, '#a8c783'))
    b.append(R(420, 110, 318, 44, 'url(#e3t2g4)', stroke='none'))
    b.append(L(420, 154, 738, 154, OUT, 2))
    for (x, y, w) in [(450, 126, 60), (560, 134, 70), (660, 122, 50)]:
        b.append(ripple(x, y, w, '#ffffff', 0.55, 2))
    b.append(far_horizon_reeds(114, 420, 738, 7))
    b.append(smoke(690, 112, 38))
    road = 'M-20 176 Q300 158 780 150'
    b.append(P(road, stroke=OUT, stroke_width=46, stroke_linecap='round'))
    b.append(P(road, stroke='#dcc088', stroke_width=40, stroke_linecap='round'))
    for (x, y, sc, carry, ci) in [(90, 176, 0.62, 'bundle', 0), (160, 173, 0.6, 'none', 1), (260, 169, 0.58, 'sack', 2), (330, 167, 0.56, 'basket', 3), (500, 160, 0.5, 'bundle', 4), (590, 157, 0.5, 'none', 5)]:
        b.append(refugee(x, y, sc, MUTED[ci], carry=carry))
    b.append(cart(420, 164, 0.55))
    # foreground grass
    b.append(P('M0 190 Q200 182 400 192 Q600 182 738 190 L738 250 L0 250 Z', '#8fbf6a', stroke=OUT, stroke_width=2.5))
    for x in range(20, 738, 60):
        b.append(tuft(x, 246, 1.0, '#5e9b48'))
    b.append(nico(95, 172, 1.2, la=(-22, 16), ra=(22, 16), expr='worry', look=3))
    b.append(sofia(215, 165, 1.15, la=(-18, 16), ra=(18, 16), expr='worry', look=3))
    b.append(toni(372, 182, 1.1, la=(-24, 8), ra=(24, 8), expr='worry', look=3))
    b.append(leo(480, 180, 1.0, wing='small', la=(-34, 22), ra=(48, -6), eyes='open'))
    ov = abal('Dove vanno tutte queste persone?', 20, 8, 250, 'br', 16, 10) + abal('Verso la laguna. Sulle isole saranno al sicuro.', 388, 6, 340, 'bl', 16, 10)
    return panel(W, H, ''.join(b), 'Nico, Sofia, Toni e Leo guardano dal bordo della strada la gente che cammina verso la laguna', ov, bg='#a8c783', height=250, defs=defs)


# ---------------------------------------------------------------- panel 3
def p3(H):
    W = 362
    b = []
    defs = gid_defs(('e3t2g5', 'v', SKYS), ('e3t2g6', 'v', WATS))
    b.append(R(0, 0, W, 180, 'url(#e3t2g5)'))
    b.append(cloud(80, 50, 0.8, 0.9) + cloud(290, 120, 0.6, 0.85))
    b.append(R(0, 176, W, H - 176, 'url(#e3t2g6)'))
    b.append(L(0, 176, W, 176, OUT, 2))
    b.append(mound(250, 180, 90, 9, '#c2ae7e', '#8fa860'))
    b.append(far_horizon_reeds(180, 10, 350, 5))
    b.append(smoke(310, 178, 40))
    for (x, y, w) in [(170, 214, 90), (250, 244, 80), (60, 262, 70), (290, 390, 60), (190, 384, 90), (260, 296, 70), (120, 220, 50)]:
        b.append(ripple(x, y, w, '#ffffff', 0.5, 2))
    # bank
    b.append(P('M0 300 Q90 296 150 318 Q172 346 196 402 L0 402 Z', '#b9a878', stroke=OUT, stroke_width=2.5))
    for (x, y) in [(20, 330), (70, 318), (110, 340), (40, 372)]:
        b.append(tuft(x, y, 0.9))
    # boat with bundles
    b.append(bundle(220, 338, 1.5) + bundle(262, 340, 1.3, '#a8806a') + sack(300, 340, 1.3))
    b.append(elena(228, 305, 1.5, la=(-30, -34), ra=(46, -10), expr='worry', look=3))
    b.append(boat(250, 336, 200, 36))
    b.append(ripple(160, 392, 130, '#ffffff', 0.5, 2.4))
    # papa carries a sack
    b.append(papa(62, 270, 1.35, la=(34, 12), ra=(44, 14), expr='smile', look=2))
    b.append(sack(120, 306, 1.7))
    # falling basket
    b.append(basket(334, 312, 1.1, 38))
    b.append(E(352, 352, 6, 5, '#d9923a', stroke=OUT, stroke_width=1.8) + E(336, 372, 7, 5, '#e8c07a', stroke=OUT, stroke_width=1.8) + C(346, 336, 4.5, '#cf4a3a', stroke=OUT, stroke_width=1.8))
    b.append(P('M320 300 L312 288 M334 298 L334 284 M346 304 L356 294', stroke='#8a5a2b', stroke_width=2.2, stroke_linecap='round'))
    ov = abal('Papà, aspetta! Il cesto!', 180, 18, 170, 'bl', 16, 10)
    return panel(W, H, ''.join(b), 'Elena e Papà caricano una barca: un cesto scivola dal bordo', ov, bg='#8ccbc8', flex=True, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4(H):
    W = 362
    b = []
    defs = gid_defs(('e3t2g7', 'v', SKYS), ('e3t2g8', 'v', WATS))
    b.append(R(0, 0, W, 180, 'url(#e3t2g7)'))
    b.append(cloud(70, 60, 0.9, 0.9) + cloud(300, 40, 0.7, 0.9))
    b.append(R(0, 176, W, 130, 'url(#e3t2g8)'))
    b.append(L(0, 176, W, 176, OUT, 2))
    b.append(far_horizon_reeds(180, 10, 350, 9))
    b.append(mound(150, 180, 100, 9, '#c2ae7e', '#8fa860'))
    for (x, y, w) in [(40, 214, 80), (230, 200, 90), (280, 250, 60), (100, 270, 70)]:
        b.append(ripple(x, y, w, '#ffffff', 0.5, 2))
    b.append(bundle(215, 268, 1.4) + bundle(255, 270, 1.2, '#a8806a'))
    b.append(boat(240, 266, 150, 26))
    b.append(P('M0 296 Q180 286 362 300 L362 %s L0 %s Z' % (f(H), f(H)), '#b9a878', stroke=OUT, stroke_width=2.5))
    for x in range(12, 362, 52):
        b.append(tuft(x, 330 + (x % 3) * 20, 1.0))
    b.append(elena(292, 293, 1.5, la=(-26, 14), ra=(40, -36), expr='happy'))
    b.append(nico(120, 292, 1.6, rot=-6, la=(-24, 14), ra=(24, 14), expr='happy'))
    b.append(basket(122, 328, 1.5, 0))
    b.append(P('M64 300 L52 292 M70 322 L56 324 M176 304 L190 296 M180 330 L196 332', stroke='#e2a93a', stroke_width=2.6, stroke_linecap='round'))
    b.append(star(60, 268, 6, '#f4b942') + star(190, 270, 6, '#f4b942'))
    ov = abal('Preso! Possiamo aiutarvi?', 8, 10, 200, 'bl', 17, 10) + abal('Venite con noi!', 170, 112, 180, 'br', 17, 10)
    return panel(W, H, ''.join(b), 'Nico ha afferrato il cesto al volo; Elena lo invita a salire sulla barca con loro', ov, bg='#8ccbc8', flex=True, defs=defs)


FH = 1012 - 360 - 250
rows = [p1(), p2(), row2(p3(FH), p4(FH), flex=True)]
write(OUTD + 'Ep3_Tavola2.dc.html', page('Ep. 3 Tavola 2 – In fuga', rows, 2))
print('ok', FH)
