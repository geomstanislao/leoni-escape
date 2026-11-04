import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep3a')
from lib3 import *

SKYS = [(0, '#8cc8ec', 1), (0.75, '#dcecee', 1), (1, '#f8eccb', 1)]
WATS = [(0, '#8ccbc8', 1), (1, '#4fa0a8', 1)]
MUD = [(0, '#c9b27c', 1), (1, '#a8946a', 1)]


def ground(W, H, y0, gid):
    b = [R(0, y0, W, H - y0, 'url(#%s)' % gid)]
    b.append(L(0, y0, W, y0, OUT, 2.5))
    r = random.Random(y0)
    for _ in range(int(W / 55)):
        x, y = r.random() * W, y0 + 14 + r.random() * (H - y0 - 20)
        b.append(E(x, y, 16 + r.random() * 14, 4 + r.random() * 3, '#9cc7cf', stroke=OUT, stroke_width=1.4, opacity=0.9))
    for _ in range(int(W / 70)):
        b.append(tuft(r.random() * W, y0 + 18 + r.random() * (H - y0 - 24), 0.9))
    return G(*b)


# ---------------------------------------------------------------- panel 1
def p1():
    W, H = 362, 340
    b = []
    defs = gid_defs(('e3t4g1', 'v', SKYS), ('e3t4g2', 'v', WATS), ('e3t4g3', 'v', MUD))
    b.append(R(0, 0, W, 175, 'url(#e3t4g1)'))
    b.append(cloud(280, 60, 0.8, 0.9) + cloud(60, 110, 0.6, 0.85))
    b.append(R(0, 160, W, 40, 'url(#e3t4g2)'))
    b.append(mound(90, 164, 120, 9, '#c2ae7e', '#8fa860') + reeds(80, 163, 4, 18, 51, 16))
    b.append(ground(W, H, 196, 'e3t4g3'))
    b.append(log_pile(246, 320, 190, 5, -4, 1.0))
    b.append(papa(78, 320 - 76 * 1.4, 1.4, la=(-24, 24), ra=(46, -4), expr='smile', look=3))
    ov = abal('Il terreno è molle. Dobbiamo piantare i pali nel fango.', 14, 8, 336, 'bl', 15, 10)
    return panel(W, H, ''.join(b), 'Papà indica una catasta di lunghi pali di legno sul terreno fangoso', ov, bg='#c9b27c', height=340, defs=defs)


# ---------------------------------------------------------------- panel 2
def p2():
    W, H = 362, 340
    b = []
    defs = gid_defs(('e3t4g4', 'v', SKYS), ('e3t4g5', 'v', WATS), ('e3t4g6', 'v', MUD))
    b.append(R(0, 0, W, 175, 'url(#e3t4g4)'))
    b.append(cloud(300, 50, 0.8, 0.9) + cloud(40, 120, 0.6, 0.85))
    b.append(R(0, 160, W, 40, 'url(#e3t4g5)'))
    b.append(mound(300, 164, 130, 9, '#c2ae7e', '#8fa860') + reeds(310, 163, 4, 18, 52, 16))
    b.append(ground(W, H, 196, 'e3t4g6'))
    b.append(pole(30, 240, 290, 9) + pole(338, 236, 288, 9))
    b.append(sofia(108, 322 - 67 * 1.5, 1.5, la=(-16, -6), ra=(16, -6), expr='wow', look=0))
    b.append(elena(258, 322 - 58 * 1.5, 1.5, la=(-22, 14), ra=(30, 8), expr='smile'))
    b.append(star(40, 150, 5, '#f4b942') + star(330, 170, 5, '#f4b942'))
    ov = abal('Anche Venezia oggi sta in piedi su milioni di pali di legno!', 20, 8, 330, 'bl', 15, 10)
    return panel(W, H, ''.join(b), 'Sofia a bocca aperta per lo stupore, con Elena accanto a lei', ov, bg='#c9b27c', height=340, defs=defs)


