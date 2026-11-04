import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *
import lib as _L

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'

# ---------------------------------------------------------------- page scaffolding (Ep. 3)
def footer(n):
    return '<div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: 700; color: #7a5a3e; margin-top: -4px">\n<span>Leoni di Laguna · Ep. 3 – Fuga in laguna</span>\n<span>%s</span>\n</div>' % n


def page(title, rows, n):
    root = '<div style="width: 794px; height: 1123px; box-sizing: border-box; padding: 28px; background: #fdf8ee; display: flex; flex-direction: column; gap: 14px; font-family: \'Comic Neue\', sans-serif">\n\n%s\n\n%s\n\n</div>' % ('\n\n'.join(rows), footer(n))
    return _L.HEAD % title + root + '\n' + _L.TAIL


def row3f(a, b, c, height=None, flex=False):
    hs = 'flex: 1; min-height: 0' if flex else 'height: %spx' % f(height)
    return '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; %s">\n%s\n%s\n%s\n</div>' % (hs, a, b, c)


def gy(yg, h, s):
    """origin y so that feet (h px below origin at s=1) land on yg"""
    return yg - h * s

SKY_DAY = [(0, '#8fd0ee', 1), (1, '#e8f4ee', 1)]
SKY_GOLD = [(0, '#8fc9e8', 1), (0.55, '#f7e3a6', 1), (1, '#f9c98a', 1)]
SKY_SUNSET = [(0, '#3b4a86', 1), (0.45, '#c9667a', 1), (0.8, '#f2a45a', 1), (1, '#f8cf7a', 1)]
SKY_NIGHT = [(0, '#1c2550', 1), (0.6, '#3b4a86', 1), (1, '#8a6a9a', 1)]
WAT = [(0, '#a8dbe4', 1), (1, '#6fb3c9', 1)]
WAT_SUN = [(0, '#f6c37a', 1), (1, '#5f7fb0', 1)]
WAT_NIGHT = [(0, '#6a6aa0', 1), (1, '#2c3a6e', 1)]

# ---------------------------------------------------------------- new characters
AUB = '#b5562c'


def elena(x, y, s=1, rot=0, la=(-24, 16), ra=(24, 16), expr='dot', look=0, run=0, flip=False, shell=False):
    b = []
    # legs + sandals
    if run:
        b.append(limb(-7, 32, -13 - run, 58, SK, 12, hand=None) + limb(7, 32, 11 + run, 52, SK, 12, hand=None))
        b.append(E(-15 - run, 61, 9, 4, '#9a6338') + E(13 + run, 55, 9, 4, '#9a6338'))
    else:
        b.append(limb(-7, 32, -8, 60, SK, 12, hand=None) + limb(7, 32, 8, 60, SK, 12, hand=None))
        b.append(E(-10, 63, 9, 4, '#9a6338') + E(10, 63, 9, 4, '#9a6338'))
        b.append(P('M-15 58 L-5 58 M5 58 L15 58', stroke='#6e4a2c', stroke_width=1.6))
    # short brown cloak (behind)
    b.append(P('M-21 -16 Q-31 10 -27 30 L27 30 Q31 10 21 -16 Q0 -26 -21 -16 Z', '#8a5a3a'))
    b.append(limb(-14, -12, la[0], la[1], '#9cc49a', 14))
    b.append(limb(14, -12, ra[0], ra[1], '#9cc49a', 14))
    # light green tunic to the knee
    b.append(P('M-17 -16 Q0 -26 17 -16 L23 40 L-23 40 Z', '#9cc49a'))
    b.append(P('M-22.5 34 L22.5 34 L23 40 L-23 40 Z', '#82ad80', stroke_width=1.5))
    b.append(R(-19, 11, 38, 6, '#8a5a2b', rx=2))
    b.append(R(-4, 10, 8, 8, '#d9a84a', rx=1.5, stroke_width=1.5))
    # cloak clasp
    b.append(C(0, -17, 3.5, '#d9a84a', stroke_width=1.5))
    # head: hair back, face, auburn cap, two low braids
    b.append(C(0, -38, 22, AUB))
    b.append(C(0, -36, 19, SK))
    b.append(P('M-21 -37 Q-21 -58 0 -58 Q21 -58 21 -37 Q11 -48 0 -47 Q-11 -48 -21 -37 Z', AUB))
    b.append(P('M0 -58 Q-1 -50 0 -47', stroke='#8f3f1c', stroke_width=1.6))
    for sx in (-1, 1):
        d = 'M%s -34 Q%s -14 %s 8' % (f(sx * 20), f(sx * 31), f(sx * 24))
        b.append(P(d, stroke=OUT, stroke_width=13) + P(d, stroke=AUB, stroke_width=8))
        b.append(P('M%s -22 L%s -20 M%s -12 L%s -10 M%s -2 L%s 0' % (f(sx * 27), f(sx * 21), f(sx * 28), f(sx * 22), f(sx * 27), f(sx * 21)), stroke='#8f3f1c', stroke_width=1.4))
        b.append(C(sx * 24, 9, 4, '#e9c46a', stroke_width=1.5))
        b.append(P('M%s 12 Q%s 20 %s 22' % (f(sx * 24), f(sx * 27), f(sx * 26)), stroke=AUB, stroke_width=3.5))
    b.append(face(0, -35, expr, my=-24, look=look))
    for fx in (-14, -11, -8, 8, 11, 14):
        b.append(C(fx, -29 + (fx % 3), 1, '#c0794a', stroke='none'))
    if shell:
        b.append(P('M0 0 Q-7 -6 -6 -12 Q0 -16 6 -12 Q7 -6 0 0 Z', '#f7e9d4', stroke_width=1.6, transform='translate(%s %s) scale(1.1)' % (f(la[0]), f(la[1]))))
    return INK(*b, transform=xf(x, y, s, rot, flip))


