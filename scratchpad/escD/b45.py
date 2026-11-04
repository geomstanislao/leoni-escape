import sys, math
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escD')
import gen
from gen import *

BR = '#9a6338'
DK = '#3a2210'
BRONZE = '#c98a3e'
BRONZE_D = '#a8692a'
WOOD = '#b57a3e'
WOOD_D = '#7a5230'
STRAW = '#d8b574'


def wpt(x, y, s, rot=0, flip=False):
    sx = -s if flip else s
    th = math.radians(rot)

    def fn(lx, ly):
        px, py = sx * lx, s * ly
        return (x + px * math.cos(th) - py * math.sin(th), y + px * math.sin(th) + py * math.cos(th))
    return fn


def xfm(x, y, s, rot=0, flip=False):
    return 'translate(%s %s) rotate(%s) scale(%s %s)' % (f(x), f(y), f(rot), f(-s if flip else s), f(s))


# ------------------------------------------------------------------ Baio / brown horse
def bhorse(x, y, s=1.0, blaze=True, braid=True, tail='long', rot=0, flip=False, blanket=False, eye='open', col=BR):
    b = []
    # tail (behind everything)
    if tail == 'long':
        b.append(P('M-15 -7 Q-29 -5 -27 11 Q-26 24 -24 34 Q-18 29 -18 17 Q-17 7 -12 1 Z', DK))
        b.append(P('M-21 8 Q-22 18 -22 28', stroke='#6b4220', stroke_width=1.2, stroke_linecap='round'))
    else:
        b.append(P('M-15 -7 Q-24 -8 -24 0 Q-23 7 -15 6 Z', DK))
    # legs
    lg = 'M-13 6 L-13 31 M-6 8 L-6 31 M9 8 L9 31 M16 6 L16 31'
    b.append(P(lg, stroke=OUT, stroke_width=6.6) + P(lg, stroke=col, stroke_width=4.2))
    for hx in (-13, -6, 9, 16):
        b.append(E(hx, 31.5, 3.8, 2.4, '#2a1a10'))
    # loose mane strands (behind neck)
    if not braid:
        for (sx, sy, ln) in [(18, -40, 16), (15, -33, 20), (12, -26, 21), (9, -19, 19), (6, -12, 16)]:
            d = 'M%s %s q-6 -8 %s -1 t%s 1 t%s -1' % (f(sx), f(sy), f(-ln * 0.4), f(-ln * 0.35), f(-ln * 0.3))
            b.append(P(d, stroke=OUT, stroke_width=6.4, stroke_linecap='round'))
        for (sx, sy, ln) in [(18, -40, 16), (15, -33, 20), (12, -26, 21), (9, -19, 19), (6, -12, 16)]:
            d = 'M%s %s q-6 -8 %s -1 t%s 1 t%s -1' % (f(sx), f(sy), f(-ln * 0.4), f(-ln * 0.35), f(-ln * 0.3))
            b.append(P(d, stroke=DK, stroke_width=4, stroke_linecap='round'))
    # neck, body
    b.append(P('M2 -8 L13 -31 L24 -19 L22 2 Z', col))
    b.append(E(0, 0, 19, 12, col))
    b.append(P('M5 -10 L13 -28 L22 -19 L20 -3 Z', col, stroke='none'))
    # head
    b.append(P('M13 -30 L19 -41 L26 -43 L42 -26 Q46 -19 44 -13 L42 -11 L33 -11 L24 -19 Z', col))
    b.append(P('M18 -40 L17 -51 L25 -43 Z', col))
    if blaze:
        b.append(P('M25.5 -43 L42 -26.5 L39 -17 L19 -36 Z', '#ffffff', stroke='none'))
        b.append(P('M25.5 -42.5 L41.5 -27 M19.5 -35.5 L38.5 -17.5', stroke=OUT, stroke_width=1.1, stroke_linecap='round'))
    if eye == 'open':
        b.append(C(29, -21, 2.3, '#2a1a10', stroke='none') + C(29.7, -21.8, 0.8, '#ffffff', stroke='none'))
    elif eye == 'closed':
        b.append(P('M26.5 -21 Q29 -18.5 31.5 -21', stroke_width=1.6))
    else:
        b.append(C(29, -21, 3.2, '#ffffff', stroke_width=1.2) + C(29.6, -21, 1.5, '#2a1a10', stroke='none'))
    b.append(C(41.5, -15.5, 1.3, '#2a1a10', stroke='none'))
    b.append(P('M34 -12.5 Q38 -14 41 -13', stroke_width=1.2, stroke_linecap='round'))
    # braided mane
    if braid:
        n = 5
        P1, P2 = (18.0, -39.0), (3.0, -9.0)
        b.append(P('M%s %s L%s %s' % (f(P1[0]), f(P1[1]), f(P2[0]), f(P2[1])), stroke=OUT, stroke_width=10.5, stroke_linecap='round'))
        b.append(P('M%s %s L%s %s' % (f(P1[0]), f(P1[1]), f(P2[0]), f(P2[1])), stroke=DK, stroke_width=7.5, stroke_linecap='round'))
        for i in range(n):
            t = i / (n - 1.0)
            cx, cy = P1[0] + (P2[0] - P1[0]) * t, P1[1] + (P2[1] - P1[1]) * t
            b.append(E(cx, cy, 5.4, 3.3, '#6b4220', stroke=OUT, stroke_width=1.2, transform='rotate(%s %s %s)' % (40 if i % 2 == 0 else -40, f(cx), f(cy))))
        pts = []
        m = 10
        for i in range(m):
            t = i / (m - 1.0)
            cx, cy = P1[0] + (P2[0] - P1[0]) * t, P1[1] + (P2[1] - P1[1]) * t
            pts.append((cx + (3.6 if i % 2 == 0 else -3.6), cy))
        b.append(P('M' + ' L'.join('%s %s' % (f(px), f(py)) for px, py in pts), stroke='#f1d9a8', stroke_width=1.5, stroke_linecap='round', stroke_linejoin='round'))
    if blanket:
        b.append(P('M-15 -10 Q0 -15 15 -10 L16 4 L-16 4 Z', '#d9a05a'))
        b.append(P('M-9 -12 L-9 4 M-1 -13 L-1 4 M7 -12 L7 4', stroke='#c8483a', stroke_width=2.4))
        b.append(P('M-12 -3 L14 -3', stroke='#fdf8ee', stroke_width=1.4, stroke_dasharray='3 2'))
        b.append(P('M-16 4 l0 3 M-12 4 l0 3 M-8 4 l0 3 M-4 4 l0 3 M0 4 l0 3 M4 4 l0 3 M8 4 l0 3 M12 4 l0 3 M16 4 l0 3', stroke='#c8483a', stroke_width=1.2))
    return ink(*b, w=1.6, transform=xfm(x, y, s, rot, flip))


