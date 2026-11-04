from lib3 import *


def stars_(W, H, n, seed, maxy):
    rnd = random.Random(seed)
    return G(*[bstar(rnd.uniform(6, W - 6), rnd.uniform(6, maxy), rnd.choice([2, 2.5, 3, 4])) for _ in range(n)])


def far_huts(xs, yb, sc=1.0, glow=True):
    s = []
    for x in xs:
        s.append(stilt_hut(x, yb - 34 * sc, yb + 6 * sc, 38 * sc, 24 * sc, glow_win=glow, rh=22 * sc))
    return G(*s)


def p1():
    W, H = 738, 270
    defs = gid_defs(('e3t7g1', 'v', SKY_SUNSET), ('e3t7g2', 'v', WAT_SUN), ('e3t7g3', 'r', [(0, '#fff6cf', 0.9), (1, '#fff6cf', 0)]))
    b = [R(0, 0, W, 172, 'url(#e3t7g1)')]
    b.append(C(560, 160, 70, 'url(#e3t7g3)', stroke='none'))
    b.append(C(560, 168, 30, '#ffe39a', stroke='none'))
    b.append(cloud(120, 60, 0.9, 0.55, '#f6b7a0') + cloud(430, 40, 0.7, 0.5, '#f6b7a0') + cloud(660, 80, 0.6, 0.5, '#f6b7a0'))
    b.append(water(0, 168, W, H - 168, 'e3t7g2', 71, 18, 0.5))
    b.append(L(0, 168, W, 168, '#a86a6a', 1.5))
    b.append(P('M520 180 L600 180 M530 192 L590 192 M540 206 L580 206', stroke='#ffe9a8', stroke_width=3, opacity=0.8))
    b.append(far_huts([40, 110], 196, 0.9))
    b.append(far_huts([640, 696], 200, 0.85))
    b.append(barena(300, 244, 170, 18, 5))
    b.append(stilt_hut(240, 150, 240, 130, 84, rh=56, ladder=True, glow_win=False))
    # boat tied to the hut
    b.append(boat(410, 232, 130, oar=False))
    b.append(P('M386 214 Q396 236 414 238', stroke='#8a6a3a', stroke_width=2.4))
    b.append(egret(160, 228, 0.7))
    b.append(gull(470, 60, 0.8, '#fff3e0') + gull(500, 78, 0.7, '#fff3e0'))
    ov = caption('Al tramonto, la casa è pronta.', 'tl')
    return panel(W, H, ''.join(b), 'Al tramonto la casa sui pali è finita, con una barca legata e altre capanne sull\'isola', ov, defs=defs, height=270)


def p2():
    W, H = 738, 300
    defs = gid_defs(('e3t7g4', 'v', SKY_SUNSET), ('e3t7g5', 'v', WAT_SUN), ('e3t7g6', 'r', [(0, '#ffb04a', 0.85), (1, '#ffb04a', 0)]))
    b = [R(0, 0, W, 190, 'url(#e3t7g4)')]
    b.append(stars_(W, H, 6, 3, 60))
    b.append(water(0, 190, W, H - 190, 'e3t7g5', 72, 12, 0.4))
    b.append(L(0, 190, W, 190, '#a86a6a', 1.5))
    b.append(far_huts([560, 660], 200, 0.8))
    # back wall + roof of the hut on the left
    b.append(woven(0, 52, 215, 162, '#bf9c52', '#9a7a36'))
    b.append(thatch(-20, 52, 255, 52))
    b.append(R(70, 96, 64, 118, '#4a3326', stroke=OUT, stroke_width=2))
    b.append(R(70, 96, 64, 118, '#f2b350', stroke='none', opacity=0.5))
    # platform
    yb = 214
    for xx in (30, 150, 270, 400, 520, 640, 710):
        b.append(pole(xx, yb, 296, 11))
    b.append(planks(0, yb, W, 15))
    b.append(E(372, yb - 4, 120, 40, 'url(#e3t7g6)', stroke='none'))
    # people along the edge, legs dangling
    b.append(nonna(80, yb - 52 * 0.95 * 1.0, 1.0, la=(-22, 18), ra=(18, 24), expr='smile', flip=False))
    b.append(papa(170, yb - 44 * 0.92, 0.92, la=(-30, 26), ra=(30, 2), expr='smile', look=2))
    b.append(elena(262, yb - 36 * 1.0, 1.0, la=(-24, 16), ra=(22, 6), expr='smile', look=2))
    b.append(brazier(372, yb + 4, 1.5))
    b.append(fish(330, yb - 12, 1.1, -10) + fish(414, yb - 10, 1.1, 8))
    b.append(sofia(470, yb - 40 * 1.0, 1.0, la=(-24, 14), ra=(20, 4), expr='smile', look=-2))
    b.append(nico(560, yb - 24 * 1.0, 1.0, la=(-24, 8), ra=(22, 2), expr='happy', look=-2))
    b.append(toni(650, yb - 26 * 1.05, 1.05, la=(-26, 6), ra=(34, -22), expr='happy', look=0))
    b.append(fish(690, yb - 26 * 1.05 - 26, 1.0, -30))
    ov = balloon('Finalmente si mangia!', 520, 8, 200, 70, 'br', 18, 12)
    return panel(W, H, ''.join(b), 'Tutti seduti sulla piattaforma attorno a un piccolo braciere di terracotta mangiano pesce alla griglia', ov, defs=defs, height=300)


