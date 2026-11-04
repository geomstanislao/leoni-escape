import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/g2611_work')
from rl import *
from common import hid, tx, svg, ink

CARDS = {}


def card(n):
    def deco(fn):
        CARDS[n] = fn
        return fn
    return deco


def T_(x, y, s, rot=0):
    return 'translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(s))


def pat_diamond(p, tag=''):
    return T('pattern', R(0, 0, 12, 12, '#f7ecd6', stroke='none') + P('M6 0 L12 6 L6 12 L0 6 Z', '#e8a496', stroke='none') +
             P('M6 3.4 L8.6 6 L6 8.6 L3.4 6 Z', '#f7ecd6', stroke='none'),
             id=p + 'dm' + tag, width=12, height=12, patternUnits='userSpaceOnUse')


def pointed(a, b, ys, yt, yb):
    m = (a + b) / 2.0
    k = (ys - yt) * .72
    return 'M%s %s L%s %s Q%s %s %s %s Q%s %s %s %s L%s %s Z' % (f(a), f(yb), f(a), f(ys), f(a), f(ys - k), f(m), f(yt), f(b), f(ys - k), f(b), f(ys), f(b), f(yb))


def ducale(p, x0, x1, yb, hh, n=6, tag='a', crenel=True):
    """Doge's Palace facade. returns (defs, svg)."""
    w = x1 - x0
    h1, h2 = hh * .26, hh * .24
    yw = yb - hh
    yl = yb - h1 - h2
    yp = yb - h1
    d = pat_diamond(p, tag) + LGd(p + 'dl' + tag, [(0, '#ffffff', .35), (1, '#5a3a20', .28)], 0, 0, 1, 0)
    b = []
    b.append(R(x0, yw, w, yl - yw + 1, U(p + 'dm' + tag), stroke=OUT, stroke_width=1.4))
    # wall windows
    wn = max(2, int(n / 2))
    for i in range(wn):
        cx = x0 + w * (i + .5) / wn if wn > 2 else x0 + w * (.3 + .4 * i)
        ww = min(w * .1, 13)
        b.append(R(cx - ww / 2 - 1.5, yw + (yl - yw) * .22, ww + 3, (yl - yw) * .52, '#f1e4c8', stroke=OUT, stroke_width=1))
        b.append(P(pointed(cx - ww / 2, cx + ww / 2, yw + (yl - yw) * .4, yw + (yl - yw) * .27, yw + (yl - yw) * .72), '#4a3a34', stroke=OUT, stroke_width=1))
        b.append(R(cx - ww / 2 - 3, yw + (yl - yw) * .74, ww + 6, 2.4, '#d8c9a4', stroke=OUT, stroke_width=.9))
    # crenellation
    if crenel:
        k = int(w / 10)
        for i in range(k):
            xx = x0 + i * w / k + 1
            b.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(xx), f(yw), f(xx), f(yw - 3), f(xx + w / k * .45), f(yw - 6.5), f(xx + w / k * .8), f(yw)), '#f7ecd6', stroke=OUT, stroke_width=.9))
    # loggia
    b.append(R(x0, yl, w, h2 + 1, '#efe1c0', stroke=OUT, stroke_width=1.3))
    m = n * 2
    for i in range(m):
        a = x0 + w * (i + .22) / m
        c = x0 + w * (i + .78) / m
        b.append(P(pointed(a, c, yl + h2 * .45, yl + h2 * .1, yp - 1), '#6e5446', stroke=OUT, stroke_width=.9))
        b.append(P(pointed(a + 1.3, c - 1.3, yl + h2 * .5, yl + h2 * .22, yp - 1), '#8a6c58', stroke='none', opacity=.6))
    # quatrefoil band
    b.append(R(x0, yl - 0.2, w, 4.6, '#e3d3ac', stroke=OUT, stroke_width=1))
    for i in range(m):
        b.append(C(x0 + w * (i + .5) / m, yl + 2.2, 1.5, '#a65e4a', stroke='none'))
    # portico
    b.append(R(x0, yp, w, h1, '#f2e6c8', stroke=OUT, stroke_width=1.5))
    for i in range(n):
        a = x0 + w * (i + .16) / n
        c = x0 + w * (i + .84) / n
        b.append(P(pointed(a, c, yp + h1 * .38, yp + h1 * .05, yb), '#3f2f28', stroke=OUT, stroke_width=1.1))
        b.append(P(pointed(a + 2, c - 2, yp + h1 * .5, yp + h1 * .25, yb), '#5a443a', stroke='none', opacity=.8))
    for i in range(n + 1):
        cx = x0 + w * i / n
        b.append(R(cx - 1.8, yp + 1, 3.6, h1, '#fbf3de', stroke=OUT, stroke_width=.9))
        b.append(R(cx - 2.6, yb - 3, 5.2, 3, '#d8c9a4', stroke=OUT, stroke_width=.8))
    b.append(R(x0, yp - 1, w, 2.4, '#d8c9a4', stroke=OUT, stroke_width=1))
    b.append(R(x0, yw, w, hh, U(p + 'dl' + tag), stroke='none'))
    b.append(R(x0, yw, w, 3, '#2a1a10', stroke='none', opacity=.18))
    return d, G(*b)