# ---------------------------------------------------------------- panel 3
def p3():
    W, H = 738, 330
    b = []
    defs = gid_defs(('e3t4g7', 'v', [(0, '#8cc8ec', 1), (0.7, '#e6eedb', 1), (1, '#fbe9c0', 1)]), ('e3t4g8', 'v', WATS), ('e3t4g9', 'v', MUD))
    b.append(R(0, 0, W, 170, 'url(#e3t4g7)'))
    b.append(cloud(80, 60, 0.9, 0.9) + cloud(600, 90, 0.8, 0.9))
    b.append(R(0, 156, W, 40, 'url(#e3t4g8)'))
    b.append(mound(420, 160, 220, 10, '#c2ae7e', '#8fa860') + reeds(400, 159, 5, 20, 53, 20))
    b.append(ground(W, H, 192, 'e3t4g9'))
    b.append(log_pile(190, 306, 170, 4, -3, 1.0))
    b.append(papa(66, 306 - 76 * 1.4, 1.4, la=(-30, -10), ra=(32, -22), expr='wow', look=3))
    b.append(sofia(468, 306 - 67 * 1.2, 1.2, la=(-20, 12), ra=(20, 12), expr='wow', look=-3))
    b.append(nico(552, 306 - 58 * 1.2, 1.2, la=(-22, 14), ra=(22, 14), expr='wow', look=-3))
    b.append(toni(636, 306 - 54 * 1.15, 1.15, la=(-22, 8), ra=(22, 8), expr='wow', look=-3))
    b.append(elena(708, 306 - 58 * 1.15, 1.15, la=(-22, 14), ra=(22, 14), expr='wow', look=-3))
    # speed streaks
    for k, (x1, y1) in enumerate([(430, 70), (450, 100), (470, 56), (420, 124)]):
        b.append(L(x1, y1, x1 + 70, y1 - 22, '#ffffff', 4, opacity=0.8, stroke_linecap='round'))
    b.append(becco_mallet(330, 150, 1.3, rot=-18, wings='up'))
    ov = abal('Un martello? Lo prendo io!', 420, 12, 300, 'bl', 18, 12)
    return panel(W, H, ''.join(b), 'Becco si tuffa dall\'alto e porta via il grosso martello di legno davanti agli occhi stupiti di tutti', ov, bg='#c9b27c', height=330, defs=defs)


# ---------------------------------------------------------------- panel 4
def p4(H):
    W = 738
    b = []
    defs = gid_defs(('e3t4g10', 'v', [(0, '#f0985a', 1), (0.45, '#f8c37c', 1), (1, '#fde8b8', 1)]), ('e3t4g11', 'v', [(0, '#f4c98a', 1), (0.3, '#8cc4b4', 1), (1, '#3f8f9a', 1)]),
                    ('e3t4g12', 'r', [(0, '#fff6cf', 1), (0.4, '#ffe3a0', 0.6), (1, '#ffe3a0', 0)]), ('e3t4g13', 'v', [(0, '#b39a6a', 1), (1, '#8f7b55', 1)]))
    b.append(R(0, 0, W, 200, 'url(#e3t4g10)'))
    b.append(C(230, 188, 150, 'url(#e3t4g12)', stroke='none'))
    b.append(C(230, 188, 46, '#fff3b0', stroke='none'))
    b.append(cloud(560, 60, 0.9, 0.7, '#ffe6c4') + cloud(90, 70, 0.8, 0.7, '#ffe6c4') + cloud(660, 150, 0.6, 0.7, '#ffe6c4'))
    b.append(R(0, 190, W, 40, 'url(#e3t4g11)'))
    for k, y in enumerate(range(196, 226, 8)):
        b.append(L(230 - 14 - k * 4, y, 230 + 14 + k * 4, y, '#ffe9a3', 3, opacity=0.65, stroke_linecap='round'))
    b.append(mound(480, 194, 200, 10, '#c2ae7e', '#8fa860') + reeds(470, 193, 5, 20, 54, 20))
    b.append(ground(W, H, 226, 'e3t4g13'))
    b.append(log_pile(690, 330, 100, 4, 0, 1.0))
    b.append(elena(120, 340 - 58 * 1.0, 1.0, la=(-20, 14), ra=(20, 14), expr='worry'))
    b.append(nico(190, 340 - 58 * 1.0, 1.0, la=(-22, 14), ra=(22, 14), expr='worry', pack=True))
    b.append(sofia(262, 340 - 67 * 1.0, 1.0, la=(-18, 14), ra=(18, 14), expr='worry'))
    b.append(toni(332, 340 - 54 * 1.0, 1.0, la=(-22, 8), ra=(22, 8), expr='worry'))
    b.append(papa(560, 332 - 76 * 1.6, 1.6, la=(-26, -58), ra=(26, -58), expr='worry'))
    ov = abal('Senza mazza, come pianteremo i pali prima di sera?', 140, 6, 480, 'br', 17, 12)
    return panel(W, H, ''.join(b), 'Papà si prende la testa tra le mani: il sole è basso e senza martello i pali non si possono piantare', ov, bg='#f8c37c', flex=True, defs=defs)


FH = 1012 - 340 - 330
rows = [row2(p1(), p2(), height=340), p3(), p4(FH)]
write(OUTD + 'Ep3_Tavola4.dc.html', page('Ep. 3 Tavola 4 – I pali', rows, 4))
print('ok', FH)