def p3():
    W, H = 237, 437
    defs = gid_defs(('e3t7g7', 'v', SKY_NIGHT), ('e3t7g8', 'v', WAT_NIGHT))
    b = [R(0, 0, W, 285, 'url(#e3t7g7)')]
    b.append(stars_(W, H, 14, 5, 200))
    b.append(water(0, 285, W, 112, 'e3t7g8', 73, 8, 0.25))
    b.append(L(0, 285, W, 285, '#5a5a90', 1.5))
    b.append(barena(60, 300, 70, 8, 7) + barena(190, 296, 60, 7, 9))
    b.append(far_huts([30, 78, 175], 300, 0.9))
    for (lx, ly) in [(30, 276), (78, 276), (175, 276)]:
        b.append(E(lx, ly, 16, 10, '#ffcf6a', stroke='none', opacity=0.25))
    # platform foreground
    b.append(planks(-4, 395, W + 8, 50))
    b.append(pole(30, 330, 395, 10) + pole(210, 330, 395, 10))
    b.append(L(30, 352, 210, 352, '#8b5e3a', 5))
    b.append(elena(100, 395 - 67 * 1.65, 1.65, la=(-24, 16), ra=(24, 16), expr='smile', look=3))
    ov = balloon('Siamo pochi, ma insieme ce la faremo.', 8, 10, 218, 118, 'br', 17, 14)
    return panel(W, H, ''.join(b), 'Elena guarda le piccole luci delle altre capanne nella sera', ov, bg='#3b4a86', defs=defs, flex=True)


def p4():
    W, H = 237, 437
    defs = gid_defs(('e3t7g9', 'v', SKY_NIGHT), ('e3t7g10', 'v', WAT_NIGHT))
    b = [R(0, 0, W, 330, 'url(#e3t7g9)')]
    b.append(stars_(W, H, 12, 8, 240))
    b.append(water(0, 330, W, 110, 'e3t7g10', 74, 8, 0.25))
    b.append(far_huts([40, 190], 340, 1.0))
    b.append(sofia(120, 296, 2.5, la=(-24, 16), ra=(24, 16), expr='smile', look=3))
    ov = balloon('Non sai quanto hai ragione…', 14, 10, 205, 100, 'bl', 18, 14)
    return panel(W, H, ''.join(b), 'Sofia sorride con aria complice', ov, bg='#3b4a86', defs=defs, flex=True)


def p5():
    W, H = 237, 437
    defs = gid_defs(('e3t7g11', 'v', SKY_NIGHT), ('e3t7g12', 'r', [(0, '#fff6cf', 0.9), (1, '#fff6cf', 0)]))
    b = [R(0, 0, W, H, 'url(#e3t7g11)')]
    b.append(stars_(W, H, 22, 11, 330))
    b.append(C(205, 190, 14, '#fff3c4', stroke='none') + C(211, 186, 12, '#3b4a86', stroke='none'))
    b.append(woven(36, 400, 170, 60))
    b.append(R(104, 408, 34, 40, '#f2b350', stroke=OUT, stroke_width=2))
    b.append(thatch(40, 440, 160, 112, over=12))
    b.append(leo(122, 262, 1.5, wing='small', eyes='open', la=(-34, 22), ra=(34, 22)))
    ov = balloon('Da queste capanne nascerà una città meravigliosa.', 14, 8, 210, 128, 'br', 16, 14)
    return panel(W, H, ''.join(b), 'Leo seduto sul tetto della capanna sotto le prime stelle', ov, bg='#1c2550', defs=defs, flex=True)


rows = [p1(), p2(), row3f(p3(), p4(), p5(), flex=True)]
write(OUTD + 'Ep3_Tavola7.dc.html', page('Ep. 3 Tavola 7 – Sera in laguna', rows, 7))
print('ok')