def campanile(x, yb, h, w=14):
    b = []
    sh = h * .66
    b.append(R(x - w / 2, yb - sh, w, sh, '#c0654a', stroke=OUT, stroke_width=1.5))
    b.append(R(x + w * .12, yb - sh, w * .38, sh, '#8c4632', stroke='none', opacity=.55))
    b.append(R(x - w / 2 + 1.5, yb - sh, 2.2, sh, '#e59a7c', stroke='none', opacity=.7))
    for k in range(1, 8):
        b.append(PLn('M%s %s l%s 0' % (f(x - w / 2), f(yb - sh * k / 8.0)), '#9a4a34', .8, .7) if False else PLn('M%s %s L%s %s' % (f(x - w / 2), f(yb - sh * k / 8.0), f(x + w / 2), f(yb - sh * k / 8.0)), '#9a4a34', .7, .55))
    for yy in (.35, .62):
        b.append(R(x - 2, yb - sh * yy - 6, 4, 9, '#3f2f28', stroke=OUT, stroke_width=.8))
    b.append(R(x - w / 2 - 1.5, yb - sh - 3, w + 3, 3.4, '#efe1c0', stroke=OUT, stroke_width=1.1))
    bw = w * .92
    b.append(R(x - bw / 2, yb - sh - 3 - h * .13, bw, h * .13, '#efe1c0', stroke=OUT, stroke_width=1.3))
    for k in range(3):
        cx = x - bw / 2 + bw * (k + .5) / 3
        b.append(P(pointed(cx - 1.9, cx + 1.9, yb - sh - 3 - h * .06, yb - sh - 3 - h * .12, yb - sh - 5), '#3f2f28', stroke='none'))
    b.append(R(x - bw / 2 - 1, yb - sh - 3 - h * .13 - 2.2, bw + 2, 2.2, '#d8c9a4', stroke=OUT, stroke_width=.9))
    yt = yb - sh - 3 - h * .13 - 2.2
    b.append(P('M%s %s L%s %s L%s %s Z' % (f(x - bw / 2), f(yt), f(x), f(yt - h * .2), f(x + bw / 2), f(yt)), '#6aa383', stroke=OUT, stroke_width=1.3))
    b.append(P('M%s %s L%s %s L%s %s Z' % (f(x), f(yt), f(x), f(yt - h * .2), f(x + bw / 2), f(yt)), '#4d8466', stroke='none', opacity=.7))
    b.append(C(x, yt - h * .2 - 1, 1.8, '#f4c64e', stroke=OUT, stroke_width=.9))
    return G(*b)


def basilica(p, x0, x1, yb, hh):
    w = x1 - x0
    d = LGd(p + 'bd', [(0, '#e8f0ee'), (1, '#a9bdb8')]) + LGd(p + 'bg', [(0, '#f1d98a'), (1, '#c99a3a')])
    b = []
    cx = (x0 + x1) / 2
    # domes
    for (dx, sc) in [(-w * .33, .78), (-w * .17, .9), (0, 1.08), (w * .17, .9), (w * .33, .78)]:
        r = w * .085 * sc
        yb_d = yb - hh * .62 - (8 if sc > 1 else 0) * 0
        c = cx + dx
        b.append(R(c - r * .7, yb_d - 1, r * 1.4, 4, '#efe1c0', stroke=OUT, stroke_width=1))
        b.append(P('M%s %s Q%s %s %s %s Q%s %s %s %s Z' % (f(c - r), f(yb_d), f(c - r * 1.1), f(yb_d - r * 1.9), f(c), f(yb_d - r * 2.1), f(c + r * 1.1), f(yb_d - r * 1.9), f(c + r), f(yb_d)), U(p + 'bd'), stroke=OUT, stroke_width=1.3))
        b.append(P('M%s %s Q%s %s %s %s' % (f(c - r * .55), f(yb_d - r * .3), f(c - r * .6), f(yb_d - r * 1.5), f(c - r * .1), f(yb_d - r * 1.9)), 'none', stroke='#ffffff', stroke_width=1.6, opacity=.8))
        b.append(R(c - .8, yb_d - r * 2.1 - 4.5, 1.6, 4.5, '#d9a441', stroke=OUT, stroke_width=.7))
        b.append(C(c, yb_d - r * 2.1 - 5, 1.5, '#f4c64e', stroke=OUT, stroke_width=.7))
    # body
    b.append(R(x0, yb - hh * .62, w, hh * .62, '#f1e4c8', stroke=OUT, stroke_width=1.5))
    # upper gold mosaic arches
    for i in range(5):
        a = x0 + w * (i + .1) / 5
        c = x0 + w * (i + .9) / 5
        big = (i == 2)
        yt = yb - hh * (.62 if not big else .6)
        b.append(P(pointed(a, c, yb - hh * .4, yb - hh * (.58 if big else .54), yb - hh * .26), U(p + 'bg'), stroke=OUT, stroke_width=1.1))
        b.append(P(pointed(a + 2.5, c - 2.5, yb - hh * .38, yb - hh * (.5 if big else .47), yb - hh * .26), '#e9c46a', stroke='none', opacity=.6))
    b.append(R(x0, yb - hh * .27, w, 2.8, '#d8c9a4', stroke=OUT, stroke_width=1))
    # portals
    for i in range(5):
        a = x0 + w * (i + .08) / 5
        c = x0 + w * (i + .92) / 5
        big = (i == 2)
        b.append(P(pointed(a, c, yb - hh * .16, yb - hh * (.25 if big else .22), yb), '#4a3426' if not big else '#3a261c', stroke=OUT, stroke_width=1.2))
        b.append(P(pointed(a + 1.8, c - 1.8, yb - hh * .14, yb - hh * (.21 if big else .18), yb), '#6e5040', stroke='none', opacity=.7))
    for i in range(6):
        cxx = x0 + w * i / 5
        b.append(R(cxx - 1.3, yb - hh * .26, 2.6, hh * .26, '#fbf3de', stroke=OUT, stroke_width=.8))
    return d, G(*b)


