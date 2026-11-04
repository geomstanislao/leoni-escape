import sys, json, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/g2611_work')
from common import *
import l3a as A
import l3b as B

SD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/'

WOOD = '#8b5e3a'
SANDY = '#f3dd8a'


def lgd(gid, stops):
    st = ''.join(T('stop', offset='%d%%' % int(o * 100), stop_color=c, stop_opacity=op) for (o, c, op) in stops)
    return T('linearGradient', st, id=gid, x1=0, y1=0, x2=0, y2=1)


def scene(pre, H, hz, gs, sky=None, wat=None, seed=1, gcol='#b79f78', ground=True, far=True, sun=None, ripples=10):
    sky = sky or B.SKY_DAY
    wat = wat or B.WAT
    defs = lgd(pre + 'sk', sky) + lgd(pre + 'wt', wat)
    body = B.lagoon_scene(W, H, hz, gs, pre + 'sk', pre + 'wt', seed, far, True, ripples, sun)
    if ground:
        body += B.ground(W, H, gs, seed + 1, gcol)
    return defs, body


def bric_side(x, yb, h=18, col='#6b4426', w=2.6, tie='#e9c46a'):
    b = [P('M%s %s L%s %s M%s %s L%s %s M%s %s L%s %s' % (f(x - 5), f(yb), f(x - 1), f(yb - h), f(x + 5), f(yb), f(x + 1), f(yb - h), f(x), f(yb), f(x), f(yb - h - 2)),
           stroke=col, stroke_width=w, stroke_linecap='round')]
    b.append(P('M%s %s L%s %s' % (f(x - 3), f(yb - h * 0.6), f(x + 3), f(yb - h * 0.6)), stroke=tie, stroke_width=2.2, stroke_linecap='round'))
    return G(*b)


def sand_dots(cx, cy, rx, ry, seed=1, n=12, col='#a8802c'):
    rnd = random.Random(seed)
    s = []
    for i in range(n):
        a = rnd.uniform(0, 6.28)
        r = rnd.uniform(0.15, 0.85)
        s.append(C(cx + rx * r * math.cos(a), cy + ry * r * math.sin(a), 1.3, col, stroke='none'))
    return G(*s)


def crystal(cx, cy, sc=1.0):
    return P('M%s %s L%s %s L%s %s L%s %s Z' % (f(cx - 4 * sc), f(cy + 3 * sc), f(cx - 1 * sc), f(cy - 4 * sc), f(cx + 3 * sc), f(cy - 3 * sc), f(cx + 5 * sc), f(cy + 3 * sc)),
             '#ffffff', stroke=OUT, stroke_width=1.1, stroke_linejoin='round')


def pool(x, y, w, h, mode, seed=1, cs=1.0):
    s = [R(x, y, w, h, '#a8855a', rx=4, stroke=OUT, stroke_width=2.2)]
    ix, iy, iw, ih = x + 4, y + 4, w - 8, h - 8
    if mode == 'water':
        s.append(R(ix, iy, iw, ih, '#6fb8d2', rx=2, stroke=OUT, stroke_width=1.4))
        s.append(P('M%s %s q5 -3 10 0 q5 3 10 0' % (f(ix + 5), f(iy + ih * 0.35)), stroke='#ffffff', stroke_width=1.8, stroke_linecap='round'))
        s.append(P('M%s %s q5 -3 10 0 q5 3 10 0' % (f(ix + iw * 0.45), f(iy + ih * 0.7)), stroke='#ffffff', stroke_width=1.8, stroke_linecap='round'))
    elif mode == 'half':
        s.append(R(ix, iy, iw, ih, '#d8cfa6', rx=2, stroke=OUT, stroke_width=1.4))
        wy = iy + ih * 0.5
        s.append(P('M%s %s q%s -4 %s 0 t%s 0 L%s %s L%s %s Z' % (f(ix), f(wy), f(iw / 4.0), f(iw / 2.0), f(iw / 2.0), f(ix + iw), f(iy + ih), f(ix), f(iy + ih)), '#8cc9de', stroke=OUT, stroke_width=1.2))
        s.append(P('M%s %s l10 0' % (f(ix + 6), f(wy + ih * 0.22)), stroke='#ffffff', stroke_width=1.8, stroke_linecap='round'))
        s.append(P('M%s %s l12 0 M%s %s l8 0' % (f(ix + 8), f(iy + ih * 0.15), f(ix + iw * 0.55), f(iy + ih * 0.3)), stroke='#b7ac80', stroke_width=1.4, stroke_linecap='round'))
    else:
        s.append(R(ix, iy, iw, ih, '#f6f6f0', rx=2, stroke=OUT, stroke_width=1.4))
        rnd = random.Random(seed)
        gx = max(2, int(iw / (11 * cs)))
        gy_ = max(2, int(ih / (10 * cs)))
        for i in range(gx):
            for j in range(gy_):
                cx = ix + (i + 0.5) * iw / gx + rnd.uniform(-1.5, 1.5)
                cy = iy + (j + 0.55) * ih / gy_ + rnd.uniform(-1.5, 1.5)
                s.append(crystal(cx, cy, 0.8 * cs))
    return G(*s)