def papa(x, y, s=1, rot=0, la=(-34, 30), ra=(34, 30), expr='dot', look=0, run=0, flip=False, hands_head=False):
    s = s * 1.0
    b = []
    if run:
        b.append(limb(-10, 40, -16 - run, 74, SK, 17, hand=None) + limb(10, 40, 14 + run, 66, SK, 17, hand=None))
        b.append(E(-18 - run, 78, 11, 5, '#7a4a26') + E(16 + run, 70, 11, 5, '#7a4a26'))
    else:
        b.append(limb(-11, 40, -12, 76, SK, 17, hand=None) + limb(11, 40, 12, 76, SK, 17, hand=None))
        b.append(E(-14, 80, 11, 5, '#7a4a26') + E(14, 80, 11, 5, '#7a4a26'))
    # grey-blue cloak behind
    b.append(P('M-27 -22 Q-39 22 -31 56 L31 56 Q39 22 27 -22 Q0 -34 -27 -22 Z', '#7f93a8'))
    b.append(P('M-31 50 L31 50', stroke='#657a90', stroke_width=1.6))

    def arm(sx, h):
        sh = (sx * 24, -14)
        mid = (sh[0] + 0.45 * (h[0] - sh[0]), sh[1] + 0.45 * (h[1] - sh[1]))
        return (limb(sh[0], sh[1], mid[0], mid[1], '#7a5638', 21, hand=None) + C(mid[0], mid[1], 10, '#6a4a30', stroke_width=2) +
                limb(mid[0], mid[1], h[0], h[1], SK, 15, hand=SK, hr=8))
    b.append(arm(-1, la))
    b.append(arm(1, ra))
    # brown tunic, knee length
    b.append(P('M-26 -18 Q0 -30 26 -18 L31 52 L-31 52 Z', '#7a5638'))
    b.append(P('M-30 46 L30 46 L31 52 L-31 52 Z', '#614028', stroke_width=1.5))
    b.append(R(-28, 16, 56, 7, '#4a3020', rx=2))
    b.append(R(-5, 15, 10, 9, '#c9a24a', rx=2, stroke_width=1.5))
    b.append(P('M-9 -22 Q0 -14 9 -22', stroke='#614028', stroke_width=2))
    # head with short dark brown beard
    b.append(C(0, -44, 22, SK))
    b.append(P('M-22 -42 Q-24 -66 0 -67 Q24 -66 22 -42 Q12 -54 0 -53 Q-12 -54 -22 -42 Z', '#3e2a1c'))
    b.append(P('M-21 -42 Q-22 -17 0 -15 Q22 -17 21 -42 Q16 -36 11 -36 Q0 -40 -11 -36 Q-16 -36 -21 -42 Z', '#4a3020'))
    b.append(E(0, -30, 8, 5, '#e8b88c', stroke='none'))
    b.append(face(0, -46, expr, my=-33, look=look, sp=8, cheeks=False))
    b.append(P('M-18 -53 L-6 -50 M18 -53 L6 -50', stroke='#3e2a1c', stroke_width=3.2))
    return INK(*b, transform=xf(x, y, s, rot, flip))


