import math, random
from common import *
import l3a as A
import l3b as B


def PLn(d, col, w=1.2, op=1, **k):
    return P(d, 'none', stroke=col, stroke_width=w, opacity=op, stroke_linecap='round', **k)


def LGd(i, stops, x1=0, y1=0, x2=0, y2=1):
    s = ''.join(T('stop', offset=o, stop_color=c, stop_opacity=(op[0] if op else 1)) for o, c, *op in stops)
    return T('linearGradient', s, id=i, x1=x1, y1=y1, x2=x2, y2=y2)


def RGd(i, stops, cx=.5, cy=.5, r=.5):
    s = ''.join(T('stop', offset=o, stop_color=c, stop_opacity=(op[0] if op else 1)) for o, c, *op in stops)
    return T('radialGradient', s, id=i, cx=cx, cy=cy, r=r)


def U(i):
    return 'url(#%s)' % i


SKIES = {
    'day': [(0, '#5fb6e6'), (.45, '#9fd8f0'), (1, '#f3f1d8')],
    'gold': [(0, '#6fb4e0'), (.5, '#f3dc9c'), (1, '#f9b878')],
    'sunset': [(0, '#2f3d78'), (.4, '#b85c7c'), (.75, '#f29a52'), (1, '#f9d27a')],
}
WATS = {
    'day': [(0, '#b4e2e8'), (.5, '#7fc2d4'), (1, '#4f98b8')],
    'gold': [(0, '#f8d49a'), (.35, '#a9cfd6'), (1, '#4f8cb0')],
    'sunset': [(0, '#f7b86a'), (.4, '#b88aa0'), (1, '#41588f')],
}


def lit_defs(p):
    """soft bevel lighting filter for characters/props"""
    flt = T('filter',
            T('feGaussianBlur', **{'in': 'SourceAlpha', 'stdDeviation': '1.6', 'result': 'bl'}) +
            T('feDiffuseLighting', T('feDistantLight', azimuth=235, elevation=52), **{'in': 'bl', 'surfaceScale': '2.6', 'diffuseConstant': '1.12', 'lighting-color': '#ffffff', 'result': 'df'}) +
            T('feComposite', **{'in': 'SourceGraphic', 'in2': 'df', 'operator': 'arithmetic', 'k1': '1.18', 'k2': '0', 'k3': '0', 'k4': '0', 'result': 'sh'}) +
            T('feComposite', **{'in': 'sh', 'in2': 'SourceAlpha', 'operator': 'in'}),
            id=p + 'lit', x='-8%', y='-8%', width='116%', height='116%', color_interpolation_filters='sRGB')
    return flt


def lit(p, *ch):
    return G(*ch, filter=U(p + 'lit'))


def shadow(x, y, rx, ry=None, op=.3):
    return E(x, y, rx, ry or rx * .18, '#1f2a30', stroke='none', opacity=op)


def cloud2(x, y, s=1, op=.95, warm=None):
    base = warm or '#cfe0ea'
    return G(E(0, 5, 47, 9, base, stroke='none', opacity=.7), E(0, 0, 44, 13, '#ffffff', stroke='none'), E(26, -9, 27, 15, '#ffffff', stroke='none'),
             E(-20, -8, 23, 12, '#ffffff', stroke='none'), E(4, -14, 18, 12, '#ffffff', stroke='none'),
             E(2, 6, 40, 6, '#e2edf3', stroke='none', opacity=.8), E(-8, -14, 9, 4, '#ffffff', stroke='none'),
             transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(s)), opacity=op)


def tree_blob(x, yb, h, c1='#5f8a4c', c2='#7fa65a'):
    return G(R(x - 1.2, yb - h * .35, 2.4, h * .35, '#5a3f26', stroke='none'),
             E(x, yb - h * .62, h * .34, h * .4, c1, stroke='none'), E(x - h * .1, yb - h * .72, h * .2, h * .24, c2, stroke='none'),
             E(x + h * .14, yb - h * .52, h * .16, h * .2, c1, stroke='none'))


