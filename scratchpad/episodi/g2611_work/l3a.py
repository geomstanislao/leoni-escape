import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/g2611_work')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'


def wpt(x, y, s, rot, lx, ly, flip=False):
    """world position of local point (lx,ly) under xf(x,y,s,rot,flip)"""
    sx = -s if flip else s
    a = math.radians(rot)
    px, py = lx * sx, ly * s
    return (x + px * math.cos(a) - py * math.sin(a), y + px * math.sin(a) + py * math.cos(a))


def abal(text, left, top, w, tail='bl', fs=16, pad=10, h=None):
    cw = 0.56 * fs
    usable = (w - 2 * pad) * 0.76
    lines = max(1, int(math.ceil(len(text) * cw * 1.2 / usable)))
    if h is None:
        h = int(lines * fs * 1.22 + 30)
    return balloon(text, left, top, w, h, tail, fs, pad)


def cap(text, maxw=None):
    c = caption(text)
    if maxw:
        c = c.replace('position: absolute;', 'position: absolute; max-width: %spx;' % maxw, 1)
    return c


# ---------------------------------------------------------------- ELENA (auburn braids, green tunic, brown cloak)
HAIR_E = '#b5562c'
GREEN = '#9cc49a'
CLOAK_E = '#8a5a3a'


def elena(x, y, s=1, rot=0, la=(-24, 16), ra=(24, 16), expr='dot', look=0, run=0, flip=False):
    b = []
    if run:
        b.append(limb(-7, 30, -13 - run, 54, SK, 12, hand=None) + limb(7, 30, 12 + run, 48, SK, 12, hand=None))
        b.append(E(-15 - run, 58, 9, 4, '#8a5a2b') + E(14 + run, 52, 9, 4, '#8a5a2b'))
    else:
        b.append(limb(-7, 30, -8, 55, SK, 12, hand=None) + limb(7, 30, 8, 55, SK, 12, hand=None))
        b.append(E(-10, 58, 9, 4, '#8a5a2b') + E(10, 58, 9, 4, '#8a5a2b'))
    b.append(P('M-17 -16 Q0 -26 17 -16 L22 34 L-22 34 Z', GREEN))
    b.append(P('M-21.5 29 L21.5 29 L22 34 L-22 34 Z', '#7fae7e', stroke_width=1.5))
    b.append(R(-18.5, 10, 37, 5, '#6b4428', rx=2))
    b.append(R(-3, 9.5, 6, 6, '#e9c46a', stroke_width=1.2))
    b.append(P('M-19 -17 Q0 -30 19 -17 L24 6 Q0 14 -24 6 Z', CLOAK_E))
    b.append(C(0, -14, 3, '#e9c46a', stroke_width=1.5))
    b.append(limb(-14, -12, la[0], la[1], GREEN, 14))
    b.append(limb(14, -12, ra[0], ra[1], GREEN, 14))
    for sg in (-1, 1):
        d = 'M%s -34 Q%s -18 %s -2' % (f(sg * 18), f(sg * 29), f(sg * 22))
        b.append(P(d, stroke=OUT, stroke_width=12) + P(d, stroke=HAIR_E, stroke_width=7))
        b.append(P('M%s -22 L%s -20 M%s -12 L%s -10' % (f(sg * 25), f(sg * 21), f(sg * 26), f(sg * 22)), stroke='#8a3f1c', stroke_width=1.3))
        b.append(C(sg * 22, 0, 3.6, '#e9c46a', stroke_width=1.5))
    b.append(C(0, -36, 20, SK))
    b.append(P('M-21 -37 Q-22 -58 0 -58 Q22 -58 21 -37 Q12 -47 0 -48 Q-12 -47 -21 -37 Z', HAIR_E))
    b.append(P('M0 -58 L0 -48', stroke='#8a3f1c', stroke_width=1.4))
    b.append(face(0, -34, expr, my=-23, look=look))
    for (fx, fy) in [(-15, -29), (-12, -26), (-17, -26), (15, -29), (12, -26), (17, -26)]:
        b.append(C(fx, fy, 0.9, '#b5562c', stroke='none'))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- PAPA (tall, short dark beard, brown tunic, grey-blue cloak)
