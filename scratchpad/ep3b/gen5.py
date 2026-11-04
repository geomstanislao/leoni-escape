from lib3 import *


def p1():
    W, H = 362, 300
    defs = gid_defs(('e3t5g1', 'v', SKY_GOLD), ('e3t5g2', 'v', WAT))
    b = lagoon_scene(W, H, 120, 170, 'e3t5g1', 'e3t5g2', 5, ripples=6)
    b.append(reedbed(0, W, 172, 46, 11, 26))
    b += ground(W, H, 172, 6)
    # sinking pole + mud ring
    b.append(pole(264, 205, 268, 30))
    b.append(E(264, 268, 40, 9, '#8f7650', stroke=OUT, stroke_width=2.2))
    b.append(E(264, 262, 24, 5, '#6e5a3c', stroke='none'))
    b.append(P('M228 262 L218 256 M300 262 L310 256', stroke='#6e5a3c', stroke_width=2.4))
    # little 'sinking' arrows
    b.append(P('M318 205 L318 232 M310 224 L318 234 L326 224', stroke='#e2573a', stroke_width=3.5))
    b.append(toni(264, 148, 1.55, la=(-30, 26), ra=(30, 26), expr='worry', look=0))
    ov = balloon('Ehi… questo palo si muove!', 8, 8, 210, 86, 'br', 17, 14)
    return panel(W, H, ''.join(b), 'Toni è seduto sulla cima di un palo corto piantato nel fango e il palo affonda un po\'', ov, defs=defs)


def p2():
    W, H = 362, 300
    defs = gid_defs(('e3t5g3', 'v', SKY_GOLD), ('e3t5g4', 'v', WAT))
    b = lagoon_scene(W, H, 120, 170, 'e3t5g3', 'e3t5g4', 7, ripples=6)
    b.append(reedbed(0, W, 172, 46, 21, 26))
    b += ground(W, H, 172, 9)
    b.append(pole(52, 232, 268, 24))
    b.append(E(52, 268, 32, 7, '#8f7650', stroke=OUT, stroke_width=2.2))
    b.append(nico(215, 262 - 63 * 1.75, 1.75, la=(-44, -34), ra=(26, 18), expr='dot', look=-2))
    b.append(lightbulb(292, 50, 1.1))
    ov = balloon('Toni! Salta sul palo!', 176, 8, 0, 0, 'bl') if False else ''
    ov = balloon('Toni! Salta sul palo!', 10, 10, 190, 80, 'br', 18, 12)
    return panel(W, H, ''.join(b), 'Nico ha un\'idea, una lampadina sopra la testa, e indica il palo', ov, defs=defs)


def p3():
    W, H = 738, 400
    defs = gid_defs(('e3t5g5', 'v', SKY_GOLD), ('e3t5g6', 'v', WAT))
    b = lagoon_scene(W, H, 130, 215, 'e3t5g5', 'e3t5g6', 12, ripples=12, sun=(600, 90, 26))
    b.append(reedbed(0, W, 217, 52, 31, 24))
    b.append(egret(110, 200, 0.7, flying=True))
    b.append(egret(690, 190, 0.6, flying=True, flip=True))
    b += ground(W, H, 217, 14)
    # watchers
    b.append(papa(655, 300 - 85 * 0.95, 0.95, la=(-30, -10), ra=(30, 10), expr='smile', look=-2, flip=True))
    b.append(elena(585, 304 - 67 * 0.95, 0.95, la=(-10, -4), ra=(10, -4), expr='wow', look=-2, flip=True))
    b.append(nico(150, 312 - 63 * 1.1, 1.1, la=(-30, 8), ra=(28, -44), expr='happy'))
    b.append(sofia(65, 320 - 72 * 1.1, 1.1, la=(-26, 6), ra=(26, 6), expr='wow'))
    # pole sinking into mud with ghost marks
    b.append(E(400, 352, 66, 13, '#8f7650', stroke=OUT, stroke_width=2.4))
    b.append(E(400, 346, 40, 7, '#6e5a3c', stroke='none'))
    b.append(pole(400, 306, 352, 34))
    b.append(P('M338 342 L324 334 M462 342 L476 334 M350 352 L340 362 M450 352 L460 362', stroke='#6e5a3c', stroke_width=3))
    for yy in (270, 288):
        b.append(P('M440 %s L462 %s' % (yy, yy), stroke='#e2573a', stroke_width=2.4, stroke_dasharray='4 4'))
    b.append(P('M476 262 L476 300 M466 290 L476 302 L486 290', stroke='#e2573a', stroke_width=4))
    # Toni mid-air
    b.append(toni(400, 168, 1.7, la=(-36, -44), ra=(36, -44), expr='happy', run=0))
    # motion marks around Toni
    b.append(P('M318 150 L338 154 M312 190 L336 192 M482 150 L462 154 M488 190 L464 192', stroke='#ffffff', stroke_width=4))
    b.append(star(335, 110, 8, '#ffe08a') + star(470, 105, 7, '#ffe08a'))
    ov = sfx('BOING! BOING!', 14, 18, 70, -6)
    return panel(W, H, ''.join(b), 'Toni salta su e giù sul palo, che a ogni salto affonda nel fango', ov, defs=defs, height=400)


def p4():
    W, H = 738, 307
    defs = gid_defs(('e3t5g7', 'v', SKY_GOLD), ('e3t5g8', 'v', WAT))
    b = lagoon_scene(W, H, 100, 185, 'e3t5g7', 'e3t5g8', 15, ripples=10)
    b.append(reedbed(0, W, 187, 48, 41, 24))
    b += ground(W, H, 187, 17)
    gl = 286
    b.append(sofia(70, gl - 72 * 1.3, 1.3, la=(-30, -40), ra=(30, -40), expr='happy'))
    b.append(nico(180, gl - 63 * 1.3, 1.3, la=(-30, -44), ra=(30, -44), expr='happy'))
    b.append(elena(300, gl - 67 * 1.35, 1.35, la=(-6, -14), ra=(6, -14), expr='happy'))
    b.append(papa(440, gl - 85 * 1.15, 1.15, la=(-34, -44), ra=(34, 18), expr='happy'))
    b.append(toni(560, gl - 59 * 1.3, 1.3, la=(-32, -44), ra=(32, -44), expr='happy'))
    b.append(leo(670, 150, 1.0, wing='small', eyes='closed', mouth='oh', la=(-34, 10), ra=(34, 10)))
    for (x, y, r) in [(260, 120, 6), (355, 100, 5), (500, 96, 6), (610, 60, 5)]:
        b.append(star(x, y, r, '#fff6cf'))
    ov = balloon('Funziona!', 262, 8, 150, 70, 'bl', 22, 10)
    return panel(W, H, ''.join(b), 'Tutti esultano: Elena batte le mani, Leo ride, Papà e i bambini alzano le braccia', ov, defs=defs, flex=True)


rows = [row2(p1(), p2(), height=300), p3(), p4()]
write(OUTD + 'Ep3_Tavola5.dc.html', page('Ep. 3 Tavola 5 – L\'idea di Toni', rows, 5))
print('ok')