def nonna(x, y, s=1, rot=0, la=(-22, 20), ra=(22, 20), expr='smile', look=0, flip=False, basket=None):
    s = s * 0.95
    b = []
    b.append(E(-9, 62, 9, 4, '#9a6338') + E(9, 62, 9, 4, '#9a6338'))
    b.append(limb(-14, -12, la[0], la[1], '#4c5f86', 14))
    b.append(limb(14, -12, ra[0], ra[1], '#4c5f86', 14))
    if basket:
        b.append(basket(ra[0], ra[1]))
    b.append(P('M-17 -16 Q0 -26 17 -16 L25 58 L-25 58 Z', '#4c5f86'))
    b.append(P('M-24.5 52 L24.5 52 L25 58 L-25 58 Z', '#3b4b6e', stroke_width=1.5))
    # beige shawl
    b.append(P('M-23 -16 Q0 -30 23 -16 L27 12 Q0 24 -27 12 Z', '#d9c8a0'))
    b.append(P('M-26 12 Q0 24 26 12', stroke='#b8a47a', stroke_width=2))
    b.append(P('M-20 4 Q0 14 20 4 M-24 -4 Q0 6 24 -4', stroke='#b8a47a', stroke_width=1.2))
    b.append(P('M-27 12 L-28 19 M-21 14 L-22 21 M-14 16 L-15 23 M-7 17 L-8 24 M0 18 L0 25 M7 17 L8 24 M14 16 L15 23 M21 14 L22 21 M27 12 L28 19', stroke='#b8a47a', stroke_width=1.5))
    # grey hair with bun
    b.append(C(0, -62, 10, '#cfcfd6'))
    b.append(P('M-4 -64 Q0 -60 4 -64 M-5 -60 Q0 -57 5 -60', stroke='#a8a8b4', stroke_width=1.3))
    b.append(C(0, -37, 22, '#cfcfd6'))
    b.append(C(0, -35, 19, SK))
    b.append(P('M-21 -37 Q-21 -57 0 -57 Q21 -57 21 -37 Q12 -49 0 -48 Q-12 -49 -21 -37 Z', '#cfcfd6'))
    b.append(P('M-9 -52 Q-4 -50 0 -52', stroke='#a8a8b4', stroke_width=1.3))
    b.append(face(0, -34, expr, my=-23, look=look))
    # kind wrinkles
    b.append(P('M-17 -37 L-13 -36 M-17 -33 L-13 -33 M17 -37 L13 -36 M17 -33 L13 -33', stroke='#b98a66', stroke_width=1.3))
    b.append(P('M-11 -28 Q-12 -22 -9 -20 M11 -28 Q12 -22 9 -20', stroke='#c79a76', stroke_width=1.2))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- objects