def man(x, y, s=1.0, rot=0, flip=False, la=(-22, 14), ra=(24, 10), expr='smile', tunic='#9a6a3e', halter=False):
    b = []
    b.append(limb(-9, 28, -10, 56, SK, 12, hand=None) + limb(9, 28, 10, 56, SK, 12, hand=None))
    b.append(E(-12, 59, 9, 5, '#6a4220') + E(12, 59, 9, 5, '#6a4220'))
    b.append(limb(-17, -12, la[0], la[1], tunic, 14))
    b.append(limb(17, -12, ra[0], ra[1], tunic, 14))
    b.append(P('M-20 36 L-17 -16 Q0 -26 17 -16 L20 36 Z', tunic))
    b.append(R(-19, 14, 38, 6, '#5e381c'))
    b.append(P('M-20 31 L20 31', stroke='#c99a2e', stroke_width=2.4))
    b.append(P('M-8 -14 L0 -4 L8 -14', stroke='#5e381c', stroke_width=1.6))
    b.append(C(0, -37, 19, SK))
    b.append(P('M-20 -39 Q-19 -58 0 -58 Q19 -58 20 -39 Q10 -49 0 -48 Q-10 -49 -20 -39 Z', '#4a3020'))
    b.append(face(0, -37, expr, my=-24, sp=7))
    b.append(P('M-17 -27 Q-18 -8 0 -6 Q18 -8 17 -27 Q12 -17 0 -16 Q-12 -17 -17 -27 Z', '#4a3020'))
    if halter:
        hx, hy = ra
        b.append(E(hx + 4, hy + 16, 9, 12, 'none', stroke=OUT, stroke_width=5))
        b.append(E(hx + 4, hy + 16, 9, 12, 'none', stroke='#d8b574', stroke_width=3))
        b.append(P('M%s %s q-10 6 -14 22' % (f(hx), f(hy + 4)), stroke=OUT, stroke_width=5, stroke_linecap='round'))
        b.append(P('M%s %s q-10 6 -14 22' % (f(hx), f(hy + 4)), stroke='#d8b574', stroke_width=3, stroke_linecap='round'))
    return ink(*b, transform=xfm(x, y, s, rot, flip))