def far_land(W, hz, seed=1, tone='day', tower=None):
    rnd = random.Random(seed)
    hz_ = {'day': ('#a9c7b0', '#8fb59a', '#6f9a7a'), 'gold': ('#c9c49a', '#a9b88a', '#7f9a6a'), 'sunset': ('#a77a96', '#8a6a8a', '#5f5a80')}[tone]
    s = []
    # hazy hills
    s.append(P('M0 %s Q30 %s 70 %s T140 %s T%s %s L%s %s L0 %s Z' % (f(hz), f(hz - 11), f(hz - 6), f(hz - 8), W, f(hz - 4), W, f(hz + 1), f(hz + 1)), hz_[0], stroke='none', opacity=.8))
    s.append(P('M0 %s Q50 %s 110 %s T%s %s L%s %s L0 %s Z' % (f(hz), f(hz - 6), f(hz - 3), W, f(hz - 5), W, f(hz + 1), f(hz + 1)), hz_[1], stroke='none', opacity=.9))
    x = rnd.uniform(6, 20)
    while x < W:
        s.append(tree_blob(x, hz + 0.6, rnd.uniform(9, 15), hz_[2], hz_[1]))
        x += rnd.uniform(9, 22)
    if tower:
        tx_ = tower
        s.append(G(R(tx_ - 2.2, hz - 20, 4.4, 20, '#c9a58a', stroke='none'), P('M%s %s L%s %s L%s %s Z' % (f(tx_ - 3), f(hz - 20), f(tx_), f(hz - 27), f(tx_ + 3), f(hz - 20)), '#b5562c', stroke='none'),
                   R(tx_ - 1, hz - 17, 2, 4, '#5a3f26', stroke='none'), opacity=.9))
    s.append(R(0, hz - 1, W, 2.5, '#ffffff', stroke='none', opacity=.35))
    return G(*s)


def sail(x, y, s=1, col='#f4e2c0'):
    return G(P('M0 0 L0 -12 L7 -2 Z', col, stroke='none'), P('M-1 0 L-8 -4 L-1 -9 Z', '#e3c690', stroke='none'),
             P('M-9 1 L9 1 L6 4 L-6 4 Z', '#6b4a30', stroke='none'), transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(s)), opacity=.9)


def sky_scene(p, W_, hz, tone='day', sun=None, seed=1, clouds=((.22, .32, .85), (.72, .22, .7), (.5, .48, .5)), tower=None, birds=True, boats=True):
    """returns (defs, body list) sky down to hz plus far land."""
    rnd = random.Random(seed)
    d = LGd(p + 'sk', SKIES[tone]) + RGd(p + 'sg', [(0, '#fff6c8', 1), (.4, '#ffe9a0', .55), (1, '#ffe9a0', 0)])
    b = [R(0, 0, W_, hz + 2, U(p + 'sk'), stroke='none')]
    if sun:
        b.append(C(sun[0], sun[1], 54, U(p + 'sg'), stroke='none'))
        b.append(C(sun[0], sun[1], sun[2], '#fff6c4', stroke='none', opacity=.95))
        b.append(C(sun[0], sun[1], sun[2] * .7, '#ffffff', stroke='none', opacity=.8))
        for k in range(14):
            a = k * math.pi / 7
            b.append(PLn('M%s %s L%s %s' % (f(sun[0] + (sun[2] + 4) * math.cos(a)), f(sun[1] + (sun[2] + 4) * math.sin(a)), f(sun[0] + (sun[2] + 14) * math.cos(a)), f(sun[1] + (sun[2] + 14) * math.sin(a))), '#fff3b0', 1.4, .5))
    for (cx, cy, cs) in clouds:
        b.append(cloud2(W_ * cx, hz * cy, cs, .95, '#f6d9b0' if tone != 'day' else None))
    if birds:
        for (bx, by) in [(W_ * .38, hz * .4), (W_ * .44, hz * .33), (W_ * .84, hz * .5)]:
            b.append(PLn('M%s %s q3 -4 6 0 q3 -4 6 0' % (f(bx), f(by)), '#4a5560', 1.1, .75))
    b.append(far_land(W_, hz, seed, 'day' if tone == 'day' else tone, tower))
    if boats:
        b.append(sail(rnd.uniform(W_ * .55, W_ * .7), hz + 3, .8))
    return d, b