def mallet(x, y, sc=1, rot=0, big=True):
    hd = G(R(-20, -15, 40, 30, '#8a5a35', rx=7), R(-20, -15, 7, 30, '#6a6e76', rx=2), R(13, -15, 7, 30, '#6a6e76', rx=2),
           P('M-8 -10 L-8 10 M0 -12 L0 12 M8 -10 L8 10', stroke='#6a4426', stroke_width=1.2), stroke=OUT, stroke_width=2.4, stroke_linejoin='round')
    hl = G(R(-4, 12, 8, 70, '#b98a55', rx=3), P('M-2 18 L-2 78', stroke='#9a6b3e', stroke_width=1.2), stroke=OUT, stroke_width=2.4)
    return G(hl, hd, transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def pole(x, yt, yb, w=11, col='#8b5e3a'):
    return G(R(x - w / 2.0, yt, w, yb - yt, col, stroke=OUT, stroke_width=2),
             P('M%s %s L%s %s M%s %s L%s %s' % (f(x - w / 2.0 + 2), f(yt + 6), f(x - w / 2.0 + 2), f(yb - 4), f(x + 1), f(yt + 10), f(x + 1), f(yb - 8)), stroke='#6a4426', stroke_width=1.2),
             E(x, yt, w / 2.0, 3, '#a9794a', stroke=OUT, stroke_width=2))


def lyingpole(x, y, ln=120, rot=0, w=12):
    return G(R(-ln / 2.0, -w / 2.0, ln, w, '#8b5e3a', rx=3, stroke=OUT, stroke_width=2), E(ln / 2.0, 0, 3, w / 2.0, '#b98a55', stroke=OUT, stroke_width=1.8),
             P('M%s -2 L%s -2 M%s 3 L%s 3' % (f(-ln / 2.0 + 8), f(ln / 2.0 - 20), f(-ln / 2.0 + 24), f(ln / 2.0 - 8)), stroke='#6a4426', stroke_width=1.2),
             transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


def reeds(x, yb, n=7, h=60, seed=1, spread=26, tufts=True):
    rnd = random.Random(seed)
    cols = ['#8a9a4e', '#6f8a46', '#a3a65a', '#7d9650']
    s = []
    for i in range(n):
        bx = x + (i - n / 2.0) * spread / n * 2 + rnd.uniform(-4, 4)
        hh = h * rnd.uniform(0.65, 1.0)
        dx = rnd.uniform(-14, 14)
        s.append(P('M%s %s Q%s %s %s %s' % (f(bx), f(yb), f(bx + dx * 0.2), f(yb - hh * 0.6), f(bx + dx), f(yb - hh)), stroke=rnd.choice(cols), stroke_width=2.6, stroke_linecap='round'))
        if tufts and rnd.random() < 0.6:
            s.append(E(bx + dx, yb - hh - 4, 2.6, 8, '#8a5a3a', stroke='none', transform='rotate(%s %s %s)' % (f(dx * 1.2), f(bx + dx), f(yb - hh))))
    return G(*s)


def reedbed(x0, x1, yb, h=50, seed=1, step=22):
    s = []
    rnd = random.Random(seed)
    x = x0
    while x < x1:
        s.append(reeds(x, yb, 6, h * rnd.uniform(0.7, 1.1), seed + int(x), 22))
        x += step * rnd.uniform(0.8, 1.2)
    return G(*s)


def barena(cx, cy, rx, ry, seed=1):
    rnd = random.Random(seed)
    s = [E(cx, cy, rx, ry, '#a58f6a', stroke=OUT, stroke_width=2.2),
         P('M%s %s Q%s %s %s %s Q%s %s %s %s Z' % (f(cx - rx * 0.92), f(cy - ry * 0.25), f(cx - rx * 0.4), f(cy - ry * 1.1), f(cx), f(cy - ry * 0.98),
                                                   f(cx + rx * 0.5), f(cy - ry * 1.05), f(cx + rx * 0.92), f(cy - ry * 0.25)) + 'Q%s %s %s %s Z' % (f(cx), f(cy - ry * 0.3), f(cx - rx * 0.92), f(cy - ry * 0.25)), '#8fa05c')]
    for i in range(int(rx / 12)):
        gx = cx + rnd.uniform(-rx * 0.8, rx * 0.8)
        gyy = cy - ry * 0.45 + rnd.uniform(-ry * 0.2, ry * 0.3)
        s.append(P('M%s %s L%s %s M%s %s L%s %s' % (f(gx), f(gyy), f(gx - 2), f(gyy - 7), f(gx + 2), f(gyy), f(gx + 3), f(gyy - 6)), stroke='#6f8a46', stroke_width=1.8))
    return G(*s)


def water(x, y, w, h, gid, seed=1, n=14, op=0.75):
    rnd = random.Random(seed)
    s = [R(x, y, w, h, 'url(#%s)' % gid)]
    for i in range(n):
        rx = x + rnd.uniform(0, w - 40)
        ry = y + rnd.uniform(6, h - 6)
        rw = rnd.uniform(22, 50)
        s.append(P('M%s %s Q%s %s %s %s' % (f(rx), f(ry), f(rx + rw / 2), f(ry - 5), f(rx + rw), f(ry)), stroke='#ffffff', stroke_width=2.2, opacity=op, stroke_linecap='round'))
    return G(*s)


def egret(x, y, sc=1, flying=False, flip=False):
    b = []
    if flying:
        b.append(P('M-4 -4 Q-30 -40 -52 -26 Q-34 -22 -14 4 Z', '#ffffff'))
        b.append(P('M4 -4 Q30 -34 52 -16 Q34 -16 14 4 Z', '#ffffff'))
        b.append(E(0, 4, 16, 8, '#ffffff'))
        b.append(P('M12 0 Q26 -8 28 -20', stroke=OUT, stroke_width=4) + P('M12 0 Q26 -8 28 -20', stroke='#ffffff', stroke_width=2))
        b.append(C(28, -21, 5, '#ffffff'))
        b.append(P('M32 -22 L44 -20 L32 -18 Z', '#f2c230', stroke_width=1.6))
        b.append(C(29, -22, 1.2, '#2a1a10', stroke='none'))
        b.append(P('M-14 8 L-34 14', stroke=OUT, stroke_width=2.6))
    else:
        b.append(P('M-2 14 L-3 44 M4 14 L6 44', stroke=OUT, stroke_width=2.6))
        b.append(E(0, 6, 16, 10, '#ffffff'))
        b.append(P('M-12 4 Q-26 8 -24 16 Q-14 16 -6 12 Z', '#f2f2ee'))
        b.append(P('M10 2 Q22 -6 14 -26', stroke=OUT, stroke_width=5) + P('M10 2 Q22 -6 14 -26', stroke='#ffffff', stroke_width=2.6))
        b.append(C(14, -28, 5.5, '#ffffff'))
        b.append(P('M19 -29 L33 -26 L19 -24 Z', '#f2c230', stroke_width=1.6))
        b.append(C(15, -29, 1.3, '#2a1a10', stroke='none'))
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=xf(x, y, sc, 0, flip))


def gull(x, y, sc=1, col='#ffffff'):
    return P('M%s %s Q%s %s %s %s Q%s %s %s %s' % (f(x - 14 * sc), f(y), f(x - 7 * sc), f(y - 9 * sc), f(x), f(y), f(x + 7 * sc), f(y - 9 * sc), f(x + 14 * sc), f(y)), stroke=col, stroke_width=2.4 * max(sc, 0.7), stroke_linecap='round')


def smoke(x, yb, h=90, w=20, col='#8f8f98', op=0.5):
    s = []
    n = 7
    for i in range(n):
        t = i / float(n - 1)
        s.append(E(x + math.sin(t * 3) * 8 + t * 14, yb - h * t, w * (0.35 + 0.65 * t), h / 8.0 * (0.8 + t * 0.6), col, stroke='none', opacity=op * (1 - 0.45 * t)))
    return G(*s)


def planks(x, y, w, h, col='#b98a55', line='#8a5f36', pw=26):
    s = [R(x, y, w, h, col, stroke=OUT, stroke_width=2.4)]
    xx = x + pw
    while xx < x + w:
        s.append(L(xx, y + 1, xx, y + h - 1, line, 1.5))
        xx += pw
    s.append(L(x + 2, y + h * 0.35, x + w - 2, y + h * 0.35, line, 1.2))
    return G(*s)


def woven(x, y, w, h, col='#c9a85f', line='#a4843e'):
    s = [R(x, y, w, h, col, stroke=OUT, stroke_width=2.2)]
    xx = x + 8
    while xx < x + w:
        s.append(L(xx, y + 1, xx, y + h - 1, line, 1.3))
        xx += 8
    yy = y + 8
    while yy < y + h:
        s.append(L(x + 1, yy, x + w - 1, yy, '#d9bd78', 1.3))
        yy += 8
    return G(*s)


def thatch(x, y, w, rh, col='#d8b866', line='#a8883c', over=10):
    s = [P('M%s %s L%s %s L%s %s Z' % (f(x - over), f(y), f(x + w + over), f(y), f(x + w / 2.0), f(y - rh)), col, stroke=OUT, stroke_width=2.4, stroke_linejoin='round')]
    n = 7
    for i in range(1, n):
        t = i / float(n)
        yy = y - rh * t
        half = (w / 2.0 + over) * (1 - t)
        s.append(L(x + w / 2.0 - half + 3, yy, x + w / 2.0 + half - 3, yy, line, 1.3))
    for i in range(9):
        t = (i + 0.5) / 9.0
        xx = x - over + (w + 2 * over) * t
        s.append(L(xx, y, xx + (w / 2.0 - (xx - x)) * 0.12, y - 7, line, 1.2))
    return G(*s)


def hut(x, yp, w=90, h=56, door=True, glow_win=False, rh=None, wcol='#c9a85f'):
    """hut on a platform: yp is platform top; x left of hut walls."""
    rh = rh or h * 0.8
    s = [woven(x, yp - h, w, h, wcol)]
    if door:
        s.append(R(x + w / 2.0 - 11, yp - h + 12, 22, h - 12, '#4a3326', stroke=OUT, stroke_width=2))
        if glow_win:
            s.append(R(x + w / 2.0 - 11, yp - h + 12, 22, h - 12, '#f6c15a', stroke=OUT, stroke_width=2))
    s.append(thatch(x, yp - h, w, rh))
    return G(*s)


def stilt_hut(x, yp, ybase, w=90, h=56, pw=None, glow_win=False, rh=None, wcol='#c9a85f', ladder=False):
    """hut + platform + poles down to ybase"""
    s = []
    pw = pw or w + 30
    px = x - 15
    for xx in (px + 8, px + pw * 0.33, px + pw * 0.66, px + pw - 8):
        s.append(pole(xx, yp, ybase, 9))
    s.append(planks(px, yp - 2, pw, 12))
    s.append(hut(x, yp - 2, w, h, True, glow_win, rh, wcol))
    if ladder:
        s.append(P('M%s %s L%s %s M%s %s L%s %s' % (f(px + pw + 4), f(yp + 8), f(px + pw + 22), f(ybase - 4), f(px + pw + 14), f(yp + 8), f(px + pw + 32), f(ybase - 4)), stroke='#8b5e3a', stroke_width=3))
    return G(*s)


def boat(x, y, w=150, flip=False, oar=False):
    s = []
    s.append(P('M0 0 Q%s %s %s 0 L%s 22 Q%s 30 %s 22 Z' % (f(w / 2.0), f(8), f(w), f(w - 22), f(w / 2.0), f(22)), '#9a6b3e', stroke=OUT, stroke_width=2.6, stroke_linejoin='round'))
    s.append(P('M12 8 Q%s 14 %s 8' % (f(w / 2.0), f(w - 12)), stroke='#7a5030', stroke_width=1.8))
    s.append(P('M0 0 Q-6 -8 -4 -14 M%s 0 Q%s -8 %s -14' % (f(w), f(w + 6), f(w + 4)), stroke=OUT, stroke_width=3))
    if oar:
        s.append(L(w * 0.55, -20, w * 0.7, 40, '#b98a55', 4))
        s.append(P('M%s 34 L%s 50 L%s 44 Z' % (f(w * 0.7 - 5), f(w * 0.7 + 4), f(w * 0.7 + 8)), '#b98a55', stroke=OUT, stroke_width=1.8))
    return G(*s, transform='translate(%s %s)' % (f(x), f(y))) if not flip else G(*s, transform='translate(%s %s) scale(-1 1)' % (f(x), f(y)))


def basket(x, y, sc=1, fill=None, col='#c79a52', rot=0):
    b = []
    if fill == 'salt':
        b.append(P('M-15 -10 Q-8 -26 0 -24 Q8 -26 15 -10 Z', '#ffffff', stroke_width=1.8))
        b.append(P('M-5 -16 L-3 -14 M4 -19 L6 -17 M0 -12 L2 -10', stroke='#c8d6dc', stroke_width=1.4))
    elif fill == 'fish':
        b.append(P('M-14 -10 Q-4 -26 12 -14', '#9fb4c4', stroke_width=1.8))
    b.append(P('M-18 -10 L-14 16 L14 16 L18 -10 Z', col, stroke_width=2.2))
    b.append(P('M-17 -2 L17 -2 M-15 6 L15 6 M-6 -10 L-5 16 M6 -10 L5 16', stroke='#8f6a30', stroke_width=1.4))
    b.append(E(0, -10, 18, 4, '#d9b068', stroke_width=2.2))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def bundle(x, y, sc=1, col='#c9a85f'):
    return G(P('M-14 0 Q-20 -14 -8 -22 Q0 -26 8 -22 Q20 -14 14 0 Z', col), P('M-12 -8 L12 -8 M0 -23 L0 0', stroke='#8a6a30', stroke_width=1.6), C(0, -24, 3, '#8a6a30', stroke='none'),
             stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def refugee(x, yb, sc=1, col='#b8a070', flip=False, carry='bundle', hair='#5a4030', kid=False):
    b = []
    b.append(limb(-5, -8, -6, 0, SK, 8, hand=None) + limb(5, -8, 6, 0, SK, 8, hand=None))
    b.append(E(-6, 1, 5, 2.5, '#7a4a26') + E(6, 1, 5, 2.5, '#7a4a26'))
    if carry == 'bundle':
        b.append(bundle(-1, -42, 1.3, '#c9a85f'))
    b.append(P('M-9 -34 Q0 -40 9 -34 L11 -10 L-11 -10 Z', col))
    b.append(L(-10.5, -13, 10.5, -13, '#6e4a2c', 2))
    b.append(limb(-9, -33, -12, -22, col, 6, hand=SK, hr=3.5) + limb(9, -33, 12, -22, col, 6, hand=SK, hr=3.5))
    if carry == 'basket':
        b.append(basket(0, -18, 0.5))
    b.append(C(0, -45, 8, SK))
    b.append(P('M-8 -46 Q-8 -54 0 -54 Q8 -54 8 -46 Q3 -50 0 -50 Q-4 -50 -8 -46 Z', hair))
    b.append(C(-2.6, -45, 1.1, '#2a1a10', stroke='none') + C(2.6, -45, 1.1, '#2a1a10', stroke='none'))
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=xf(x, yb, sc, 0, flip))


def cart(x, yb, sc=1):
    b = [R(-34, -34, 68, 20, '#9a6b3e', stroke_width=2.2), P('M-30 -34 L-26 -50 L26 -50 L30 -34 Z', '#c9a85f', stroke_width=2),
         bundle(-12, -48, 1.1, '#b8a070'), bundle(14, -48, 1.0, '#c9a85f'),
         C(-18, -8, 13, '#8a5a35', stroke_width=2.4), C(-18, -8, 4, '#5a3a20', stroke_width=1.8), P('M-18 -21 L-18 5 M-31 -8 L-5 -8', stroke='#5a3a20', stroke_width=1.6),
         C(18, -8, 13, '#8a5a35', stroke_width=2.4), C(18, -8, 4, '#5a3a20', stroke_width=1.8), P('M18 -21 L18 5 M5 -8 L31 -8', stroke='#5a3a20', stroke_width=1.6),
         P('M34 -26 L62 -16', stroke='#8a5a35', stroke_width=4)]
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(yb), f(sc)))