def fence(x1, x2, yb, h=24, step=26, col=WOOD):
    s = ''
    x = x1
    while x <= x2 + 0.1:
        s += ink(R(x - 2.5, yb - h, 5, h, WOOD_D, rx=1.5), w=1.4)
        x += step
    s += ink(R(x1 - 2, yb - h + 5, x2 - x1 + 4, 4.5, col, rx=1.5), R(x1 - 2, yb - h + 14, x2 - x1 + 4, 4.5, col, rx=1.5), w=1.4)
    return s


def hut(x, yb, w, h, rh=None):
    rh = rh or h * 0.8
    s = ink(R(x, yb - h, w, h, '#b98a4a'), w=1.8)
    for k in range(1, int(w // 8)):
        s += P('M%s %s L%s %s' % (f(x + k * 8), f(yb - h + 1), f(x + k * 8), f(yb - 1)), stroke='#8a5a2b', stroke_width=1)
    s += ink(R(x + w / 2 - 6, yb - 17, 12, 17, '#4a3020'), w=1.5)
    s += ink(P('M%s %s L%s %s L%s %s Z' % (f(x - 7), f(yb - h + 3), f(x + w / 2), f(yb - h - rh), f(x + w + 7), f(yb - h + 3)), STRAW), w=1.8)
    for k in range(-2, 3):
        s += P('M%s %s L%s %s' % (f(x + w / 2 + k * 5), f(yb - h - rh + 8 + abs(k) * 2), f(x + w / 2 + k * 11), f(yb - h)), stroke='#a8803f', stroke_width=1.1, stroke_linecap='round')
    return s


def sanctuary_far(x, yb, w=34, h=14):
    s = ink(R(x, yb - h, w, h, '#f1e6cf'), w=1.4)
    s += ink(P('M%s %s L%s %s L%s %s Z' % (f(x - 4), f(yb - h), f(x + w / 2), f(yb - h - 14), f(x + w + 4), f(yb - h)), '#c8683f'), w=1.4)
    for k in range(4):
        s += P('M%s %s L%s %s' % (f(x + 5 + k * (w - 10) / 3.0), f(yb - h + 1), f(x + 5 + k * (w - 10) / 3.0), f(yb - 1)), stroke='#a89874', stroke_width=1.4)
    return s


def bridge_broken(cx, yf, yn, H, hid_n=None):
    s = ''
    # floating pieces in the gap
    gy = (yf + 14 + yn) / 2.0
    s += R(-9, -2.5, 18, 5, WOOD, stroke=OUT, stroke_width=1.3, transform='translate(%s %s) rotate(-24)' % (f(cx - 22), f(gy + 2)))
    s += R(-8, -2.5, 16, 5, '#9a6638', stroke=OUT, stroke_width=1.3, transform='translate(%s %s) rotate(14)' % (f(cx + 20), f(gy - 3)))
    s += P('M%s %s q5 -3 10 0 t10 0' % (f(cx - 12), f(gy + 10)), stroke='#cfeaf0', stroke_width=1.8, stroke_linecap='round')
    # far stub
    s += ink(P('M%s %s L%s %s L%s %s L%s %s L%s %s L%s %s L%s %s L%s %s Z' % (
        f(cx - 15), f(yf), f(cx + 15), f(yf), f(cx + 18), f(yf + 13), f(cx + 10), f(yf + 10), f(cx + 3), f(yf + 15), f(cx - 5), f(yf + 10), f(cx - 12), f(yf + 15), f(cx - 18), f(yf + 12)), WOOD), w=1.8)
    s += P('M%s %s L%s %s M%s %s L%s %s' % (f(cx - 14), f(yf + 4), f(cx + 14), f(yf + 4), f(cx - 15), f(yf + 8), f(cx + 15), f(yf + 8)), stroke=WOOD_D, stroke_width=1.2)
    s += ink(R(cx - 19, yf - 8, 4.5, 16, WOOD_D, rx=1.5), R(cx + 14.5, yf - 8, 4.5, 16, WOOD_D, rx=1.5), w=1.4)
    # near stub
    ys = [yn + 4, yn, yn + 6, yn + 1, yn + 7, yn + 1, yn + 5]
    xs = [-22, -15, -7, 2, 9, 16, 22]
    d = 'M' + ' L'.join('%s %s' % (f(cx + xx), f(yy)) for xx, yy in zip(xs, ys)) + ' L%s %s L%s %s Z' % (f(cx + 29), f(H), f(cx - 29), f(H))
    s += ink(P(d, WOOD), w=1.8)
    for k in range(1, 4):
        yy = yn + 6 + k * 6
        if yy < H - 1:
            s += P('M%s %s L%s %s' % (f(cx - 24 - k), f(yy), f(cx + 24 + k), f(yy)), stroke=WOOD_D, stroke_width=1.2)
    s += ink(R(cx - 30, yn + 6, 5, H - yn - 6, WOOD_D, rx=1.5), P('M%s %s L%s %s L%s %s L%s %s Z' % (f(cx + 25), f(H), f(cx + 25), f(yn + 12), f(cx + 31), f(yn + 8), f(cx + 31), f(H)), WOOD_D), w=1.4)
    if hid_n:
        s += hid(cx, yn + (H - yn) / 2.0 + 3, hid_n)
    return s


def ditch_water(y, H):
    s = water(y, H)
    s += P('M0 %s Q20 %s 40 %s T80 %s T120 %s T160 %s T215 %s' % tuple(f(v) for v in (y, y - 3, y, y, y, y, y)), stroke=OUT, stroke_width=1.8)
    return s


def sign(cx, y, n, w=42, h=32, fs=22):
    s = R(cx - w / 2.0, y, w, h, '#ffffff', stroke='#7a4a26', stroke_width=3, rx=4)
    s += R(cx - 3, y - 7, 6, 8, '#7a4a26', stroke=OUT, stroke_width=1)
    s += txt(str(n), cx, y + h * 0.5 + fs * 0.35, fs, DARK)
    return s


def gate_wood(x, y, w, h):
    s = ink(R(x, y, w, h, '#a8703a'), w=2)
    k = 1
    while x + k * 11 < x + w - 1:
        s += P('M%s %s L%s %s' % (f(x + k * 11), f(y + 1), f(x + k * 11), f(y + h - 1)), stroke='#7a4a26', stroke_width=1.2)
        k += 1
    return s


def lock_body(cx, cy, sc=1.0, w=32, h=27, shackle=True):
    s = ''
    if shackle:
        s += P('M%s %s L%s %s Q%s %s %s %s L%s %s' % (f(cx - w * 0.3), f(cy - h / 2), f(cx - w * 0.3), f(cy - h / 2 - 9 * sc),
                                                   f(cx), f(cy - h / 2 - 26 * sc), f(cx + w * 0.3), f(cy - h / 2 - 9 * sc), f(cx + w * 0.3), f(cy - h / 2)),
               stroke=OUT, stroke_width=9 * sc, stroke_linecap='round')
        s += P('M%s %s L%s %s Q%s %s %s %s L%s %s' % (f(cx - w * 0.3), f(cy - h / 2), f(cx - w * 0.3), f(cy - h / 2 - 9 * sc),
                                                   f(cx), f(cy - h / 2 - 26 * sc), f(cx + w * 0.3), f(cy - h / 2 - 9 * sc), f(cx + w * 0.3), f(cy - h / 2)),
               stroke='#d9a05a', stroke_width=5.5 * sc, stroke_linecap='round')
    s += ink(R(cx - w / 2.0, cy - h / 2.0, w, h, BRONZE, rx=5), w=2)
    s += P('M%s %s L%s %s' % (f(cx - w / 2.0 + 4), f(cy - h / 2.0 + 4), f(cx + w / 2.0 - 4), f(cy - h / 2.0 + 4)), stroke='#e8b469', stroke_width=2, stroke_linecap='round')
    return s


def key_shape(sc=1.0):
    k = ink(C(-50, 0, 24, BRONZE), w=2.2) + C(-50, 0, 11, '#fff6dc', stroke=OUT, stroke_width=2.2)
    k += ink(R(-27, -6, 92, 12, BRONZE, rx=3), R(-21, -9, 7, 18, BRONZE_D, rx=2), R(38, 5, 11, 18, BRONZE, rx=2), R(54, 5, 11, 13, BRONZE, rx=2), w=2.2)
    k += P('M-62 -16 Q-52 -22 -42 -16', stroke='#e8b469', stroke_width=2.6, stroke_linecap='round')
    k += P('M-25 -2 L60 -2', stroke='#e8b469', stroke_width=1.6, stroke_linecap='round')
    return k


def small_key(x, y, s=1.0, rot=0):
    return G(key_shape(), transform=xfm(x, y, s, rot))


def drops(pts, col='#9fd0e3'):
    out = ''
    for (x, y, sc) in pts:
        out += P('M0 -6 Q5 1 0 5 Q-5 1 0 -6 Z', col, stroke=OUT, stroke_width=1, transform=xfm(x, y, sc))
    return out


def hearts(pts):
    out = ''
    for (x, y, sc) in pts:
        out += P('M0 4 C-9 -3 -5 -9 0 -4 C5 -9 9 -3 0 4 Z', '#e2573a', stroke=OUT, stroke_width=1, transform=xfm(x, y, sc))
    return out


def dash_ring(cx, cy, rx, ry, col='#d9472f'):
    return E(cx, cy, rx, ry, 'none', stroke=col, stroke_width=2.2, stroke_dasharray='5 3')


def qmark(x, y, sz=22, col='#8a5fb0', rot=0):
    return T('text', '?', x=x, y=y, text_anchor='middle', font_family='Bangers, sans-serif', font_size=sz, fill=col, stroke=OUT, stroke_width=0.8, transform='rotate(%s %s %s)' % (f(rot), f(x), f(y)))


def bang(text, x, y, sz=22, col='#d9472f', rot=0):
    return T('text', text, x=x, y=y, text_anchor='middle', font_family='Bangers, sans-serif', font_size=sz, fill=col, stroke=OUT, stroke_width=0.8, transform='rotate(%s %s %s)' % (f(rot), f(x), f(y)))


def grass_ground(H, ytop, col='#9ac17a'):
    return R(0, ytop, W, H - ytop, col, stroke='none') + P('M0 %s L215 %s' % (f(ytop), f(ytop)), stroke=OUT, stroke_width=1.8)


def becco_wing_belly(x, y, s):
    """gray wings pressed on the belly, world coords"""
    p = wpt(x, y, s)
    a = p(-12, 12)
    b = p(8, 12)
    return (ink(E(a[0], a[1], 9 * s * 1.1, 17 * s * 1.1, '#a4a8b0'), w=1.6, transform='rotate(14 %s %s)' % (f(a[0]), f(a[1])))
            + ink(E(b[0], b[1], 9 * s * 1.1, 17 * s * 1.1, '#a4a8b0'), w=1.6, transform='rotate(-14 %s %s)' % (f(b[0]), f(b[1]))))