def pennant_line(x1, y1, x2, y2, n=8, cols=('#d94a3a', '#f4c64e', '#4f9a5a', '#ffffff'), sag=7, size=6):
    b = [PLn('M%s %s Q%s %s %s %s' % (f(x1), f(y1), f((x1 + x2) / 2), f((y1 + y2) / 2 + sag * 2), f(x2), f(y2)), '#5a3a22', 1.1)]
    for i in range(n):
        t = (i + .5) / n
        x = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * ((x1 + x2) / 2) + t * t * x2
        y = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * ((y1 + y2) / 2 + sag * 2) + t * t * y2
        b.append(P('M%s %s L%s %s L%s %s Z' % (f(x - size / 2), f(y), f(x + size / 2), f(y), f(x), f(y + size * 1.2)), cols[i % len(cols)], stroke=OUT, stroke_width=.8))
    return G(*b)


def flagpole(x, yb, yt, flag, w=30, h=20, wave=3, kind='it'):
    """flag on pole. kind: it (green white red), fr (blue white red), lion (red with gold lion)"""
    b = [R(x - 1.2, yt, 2.4, yb - yt, '#7a5a3a', stroke=OUT, stroke_width=1.1), C(x, yt - .8, 2.2, '#f4c64e', stroke=OUT, stroke_width=.9)]
    cols = {'it': ('#3a9a58', '#fbf8ee', '#d9392e'), 'fr': ('#2f5aa8', '#fbf8ee', '#d9392e')}.get(kind)
    y0 = yt + 3
    if cols:
        for i in range(3):
            xa = x + 1.2 + w * i / 3.0
            xb = x + 1.2 + w * (i + 1) / 3.0
            ya = wave * math.sin(i * 1.3)
            yb2 = wave * math.sin((i + 1) * 1.3)
            b.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(xa), f(y0 + ya), f(xb), f(y0 + yb2), f(xb), f(y0 + yb2 + h), f(xa), f(y0 + ya + h)), cols[i], stroke=OUT, stroke_width=.9))
        b.append(P('M%s %s Q%s %s %s %s' % (f(x + 1.2), f(y0 + h * .55), f(x + w * .5), f(y0 + h * .55 + wave * 1.2), f(x + 1.2 + w), f(y0 + h * .55 + wave * .5)), 'none', stroke='#000000', stroke_width=3, opacity=.06))
    else:
        b.append(P('M%s %s Q%s %s %s %s L%s %s Q%s %s %s %s Z' % (f(x + 1.2), f(y0), f(x + w * .5), f(y0 + wave), f(x + 1.2 + w), f(y0), f(x + 1.2 + w), f(y0 + h), f(x + w * .5), f(y0 + h + wave), f(x + 1.2), f(y0 + h)), '#c0392b', stroke=OUT, stroke_width=1))
        b.append(lion_wing_emblem(x + 1.2 + w * .5, y0 + h * .52 + wave * .5, w / 34.0))
    return G(*b)