TUN_P = '#7a5638'
CLOAK_P = '#7f93ab'


def papa(x, y, s=1, rot=0, la=(-30, 20), ra=(30, 20), expr='smile', look=0, flip=False, run=0):
    b = []
    b.append(P('M-24 -24 Q-44 20 -38 58 L38 58 Q44 20 24 -24 Z', CLOAK_P))
    b.append(L(-30, 40, -28, 56, '#62748c', 1.6) + L(30, 40, 28, 56, '#62748c', 1.6))
    if run:
        b.append(limb(-10, 38, -15 - run, 72, SK, 17, hand=None) + limb(10, 38, 14 + run, 66, SK, 17, hand=None))
        b.append(E(-17 - run, 76, 11, 5, '#5a3a22') + E(16 + run, 70, 11, 5, '#5a3a22'))
    else:
        b.append(limb(-10, 38, -11, 72, SK, 17, hand=None) + limb(10, 38, 11, 72, SK, 17, hand=None))
        b.append(E(-13, 76, 11, 5, '#5a3a22') + E(13, 76, 11, 5, '#5a3a22'))
    b.append(P('M-22 -22 Q0 -34 22 -22 L27 46 L-27 46 Z', TUN_P))
    b.append(P('M-26.5 40 L26.5 40 L27 46 L-27 46 Z', '#5e4129', stroke_width=1.5))
    b.append(R(-25, 16, 50, 6, '#3f2a1a', rx=2))
    b.append(P('M-3 22 L-6 34 M3 22 L5 33', stroke='#3f2a1a', stroke_width=2.4))
    b.append(P('M-12 -24 Q0 -17 12 -24', stroke='#62748c', stroke_width=2))
    for sg, h in ((-1, la), (1, ra)):
        sx, sy = sg * 25, -16
        mx, my = (sx + h[0]) / 2.0 + sg * 3, (sy + h[1]) / 2.0 + 5
        b.append(limb(sx, sy, mx, my, TUN_P, 20, hand=None))
        b.append(limb(mx, my, h[0], h[1], SK, 14, hand=SK, hr=7.5))
        b.append(E(mx, my, 8, 4.5, '#5e4129', stroke_width=1.6, transform='rotate(%s %s %s)' % (f(math.degrees(math.atan2(h[1] - sy, h[0] - sx)) + 90), f(mx), f(my))))
    b.append(C(0, -48, 22, SK))
    b.append(P('M-23 -50 Q-24 -75 0 -75 Q24 -75 23 -50 Q12 -63 0 -63 Q-12 -63 -23 -50 Z', '#4a2f1c'))
    b.append(P('M-22 -46 Q-25 -17 0 -16 Q25 -17 22 -46 Q16 -31 0 -30 Q-16 -31 -22 -46 Z', '#4a2f1c'))
    b.append(face(0, -46, expr, my=-37, look=look, sp=8, cheeks=False))
    b.append(P('M-9 -34 Q0 -29 9 -34', stroke='#4a2f1c', stroke_width=3.2))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- NONNA (small, grey bun, dark blue tunic, beige shawl)