def water_scene(p, W_, hz, gs, tone='day', sun=None, seed=1, ripples=16, refl_land=True):
    rnd = random.Random(seed + 50)
    d = LGd(p + 'wt', WATS[tone])
    b = [R(0, hz, W_, gs - hz + 4, U(p + 'wt'), stroke='none')]
    # soft bands
    for i in range(5):
        y = hz + (gs - hz) * (i + 1) / 6.0
        b.append(P('M0 %s Q%s %s %s %s T%s %s' % (f(y), f(W_ * .25), f(y - 3), f(W_ * .5), f(y), W_, f(y)), 'none', stroke='#ffffff', stroke_width=5, opacity=.10))
    # land reflection
    if refl_land:
        b.append(R(0, hz, W_, 6, '#4f7a6a', stroke='none', opacity=.25))
        for i in range(5):
            b.append(E(rnd.uniform(0, W_), hz + 3, rnd.uniform(14, 40), 1.4, '#3f6a5c', stroke='none', opacity=.3))
    if sun:
        for k in range(7):
            y = hz + 4 + k * (gs - hz) / 8.0
            w = 20 - k * 1.4 + rnd.uniform(-3, 3)
            b.append(R(sun[0] - w / 2 + rnd.uniform(-4, 4), y, w, 1.8, '#fff6c8', stroke='none', opacity=.8 - k * .06, rx=1))
    for i in range(ripples):
        yy = rnd.uniform(hz + 6, gs - 3)
        t = (yy - hz) / max(1, (gs - hz))
        w = 12 + 36 * t + rnd.uniform(-4, 4)
        xx = rnd.uniform(-6, W_ - w + 6)
        b.append(PLn('M%s %s q%s -3.2 %s 0 q%s 3.2 %s 0' % (f(xx), f(yy), f(w / 4), f(w / 2), f(w / 4), f(w / 2)), '#ffffff', 1.5 + t, .85))
        b.append(PLn('M%s %s q%s -3.2 %s 0' % (f(xx + 2), f(yy + 2.6), f(w / 4), f(w / 2)), '#3f86a8', 1, .35))
    b.append(L(0, hz, W_, hz, '#5f94ad', 1, opacity=.8))
    return d, b


def shore(p, W_, H, gs, seed=2, col1='#cdb68a', col2='#a98d62', wet='#8c7752', pebbles=True):
    rnd = random.Random(seed)
    d = LGd(p + 'gr', [(0, col1), (1, col2)])
    top = 'M0 %s Q%s %s %s %s T%s %s T%s %s L%s %s L0 %s Z' % (f(gs), f(W_ * .13), f(gs - 5), f(W_ * .27), f(gs - 1), f(W_ * .55), f(gs - 2), W_, f(gs - 3), W_, H, H)
    b = [P(top, U(p + 'gr'), stroke='none')]
    # wet band + foam
    b.append(P('M0 %s Q%s %s %s %s T%s %s T%s %s L%s %s Q%s %s 0 %s Z' % (f(gs), f(W_ * .13), f(gs - 5), f(W_ * .27), f(gs - 1), f(W_ * .55), f(gs - 2), W_, f(gs - 3), W_, f(gs + 5), f(W_ * .5), f(gs + 9), f(gs + 5)), wet, stroke='none', opacity=.55))
    b.append(P('M0 %s Q%s %s %s %s T%s %s T%s %s' % (f(gs + 1), f(W_ * .13), f(gs - 4), f(W_ * .27), f(gs), f(W_ * .55), f(gs - 1), W_, f(gs - 2)), 'none', stroke='#ffffff', stroke_width=2, opacity=.7))
    b.append(P('M0 %s Q%s %s %s %s T%s %s T%s %s' % (f(gs), f(W_ * .13), f(gs - 5), f(W_ * .27), f(gs - 1), f(W_ * .55), f(gs - 2), W_, f(gs - 3)), 'none', stroke=OUT, stroke_width=2))
    for i in range(int(W_ / 30)):
        b.append(E(rnd.uniform(0, W_), rnd.uniform(gs + 10, H - 3), rnd.uniform(10, 26), rnd.uniform(2, 4.5), '#8c7552', stroke='none', opacity=.35))
    if pebbles:
        for i in range(int(W_ / 7)):
            x = rnd.uniform(0, W_)
            y = rnd.uniform(gs + 6, H - 2)
            r = rnd.uniform(.8, 2.0)
            b.append(E(x, y, r * 1.4, r, rnd.choice(['#e6d9b8', '#b79f78', '#8c7552', '#f1e6cc']), stroke='none', opacity=.8))
    for i in range(int(W_ / 25)):
        x = rnd.uniform(4, W_ - 4)
        y = rnd.uniform(gs + 6, H - 3)
        b.append(PLn('M%s %s q-2 -5 -4 -8 M%s %s l0 -9 M%s %s q2 -5 4 -7' % (f(x), f(y), f(x), f(y), f(x), f(y)), rnd.choice(['#5f8a3c', '#78a048']), 1.4))
    return d, b