def lion_wing_emblem(x, y, s=1):
    b = [P('M-11 3 Q-18 -13 -8 -18 Q-2 -22 3 -14 L5 4 Z', '#f6d56a', stroke_width=1.1),
         P('M-9 -4 Q-4 -10 0 -12 M-8 2 Q-2 -4 3 -8', 'none', stroke='#c99a2e', stroke_width=.9),
         E(3, 5, 11, 6, '#f4c64e', stroke_width=1.1), C(12, 0, 5.5, '#e39a3b', stroke_width=1.1), C(13, 1, 3.5, '#f4c64e', stroke='none'),
         P('M-8 9 L-8 15 M-1 10 L-1 16 M7 10 L7 16 M12 9 L12 15', stroke_width=2.2, stroke='#f4c64e'), P('M-8 9 L-8 15 M-1 10 L-1 16 M7 10 L7 16 M12 9 L12 15', stroke_width=.8, stroke=OUT)]
    return G(*b, stroke=OUT, stroke_width=1.1, stroke_linejoin='round', stroke_linecap='round', transform=T_(x, y, s))


def paving_persp(p, y0, H, W_=215, c1='#e1d3b0', c2='#bda97e', vx=107, vy=None, seed=1, rows=7, cols=11, tint='#8a7650'):
    rnd = random.Random(seed)
    vy = y0 - 60 if vy is None else vy
    d = LGd(p + 'pv', [(0, c1), (1, c2)])
    b = [R(0, y0, W_, H - y0, U(p + 'pv'), stroke='none')]
    # horizontal joints with growing spacing
    ys = []
    for i in range(rows + 1):
        t = (i / float(rows)) ** 1.6
        ys.append(y0 + t * (H - y0))
    for y in ys[1:-1]:
        b.append(L(0, y, W_, y, tint, 1.1, opacity=.5))
    # verticals converging
    for j in range(-cols, cols + 1):
        x_top = vx + j * (W_ / float(cols)) * .35
        x_bot = vx + j * (W_ / float(cols)) * 1.0
        b.append(L(x_top, y0, x_bot, H, tint, 1.0, opacity=.4))
    # darker slabs
    for i in range(rows):
        for _ in range(2):
            j = rnd.randint(-cols, cols - 1)
            ya, yb_ = ys[i], ys[i + 1]
            ta = (ya - y0) / (H - y0 + 1e-6) * .65 + .35
            tb = (yb_ - y0) / (H - y0 + 1e-6) * .65 + .35
            xa0 = vx + j * (W_ / float(cols)) * .35 * (1 - (ya - y0) / (H - y0 + 1e-6)) + j * (W_ / float(cols)) * (ya - y0) / (H - y0 + 1e-6)
            xa1 = xa0 + (W_ / float(cols)) * ta
            xb0 = vx + j * (W_ / float(cols)) * .35 * (1 - (yb_ - y0) / (H - y0 + 1e-6)) + j * (W_ / float(cols)) * (yb_ - y0) / (H - y0 + 1e-6)
            xb1 = xb0 + (W_ / float(cols)) * tb
            b.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(xa0), f(ya), f(xa1), f(ya), f(xb1), f(yb_), f(xb0), f(yb_)), tint, stroke='none', opacity=.14))
    b.append(R(0, y0, W_, 5, '#000000', stroke='none', opacity=.12))
    return d, G(*b)


def wood_planks(p, x, y, w, h, col1='#b98a55', col2='#8a5f36', pw=26, tilt=0):
    d = LGd(p + 'wp', [(0, col1), (1, col2)])
    b = [R(x, y, w, h, U(p + 'wp'), stroke='none')]
    n = int(w / pw) + 1
    for i in range(n + 1):
        xx = x + i * pw
        b.append(L(xx, y, xx - tilt, y + h, '#4a3020', 1.2, opacity=.7))
    k = int(h / 12)
    rnd = random.Random(3)
    for i in range(k):
        yy = y + 4 + i * 12 + rnd.uniform(-1, 1)
        for j in range(n):
            if rnd.random() < .6:
                x1 = x + j * pw + rnd.uniform(2, pw * .4)
                b.append(PLn('M%s %s l%s 0' % (f(x1), f(yy), f(rnd.uniform(6, pw * .5))), '#6b4426', .8, .5))
    return d, G(*b)


