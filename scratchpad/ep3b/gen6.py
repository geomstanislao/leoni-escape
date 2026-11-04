from lib3 import *


def wall_frame(x, ytop, ybot, w, woven_w):
    s = []
    s.append(woven(x, ytop, woven_w, ybot - ytop))
    xx = x + woven_w
    while xx <= x + w:
        s.append(R(xx - 2, ytop, 4, ybot - ytop, '#8b5e3a', stroke=OUT, stroke_width=1.6))
        xx += 14
    s.append(R(x, ytop - 3, w, 5, '#8b5e3a', stroke=OUT, stroke_width=1.8))
    return G(*s)


def p1():
    W, H = 738, 300
    defs = gid_defs(('e3t6g1', 'v', SKY_GOLD), ('e3t6g2', 'v', WAT))
    b = lagoon_scene(W, H, 105, 200, 'e3t6g1', 'e3t6g2', 21, ripples=10)
    b.append(reedbed(0, W, 202, 46, 51, 24))
    b.append(stilt_hut(640, 160, 206, 52, 34, glow_win=False, rh=30))
    b += ground(W, H, 202, 24)
    # platform on poles
    for xx in (180, 260, 340, 420, 500, 560):
        b.append(pole(xx, 196, 262, 10))
    b.append(planks(160, 190, 430, 14))
    b.append(wall_frame(190, 112, 190, 200, 120))
    b.append(wall_frame(430, 124, 190, 120, 40))
    # people on platform
    b.append(elena(212, 190 - 67 * 0.8, 0.8, la=(-6, -22), ra=(18, -30), expr='dot', look=2))
    b.append(nico(330, 190 - 63 * 0.8, 0.8, la=(-26, -4), ra=(28, 6), expr='det', look=2, pack=True))
    b.append(sofia(395, 190 - 72 * 0.8, 0.8, la=(-26, -6), ra=(22, -2), expr='smile', look=-2))
    b.append(papa(520, 190 - 85 * 0.78, 0.78, la=(-30, -84), ra=(30, -84), expr='smile', look=2))
    b.append(P('M478 58 L562 54', stroke=OUT, stroke_width=12) + P('M478 58 L562 54', stroke='#b98a55', stroke_width=8))
    # ground helpers
    b.append(toni(110, 262 - 59 * 0.8, 0.8, la=(-26, -4), ra=(26, 4), expr='dot'))
    b.append(bundle(104, 214, 1.3, '#c9a85f'))
    b.append(refugee(40, 262, 0.9, '#b8a070', flip=False))
    b.append(refugee(610, 266, 0.9, '#9a9a6a', flip=True, carry='basket'))
    # Leo with bundle of reeds
    b.append(leo(650, 70, 0.7, wing='small', eyes='open', la=(-34, 14), ra=(34, 14)))
    b.append(bundle(650, 96, 0.95, '#a3a65a'))
    b.append(egret(300, 74, 0.55, flying=True))
    return panel(W, H, ''.join(b), 'Tutti costruiscono una piattaforma di legno su pali, con pareti di canne intrecciate; Leo vola con un fascio di canne', '', defs=defs, height=300)


def p2():
    W, H = 362, 330
    defs = gid_defs(('e3t6g3', 'v', SKY_GOLD), ('e3t6g4', 'v', WAT))
    b = lagoon_scene(W, H, 112, 205, 'e3t6g3', 'e3t6g4', 31, ripples=6)
    b.append(reedbed(0, W, 207, 44, 61, 26))
    b += ground(W, H, 205, 33)
    b.append(salt_pools(0, 232, 232, 98, 5))
    b.append(nonna(285, 300 - 62 * 0.95 * 1.5, 1.5, la=(-22, 16), ra=(34, 20), expr='smile',
                   basket=lambda x, y: basket(x + 2, y + 8, 0.95, 'salt')))
    ov = balloon("Con l'acqua del mare facciamo il sale. Vale più dell'oro!", 8, 6, 330, 100, 'br', 15, 14)
    return panel(W, H, ''.join(b), 'Nonna accanto alle vasche basse dove si vedono i cristalli bianchi di sale, con un cesto di sale in mano', ov, defs=defs, height=330)


def p3():
    W, H = 362, 330
    defs = gid_defs(('e3t6g5', 'v', SKY_GOLD), ('e3t6g6', 'v', WAT))
    b = lagoon_scene(W, H, 112, 205, 'e3t6g5', 'e3t6g6', 41, ripples=6)
    b.append(reedbed(0, W, 207, 44, 71, 26))
    b += ground(W, H, 205, 43)
    b.append(salt_pools(150, 214, 212, 40, 8) if False else '')
    b.append(basket(72, 300, 1.9, 'salt'))
    b.append(nonna(318, 270 - 62 * 0.95 * 0.6, 0.6, la=(-22, 16), ra=(22, 20), expr='smile', flip=True))
    # sneaking Becco facing left toward the basket
    s = 1.45
    by = 300 - 58 * s
    b.append(becco(235, by, s, rot=-6, wings='down'))
    b.append(mallet(262, by + 26 * s, 0.62, 78))
    b.append(P('M300 250 L322 246 M304 266 L328 264', stroke='#ffffff', stroke_width=3))
    ov = balloon('Sale? Perfetto per il mio panino…', 12, 8, 260, 84, 'br', 17, 16)
    return panel(W, H, ''.join(b), 'Becco si avvicina furtivo al cesto di sale con il martello nascosto sotto l\'ala', ov, defs=defs, height=330)


def p4():
    W, H = 738, 377
    defs = gid_defs(('e3t6g7', 'v', SKY_GOLD), ('e3t6g8', 'v', WAT))
    b = lagoon_scene(W, H, 120, 255, 'e3t6g7', 'e3t6g8', 51, ripples=12)
    b.append(reedbed(0, W, 257, 52, 81, 24))
    b += ground(W, H, 255, 53)
    b.append(sunburst(200, 250, 90, 'x', '#ffe08a', 16, 0.35))
    b.append(nico(340, 366 - 63 * 0.8, 0.8, la=(-26, 6), ra=(26, 6), expr='wow'))
    b.append(sofia(412, 372 - 72 * 0.8, 0.8, la=(-26, 6), ra=(26, 6), expr='smile'))
    b.append(toni(480, 366 - 59 * 0.8, 0.8, la=(-26, 6), ra=(26, 6), expr='wow'))
    b.append(leo(200, 241, 1.9, wing='open', eyes='proud', mouth='oh', la=(-38, 14), ra=(38, 14)))
    b.append(becco(640, 207, 1.3, rot=8, wings='up', legs_on=True))
    b.append(mallet(570, 300, 0.9, -24))
    b.append(P('M552 248 L560 270 M575 244 L580 262 M594 250 L592 268', stroke='#ffffff', stroke_width=3.5))
    b.append(P('M560 130 L548 112 M575 124 L570 102 M590 132 L598 114', stroke='#e2573a', stroke_width=4))
    b.append(P('M575 120 L575 150', stroke='#e2573a', stroke_width=0))
    ov = (balloon('ROAAAR!', 140, 12, 250, 84, 'bl', 30, 10) +
          balloon('Va bene, va bene! Ecco il martello!', 410, 6, 300, 74, 'br', 17, 14))
    return panel(W, H, ''.join(b), 'Leo ruggisce orgoglioso e Becco, spaventato, lascia cadere il martello', ov, defs=defs, flex=True)


rows = [p1(), row2(p2(), p3(), height=330), p4()]
write(OUTD + 'Ep3_Tavola6.dc.html', page('Ep. 3 Tavola 6 – La casa sui pali', rows, 6))
print('ok')