def nonna(x, y, s=1, rot=0, la=(-20, 16), ra=(20, 16), expr='smile', look=0, flip=False):
    b = []
    b.append(E(-9, 58, 8, 4, '#6b4a2c') + E(9, 58, 8, 4, '#6b4a2c'))
    b.append(P('M-15 -12 Q0 -21 15 -12 L26 56 L-26 56 Z', '#4c5f86'))
    b.append(P('M-25 50 L25 50 L26 56 L-26 56 Z', '#3a4a6e', stroke_width=1.5))
    b.append(limb(-13, -9, la[0], la[1], '#4c5f86', 13, hr=5.5))
    b.append(limb(13, -9, ra[0], ra[1], '#4c5f86', 13, hr=5.5))
    b.append(P('M-21 -13 Q0 -27 21 -13 L16 10 L0 26 L-16 10 Z', '#e4d2a8'))
    b.append(P('M-12 14 L-14 22 M-6 21 L-8 29 M12 14 L14 22 M6 21 L8 29', stroke='#c9b27c', stroke_width=1.6))
    b.append(P('M-12 -15 Q0 -8 12 -15', stroke='#bfa772', stroke_width=1.6))
    b.append(C(0, -55, 9, '#cfcfd6'))
    b.append(P('M-3 -57 Q0 -53 3 -57', stroke='#9a9aa4', stroke_width=1.3))
    b.append(C(0, -31, 18, SK))
    b.append(P('M-19 -32 Q-20 -51 0 -51 Q20 -51 19 -32 Q10 -42 0 -43 Q-10 -42 -19 -32 Z', '#cfcfd6'))
    b.append(face(0, -29, expr, my=-19, look=look, sp=6.5))
    b.append(P('M-14 -30 L-18 -31 M-14 -27 L-18 -26 M14 -30 L18 -31 M14 -27 L18 -26 M-9 -39 Q0 -42 9 -39', stroke='#b98f72', stroke_width=1.2))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- props
def reeds(x, yb, n=7, h=60, seed=1, spread=26, heads=True):
    rnd = random.Random(seed)
    s = []
    for i in range(n):
        dx = (rnd.random() - 0.5) * spread * 2
        hh = h * (0.65 + 0.5 * rnd.random())
        bend = (rnd.random() - 0.5) * 22
        col = rnd.choice(['#6e8a3a', '#7f9c46', '#5f7a32', '#8aa84e'])
        s.append(P('M%s %s Q%s %s %s %s' % (f(x + dx), f(yb), f(x + dx + bend * 0.3), f(yb - hh * 0.6), f(x + dx + bend), f(yb - hh)), stroke=col, stroke_width=2.6, stroke_linecap='round'))
        if heads and rnd.random() < 0.45:
            s.append(E(x + dx + bend, yb - hh - 6, 2.6, 8, '#8a5a2b', stroke='#5a3a1c', stroke_width=1))
    return G(*s)


def tuft(x, yb, sc=1, col='#7f9c46'):
    return P('M%s %s Q%s %s %s %s M%s %s Q%s %s %s %s M%s %s Q%s %s %s %s' % (
        f(x - 6 * sc), f(yb), f(x - 8 * sc), f(yb - 8 * sc), f(x - 12 * sc), f(yb - 14 * sc),
        f(x), f(yb), f(x), f(yb - 10 * sc), f(x + 1 * sc), f(yb - 18 * sc),
        f(x + 6 * sc), f(yb), f(x + 8 * sc), f(yb - 8 * sc), f(x + 13 * sc), f(yb - 13 * sc)), stroke=col, stroke_width=2.2, stroke_linecap='round')