# ---------------------------------------------------------- characters
def corno(x, y, s=1, rot=0, flip=False, sad=False):
    """doge's horn cap; origin at the centre of the base band (bottom)"""
    b = []
    b.append(P('M-17 0 Q-21 -22 -6 -31 Q8 -35 14 -45 Q23 -54 21 -33 Q19 -17 17 0 Z', '#c8352a'))
    b.append(P('M6 -32 Q14 -38 18 -46 Q23 -52 21 -33 Q19 -17 17 0 L8 0 Q14 -15 6 -32 Z', '#9c2420', stroke='none'))
    b.append(P('M-12 -9 Q-13 -20 -5 -27', 'none', stroke='#f08a7a', stroke_width=2.4))
    b.append(P('M14 -45 Q20 -52 21 -36', 'none', stroke='#f4c64e', stroke_width=1.6))
    b.append(P('M-19 3 L19 3 L17 -8 L-17 -8 Z', '#f4c64e'))
    b.append(P('M-17 -8 L17 -8', 'none', stroke='#fff2b8', stroke_width=1.6))
    b.append(P('M-16 -1 L16 -1', 'none', stroke='#c99a2e', stroke_width=1.2))
    b.append(C(0, -2.6, 3.2, '#3a86c8', stroke_width=1.3))
    b.append(C(-.8, -3.4, 1, '#cfe9ff', stroke='none'))
    if sad:
        b.append(E(-6, -17, 1.8, 2.6, '#2a1a10', stroke='none') + E(4, -17, 1.8, 2.6, '#2a1a10', stroke='none') + P('M-8 -22 L-4 -24 M6 -22 L2 -24', 'none', stroke_width=1.3) + P('M-5 -11 Q-1 -15 3 -11', 'none', stroke_width=1.5) + P('M5 -14 Q7 -10 5 -8', '#bfe3f2', stroke_width=1))
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=T_(x, y, s, rot) if not flip else 'translate(%s %s) rotate(%s) scale(%s %s)' % (f(x), f(y), f(rot), f(-s), f(s)))


def cuffia(x, y, s=1, rot=0):
    """white inner bonnet (cloth)"""
    b = [P('M-16 0 Q-18 -16 0 -19 Q18 -16 16 0 Q0 5 -16 0 Z', '#fbf8ee'), P('M-10 -4 Q0 -1 10 -4', 'none', stroke='#d8cfb8', stroke_width=1.2),
         P('M6 -16 Q12 -12 13 -4', 'none', stroke='#e4dcc6', stroke_width=1.2)]
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=T_(x, y, s, rot))


def doge(x, y, s=1, expr='sad', tear=True, la=(-26, 24), ra=(26, 24), cloth=None, flip=False, robe='#c8352a'):
    """Ludovico Manin: red robe, ermine collar, gold buttons, white side hair, bald top. origin: chest."""
    b = []
    b.append(E(-12, 66, 10, 5, '#5a3a22') + E(12, 66, 10, 5, '#5a3a22'))
    b.append(P('M-21 -18 Q-27 22 -32 66 L32 66 Q27 22 21 -18 Q0 -26 -21 -18 Z', robe))
    b.append(P('M8 -20 Q15 22 20 66 L32 66 Q27 22 21 -18 Z', '#9c2420', stroke='none'))
    b.append(P('M-24 56 Q0 62 24 56', 'none', stroke='#f4c64e', stroke_width=2.6))
    b.append(P('M0 -14 L0 64', 'none', stroke='#f4c64e', stroke_width=1.6))
    for yy in (-4, 10, 24, 38, 52):
        b.append(C(0, yy, 2.3, '#f4c64e', stroke_width=1.1))
    # arms/sleeves
    b.append(limb(-18, -10, la[0], la[1], robe, 16, hand=SK, hr=6))
    b.append(limb(18, -10, ra[0], ra[1], robe, 16, hand=SK, hr=6))
    if cloth:
        b.append(G(P('M-9 -4 Q-14 6 -9 14 L9 14 Q14 6 9 -4 Z', '#fbf8ee'), P('M-7 2 Q0 5 7 2 M-6 8 Q0 11 6 8', 'none', stroke='#d8cfb8', stroke_width=1.2),
                   transform='translate(%s %s) rotate(%s)' % (f(cloth[0]), f(cloth[1]), f(cloth[2] if len(cloth) > 2 else 0))))
    # ermine collar
    b.append(P('M-22 -17 Q0 -9 22 -17 Q24 -8 18 -4 Q0 3 -18 -4 Q-24 -8 -22 -17 Z', '#fbf8ee'))
    for (cx, cy) in [(-14, -9), (-6, -4), (6, -4), (14, -9), (0, -8)]:
        b.append(P('M%s %s l1.4 3.4 M%s %s l-1.4 3.4 M%s %s l0 3' % (f(cx), f(cy), f(cx), f(cy), f(cx), f(cy)), 'none', stroke='#2a1a10', stroke_width=1.2))
    # head
    b.append(C(-16, -38, 8, '#f4f0e6') + C(16, -38, 8, '#f4f0e6'))
    b.append(C(0, -38, 19, SK))
    b.append(P('M-12 -52 Q-4 -57 4 -55', 'none', stroke='#ffffff', stroke_width=3, opacity=.7))
    b.append(C(0, -35, 2.6, '#f0c9a0', stroke_width=1.2))
    b.append(face(0, -38, expr, my=-27, sp=7))
    b.append(P('M-11 -45 Q-7 -48 -3 -45 M3 -45 Q7 -48 11 -45', 'none', stroke='#f4f0e6', stroke_width=3))
    b.append(P('M-9 -29 Q0 -25 9 -29 Q0 -23 -9 -29 Z', '#f4f0e6', stroke_width=1.2) if expr != 'dot' else '')
    if tear:
        b.append(P('M9 -33 Q12 -26 9 -22 Q6 -26 9 -33 Z', '#bfe3f2', stroke_width=1.1))
    return ink(*b, transform=xf(x, y, s, 0, flip))


