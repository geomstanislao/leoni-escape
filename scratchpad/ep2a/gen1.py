import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'


def tablet(x, y, w, h, rot=0, glow_on=True):
    b = []
    b.append(R(-w / 2.0 + 4, -h / 2.0 + 5, w, h, '#2a1a10', rx=8, opacity=0.35, stroke='none'))
    b.append(R(-w / 2.0, -h / 2.0, w, h, '#b5793a', rx=8, stroke=OUT, stroke_width=2.5))
    b.append(R(-w / 2.0 + 6, -h / 2.0 + 6, w - 12, h - 12, '#c98d47', rx=5, stroke='#e9b949', stroke_width=2))
    # engraved squiggles
    for i in range(4):
        yy = -h / 2.0 + 18 + i * (h - 36) / 3.0
        b.append(P('M%s %s q8 -6 16 0 t16 0 t16 0 t%s 0' % (f(-w / 2.0 + 14), f(yy), f(max(8, w - 80))), stroke='#7a4a1c', stroke_width=2))
    b.append(C(w / 2.0 - 26, -h / 2.0 + 22, 8, '#f4c64e', stroke='#7a4a1c', stroke_width=1.5))
    return G(*b, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


# ---------------------------------------------------------------- panel 1: bedroom
def p1():
    W, H = 738, 330
    b = []
    defs = gid_defs(('e2t1g1', 'v', [(0, '#3c3a78', 1), (0.55, '#c9657f', 1), (1, '#f7b36a', 1)]),
                    ('e2t1g2', 'r', [(0, '#fff0b0', 0.85), (1, '#ffd36e', 0)]),
                    ('e2t1g3', 'r', [(0, '#ffe9a3', 0.9), (1, '#ffe9a3', 0)]))
    b.append(R(0, 0, W, H, '#d8c3cf'))
    b.append(R(0, 255, W, 75, '#b98a5e'))
    b.append(L(0, 255, W, 255, '#8b6a45', 3))
    for i in range(0, 750, 60):
        b.append(L(i, 255, i - 30, 330, '#a47a50', 1.5))
    # window
    b.append(R(55, 58, 130, 108, 'url(#e2t1g1)', stroke=OUT, stroke_width=3))
    b.append(C(150, 92, 12, '#fff3c4', stroke='none'))
    b.append(star(90, 84, 4, '#fff3c4') + star(115, 112, 3, '#fff3c4') + star(70, 125, 3, '#fff3c4'))
    b.append(P('M55 166 L55 146 L75 140 L90 150 L112 138 L135 150 L158 142 L185 150 L185 166 Z', '#4a3a6a', stroke='none'))
    b.append(L(120, 58, 120, 166, OUT, 3) + L(55, 112, 185, 112, OUT, 3))
    b.append(R(48, 166, 144, 8, '#efe0c2', stroke=OUT, stroke_width=2.5))
    b.append(P('M40 52 L52 52 L52 172 L40 172 Z', '#b86a7a', stroke=OUT, stroke_width=2))
    b.append(P('M188 52 L200 52 L200 172 L188 172 Z', '#b86a7a', stroke=OUT, stroke_width=2))
    # bed
    b.append(R(10, 182, 215, 40, '#e6d8c0', stroke=OUT, stroke_width=2.5, rx=4))
    b.append(R(10, 214, 225, 52, '#6f8fc4', stroke=OUT, stroke_width=2.5, rx=6))
    b.append(R(20, 190, 60, 26, '#fbfaf4', stroke=OUT, stroke_width=2.2, rx=8))
    b.append(P('M90 222 L225 222', stroke='#9fb6dc', stroke_width=3))
    b.append(R(14, 262, 10, 12, '#8b5a35', stroke=OUT, stroke_width=2) + R(212, 262, 10, 12, '#8b5a35', stroke=OUT, stroke_width=2))
    # poster
    b.append(R(250, 78, 62, 70, '#efe0c2', stroke=OUT, stroke_width=2.5))
    b.append(R(256, 84, 50, 58, '#4f74a8', stroke='none'))
    b.append(P('M268 128 Q281 96 294 128 Z', '#f4c64e', stroke=OUT, stroke_width=1.8))
    b.append(P('M262 134 q6 -4 12 0 t12 0 t12 0', stroke='#fbfaf4', stroke_width=2))
    # bookshelf
    b.append(R(588, 36, 140, 224, '#8b5a35', stroke=OUT, stroke_width=3))
    rnd = random.Random(5)
    cols = ['#e2573a', '#4f74a8', '#f2c043', '#7fa05a', '#b86aa0', '#fbfaf4', '#d98a3a', '#5a8a9a']
    for k in range(4):
        ys = 44 + k * 54
        b.append(R(594, ys, 128, 46, '#6e4a2c', stroke='none'))
        xx = 598
        while xx < 712:
            wb = rnd.randint(8, 15)
            hb = rnd.randint(28, 42)
            b.append(R(xx, ys + 46 - hb, wb, hb, rnd.choice(cols), stroke=OUT, stroke_width=1.6))
            xx += wb + 1
        b.append(R(590, ys + 46, 136, 6, '#a06a3c', stroke=OUT, stroke_width=2))
    # lamp glow
    b.append(C(372, 205, 70, 'url(#e2t1g3)', stroke='none'))
    # chair back
    b.append(R(393, 186, 86, 52, '#8b5a35', stroke=OUT, stroke_width=2.5, rx=6))
    # Sofia
    b.append(sofia(436, 222, 1.2, la=(-16, 14), ra=(16, 14), expr='wow', look=0))
    # desk
    b.append(R(335, 236, 205, 12, '#b9783f', stroke=OUT, stroke_width=2.5))
    b.append(R(345, 248, 185, 46, '#a06a3c', stroke=OUT, stroke_width=2.5))
    b.append(R(358, 258, 70, 30, '#8b5a35', stroke=OUT, stroke_width=1.8, rx=2))
    b.append(R(443, 258, 70, 30, '#8b5a35', stroke=OUT, stroke_width=1.8, rx=2))
    b.append(R(348, 294, 12, 22, '#8b5a35', stroke=OUT, stroke_width=2) + R(515, 294, 12, 22, '#8b5a35', stroke=OUT, stroke_width=2))
    # lamp
    b.append(P('M368 236 L372 206 L378 206 L382 236 Z', '#6e4a2c', stroke=OUT, stroke_width=2))
    b.append(P('M356 208 L366 182 L388 182 L398 208 Z', '#f2c043', stroke=OUT, stroke_width=2.4))
    b.append(L(362, 212, 392, 212, '#fff3c4', 3, opacity=0.8))
    # tablet on desk
    b.append(C(436, 232, 30, 'url(#e2t1g2)', stroke='none'))
    b.append(tablet(436, 231, 38, 22, -4))
    b.append(star(398, 214, 5) + star(474, 218, 4) + star(436, 204, 4))
    # rug
    b.append(E(222, 322, 190, 34, '#c9694f', stroke=OUT, stroke_width=2.5))
    b.append(E(222, 322, 168, 26, 'none', stroke='#f2c043', stroke_width=2.5))
    # cards on rug
    for i, (cx, cy, r) in enumerate([(206, 318, -18), (222, 314, 2), (240, 318, 22)]):
        b.append(R(cx - 9, cy - 13, 18, 26, '#fbfaf4', stroke=OUT, stroke_width=1.8, rx=2, transform='rotate(%s %s %s)' % (f(r), f(cx), f(cy))))
    b.append(C(224, 312, 3, '#e2573a', stroke='none'))
    # Nico + Toni
    b.append(nico(130, 322, 1.15, rot=-3, la=(-20, 18), ra=(26, 14), expr='dot'))
    b.append(toni(318, 324, 1.1, rot=3, la=(-24, -4), ra=(-6, -12), expr='smile'))
    ov = caption('Qualche giorno dopo, a Padova.') + balloon('La tavoletta della sacerdotessa… sta brillando!', 468, 18, 258, 98, 'bl', 16, 12)
    return panel(W, H, ''.join(b), 'La camera di Sofia di sera: Sofia alla scrivania guarda una piccola tavoletta di bronzo, Nico e Toni giocano a carte sul pavimento', ov, bg='#d8c3cf', height=330, defs=defs)


# ---------------------------------------------------------------- panel 2: tablet close-up
def p2():
    W, H = 362, 290
    b = []
    defs = gid_defs(('e2t1g4', 'r', [(0, '#fff6cf', 1), (0.45, '#ffd36e', 0.7), (1, '#f4b942', 0)]),
                    ('e2t1g5', 'v', [(0, '#5a3424', 1), (1, '#2e1a10', 1)]))
    b.append(R(0, 0, W, H, 'url(#e2t1g5)'))
    b.append(R(0, 214, W, 76, '#8b5a35'))
    b.append(L(0, 214, W, 214, OUT, 3))
    for i in range(0, 380, 46):
        b.append(L(i, 214, i + 12, 290, '#6e4a2c', 1.5))
    b.append(C(181, 138, 190, 'url(#e2t1g4)', stroke='none'))
    rays = []
    for k in range(20):
        a = 2 * math.pi * k / 20
        rays.append(L(181 + 110 * math.cos(a), 138 + 110 * math.sin(a), 181 + 330 * math.cos(a), 138 + 330 * math.sin(a), '#ffe08a', 4, stroke_linecap='round'))
    b.append(G(*rays, opacity=0.6))
    b.append(tablet(181, 140, 206, 128, -7))
    # lion emblem
    b.append(INK(P('M150 164 Q166 132 181 128 Q196 132 212 164 Z', '#f4c64e'), C(181, 138, 14, '#f9dc85'),
                 P('M150 150 Q138 128 130 122 Q150 124 160 136 Z', '#f4c64e'), P('M212 150 Q224 128 232 122 Q212 124 202 136 Z', '#f4c64e'), transform='rotate(-7 181 140)'))
    for (x, y, r) in [(60, 60, 9), (300, 56, 11), (48, 170, 7), (318, 176, 8), (110, 28, 6), (250, 24, 7), (181, 52, 8)]:
        b.append(star(x, y, r, '#fff6cf'))
    b.append(G(star(90, 100, 5, '#ffe08a'), star(280, 112, 5, '#ffe08a'), star(228, 70, 4, '#ffe08a')))
    return panel(W, H, ''.join(b), 'Primo piano della piccola tavoletta di bronzo che brilla d\'oro tra scintille', '', bg='#2e1a10', defs=defs)


# ---------------------------------------------------------------- panel 3: Leo pops out
def p3():
    W, H = 362, 290
    b = []
    defs = gid_defs(('e2t1g6', 'r', [(0, '#fff6cf', 1), (0.5, '#ffe9a3', 0.7), (1, '#ffd36e', 0)]),
                    ('e2t1g7', 'v', [(0, '#f6c76a', 1), (1, '#fbe7a6', 1)]))
    b.append(R(0, 0, W, H, 'url(#e2t1g7)'))
    b.append(P('M190 282 L240 282 L372 -10 L40 -10 Z', '#fff6cf', opacity=0.55, stroke='none'))
    b.append(C(215, 150, 150, 'url(#e2t1g6)', stroke='none'))
    for k in range(14):
        a = math.pi * (1.05 + 0.9 * k / 13.0)
        b.append(L(215 + 90 * math.cos(a), 150 + 90 * math.sin(a), 215 + 260 * math.cos(a), 150 + 260 * math.sin(a), '#f0a92e', 3, opacity=0.5, stroke_linecap='round'))
    b.append(tablet(215, 292, 62, 36, 0))
    b.append(leo(215, 172, 1.15, wing='small', la=(-46, -8), ra=(46, -8), eyes='proud'))
    b.append(toni(66, 322, 1.15, rot=-4, la=(-26, -14), ra=(26, -14), expr='wow'))
    for (x, y, r) in [(300, 70, 8), (330, 190, 7), (150, 60, 6), (292, 238, 6), (120, 190, 6)]:
        b.append(star(x, y, r, '#fff6cf'))
    ov = balloon('Pax tibi! Pronti per un altro viaggio?', 6, 6, 186, 72, 'br', 15, 10) + balloon('Ci sarà da mangiare, stavolta?', 6, 98, 134, 100, 'bl', 14, 10)
    return panel(W, H, ''.join(b), 'Leo esce dalla luce dorata della tavoletta con le zampe aperte, mentre Toni lo guarda da un angolo', ov, bg='#f6c76a', defs=defs)


# ---------------------------------------------------------------- panel 4: swirl
def p4():
    W, H = 738, 392
    b = []
    cx, cy = 530, 196
    defs = gid_defs(('e2t1g8', 'r', [(0, '#ffffff', 1), (0.35, '#ffe9a3', 0.95), (1, '#f4b942', 0)]),
                    ('e2t1g9', 'v', [(0, '#f8c660', 1), (1, '#fde8a8', 1)]))
    b.append(R(0, 0, W, H, 'url(#e2t1g9)'))
    # speed lines
    sl = []
    for k in range(34):
        a = 2 * math.pi * k / 34 + 0.05
        r0 = 150 + (k % 3) * 40
        sl.append(L(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + 700 * math.cos(a), cy + 700 * math.sin(a), '#f0a92e', 4 if k % 2 else 3, stroke_linecap='round'))
    b.append(G(*sl, opacity=0.6))
    b.append(C(cx, cy, 230, 'url(#e2t1g8)', stroke='none'))
    # spirals
    for (w, col, op) in [(26, '#f4b942', 0.85), (16, '#ffd36e', 0.95), (7, '#fff6cf', 1)]:
        for arm in range(3):
            pts = []
            a0 = arm * 2 * math.pi / 3
            r = 8
            while r < 330:
                a = a0 + r * 0.021
                pts.append('%s %s' % (f(cx + r * math.cos(a)), f(cy + r * math.sin(a) * 0.82)))
                r += 6
            b.append(P('M' + ' L'.join(pts), stroke=col, stroke_width=w * (0.5 + 0.0025 * 0) , stroke_linecap='round', opacity=op))
    b.append(C(cx, cy, 36, '#ffffff', stroke='none', opacity=0.9))
    # characters pulled in
    b.append(nico(150, 262, 1.25, rot=38, la=(-30, -30), ra=(30, -22), expr='wow'))
    b.append(sofia(292, 248, 1.15, rot=48, la=(-30, -26), ra=(28, -30), expr='wow'))
    b.append(toni(408, 228, 1.0, rot=62, la=(-34, -22), ra=(30, -28), expr='wow'))
    b.append(leo(560, 190, 0.85, rot=58, wing='open', la=(-34, -10), ra=(34, -16), eyes='open'))
    for (x, y, r) in [(220, 120, 8), (350, 330, 9), (440, 90, 7), (650, 320, 8), (680, 80, 9), (90, 150, 6), (600, 360, 6), (200, 350, 7)]:
        b.append(star(x, y, r, '#fff6cf'))
    ov = sfx('FWOOSH!', 24, 14, 84, -8)
    return panel(W, H, ''.join(b), 'Un vortice dorato risucchia Nico, Sofia, Toni e Leo con linee di velocità', ov, bg='#f8c660', flex=True, defs=defs)


rows = [p1(), row2(p2(), p3(), height=290), p4()]
write(OUTD + 'Ep2_Tavola1.dc.html', page('Ep. 2 Tavola 1 – La tavoletta brilla', rows, 1))
print('ok')
