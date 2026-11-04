from lib3 import *


def postcard(x, y, sc=1.0, rot=0):
    b = []
    b.append(R(0, 0, 200, 140, '#fffdf7', rx=3, stroke_width=2.4))
    b.append(R(8, 8, 184, 124, '#cfe8f0', stroke_width=1.6))
    b.append(E(100, 40, 22, 8, '#ffffff', stroke='none', opacity=0.9) + E(150, 28, 18, 6, '#ffffff', stroke='none', opacity=0.9))
    # far dome and tower
    b.append(P('M88 82 Q88 56 104 56 Q120 56 120 82 Z', '#f1e6cf', stroke_width=1.8) + R(100, 44, 8, 14, '#f1e6cf', stroke_width=1.5) + P('M99 44 L104 34 L109 44 Z', '#c8683f', stroke_width=1.5))
    b.append(R(84, 82, 40, 20, '#e6d6b0', stroke_width=1.8))
    # left palaces
    b.append(R(8, 54, 58, 50, '#e8b5a0', stroke_width=2))
    b.append(R(8, 48, 58, 8, '#f4d9c4', stroke_width=1.6))
    for wx in (16, 30, 44, 56):
        b.append(P('M%s 92 L%s 70 Q%s 64 %s 70 L%s 92 Z' % (f(wx - 3), f(wx - 3), f(wx), f(wx + 3), f(wx + 3)), '#6a5a50', stroke_width=1.2))
    b.append(R(66, 66, 34, 38, '#efd9a8', stroke_width=2))
    b.append(P('M66 66 L100 66 L96 58 L70 58 Z', '#c8683f', stroke_width=1.6))
    for wx in (74, 90):
        b.append(P('M%s 94 L%s 78 Q%s 73 %s 78 L%s 94 Z' % (f(wx - 3), f(wx - 3), f(wx), f(wx + 3), f(wx + 3)), '#6a5a50', stroke_width=1.2))
    # right palaces
    b.append(R(136, 48, 56, 56, '#efd9a8', stroke_width=2))
    b.append(P('M134 48 L194 48 L190 40 L138 40 Z', '#c8683f', stroke_width=1.6))
    for wx in (146, 160, 174, 186):
        b.append(P('M%s 92 L%s 68 Q%s 62 %s 68 L%s 92 Z' % (f(wx - 3), f(wx - 3), f(wx), f(wx + 3), f(wx + 3)), '#6a5a50', stroke_width=1.2))
    b.append(R(104, 72, 32, 32, '#e8b5a0', stroke_width=2))
    for wx in (112, 128):
        b.append(P('M%s 94 L%s 80 Q%s 75 %s 80 L%s 94 Z' % (f(wx - 3), f(wx - 3), f(wx), f(wx + 3), f(wx + 3)), '#6a5a50', stroke_width=1.2))
    # water
    b.append(R(8, 104, 184, 28, '#6fb0a8', stroke_width=1.6))
    b.append(P('M16 112 Q24 108 32 112 M120 118 Q128 114 136 118 M150 124 Q158 120 166 124 M40 124 Q48 120 56 124', stroke='#d9f0ee', stroke_width=1.6))
    # gondola
    b.append(P('M64 118 Q62 110 56 108 Q76 120 104 122 Q128 120 140 108 Q134 112 132 118 Z', '#2a2a30', stroke_width=1.6))
    b.append(P('M56 108 L54 100 L58 102 L60 106', '#c9ccd2', stroke_width=1.2))
    b.append(R(98, 94, 6, 22, '#fbfaf4', rx=2, stroke_width=1.4) + C(101, 90, 4, '#fde3c8', stroke_width=1.4))
    b.append(L(104, 98, 124, 120, '#8b5e3a', 2))
    b.append(C(100, 4, 5, '#e2573a', stroke_width=1.8))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def bedroom(W, H, fy, gid, win=None, bed=None, desk=None, wall='#f3dcc0'):
    b = [R(0, 0, W, fy, wall), R(0, fy - 12, W, 12, '#e6c9a0', stroke='none'), L(0, fy - 12, W, fy - 12, '#c9a47a', 2),
         R(0, fy, W, H - fy, '#c9a078'), L(0, fy, W, fy, OUT, 2.5)]
    for k in range(1, int((H - fy) / 14) + 1):
        b.append(L(0, fy + k * 14, W, fy + k * 14, '#b58a62', 1.2))
    if win:
        wx, wy, ww, wh = win
        b.append(R(wx, wy, ww, wh, 'url(#%s)' % gid, stroke=OUT, stroke_width=3))
        b.append(bstar(wx + ww * 0.25, wy + wh * 0.2, 2.5) + bstar(wx + ww * 0.7, wy + wh * 0.3, 2))
        b.append(L(wx + ww / 2.0, wy, wx + ww / 2.0, wy + wh, '#8b5e3a', 4) + L(wx, wy + wh / 2.0, wx + ww, wy + wh / 2.0, '#8b5e3a', 4))
        b.append(R(wx - 6, wy + wh, ww + 12, 7, '#d9b890', stroke=OUT, stroke_width=2))
        b.append(P('M%s %s Q%s %s %s %s L%s %s L%s %s Z' % (f(wx - 8), f(wy - 4), f(wx + 10), f(wy + wh * 0.5), f(wx - 8), f(wy + wh), f(wx + 14), f(wy + wh), f(wx + 14), f(wy - 4)), '#d9776a', stroke=OUT, stroke_width=2))
    if bed:
        bx, by, bw = bed
        b.append(R(bx, by - 40, 10, 66, '#8b5e3a', stroke=OUT, stroke_width=2.4))
        b.append(R(bx, by, bw, 26, '#a67548', stroke=OUT, stroke_width=2.4))
        b.append(R(bx + 8, by - 18, bw - 8, 20, '#fbfaf4', rx=6, stroke=OUT, stroke_width=2.4))
        b.append(R(bx + 12, by - 28, 44, 16, '#fbfaf4', rx=7, stroke=OUT, stroke_width=2.2))
        b.append(R(bx + 58, by - 16, bw - 58, 18, '#4f74a8', rx=6, stroke=OUT, stroke_width=2.2))
        b.append(P('M%s %s L%s %s M%s %s L%s %s' % (f(bx + 80), f(by - 14), f(bx + 80), f(by), f(bx + 110), f(by - 14), f(bx + 110), f(by)), stroke='#3a5a88', stroke_width=1.6))
        b.append(R(bx + bw - 6, by + 22, 8, 12, '#8b5e3a', stroke=OUT, stroke_width=2))
    if desk:
        dx, dy, dw = desk
        b.append(R(dx, dy, dw, 9, '#b98a55', stroke=OUT, stroke_width=2.4))
        b.append(R(dx + 6, dy + 9, 8, fy - dy - 9, '#8b5e3a', stroke=OUT, stroke_width=2) + R(dx + dw - 14, dy + 9, 8, fy - dy - 9, '#8b5e3a', stroke=OUT, stroke_width=2))
        b.append(P('M%s %s L%s %s' % (f(dx + dw - 40), f(dy), f(dx + dw - 28), f(dy - 40)), stroke=OUT, stroke_width=3))
        b.append(P('M%s %s L%s %s L%s %s Z' % (f(dx + dw - 40), f(dy - 38), f(dx + dw - 14), f(dy - 38), f(dx + dw - 27), f(dy - 52)), '#e2573a', stroke=OUT, stroke_width=2))
        b.append(R(dx + 14, dy - 14, 30, 14, '#f2c043', stroke=OUT, stroke_width=2) + R(dx + 18, dy - 26, 26, 12, '#4f74a8', stroke=OUT, stroke_width=2))
    return b