def napoleon(x, y, s=1):
    b = []
    b.append(P('M-48 70 Q-52 10 -26 -14 Q0 -22 26 -14 Q52 10 48 70 Z', '#2c4a8c'))
    b.append(P('M20 -14 Q52 10 48 70 L28 70 Q34 20 20 -14 Z', '#1f3770', stroke='none'))
    b.append(P('M-18 -14 L0 56 L18 -14 L10 -20 L0 -4 L-10 -20 Z', '#fbf8ee'))
    b.append(P('M-24 -12 L-6 58 L-14 66 L-34 4 Z', '#2c4a8c') + P('M24 -12 L6 58 L14 66 L34 4 Z', '#2c4a8c'))
    b.append(P('M-24 -12 L-6 58 L-14 66 L-34 4 Z', 'none', stroke='#f4c64e', stroke_width=1.6))
    b.append(P('M-6 20 L-22 -6 M6 20 L22 -6', 'none', stroke='#f4c64e', stroke_width=2))
    for yy in (22, 34, 46):
        b.append(C(-9 + (yy - 22) * .12, yy, 2.2, '#f4c64e', stroke_width=1.1) + C(9 - (yy - 22) * .12, yy, 2.2, '#f4c64e', stroke_width=1.1))
    b.append(P('M-12 -22 L0 -6 L12 -22 L16 -12 L0 4 L-16 -12 Z', '#c8352a'))
    b.append(P('M-26 -12 Q-44 -6 -48 12 L-34 16 L-26 0 Z', '#f4c64e'))
    b.append(P('M-44 12 L-50 24 M-40 14 L-44 26 M-36 15 L-38 27 M-47 16 L-54 22', 'none', stroke='#d9a441', stroke_width=2))
    b.append(P('M26 -12 Q44 -6 48 12 L34 16 L26 0 Z', '#f4c64e'))
    b.append(P('M44 12 L50 24 M40 14 L44 26 M36 15 L38 27 M47 16 L54 22', 'none', stroke='#d9a441', stroke_width=2))
    # hand in coat
    b.append(P('M-4 30 Q8 24 20 32 Q12 42 -2 40 Z', SK))
    b.append(P('M2 30 L4 38 M8 29 L10 38 M14 30 L14 38', 'none', stroke='#d9a67a', stroke_width=1.2))
    # neck + head
    b.append(R(-8, -26, 16, 14, '#e9bf94', stroke_width=2))
    b.append(P('M-22 -42 Q-24 -22 -8 -18 Q0 -14 8 -18 Q24 -22 22 -42 Q22 -62 0 -62 Q-22 -62 -22 -42 Z', SK))
    b.append(P('M-22 -42 Q-27 -34 -24 -26 L-20 -34 Z', '#6a4a2e', stroke_width=1.4) + P('M22 -42 Q27 -34 24 -26 L20 -34 Z', '#6a4a2e', stroke_width=1.4))
    b.append(P('M-22 -50 Q-10 -56 0 -52 Q10 -56 22 -50 L22 -44 Q10 -50 0 -46 Q-10 -50 -22 -44 Z', '#6a4a2e', stroke_width=1.4))
    b.append(P('M-4 -38 Q-6 -30 -2 -29', 'none', stroke='#d9a67a', stroke_width=1.5))
    b.append(E(-9, -40, 3.2, 3.6, '#ffffff', stroke_width=1.2) + E(9, -40, 3.2, 3.6, '#ffffff', stroke_width=1.2))
    b.append(C(-8.5, -40, 1.5, '#2a1a10', stroke='none') + C(8.5, -40, 1.5, '#2a1a10', stroke='none'))
    b.append(P('M-15 -47 L-4 -43 M15 -47 L4 -43', 'none', stroke='#3a2414', stroke_width=2.8))
    b.append(P('M-7 -24 Q0 -27 7 -24', 'none', stroke_width=2.2))
    b.append(C(-14, -32, 3.2, '#f0a090', stroke='none', opacity=.55) + C(14, -32, 3.2, '#f0a090', stroke='none', opacity=.55))
    # bicorne hat
    b.append(P('M-44 -56 Q-30 -76 -4 -78 Q22 -80 44 -56 Q42 -64 36 -66 Q16 -72 0 -70 Q-18 -72 -36 -66 Q-42 -62 -44 -56 Z', '#2a1f2a'))
    b.append(P('M-44 -56 Q-30 -76 -4 -78 Q22 -80 44 -56 Q38 -52 30 -56 Q0 -66 -30 -56 Q-38 -52 -44 -56 Z', '#2f2630'))
    b.append(P('M-42 -57 Q-30 -76 -4 -78 Q22 -80 42 -57', 'none', stroke='#f4c64e', stroke_width=2.2))
    b.append(P('M-26 -62 Q-8 -70 14 -66', 'none', stroke='#6a5a72', stroke_width=1.6))
    b.append(G(C(0, 0, 6, '#2f5aa8') + C(0, 0, 4, '#fbf8ee', stroke='none') + C(0, 0, 2, '#d9392e', stroke='none'), transform='translate(0 -62)'))
    return ink(*b, transform=T_(x, y, s))