def egret(x, y, s=1, flying=False, flip=False, wing='up'):
    b = []
    if flying:
        b.append(P('M-12 6 L-30 12', stroke='#4a4a4a', stroke_width=2))
        w1 = 'M-4 -4 Q-14 -40 -42 -34 Q-22 -16 -2 4 Z' if wing == 'up' else 'M-4 -2 Q-10 26 -38 34 Q-20 8 -2 4 Z'
        b.append(P(w1, '#f5f5f0', stroke_width=1.8))
        b.append(E(0, 0, 18, 8, '#fdfdf8', transform='rotate(-8)'))
        b.append(P('M14 -4 Q24 -8 24 -16', stroke=OUT, stroke_width=6) + P('M14 -4 Q24 -8 24 -16', stroke='#fdfdf8', stroke_width=3))
        b.append(C(25, -18, 5, '#fdfdf8'))
        b.append(P('M29 -19 L42 -16 L29 -15 Z', '#f0b23a', stroke_width=1.5))
        b.append(C(26, -19, 1.1, '#2a1a10', stroke='none'))
    else:
        b.append(P('M-4 8 L-5 34 M4 8 L5 34', stroke='#3a3a3a', stroke_width=2.2))
        b.append(P('M-5 34 L-12 36 M5 34 L12 36', stroke='#3a3a3a', stroke_width=2))
        b.append(P('M-14 -2 L-26 6 L-12 6 Z', '#fdfdf8', stroke_width=1.6))
        b.append(E(0, 0, 15, 9, '#fdfdf8', transform='rotate(-14)'))
        b.append(P('M9 -6 Q20 -14 12 -28', stroke=OUT, stroke_width=6) + P('M9 -6 Q20 -14 12 -28', stroke='#fdfdf8', stroke_width=3))
        b.append(C(13, -30, 5, '#fdfdf8'))
        b.append(P('M17 -31 L31 -28 L17 -26 Z', '#f0b23a', stroke_width=1.5))
        b.append(C(14, -31, 1.1, '#2a1a10', stroke='none'))
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=xf(x, y, s, 0, flip))


def gull(x, y, s=1, col='#fdfdf8'):
    return P('M%s %s Q%s %s %s %s Q%s %s %s %s' % (f(x - 14 * s), f(y), f(x - 7 * s), f(y - 9 * s), f(x), f(y), f(x + 7 * s), f(y - 9 * s), f(x + 14 * s), f(y)), stroke=col, stroke_width=2.4 * s, stroke_linecap='round', stroke_linejoin='round')


def mound(cx, yb, w, h, col='#b9a878', top='#8fa860'):
    s = [P('M%s %s Q%s %s %s %s Q%s %s %s %s Z' % (f(cx - w / 2.0), f(yb), f(cx - w * 0.28), f(yb - h * 1.1), f(cx), f(yb - h), f(cx + w * 0.3), f(yb - h * 1.1), f(cx + w / 2.0), f(yb)), col, stroke=OUT, stroke_width=2)]
    s.append(P('M%s %s Q%s %s %s %s Q%s %s %s %s' % (f(cx - w * 0.36), f(yb - h * 0.55), f(cx - w * 0.22), f(yb - h * 0.95), f(cx), f(yb - h * 0.88), f(cx + w * 0.22), f(yb - h * 0.95), f(cx + w * 0.38), f(yb - h * 0.5)), stroke=top, stroke_width=4, stroke_linecap='round'))
    for k in range(3):
        s.append(tuft(cx - w * 0.2 + k * w * 0.22, yb - h * (0.8 - 0.1 * (k % 2)), 0.7))
    return G(*s)


def pole(x, yt, yb, w=8, col='#8b5a35'):
    s = [R(x - w / 2.0, yt, w, yb - yt, col, stroke=OUT, stroke_width=1.8)]
    s.append(L(x - w / 4.0, yt + 4, x - w / 4.0, yb - 3, '#a8703a', 1.4))
    s.append(E(x, yt, w / 2.0, w / 4.0, '#d9a96e', stroke=OUT, stroke_width=1.5))
    return G(*s)