def p1():
    W, H = 362, 300
    defs = gid_defs(('e3t8g1', 'v', SKY_GOLD), ('e3t8g2', 'v', WAT))
    b = lagoon_scene(W, H, 120, 262, 'e3t8g1', 'e3t8g2', 61, ripples=8)
    b.append(far_huts([60, 300], 200, 0.9, glow=False))
    b.append(planks(-4, 275, W + 8, 30))
    b.append(pole(40, 262, 300, 10) + pole(320, 262, 300, 10))
    b.append(elena(108, 285 - 67 * 1.5, 1.5, la=(-24, 16), ra=(46, -4), expr='smile', look=2))
    b.append(sofia(252, 285 - 72 * 1.5, 1.5, la=(-46, -2), ra=(24, 16), expr='happy', look=-2))
    b.append(shell_el(178, 285 - 67 * 1.5 - 4 * 1.5 - 4, 1.0, -10))
    ov = balloon('Una conchiglia della laguna, per ricordarti di noi.', 8, 6, 346, 76, 'bl', 16, 18)
    return panel(W, H, ''.join(b), 'Elena porge a Sofia una piccola conchiglia della laguna', ov, defs=defs, height=300)


def p2():
    W, H = 362, 300
    defs = gid_defs(('e3t8g3', 'r', [(0, '#ffffff', 1), (0.35, '#fff3b8', 1), (1, '#f4c64e', 1)]))
    b = [R(0, 0, W, H, 'url(#e3t8g3)')]
    b.append(sunburst(181, 150, 60, 'x', '#ffffff', 22, 0.75))
    for (x, y, r) in [(40, 50, 10), (320, 60, 9), (60, 240, 8), (300, 230, 10), (180, 28, 7), (120, 40, 5), (250, 40, 6), (28, 140, 6), (336, 150, 6)]:
        b.append(star(x, y, r, '#ffffff'))
    b.append(sofia(90, 300 - 72 * 1.15, 1.15, la=(-26, 6), ra=(40, -52), expr='happy'))
    b.append(nico(181, 300 - 63 * 1.15, 1.15, la=(-40, -50), ra=(40, -50), expr='happy'))
    b.append(toni(272, 300 - 59 * 1.15, 1.15, la=(-40, -50), ra=(30, 6), expr='happy'))
    return panel(W, H, ''.join(b), 'Un lampo dorato: i tre bambini salutano con la mano', '', bg='#fff3b8', defs=defs, height=300)