def rake(x, y, ln=60):
    """rake with head lying at (x,y), handle going up-right"""
    b = [P('M%s %s L%s %s' % (f(x), f(y), f(x + ln * 0.5), f(y - ln)), stroke=OUT, stroke_width=6, stroke_linecap='round'),
         P('M%s %s L%s %s' % (f(x), f(y), f(x + ln * 0.5), f(y - ln)), stroke='#c99a62', stroke_width=3, stroke_linecap='round'),
         R(x - 13, y - 2, 26, 5, '#c99a62', rx=2, stroke=OUT, stroke_width=1.8)]
    for k in range(5):
        b.append(L(x - 11 + k * 5.5, y + 3, x - 11 + k * 5.5, y + 10, OUT, 2, stroke_linecap='round'))
    return G(*b)


def clothbag(x, y, sc=1.0, crystals=True):
    b = []
    if crystals:
        for (cx, cy, k) in [(-14, -36, 1.5), (-4, -42, 1.7), (7, -40, 1.6), (15, -35, 1.4), (0, -34, 1.5), (-9, -33, 1.4), (10, -33, 1.3)]:
            b.append(crystal(cx, cy, k))
    b.append(P('M-34 40 Q-46 2 -24 -20 L-14 -32 Q0 -27 14 -32 L24 -20 Q46 2 34 40 Q0 46 -34 40 Z', '#e8d9b0'))
    b.append(P('M-26 24 Q-24 4 -14 -8 M26 24 Q24 4 14 -8', stroke='#cdb98a', stroke_width=1.6))
    b.append(P('M-18 22 L-14 18 M-12 30 L-8 26 M14 24 L18 20 M8 32 L12 28', stroke='#b89f6e', stroke_width=1.6))
    b.append(P('M-15 -28 Q0 -22 15 -28 L14 -22 Q0 -16 -14 -22 Z', '#c8483a', stroke_width=2))
    b.append(P('M10 -22 L18 -12 M12 -21 L22 -16', stroke='#c8483a', stroke_width=3))
    return G(*b, stroke=OUT, stroke_width=2.2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def wood_sign(x, y, w, h, num, size=12, post=10):
    return G(R(x + w / 2.0 - 2, y + h, 4, post, WOOD, stroke=OUT, stroke_width=1.6),
             R(x, y, w, h, '#ffffff', rx=3, stroke=OUT, stroke_width=1.8),
             tx(str(num), x + w / 2.0, y + h / 2.0 + size * 0.36, size, '#2a1a10'))


def mud_poles(x, y, ln, rot=0, tip='r', w=13):
    h = w / 2.0
    body = P('M%s %s L%s %s L%s 0 L%s %s L%s %s Z' % (f(-ln / 2.0), f(-h), f(ln / 2.0 - 26), f(-h), f(ln / 2.0), f(ln / 2.0 - 26), f(h), f(-ln / 2.0), f(h)),
             '#a4713f', stroke=OUT, stroke_width=2.2, stroke_linejoin='round')
    bark = P('M%s -2 L%s -2 M%s 3 L%s 3' % (f(-ln / 2.0 + 8), f(ln / 2.0 - 40), f(-ln / 2.0 + 30), f(ln / 2.0 - 30)), stroke='#7a4a22', stroke_width=1.3, stroke_linecap='round')
    tipc = P('M%s %s L%s 0 L%s %s Z' % (f(ln / 2.0 - 10), f(-h * 0.35), f(ln / 2.0), f(ln / 2.0 - 10), f(h * 0.35)), '#d9a96e', stroke='none')
    return G(body, bark, tipc, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


def bez(P0, P1, P2, P3, t):
    u = 1 - t
    x = u ** 3 * P0[0] + 3 * u * u * t * P1[0] + 3 * u * t * t * P2[0] + t ** 3 * P3[0]
    y = u ** 3 * P0[1] + 3 * u * u * t * P1[1] + 3 * u * t * t * P2[1] + t ** 3 * P3[1]
    dx = 3 * u * u * (P1[0] - P0[0]) + 6 * u * t * (P2[0] - P1[0]) + 3 * t * t * (P3[0] - P2[0])
    dy = 3 * u * u * (P1[1] - P0[1]) + 6 * u * t * (P2[1] - P1[1]) + 3 * t * t * (P3[1] - P2[1])
    ln = math.hypot(dx, dy) or 1
    return x, y, -dy / ln, dx / ln




def bric_top(x, y, r=1.0):
    pts = [(x - 3.6 * r, y + 2.4 * r), (x + 3.6 * r, y + 2.4 * r), (x, y - 4 * r)]
    b = [P('M%s %s L%s %s L%s %s Z' % (f(pts[0][0]), f(pts[0][1]), f(pts[1][0]), f(pts[1][1]), f(pts[2][0]), f(pts[2][1])), 'none', stroke='#f4efe0', stroke_width=1.3)]
    for (px, py) in pts:
        b.append(C(px, py, 2.9 * r, '#6b4426', stroke=OUT, stroke_width=1.2))
        b.append(C(px - 0.7, py - 0.7, 0.9, '#d9a96e', stroke='none'))
    return G(*b)