def becco2(x, y, s=1, rot=0, flip=False, wings='down', hat='captain', legs_on=True, beak='closed', eyes='open'):
    b = []
    if legs_on:
        b.append(P('M-8 34 L-10 52 M10 34 L10 52', stroke='#f08a24', stroke_width=4))
        b.append(P('M-10 52 L-19 56 M-10 52 L-8 58 M-10 52 L-2 56 M10 52 L1 56 M10 52 L12 58 M10 52 L18 56', stroke='#f08a24', stroke_width=3))
    wg = 'M-22 -20 Q-54 0 -42 40 Q-30 32 -22 22 Z'
    if wings == 'up':
        wl = G(P(wg, '#a4a8b0'), transform='rotate(100 -22 -14)')
        wr = G(G(P(wg, '#a4a8b0'), transform='rotate(100 -22 -14)'), transform='scale(-1 1)')
    elif wings == 'wave':
        wl = P(wg, '#a4a8b0')
        wr = G(G(P(wg, '#a4a8b0'), transform='rotate(120 -22 -14)'), transform='scale(-1 1)')
    else:
        wl = P(wg, '#a4a8b0')
        wr = G(P(wg, '#a4a8b0'), transform='scale(-1 1)')
    b.append(wl)
    b.append(wr)
    b.append(E(0, 0, 28, 36, '#b9bcc2'))
    b.append(P('M10 -30 Q30 -8 24 22 Q18 34 6 36 Q22 10 10 -30 Z', '#9a9ea6', stroke='none'))
    b.append(E(-2, 8, 19, 28, '#ffffff', stroke='none'))
    b.append(P('M-7 4 L3 16 M3 4 L-7 16', stroke='#a8453a', stroke_width=2.6))
    b.append(C(0, -44, 22, '#fafaf7'))
    if beak == 'open':
        b.append(P('M-16 -49 L-46 -45 L-16 -41 Z', '#f08a24'))
        b.append(P('M-16 -39 L-42 -33 L-16 -35 Z', '#e0731a'))
    else:
        b.append(P('M-16 -49 L-46 -41 L-16 -38 Z', '#f08a24'))
        b.append(P('M-16 -38 L-40 -36 L-16 -31 Z', '#e0731a'))
    b.append(P('M-14 -36 Q-18 -29 -9 -31', stroke_width=2))
    if eyes == 'open':
        b.append(C(-6, -50, 5.5, '#ffe08a', stroke_width=2))
        b.append(C(-8, -50, 2.4, '#2a1a10', stroke='none'))
        b.append(P('M-14 -58 L1 -53', stroke_width=3))
    if hat == 'corno':
        b.append(corno(0, -60, 1.05, -6))
    elif hat == 'bigcorno':
        b.append(corno(-4, -47, 1.3, -12))
    if hat == 'captain':
        b.append(P('M-23 -58 Q-25 -80 0 -83 Q25 -80 23 -58 Z', '#ffffff'))
        b.append(P('M-23 -65 Q0 -59 23 -65 L22.5 -57 Q0 -51 -22.5 -57 Z', '#1f2f5a'))
        b.append(P('M-24 -56 Q-40 -54 -45 -48 Q-30 -47 -20 -51 Z', '#1f2f5a'))
        b.append(C(0, -61, 4.2, '#e9c46a', stroke_width=1.5))
    return ink(*b, transform=xf(x, y, s, rot, flip))


def kid_boots(x, y, s, kind, flip=False):
    """yellow rubber boots overlaid on nico/sofia/toni feet (same transform)"""
    fy, lx, bt = {'nico': (58, 12, 30), 'sofia': (67, 12, 44), 'toni': (54, 14, 28)}[kind]
    b = []
    for sx in (-1, 1):
        cx = sx * lx
        top = fy - (fy - bt) - 2 if False else bt
        b.append(P('M%s %s L%s %s L%s %s Q%s %s %s %s L%s %s Q%s %s %s %s Z' % (f(cx - 6.5), f(top), f(cx + 6.5), f(top), f(cx + 6.5), f(fy - 3), f(cx + 15), f(fy - 3), f(cx + 15), f(fy + 4), f(cx - 7), f(fy + 4.5), f(cx - 8), f(fy + 4), f(cx - 6.5), f(fy - 4)), '#f4c64e'))
        b.append(R(cx - 7, top, 14, 3.4, '#e39a3b', stroke_width=1.2))
        b.append(P('M%s %s L%s %s' % (f(cx - 3), f(top + 6), f(cx - 3), f(fy - 4)), 'none', stroke='#fff3c0', stroke_width=2))
        b.append(P('M%s %s L%s %s' % (f(cx - 8), f(fy + 2), f(cx + 15), f(fy + 2)), 'none', stroke='#b07a22', stroke_width=1.2))
    return ink(*b, transform=xf(x, y, s, 0, flip), sw=1.8)