def p3():
    W, H = 738, 280
    defs = gid_defs(('e3t8g4', 'v', SKY_SUNSET))
    b = bedroom(W, H, 205, 'e3t8g4', win=(300, 24, 130, 118), bed=(14, 175, 190), desk=(540, 160, 190))
    b.append(postcard(455, 40, 0.5, -4))
    ky = 255
    b.append(toni(250, ky - 59 * 1.05, 1.05, la=(-26, 6), ra=(26, 6), expr='smile'))
    b.append(nico(500, ky - 63 * 1.05, 1.05, la=(-26, 6), ra=(26, 6), expr='smile', look=-2))
    sy = ky - 72 * 1.1
    b.append(sofia(375, sy, 1.1, la=(-24, 16), ra=(12, -42), expr='happy'))
    b.append(shell_el(375 + 12 * 1.1, sy - 42 * 1.1 - 12, 1.15, -8))
    return panel(W, H, ''.join(b), 'Di nuovo nella camera di Nico: Sofia tiene in mano la conchiglia', '', bg='#f3dcc0', defs=defs, height=280)


def p4():
    W, H = 362, 427
    defs = gid_defs(('e3t8g5', 'v', SKY_SUNSET))
    b = bedroom(W, H, 380, 'e3t8g5')
    b.append(postcard(66, 16, 1.15, -3))
    b.append(P('M84 4 L84 16', stroke='#e2573a', stroke_width=0))
    ny = 428 - 63 * 1.2
    b.append(nico(120, ny, 1.2, la=(-26, 10), ra=(40, -52), expr='wow', look=0))
    ov = balloon('Pensare che tutto è cominciato con poche capanne…', 8, 184, 346, 80, 'bl', 16, 16)
    return panel(W, H, ''.join(b), 'Nico guarda la cartolina di Venezia, con canale, palazzi e gondola, appesa alla parete', ov, bg='#f3dcc0', defs=defs, flex=True)


def p5():
    W, H = 362, 427
    defs = gid_defs(('e3t8g6', 'v', SKY_SUNSET))
    b = bedroom(W, H, 360, 'e3t8g6', win=(112, 120, 138, 120))
    ty = 400 - 59 * 2.0
    b.append(toni(181, ty, 2.0, la=(-30, 10), ra=(46, -26), expr='happy'))
    hx, hy = 181 + 46 * 2.0, ty - 26 * 2.0
    b.append(E(hx + 2, hy - 18, 6, 12, '#fde3c8', stroke=OUT, stroke_width=2.5, transform='rotate(-10 %s %s)' % (f(hx), f(hy))))
    b.append(star(40, 150, 9, '#f4b942') + star(320, 140, 8, '#f4b942') + star(300, 330, 7, '#f4b942'))
    ov = balloon('E con il mio salto sul palo!', 20, 10, 300, 92, 'bl', 22, 18) + caption('Continua…', 'br')
    return panel(W, H, ''.join(b), 'Toni fiero alza il pollice', ov, bg='#f3dcc0', defs=defs, flex=True)


rows = [row2(p1(), p2(), height=300), p3(), row2(p4(), p5(), flex=True)]
write(OUTD + 'Ep3_Tavola8.dc.html', page('Ep. 3 Tavola 8 – Ritorno', rows, 8))
print('ok')