def reedbed2(x0, x1, yb, h=46, seed=1, dens=1.0, refl=True):
    rnd = random.Random(seed)
    s = []
    n = int((x1 - x0) / 4.5 * dens)
    cols = ['#4f7a34', '#628f3e', '#7aa44c', '#8db35a', '#3f6a2e']
    items = []
    for i in range(n):
        items.append((rnd.uniform(x0, x1), rnd.uniform(.55, 1.0)))
    items.sort(key=lambda t: t[1])
    for (bx, hf) in items:
        hh = h * hf
        dx = rnd.uniform(-12, 12)
        c = rnd.choice(cols)
        s.append(PLn('M%s %s Q%s %s %s %s' % (f(bx), f(yb), f(bx + dx * .25), f(yb - hh * .6), f(bx + dx), f(yb - hh)), c, 2.2 * hf + .6))
        if rnd.random() < .5:
            s.append(PLn('M%s %s Q%s %s %s %s' % (f(bx + dx * .3), f(yb - hh * .45), f(bx + dx * .3 + 8), f(yb - hh * .6), f(bx + dx * .3 + 11), f(yb - hh * .45 - 12)), '#9ac060', 1.3, .9))
        if rnd.random() < .34:
            s.append(G(E(0, 0, 2.6, 8, '#8a5a2b', stroke=OUT, stroke_width=1), E(-.7, -2, .7, 4, '#c99a5a', stroke='none'), PLn('M0 -8 l0 -5', '#c99a5a', .9),
                       transform='translate(%s %s) rotate(%s)' % (f(bx + dx), f(yb - hh - 5), f(dx * 1.1))))
    if refl:
        for i in range(int((x1 - x0) / 9)):
            x = rnd.uniform(x0, x1)
            s.append(PLn('M%s %s l0 %s' % (f(x), f(yb + 2), f(rnd.uniform(4, 8))), '#3f6a2e', 1.8, .35))
    return G(*s)


def vignette(p, W_, H, strength=.35):
    d = RGd(p + 'vg', [(0, '#000000', 0), (.7, '#1a0d05', 0), (1, '#1a0d05', strength)], .5, .5, .75)
    return d, R(0, 0, W_, H, U(p + 'vg'), stroke='none')


def sparkle4(x, y, r=4, col='#fff6cf', op=.9):
    return P('M%s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Z' % (
        f(x), f(y - r), f(x + r * .15), f(y - r * .15), f(x + r), f(y), f(x + r * .15), f(y + r * .15), f(x), f(y + r), f(x - r * .15), f(y + r * .15), f(x - r), f(y), f(x - r * .15), f(y - r * .15), f(x), f(y - r)),
             col, stroke='none', opacity=op)


def lily(x, y, s=1):
    return G(E(0, 0, 8, 2.8, '#6f9a4a', stroke=OUT, stroke_width=1), E(-1, -.6, 5, 1.4, '#8ab85a', stroke='none'), P('M0 0 L7 -.5', stroke=OUT, stroke_width=.8), transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(s)))