def hut(cx, yb, sc=1, boat=False):
    b = []
    for px in (-46, -16, 16, 46):
        b.append(R(px - 4, -40, 8, 46, '#8b5a35', stroke_width=1.8))
    b.append(R(-58, -46, 116, 9, '#c99a62'))
    b.append(L(-30, -46, -30, -37, '#8b5a35', 1.4) + L(0, -46, 0, -37, '#8b5a35', 1.4) + L(30, -46, 30, -37, '#8b5a35', 1.4))
    b.append(R(-46, -104, 92, 58, '#b79a5e'))
    for yy in range(-98, -50, 8):
        b.append(L(-46, yy, 46, yy, '#8f7440', 1.4))
    for xx in range(-38, 46, 12):
        b.append(L(xx, -104, xx, -46, '#a68a50', 1.2))
    b.append(E(-30, -64, 9, 5, '#c9b27c', stroke='none') + E(30, -90, 9, 5, '#c9b27c', stroke='none'))
    b.append(R(-10, -86, 20, 40, '#4a3426'))
    b.append(P('M-64 -100 L0 -146 L64 -100 Z', '#d9b560'))
    for k in range(1, 6):
        t = k / 6.0
        b.append(L(-64 + 64 * t - 2, -100 - 46 * t, 64 - 64 * t + 2, -100 - 46 * t, '#a8883c', 1.4))
    b.append(P('M-64 -100 L-58 -94 M64 -100 L58 -94 M-40 -100 L-38 -93 M-14 -100 L-13 -93 M14 -100 L13 -93 M40 -100 L38 -93', stroke='#a8883c', stroke_width=2))
    if boat:
        b.append(P('M52 -40 Q70 -26 74 -6', stroke='#6b4428', stroke_width=2))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) scale(%s)' % (f(cx), f(yb), f(sc)))


def boat(cx, y, w=240, d=34, hull='#9a6a3c'):
    l, r = -w / 2.0, w / 2.0
    te = y - 18
    b = [P('M%s %s Q0 %s %s %s Q%s %s %s %s L%s %s Q%s %s %s %s Z' % (
        f(l), f(te), f(2 * y - te), f(r), f(te), f(r - 6), f(y + d * 0.6), f(r - 38), f(y + d), f(l + 38), f(y + d), f(l + 6), f(y + d * 0.6), f(l), f(te)), hull)]
    b.append(P('M%s %s Q0 %s %s %s' % (f(l + 2), f(te + 2), f(2 * y - te + 2), f(r - 2), f(te + 2)), stroke='#d9a96e', stroke_width=4))
    for k in (0.38, 0.7):
        b.append(P('M%s %s L%s %s' % (f(l + 14 + 6 * k * 3), f(y + d * k), f(r - 14 - 6 * k * 3), f(y + d * k)), stroke='#6e4a2c', stroke_width=1.8))
    return G(*b, stroke=OUT, stroke_width=2.4, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s 0)' % f(cx))


def oar(x1, y1, x2, y2, bl=34):
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    d = 'M%s %s L%s %s' % (f(x1), f(y1), f(x2), f(y2))
    return G(P(d, stroke=OUT, stroke_width=6, stroke_linecap='round'), P(d, stroke='#c99a62', stroke_width=3, stroke_linecap='round'),
             G(E(-bl / 2.0 + 2, 0, bl / 2.0, 6.5, '#c99a62', stroke=OUT, stroke_width=2), transform='translate(%s %s) rotate(%s)' % (f(x2), f(y2), f(ang))))


def ripple(x, y, w, col='#ffffff', op=0.55, sw=2.4):
    return P('M%s %s Q%s %s %s %s Q%s %s %s %s' % (f(x), f(y), f(x + w / 4.0), f(y - 4), f(x + w / 2.0), f(y), f(x + 3 * w / 4.0), f(y + 4), f(x + w), f(y)), stroke=col, stroke_width=sw, opacity=op, stroke_linecap='round')


def smoke(x, yb, h=50, col='#8a8a92'):
    d = 'M%s %s Q%s %s %s %s T%s %s T%s %s' % (f(x), f(yb), f(x + 6), f(yb - h * 0.25), f(x), f(yb - h * 0.5), f(x + 3), f(yb - h * 0.8), f(x - 2), f(yb - h))
    return G(P(d, stroke=col, stroke_width=4, stroke_linecap='round', opacity=0.5), E(x - 2, yb - h - 4, 9, 4, col, stroke='none', opacity=0.28), E(x + 3, yb - h - 9, 13, 5, col, stroke='none', opacity=0.2))