def brazier(x, y, sc=1, glow=True):
    b = []
    b.append(P('M-4 4 L-14 22 M4 4 L14 22', stroke='#8a4a2a', stroke_width=5))
    b.append(P('M-18 -6 Q-18 12 0 12 Q18 12 18 -6 Z', '#c8683f', stroke_width=2.4))
    b.append(E(0, -6, 18, 5, '#8a3f22', stroke_width=2.2))
    b.append(E(0, -7, 13, 3, '#f08a3a', stroke='none'))
    b.append(E(-5, -8, 4, 1.6, '#ffd36a', stroke='none') + E(5, -7, 3.5, 1.4, '#ffd36a', stroke='none'))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def fish(x, y, sc=1, rot=0, col='#c9b08a'):
    return G(P('M-16 0 Q-4 -9 10 0 Q-4 9 -16 0 Z', col, stroke_width=1.8), P('M10 0 L18 -6 L18 6 Z', '#b8996a', stroke_width=1.6),
             P('M-6 -4 L-4 4 M0 -4 L2 4', stroke='#8a6a40', stroke_width=1.2), C(-11, -1, 1.2, '#2a1a10', stroke='none'),
             stroke=OUT, stroke_width=1.8, stroke_linejoin='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def salt_pools(x, y, w, h, seed=3):
    rnd = random.Random(seed)
    s = [R(x, y, w, h, '#c9b98e'), L(x, y, x + w, y, OUT, 2.2)]
    cols = 3
    rows = 2
    pw = (w - 20) / float(cols)
    ph = (h - 18) / float(rows)
    for r_ in range(rows):
        for c_ in range(cols):
            px = x + 10 + c_ * pw + 3
            py = y + 8 + r_ * ph + 3
            s.append(R(px, py, pw - 8, ph - 8, '#b9e3ec', rx=5, stroke=OUT, stroke_width=2))
            s.append(P('M%s %s L%s %s' % (f(px + 6), f(py + 8), f(px + 24), f(py + 8)), stroke='#ffffff', stroke_width=2, opacity=0.8))
            for k in range(3):
                cx = px + rnd.uniform(10, pw - 18)
                cy = py + rnd.uniform(ph * 0.4, ph - 14)
                s.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(cx - 5), f(cy + 3), f(cx - 2), f(cy - 5), f(cx + 3), f(cy - 4), f(cx + 6), f(cy + 3)), '#ffffff', stroke=OUT, stroke_width=1.4))
    return G(*s)