def boat2(x, y, w=150, refl=True, tilt=0, pivot=None):
    """boat with planks, highlights, waterline foam and reflection; origin like B.boat"""
    s = []
    if refl:
        s.append(E(x + w / 2, y + 30, w * .5, 3.5, '#2a5a78', stroke='none', opacity=.35))
        s.append(E(x + w / 2, y + 27, w * .42, 2, '#0f3a55', stroke='none', opacity=.35))
    hull = [B.boat(x, y, w)]
    hull.append(PLn('M%s %s Q%s %s %s %s' % (f(x + 8), f(y + 10), f(x + w / 2), f(y + 19), f(x + w - 8), f(y + 10)), '#6b4426', 1.3, .8))
    hull.append(PLn('M%s %s Q%s %s %s %s' % (f(x + 16), f(y + 16), f(x + w / 2), f(y + 24), f(x + w - 16), f(y + 16)), '#6b4426', 1.2, .6))
    hull.append(PLn('M%s %s Q%s %s %s %s' % (f(x + 5), f(y + 2), f(x + w / 2), f(y + 8.5), f(x + w - 5), f(y + 2)), '#e0b27a', 1.6, .9))
    hull.append(PLn('M%s %s Q%s %s %s %s' % (f(x + 20), f(y + 20), f(x + w / 2), f(y + 29), f(x + w - 20), f(y + 20)), '#2a1a10', 1.8, .22))
    for k in range(int(w / 26)):
        hull.append(PLn('M%s %s l0 6' % (f(x + 18 + k * 26), f(y + 6 + 2 * math.sin(k))), '#7a5030', 1, .5))
    s.append(G(*hull, transform=('rotate(%s %s %s)' % (f(tilt), f(pivot[0]), f(pivot[1]))) if tilt else None))
    s.append(PLn('M%s %s q4 -2.5 8 0 q4 2.5 8 0' % (f(x - 8), f(y + 24)), '#ffffff', 1.8, .9))
    s.append(PLn('M%s %s q4 -2.5 8 0 q4 2.5 8 0' % (f(x + w - 4), f(y + 25)), '#ffffff', 1.8, .9))
    s.append(PLn('M%s %s q6 -3 12 0 q6 3 12 0' % (f(x + w * .35), f(y + 32)), '#ffffff', 1.6, .7))
    return G(*s)


def post(x, yt, yb, h=0, w=5):
    return G(R(x - w / 2, yt, w, yb - yt, '#7a4f2c', stroke=OUT, stroke_width=1.6), R(x - w / 2 + .6, yt + 2, 1.4, yb - yt - 4, '#b98a55', stroke='none', opacity=.8),
             E(x, yt, w / 2, 1.6, '#c99a62', stroke=OUT, stroke_width=1.3))


def barrel(x, y, s=1):
    return G(E(0, 9, 9, 2.5, '#1f2a30', stroke='none', opacity=.3), P('M-8 -9 Q-11 0 -8 9 L8 9 Q11 0 8 -9 Z', '#a8703f', stroke=OUT, stroke_width=1.6), E(0, -9, 8, 2.4, '#c99a62', stroke=OUT, stroke_width=1.4),
             PLn('M-9.5 -3 Q0 0 9.5 -3 M-9.5 4 Q0 7 9.5 4', '#4a4a52', 1.5), PLn('M-4 -8 l0 16', '#d9a96e', 1, .6), transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(s)))


def rope(x1, y1, x2, y2, sag=4):
    return PLn('M%s %s Q%s %s %s %s' % (f(x1), f(y1), f((x1 + x2) / 2), f((y1 + y2) / 2 + sag), f(x2), f(y2)), '#7a5a30', 1.5)


def net(x, y, w, h, rot=0):
    s = [R(0, 0, w, h, '#c9b98a', stroke='none', opacity=.18)]
    for i in range(1, int(w / 5)):
        s.append(PLn('M%s 0 L%s %s' % (f(i * 5), f(i * 5 + 2), f(h)), '#8a6a3a', .8, .9))
    for j in range(1, int(h / 5)):
        s.append(PLn('M0 %s Q%s %s %s %s' % (f(j * 5), f(w / 2), f(j * 5 + 2.5), f(w), f(j * 5)), '#8a6a3a', .8, .9))
    return G(*s, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


def sand_dots2(cx, cy, rx, ry, seed=1, n=12, col='#a8802c'):
    rnd = random.Random(seed)
    s = []
    for i in range(n):
        a = rnd.uniform(0, 6.28)
        r = rnd.uniform(.15, .88)
        s.append(E(cx + rx * r * math.cos(a), cy + ry * r * math.sin(a), rnd.uniform(.8, 1.6), rnd.uniform(.6, 1.0), col, stroke='none', opacity=.8))
    return G(*s)