def fig(x, y, s=1, shirt='#6a8ab8', hair='#3a2a20', skin=SK, arms='up', pants='#4a3a30', hat=None, flip=False, beard=False, expr='happy', hold=None, shoe='#4a3020'):
    b = []
    b.append(limb(-6, 28, -7, 54, pants, 10, hand=None) + limb(6, 28, 7, 54, pants, 10, hand=None))
    b.append(E(-8, 57, 7, 3.6, shoe) + E(8, 57, 7, 3.6, shoe))
    if arms == 'up':
        b.append(limb(-11, -6, -26, -32, shirt, 9, hand=skin, hr=4.6) + limb(11, -6, 25, -36, shirt, 9, hand=skin, hr=4.6))
    elif arms == 'one':
        b.append(limb(-11, -6, -12, 18, shirt, 9, hand=skin, hr=4.6) + limb(11, -6, 26, -36, shirt, 9, hand=skin, hr=4.6))
    elif arms == 'out':
        b.append(limb(-11, -6, -26, 8, shirt, 9, hand=skin, hr=4.6) + limb(11, -6, 28, 2, shirt, 9, hand=skin, hr=4.6))
    else:
        b.append(limb(-11, -6, -14, 20, shirt, 9, hand=skin, hr=4.6) + limb(11, -6, 14, 20, shirt, 9, hand=skin, hr=4.6))
    b.append(P('M-14 32 L-12 -8 Q0 -16 12 -8 L14 32 Z', shirt))
    b.append(P('M5 -10 L12 -8 L14 32 L6 32 Z', '#000000', stroke='none', opacity=.12))
    b.append(C(0, -24, 12, skin))
    if hat == 'straw':
        b.append(E(0, -30, 20, 5, '#e9c46a') + P('M-11 -32 Q-10 -48 0 -48 Q10 -48 11 -32 Z', '#e9c46a') + P('M-11 -34 Q0 -30 11 -34', 'none', stroke='#d9472f', stroke_width=2))
    elif hat == 'cap':
        b.append(P('M-12 -28 Q-12 -42 0 -42 Q12 -42 12 -28 Z', hair) + P('M-12 -28 L-20 -26', 'none', stroke=hair, stroke_width=3))
    else:
        b.append(P('M-12 -26 Q-13 -39 0 -39 Q13 -39 12 -26 Q6 -33 0 -32 Q-6 -33 -12 -26 Z', hair))
    if beard:
        b.append(P('M-8 -20 Q0 -8 8 -20 Q0 -15 -8 -20 Z', '#e8e0d0', stroke_width=1.2))
    b.append(E(-4.2, -25, 1.5, 2, '#2a1a10', stroke='none') + E(4.2, -25, 1.5, 2, '#2a1a10', stroke='none'))
    if expr == 'happy':
        b.append(P('M-4 -19 Q0 -14 4 -19 Z', '#a8453a', stroke_width=1))
    else:
        b.append(P('M-3 -18 Q0 -20 3 -18', 'none', stroke_width=1.2))
    if hold:
        b.append(hold)
    return ink(*b, transform=xf(x, y, s, 0, flip), sw=2.2)


def ballot(x, y, s=1, rot=0):
    return G(R(-6, -8, 12, 16, '#ffffff', stroke=OUT, stroke_width=1.2), P('M-3 -4 L3 -4 M-3 0 L3 0 M-3 4 L1 4', 'none', stroke='#9aa4b0', stroke_width=.9), transform=T_(x, y, s, rot))


def sparkles(*pts):
    return ''.join(sparkle4(x, y, r) for (x, y, r) in pts)


def full_bg(p, H, hz, gs, tone='day', sun=None, seed=1, tower=None, clouds=((.22, .32, .85), (.72, .22, .7), (.5, .48, .5)), shore_on=True, ripples=16, gcol=('#cdb68a', '#a98d62'), boats=True, birds=True):
    d1, b1 = sky_scene(p, 215, hz, tone, sun, seed, clouds, tower, birds, boats)
    d2, b2 = water_scene(p, 215, hz, gs if shore_on else H, tone, sun, seed, ripples)
    d = d1 + d2 + lit_defs(p)
    b = b1 + b2
    if shore_on:
        d3, b3 = shore(p, 215, H, gs, seed + 1, gcol[0], gcol[1])
        d += d3
        b += b3
    return d, b


def finish(p, H, d, b, vs=.3, after=()):
    vd, vr = vignette(p, 215, H, vs)
    return H, d + vd, ''.join(b) + vr + ''.join(after)