def bundle(x, y, sc=1, col='#c9a96a'):
    return G(E(0, -8, 14, 11, col), P('M-11 -12 Q0 -4 11 -12 M0 -19 L0 2', stroke='#7a5a3a', stroke_width=1.6), C(0, -19, 2.4, '#7a5a3a'),
             stroke=OUT, stroke_width=1.8, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def sackbag(x, y, sc=1, col='#e0cfa0'):
    return sack(x, y, sc, col)


def basket(x, y, sc=1, rot=0, items=True):
    b = [P('M-16 -18 Q-26 -34 0 -38 Q26 -34 16 -18 Q-26 -34 -16 -18 Z', 'none', stroke_width=2.4)]
    if items:
        b.append(E(-6, -22, 7, 5, '#e8c07a') + E(6, -22, 7, 5, '#d9923a') + C(0, -26, 5, '#cf4a3a'))
    b.append(P('M-18 -20 L18 -20 L13 0 L-13 0 Z', '#b8844a'))
    b.append(P('M-16 -13 L16 -13 M-14 -6 L14 -6 M-6 -20 L-4 0 M3 -20 L4 0', stroke='#8a5a2b', stroke_width=1.6))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def mallet(x, y, sc=1, rot=0):
    """origin at the grip (lower end of handle); head at top"""
    return G(R(-3.5, -52, 7, 56, '#8b5a35'), R(-20, -76, 40, 28, '#b07a42', rx=4),
             L(-12, -76, -12, -48, '#7a4a22', 2) + L(12, -76, 12, -48, '#7a4a22', 2),
             P('M-17 -66 L17 -66', stroke='#d9a96e', stroke_width=1.6),
             stroke=OUT, stroke_width=2.2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def log_pile(x, y, ln=150, n=4, ang=0, sc=1):
    b = []
    for i in range(n):
        yo = -i * 13
        sh = (i % 2) * 7 - 3
        b.append(G(R(-ln / 2.0 + sh, yo - 14, ln, 14, '#8b5a35', rx=7), L(-ln / 2.0 + sh + 12, yo - 10, ln / 2.0 + sh - 14, yo - 10, '#a8703a', 1.5),
                   E(ln / 2.0 + sh - 4, yo - 7, 4, 6, '#d9a96e'), L(-ln / 4.0 + sh, yo - 14, -ln / 4.0 + sh + 3, yo, '#6e4a2c', 1.3)))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(ang), f(sc)))


def refugee(x, yb, sc=1, col='#9a9a5a', flip=False, carry='bundle', hair='#3a2a20'):
    b = [roman(x, yb, sc, col, flip, hair, arms='carry')]
    ex = []
    if carry == 'bundle':
        ex.append(G(E(-13, -30, 9, 11, '#c9a96a'), P('M-19 -36 Q-13 -30 -7 -36', stroke='#7a5a3a', stroke_width=1.5)))
    elif carry == 'basket':
        ex.append(G(P('M-8 -48 L8 -48 L6 -38 L-6 -38 Z', '#b8844a')))
        ex.append(G(E(0, -54, 9, 6, '#d9923a')))
    elif carry == 'sack':
        ex.append(G(P('M-6 -34 Q-18 -30 -16 -12 L-6 -10 Z', '#e0cfa0')))
    elif carry == 'hood':
        ex.append(P('M-9 -46 Q-12 -58 0 -58 Q12 -58 9 -46 Q0 -52 -9 -46 Z', '#a77a5a'))
    if ex:
        b.append(G(*ex, stroke=OUT, stroke_width=1.6, stroke_linejoin='round', transform=xf(x, yb, sc, 0, flip)))
    return ''.join(b)