def sparkle(x, y, r=6, col='#ffffff'):
    return star(x, y, r, col)


def shell_el(x, y, sc=1, rot=0):
    return G(P('M0 10 Q-14 0 -12 -10 Q-6 -16 0 -14 Q6 -16 12 -10 Q14 0 0 10 Z', '#f7e9d4'),
             P('M0 10 L0 -13 M0 10 L-7 -11 M0 10 L7 -11 M0 10 L-11 -5 M0 10 L11 -5', stroke='#d9b090', stroke_width=1.3),
             stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def sunburst(cx, cy, r, gid, col='#ffe08a', n=20, op=0.45):
    sl = []
    for k in range(n):
        a = 2 * math.pi * k / n
        sl.append(L(cx + r * math.cos(a), cy + r * math.sin(a), cx + r * 4 * math.cos(a), cy + r * 4 * math.sin(a), col, 4, stroke_linecap='round'))
    return G(*sl, opacity=op)


def bstar(x, y, r=3):
    return star(x, y, r, '#fff6cf')


# ---------------------------------------------------------------- scene builders
def lagoon_scene(W, H, hz, gs, sk, wt, seed=1, far=True, reeds_n=True, ripples=10, sun=None):
    """sky rect to hz, water hz..gs, mud ground gs..H. returns list of svg strings"""
    rnd = random.Random(seed)
    b = [R(0, 0, W, hz + 2, 'url(#%s)' % sk)]
    if sun:
        b.append(C(sun[0], sun[1], sun[2], '#fff0b0', stroke='none', opacity=0.95))
    b.append(cloud(W * 0.2, hz * 0.35, 0.8, 0.85) + cloud(W * 0.72, hz * 0.25, 0.65, 0.85))
    if far:
        for i in range(5):
            cx = W * (0.1 + 0.2 * i) + rnd.uniform(-20, 20)
            b.append(E(cx, hz + 2, rnd.uniform(40, 80), rnd.uniform(4, 8), '#8fa07a', stroke='none', opacity=0.9))
    b.append(water(0, hz, W, gs - hz, wt, seed, ripples))
    b.append(L(0, hz, W, hz, '#6fa0b8', 1.5))
    return b


def ground(W, H, gs, seed=2, col='#b79f78'):
    rnd = random.Random(seed)
    b = [R(0, gs, W, H - gs, col), P('M0 %s Q%s %s %s %s T%s %s' % (f(gs), f(W * 0.25), f(gs - 6), f(W * 0.5), f(gs), f(W), f(gs - 2)), stroke=OUT, stroke_width=2.4)]
    for i in range(int(W / 60)):
        b.append(E(rnd.uniform(0, W), rnd.uniform(gs + 14, H - 6), rnd.uniform(14, 30), rnd.uniform(3, 6), '#9c8560', stroke='none', opacity=0.7))
    for i in range(int(W / 50)):
        gx = rnd.uniform(6, W - 6)
        gyy = rnd.uniform(gs + 8, H - 4)
        b.append(P('M%s %s L%s %s M%s %s L%s %s' % (f(gx), f(gyy), f(gx - 3), f(gyy - 9), f(gx + 2), f(gyy), f(gx + 4), f(gyy - 8)), stroke='#6f8a46', stroke_width=2))
    return b


def lightbulb(x, y, sc=1):
    return G(C(0, 0, 15, '#ffe36a', stroke_width=2.4), R(-7, 13, 14, 9, '#b8bcc4', rx=2, stroke_width=2), L(-5, 18, 5, 18, OUT, 1.4),
             P('M-5 6 Q0 -6 5 6', stroke='#e0a020', stroke_width=1.6),
             P('M0 -22 L0 -32 M-18 -14 L-26 -22 M18 -14 L26 -22 M-22 0 L-32 0 M22 0 L32 0', stroke='#f2a900', stroke_width=3.2),
             stroke=OUT, stroke_width=2.2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def far_huts(xs, yb, sc=1.0, glow=True):
    s = []
    for x in xs:
        s.append(stilt_hut(x, yb - 34 * sc, yb + 6 * sc, 38 * sc, 24 * sc, glow_win=glow, rh=22 * sc))
    return G(*s)