def cart(x, yb, sc=1):
    b = [R(-34, -34, 68, 16, '#9a6a3c'), P('M-34 -34 L-40 -50 M34 -34 L40 -50', stroke=OUT, stroke_width=3),
         E(-14, -42, 15, 11, '#c9a96a'), E(12, -44, 14, 12, '#d1b87e'), E(0, -50, 11, 9, '#a77a5a')]
    b.append(C(0, -14, 14, '#8b5a35', stroke_width=2.6) + C(0, -14, 4, '#c99a62') + L(-14, -14, 14, -14, OUT, 1.6) + L(0, -28, 0, 0, OUT, 1.6))
    b.append(P('M34 -28 L66 -14', stroke=OUT, stroke_width=3))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(yb), f(sc)))


def sandwich(x, y, sc=1, rot=0):
    return G(P('M-16 -2 Q-16 -14 0 -14 Q16 -14 16 -2 Z', '#e6b86a'), R(-17, -2, 34, 5, '#e2573a', rx=2), R(-17, 3, 34, 4, '#8fbf5a', rx=2),
             R(-16, 7, 32, 6, '#e6b86a', rx=3),
             stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(sc)))


def coin(x, y, r, rot=0):
    b = [C(0, 0, r, '#b5793a', stroke_width=2.5), C(0, 0, r - 4 * max(1, r / 14.0), '#d19a4a', stroke='#e9b949', stroke_width=max(1.2, r / 14.0))]
    n = 14
    for k in range(n):
        a = 2 * math.pi * k / n
        b.append(E((r * 0.78) * math.cos(a), (r * 0.78) * math.sin(a), r * 0.1, r * 0.05, '#7a4a1c', stroke='none', transform='rotate(%s %s %s)' % (f(math.degrees(a) + 90), f((r * 0.78) * math.cos(a)), f((r * 0.78) * math.sin(a)))))
    b.append(C(-r * 0.04, -r * 0.05, r * 0.46, '#c98d47', stroke='#7a4a1c', stroke_width=max(1, r / 18.0)))
    b.append(P('M%s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Z' % (f(-r * 0.12), f(-r * 0.36), f(r * 0.2), f(-r * 0.36), f(r * 0.22), f(-r * 0.1), f(r * 0.3), f(r * 0.0), f(r * 0.12), f(r * 0.06), f(-r * 0.1), f(r * 0.3), f(-r * 0.2), f(-r * 0.1)), '#9a6a2a', stroke='#6a3f14', stroke_width=max(1, r / 22.0)))
    return G(*b, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


def swirl_sky(W, H, cx, cy, gid_a, gid_b, seed=0):
    b = []
    b.append(R(0, 0, W, H, 'url(#%s)' % gid_b))
    sl = []
    for k in range(34):
        a = 2 * math.pi * k / 34 + 0.05
        r0 = 150 + (k % 3) * 40
        sl.append(L(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + 700 * math.cos(a), cy + 700 * math.sin(a), '#f0a92e', 4 if k % 2 else 3, stroke_linecap='round'))
    b.append(G(*sl, opacity=0.6))
    b.append(C(cx, cy, 230, 'url(#%s)' % gid_a, stroke='none'))
    for (w, col, op) in [(26, '#f4b942', 0.85), (16, '#ffd36e', 0.95), (7, '#fff6cf', 1)]:
        for arm in range(3):
            pts = []
            a0 = arm * 2 * math.pi / 3
            r = 8
            while r < 330:
                a = a0 + r * 0.021
                pts.append('%s %s' % (f(cx + r * math.cos(a)), f(cy + r * math.sin(a) * 0.82)))
                r += 6
            b.append(P('M' + ' L'.join(pts), stroke=col, stroke_width=w * 0.5, stroke_linecap='round', opacity=op))
    b.append(C(cx, cy, 36, '#ffffff', stroke='none', opacity=0.9))
    return ''.join(b)


def becco_mallet(x, y, s=1, rot=0, flip=False, wings='up'):
    """Becco flying with the wooden mallet gripped in his claws"""
    mx, my = wpt(x, y, s, rot, 0, 54, flip)
    m = mallet(mx, my, 0.62 * s, 180 + rot * 0.5 + (12 if not flip else -12))
    return becco(x, y, s, rot, flip, wings, False, True) + m
