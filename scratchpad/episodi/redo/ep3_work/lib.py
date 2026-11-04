import math, random

OUT = '#3b2416'
SK = '#fde3c8'


def f(v):
    if isinstance(v, float):
        s = ('%.1f' % v).rstrip('0').rstrip('.')
        return s if s not in ('-0', '') else '0'
    return str(v)


def attrs(kw):
    return ''.join(' %s="%s"' % (k.replace('_', '-'), f(v)) for k, v in kw.items() if v is not None)


def T(name, *ch, **kw):
    return '<%s%s>%s</%s>' % (name, attrs(kw), ''.join(ch), name)


def G(*ch, **kw):
    return T('g', *ch, **kw)


def R(x, y, w, h, fill, **kw):
    return T('rect', x=x, y=y, width=w, height=h, fill=fill, **kw)


def C(cx, cy, r, fill, **kw):
    return T('circle', cx=cx, cy=cy, r=r, fill=fill, **kw)


def E(cx, cy, rx, ry, fill, **kw):
    return T('ellipse', cx=cx, cy=cy, rx=rx, ry=ry, fill=fill, **kw)


def P(d, fill='none', **kw):
    return T('path', d=d, fill=fill, **kw)


def L(x1, y1, x2, y2, stroke, w=2, **kw):
    return T('line', x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke, stroke_width=w, **kw)


def INK(*ch, **kw):
    return G(*ch, stroke=OUT, stroke_width=2.5, stroke_linejoin='round', stroke_linecap='round', **kw)


def star(x, y, r=7, fill='#f4b942'):
    return P('M%s %s L%s %s L%s %s L%s %s L%s %s L%s %s L%s %s L%s %s Z' % (
        f(x), f(y - r), f(x + r * .28), f(y - r * .28), f(x + r), f(y), f(x + r * .28), f(y + r * .28),
        f(x), f(y + r), f(x - r * .28), f(y + r * .28), f(x - r), f(y), f(x - r * .28), f(y - r * .28)), fill)


def cloud(x, y, s=1, op=0.92, col='#ffffff'):
    return G(E(0, 0, 44, 14, col), E(26, -10, 28, 16, col), E(-22, -8, 24, 12, col),
             fill=col, opacity=op, transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(s)))


# ---------------------------------------------------------------- faces
def face(ex, ey, expr='dot', my=None, look=0, sp=7, cheeks=True):
    if my is None:
        my = ey + 11
    by = ey - 9
    out = []
    dark = '#2a1a10'

    def dots():
        return (E(-sp, ey, 3.5, 5, dark, stroke='none') + C(-sp + 1.4, ey - 2, 1.3, '#ffffff', stroke='none') +
                E(sp, ey, 3.5, 5, dark, stroke='none') + C(sp + 1.4, ey - 2, 1.3, '#ffffff', stroke='none'))

    def wide():
        return (C(-sp, ey, 6.5, '#ffffff', stroke_width=2) + C(-sp + look, ey, 2, dark, stroke='none') +
                C(sp, ey, 6.5, '#ffffff', stroke_width=2) + C(sp + look, ey, 2, dark, stroke='none'))

    if cheeks:
        out.append(C(-sp - 7, ey + 8, 4, '#f6a99a', fill_opacity=0.6, stroke='none'))
        out.append(C(sp + 7, ey + 8, 4, '#f6a99a', fill_opacity=0.6, stroke='none'))
    if expr == 'dot':
        out.append(dots())
        out.append(P('M-6 %s Q0 %s 6 %s Z' % (f(my - 2), f(my + 9), f(my - 2)), '#a8453a', stroke_width=2))
    elif expr == 'smile':
        out.append(dots())
        out.append(P('M-6 %s Q0 %s 6 %s' % (f(my - 1), f(my + 6), f(my - 1)), stroke_width=2.2))
    elif expr == 'wow':
        out.append(wide())
        out.append(P('M-%s %s L-4 %s M%s %s L4 %s' % (f(sp + 6), f(by - 1), f(by - 4), f(sp + 6), f(by - 1), f(by - 4)), stroke_width=2.2))
        out.append(E(0, my, 7, 9, '#a8453a', stroke_width=2))
        out.append(E(0, my + 5, 4, 3, '#e8837a', stroke='none'))
    elif expr == 'sad':
        out.append(dots())
        out.append(P('M-%s %s L-4 %s M%s %s L4 %s' % (f(sp + 6), f(by + 2), f(by - 2), f(sp + 6), f(by + 2), f(by - 2)), stroke_width=2.2))
        out.append(P('M-5 %s Q0 %s 5 %s' % (f(my + 3), f(my - 3), f(my + 3)), stroke_width=2.2))
        out.append(P('M%s %s Q%s %s %s %s' % (f(sp + 3), f(ey + 5), f(sp + 5), f(ey + 11), f(sp + 2), f(ey + 15)), '#bfe3f2', stroke_width=1.5))
    elif expr == 'det':
        out.append(dots())
        out.append(P('M-%s %s L-4 %s M%s %s L4 %s' % (f(sp + 6), f(by - 3), f(by + 1), f(sp + 6), f(by - 3), f(by + 1)), stroke_width=2.6))
        out.append(P('M-7 %s Q0 %s 7 %s Z' % (f(my - 2), f(my + 8), f(my - 2)), '#a8453a', stroke_width=2))
    elif expr == 'worry':
        out.append(wide())
        out.append(P('M-%s %s L-4 %s M%s %s L4 %s' % (f(sp + 6), f(by + 2), f(by - 3), f(sp + 6), f(by + 2), f(by - 3)), stroke_width=2.2))
        out.append(P('M-5 %s Q-2 %s 0 %s Q2 %s 5 %s' % (f(my + 3), f(my), f(my + 3), f(my + 6), f(my + 3)), stroke_width=2.2))
    elif expr == 'happy':
        out.append(P('M-%s %s Q-%s %s -%s %s M%s %s Q%s %s %s %s' % (f(sp + 5), f(ey + 1), f(sp), f(ey - 7), f(sp - 5), f(ey + 1),
                                                                      f(sp - 5), f(ey + 1), f(sp), f(ey - 7), f(sp + 5), f(ey + 1)), stroke_width=2.6))
        out.append(P('M-7 %s Q0 %s 7 %s Z' % (f(my - 2), f(my + 10), f(my - 2)), '#a8453a', stroke_width=2))
    return G(*out)


# ---------------------------------------------------------------- limbs
def limb(x1, y1, x2, y2, col, w=15, hand=SK, hr=6.5):
    d = 'M%s %s L%s %s' % (f(x1), f(y1), f(x2), f(y2))
    s = P(d, stroke=OUT, stroke_width=w) + P(d, stroke=col, stroke_width=w - 5)
    if hand:
        s += C(x2, y2, hr, hand)
    return s


def legs(top, run, col, w=15, foot=None, shoe='#9a6338', bot=54, fy=58):
    if run:
        a = (-8, top, -14 - run, bot - 2)
        b = (8, top, 12 + run, bot - 8)
        fa = (-14 - run - 2, bot + 2)
        fb = (12 + run + 2, bot - 4)
    else:
        a = (-8, top, -10, bot)
        b = (8, top, 10, bot)
        fa = (-12, fy)
        fb = (12, fy)
    s = limb(a[0], a[1], a[2], a[3], col, w, hand=None) + limb(b[0], b[1], b[2], b[3], col, w, hand=None)
    s += E(fa[0], fa[1], 9, 5, shoe) + E(fb[0], fb[1], 9, 5, shoe)
    return s


def xf(x, y, s, rot=0, flip=False):
    return 'translate(%s %s) rotate(%s) scale(%s %s)' % (f(x), f(y), f(rot), f(-s if flip else s), f(s))


# ---------------------------------------------------------------- Nico
def nico(x, y, s=1, rot=0, la=(-24, 16), ra=(24, 16), expr='dot', look=0, run=0, flip=False, pack=True):
    b = []
    b.append(legs(22, run, '#4f74a8', 15))
    if pack:
        b.append(R(-28, -16, 14, 34, '#efdcb4', rx=4))
        b.append(P('M-26 18 L-32 34 L-24 36 L-20 20 Z', '#e9a94a'))
    b.append(limb(-14, -12, la[0], la[1], '#e2573a'))
    b.append(limb(14, -12, ra[0], ra[1], '#e2573a'))
    b.append(P('M-18 22 L-16 -16 Q0 -26 16 -16 L18 22 Z', '#e2573a'))
    b.append(C(0, -36, 20, SK))
    b.append(P('M-21 -38 L-24 -56 L-12 -48 L-10 -64 L0 -52 L8 -66 L12 -50 L24 -56 L21 -38 Q0 -50 -21 -38 Z', '#7a4a26'))
    b.append(face(0, -34, expr, my=-23, look=look))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- Sofia
def sofia(x, y, s=1, rot=0, la=(-24, 16), ra=(24, 16), expr='dot', look=0, run=0, flip=False):
    b = []
    if run:
        b.append(limb(-8, 40, -14 - run, 62, SK, 13, hand=None) + limb(8, 40, 12 + run, 56, SK, 13, hand=None))
        b.append(E(-16 - run, 66, 9, 5, '#9a6338') + E(14 + run, 60, 9, 5, '#9a6338'))
    else:
        b.append(limb(-8, 40, -10, 64, SK, 13, hand=None) + limb(8, 40, 10, 64, SK, 13, hand=None))
        b.append(E(-12, 67, 9, 5, '#9a6338') + E(12, 67, 9, 5, '#9a6338'))
    b.append(limb(-14, -12, la[0], la[1], '#f2c043'))
    b.append(limb(14, -12, ra[0], ra[1], '#f2c043'))
    b.append(P('M-16 16 L-32 42 L32 42 L16 16 Z', '#8a7a6a'))
    b.append(P('M-17 18 L-15 -16 Q0 -26 15 -16 L17 18 Z', '#f2c043'))
    b.append(C(0, -2, 2, '#b8862a', stroke='none') + C(0, 8, 2, '#b8862a', stroke='none'))
    b.append(P('M14 -50 Q36 -38 31 -12', stroke=OUT, stroke_width=14) + P('M14 -50 Q36 -38 31 -12', stroke='#5e381c', stroke_width=9))
    b.append(C(31, -9, 4.5, '#f2c043'))
    b.append(C(0, -38, 23, '#7a4a26'))
    b.append(C(0, -36, 19, SK))
    b.append(P('M-20 -38 Q-18 -56 0 -56 Q18 -56 20 -38 Q10 -48 0 -48 Q-10 -48 -20 -38 Z', '#7a4a26'))
    b.append(face(0, -35, expr, my=-24, look=look))
    b.append(C(-7, -35, 7, 'none', stroke_width=2) + C(7, -35, 7, 'none', stroke_width=2) + P('M-0.5 -35 Q0 -37 0.5 -35', stroke_width=2))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- Toni
def toni(x, y, s=1, rot=0, la=(-30, -30), ra=(30, -30), expr='dot', look=0, run=0, flip=False, bend=0, target=None):
    b = []
    if run:
        b.append(limb(-8, 24, -14 - run, 54, SK, 14, hand=None) + limb(8, 24, 12 + run, 48, SK, 14, hand=None))
        b.append(E(-16 - run, 58, 9, 5, '#9a6338') + E(14 + run, 52, 9, 5, '#9a6338'))
    else:
        b.append(limb(-12, 24, -12, 50, SK, 14, hand=None) + limb(12, 24, 12, 50, SK, 14, hand=None))
        b.append(E(-14, 54, 9, 5, '#9a6338') + E(14, 54, 9, 5, '#9a6338'))
    up = []
    if bend and target:
        th = math.radians(-bend)
        tx, ty = target[0], target[1] - 24
        lx = tx * math.cos(th) - ty * math.sin(th)
        ly = tx * math.sin(th) + ty * math.cos(th) + 24
        ra = (lx, ly)
        la = (lx - 14, ly - 4)
    up.append(limb(-24, -16, la[0], la[1], '#fbfaf4', 16, hr=7))
    up.append(limb(24, -16, ra[0], ra[1], '#fbfaf4', 16, hr=7))
    up.append(R(-26, 14, 52, 16, '#4a3426', rx=5))
    up.append(P('M-28 18 Q-33 -10 -23 -22 Q0 -32 23 -22 Q33 -10 28 18 Z', '#fbfaf4'))
    up.append(G(L(-30, -8, 30, -8, '#6f8fc4', 4), L(-31, 2, 31, 2, '#6f8fc4', 4), L(-30, 11, 30, 11, '#6f8fc4', 4)))
    up.append(P('M-28 18 Q-33 -10 -23 -22 Q0 -32 23 -22 Q33 -10 28 18 Z'))
    up.append(P('M-10 -24 L0 -10 L10 -24 Z', '#d9472f'))
    up.append(C(0, -44, 23, SK))
    up.append(P('M-23 -46 Q-22 -62 0 -64 Q22 -62 23 -46 Q12 -56 0 -56 Q-12 -56 -23 -46 Z', '#4a3020'))
    up.append(face(0, -42, expr, my=-31, look=look, sp=8))
    up.append(G(P('M-17 0 Q-16 -26 0 -28 Q16 -26 17 0 Z', '#e9c46a'), E(0, 0, 40, 9, '#e9c46a'),
                P('M-16 -8 Q0 -13 16 -8 L17 0 Q0 -5 -17 0 Z', '#d9472f'),
                P('M-32 0 Q-30 6 -20 8 M32 0 Q30 6 20 8', stroke='#c9952e', stroke_width=1.2),
                transform='translate(0 -60) rotate(-4)'))
    if bend:
        b.append(G(*up, transform='rotate(%s 0 24)' % f(bend)))
    else:
        b.extend(up)
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- Tito
TUN = '#f3ecdc'
TSK = '#f0cfa8'


def tito(x, y, s=1, rot=0, la=(-24, 16), ra=(24, 16), expr='dot', look=0, run=0, flip=False, front=False):
    s = s * 1.05
    b = []
    if run:
        b.append(limb(-7, 36, -13 - run, 56, TSK, 12, hand=None) + limb(7, 36, 12 + run, 50, TSK, 12, hand=None))
        b.append(E(-15 - run, 59, 9, 4, '#7a4a26') + E(14 + run, 53, 9, 4, '#7a4a26'))
    else:
        b.append(limb(-7, 36, -8, 56, TSK, 12, hand=None) + limb(7, 36, 8, 56, TSK, 12, hand=None))
        b.append(E(-10, 59, 9, 4, '#7a4a26') + E(10, 59, 9, 4, '#7a4a26'))
    arms_ = limb(-14, -12, la[0], la[1], TUN, 14, hand=TSK) + limb(14, -12, ra[0], ra[1], TUN, 14, hand=TSK)
    if not front:
        b.append(arms_)
    b.append(P('M-17 -16 Q0 -26 17 -16 L21 40 L-21 40 Z', TUN))
    b.append(P('M-20.5 34 L20.5 34 L21 40 L-21 40 Z', '#c8483a', stroke_width=1.5))
    b.append(R(-18.5, 12, 37, 5, '#8a5a2b', rx=2))
    b.append(C(5, 14.5, 3.5, '#8a5a2b', stroke_width=1.5) + P('M5 17 L2 27 M5 17 L9 26', stroke='#8a5a2b', stroke_width=2.4))
    if front:
        b.append(arms_)
    b.append(C(0, -36, 20, TSK))
    b.append(P('M-21 -34 Q-24 -58 0 -60 Q24 -58 21 -34 Q12 -46 0 -45 Q-12 -46 -21 -34 Z', '#2a1f1a'))
    for cx, cy, r in [(-15, -50, 8), (-6, -57, 8), (5, -58, 8), (15, -51, 8), (-21, -41, 6), (21, -41, 6), (0, -50, 7)]:
        b.append(C(cx, cy, r, '#2a1f1a', stroke_width=1.8))
    b.append(face(0, -34, expr, my=-23, look=look))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- Leo
WING_OPEN = ('M-14 -2 C-31.4 -34.8 -56.9 -37.7 -67.8 -19.5 Q-75.1 -5.3 -61.7 -0.9 Q-66 12.5 -52.2 12.2 Q-53.7 24.9 -39.5 19.8 Q-38 31.8 -24.2 25.3 Q-15.5 16.9 -14 -2 Z',
             'M-61.7 -0.9 Q-46.7 -9.3 -30.7 -7.1 M-52.2 12.2 Q-40.2 4.5 -24.9 3.8 M-39.5 19.8 Q-31.5 14.7 -22.7 12.5')
WING_SMALL = ('M-14 -2 C-20 -26 -36 -32 -46 -22 Q-53 -14 -45 -9 Q-50 -1 -41 1 Q-44 9 -34 8 Q-35 16 -25 14 Q-18 10 -14 -2 Z',
              'M-45 -9 Q-34 -12 -24 -8 M-41 1 Q-32 -2 -22 0 M-34 8 Q-28 6 -22 6')


def leo(x, y, s=1, rot=0, wing='small', la=(-34, 22), ra=(34, 22), eyes='open', mouth='smile', flip=False, shh=False):
    wp = WING_OPEN if wing == 'open' else WING_SMALL
    b = []
    b.append(E(0, -70, 21, 6.5, 'none', stroke='#fff2b8', stroke_width=10, opacity=0.6))
    one = P(wp[0], '#f4c64e') + P(wp[1], stroke='#d99a2b', stroke_width=1.4)
    b.append(one)
    b.append(G(one, transform='scale(-1 1)'))
    b.append(P('M20 28 Q54 30 50 -2', stroke=OUT, stroke_width=10) + P('M20 28 Q54 30 50 -2', stroke='#f4c64e', stroke_width=5))
    b.append(E(50, -8, 7, 9, '#e39a3b'))
    b.append(E(-12, 40, 10, 7, '#f4c64e') + E(12, 40, 10, 7, '#f4c64e'))
    b.append(E(0, 12, 24, 28, '#f4c64e'))
    b.append(E(0, 16, 13, 19, '#fff3d0', stroke='none'))
    b.append(limb(-18, 4, la[0], la[1], '#f4c64e', 16, hand='#f4c64e', hr=7))
    if not shh:
        b.append(limb(18, 4, ra[0], ra[1], '#f4c64e', 16, hand='#f4c64e', hr=7))
    b.append(C(0, -28, 34, '#e39a3b'))
    for cx, cy in [(33, -28), (26.7, -8.6), (10.2, 3.4), (-10.2, 3.4), (-26.7, -8.6), (-33, -28), (-26.7, -47.4), (-10.2, -59.4), (10.2, -59.4), (26.7, -47.4)]:
        b.append(C(cx, cy, 11, '#e39a3b'))
    b.append(C(0, -28, 31, '#e39a3b', stroke='none'))
    b.append(C(-24, -52, 8, '#f4c64e') + C(24, -52, 8, '#f4c64e') + C(-24, -52, 4, '#e39a3b', stroke='none') + C(24, -52, 4, '#e39a3b', stroke='none'))
    b.append(C(0, -26, 25, '#f4c64e'))
    b.append(E(0, -70, 21, 6.5, 'none', stroke='#f4b942', stroke_width=3.2))
    if eyes == 'open':
        b.append(E(-10, -28, 5.5, 7.5, '#2a1a10', stroke='none') + C(-11.5, -31, 2.2, '#ffffff', stroke='none') + C(-8, -26, 1.1, '#ffffff', stroke='none'))
        b.append(E(10, -28, 5.5, 7.5, '#2a1a10', stroke='none') + C(8.5, -31, 2.2, '#ffffff', stroke='none') + C(12, -26, 1.1, '#ffffff', stroke='none'))
    elif eyes == 'proud':
        b.append(E(-10, -28, 5.5, 7.5, '#2a1a10', stroke='none') + C(-11.5, -31, 2.2, '#ffffff', stroke='none'))
        b.append(E(10, -28, 5.5, 7.5, '#2a1a10', stroke='none') + C(8.5, -31, 2.2, '#ffffff', stroke='none'))
        b.append(P('M-17 -37 L-4 -35 M17 -37 L4 -35', stroke_width=2.5))
    else:
        b.append(P('M-16 -28 Q-10 -35 -4 -28 M4 -28 Q10 -35 16 -28', stroke_width=2.6))
    b.append(C(-18, -17, 4, '#f6a99a', fill_opacity=0.6, stroke='none') + C(18, -17, 4, '#f6a99a', fill_opacity=0.6, stroke='none'))
    b.append(E(0, -14, 11, 8, '#fff3d0', stroke='none'))
    b.append(P('M-4 -19 L4 -19 L0 -14.5 Z', '#a8453a', stroke_width=1.5))
    if mouth == 'smile':
        b.append(P('M0 -14.5 L0 -12 M-7 -12 Q-3.5 -6 0 -12 Q3.5 -6 7 -12', stroke_width=2))
    elif mouth == 'oh':
        b.append(P('M0 -14.5 L0 -12', stroke_width=2) + E(0, -7, 4.5, 5.5, '#a8453a', stroke_width=2))
    if shh:
        b.append(limb(17, 0, 8, -9, '#f4c64e', 16, hand='#f4c64e', hr=7))
    return INK(*b, transform=xf(x, y, s, rot, flip))


# ---------------------------------------------------------------- Becco (profile, faces left)
def becco(x, y, s=1, rot=0, flip=False, wings='down', scroll=False, legs_on=True, bundle=False):
    b = []
    if legs_on:
        b.append(P('M-8 34 L-10 52 M10 34 L10 52', stroke='#f08a24', stroke_width=4))
        b.append(P('M-10 52 L-19 56 M-10 52 L-8 58 M-10 52 L-2 56 M10 52 L1 56 M10 52 L12 58 M10 52 L18 56', stroke='#f08a24', stroke_width=3))
    if bundle:
        b.append(scroll_el(-2, 50, 62, -8) + scroll_el(2, 56, 60, 6) + scroll_el(-6, 46, 58, 14))
    wg = 'M-22 -20 Q-54 0 -42 40 Q-30 32 -22 22 Z'
    if wings == 'up':
        wl = G(P(wg, '#a4a8b0'), transform='rotate(100 -22 -14)')
        wr = G(G(P(wg, '#a4a8b0'), transform='rotate(100 -22 -14)'), transform='scale(-1 1)')
    else:
        wl = P(wg, '#a4a8b0')
        wr = G(P(wg, '#a4a8b0'), transform='scale(-1 1)')
    b.append(wl)
    b.append(wr)
    b.append(E(0, 0, 28, 36, '#b9bcc2'))
    b.append(E(-2, 8, 19, 28, '#ffffff', stroke='none'))
    b.append(P('M-7 4 L3 16 M3 4 L-7 16', stroke='#a8453a', stroke_width=2.6))
    b.append(C(0, -44, 22, '#fafaf7'))
    b.append(P('M-16 -49 L-46 -41 L-16 -38 Z', '#f08a24'))
    b.append(P('M-16 -38 L-40 -36 L-16 -31 Z', '#e0731a'))
    b.append(P('M-14 -36 Q-18 -29 -9 -31', stroke_width=2))
    b.append(C(-6, -50, 5.5, '#ffe08a', stroke_width=2))
    b.append(C(-8, -50, 2.4, '#2a1a10', stroke='none'))
    b.append(P('M-14 -58 L1 -53', stroke_width=3))
    b.append(P('M-23 -58 Q-25 -80 0 -83 Q25 -80 23 -58 Z', '#ffffff'))
    b.append(P('M-23 -65 Q0 -59 23 -65 L22.5 -57 Q0 -51 -22.5 -57 Z', '#1f2f5a'))
    b.append(P('M-24 -56 Q-40 -54 -45 -48 Q-30 -47 -20 -51 Z', '#1f2f5a'))
    b.append(C(0, -61, 4.2, '#e9c46a', stroke_width=1.5))
    if scroll:
        b.append(scroll_el(-52, -38, 44, -6))
    return INK(*b, transform=xf(x, y, s, rot, flip))


def scroll_el(x, y, ln=40, rot=0, col='#f1e2b8', tied=True):
    h = ln / 2.0
    b = [R(-h, -6, ln, 12, col, rx=5), E(-h, 0, 3.5, 6, '#d9c08a'), E(h, 0, 3.5, 6, '#d9c08a')]
    b.append(P('M%s -3 L%s 3 M%s 0 L%s 0' % (f(-h + 8), f(-h + 8), f(-h + 12), f(h - 12)), stroke='#c9a96a', stroke_width=1.2))
    if tied:
        b.append(R(-3, -7, 6, 14, '#c8483a', stroke_width=1.5))
        b.append(P('M0 7 L-4 12 M0 7 L4 12', stroke='#c8483a', stroke_width=2))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


# ---------------------------------------------------------------- Roman scenery
def paving(x, y, w, h, rh=18, cw=34, col='#cdbf9f', line='#a89874', seed=1):
    rnd = random.Random(seed)
    s = [R(x, y, w, h, col)]
    n = int(h / rh) + 1
    for i in range(n):
        yy = y + i * rh
        s.append(L(x, yy, x + w, yy, line, 1.6))
        off = (i % 2) * cw / 2.0
        xx = x + off
        while xx < x + w:
            if yy + rh <= y + h + 1:
                s.append(L(xx, yy, xx, yy + rh, line, 1.4))
            xx += cw * (0.85 + 0.3 * rnd.random())
    return G(*s)


def roof(x, y, w, rh, col='#c8683f', line='#a14f2c', inset=14):
    s = [P('M%s %s L%s %s L%s %s L%s %s Z' % (f(x - 6), f(y), f(x + w + 6), f(y), f(x + w - inset), f(y - rh), f(x + inset), f(y - rh)), col, stroke=OUT, stroke_width=2, stroke_linejoin='round')]
    n = max(2, int(rh / 7))
    for i in range(1, n):
        t = i / float(n)
        yy = y - rh * t
        xl = x - 6 + (inset + 6) * t
        xr = x + w + 6 - (inset + 6) * t
        s.append(L(xl, yy, xr, yy, line, 1.3))
    return G(*s)


def house(x, yb, w, h, wall='#e8d5b0', rcol='#c8683f', rh=None, door=True, win=True, seed=2, shut='#8b5a35'):
    rh = rh or h * 0.45
    s = [R(x, yb - h, w, h, wall, stroke=OUT, stroke_width=2)]
    s.append(L(x + 2, yb - h * 0.5, x + w - 2, yb - h * 0.5, '#c9b58a', 1.2))
    s.append(L(x + w * 0.5, yb - h + 2, x + w * 0.5, yb - h * 0.5, '#c9b58a', 1.2))
    if door:
        s.append(R(x + w * 0.5 - 7, yb - 24, 14, 24, '#6b4428', stroke=OUT, stroke_width=1.8, rx=7 if False else 0))
    if win and w > 60:
        s.append(R(x + 10, yb - h + 12, 14, 18, '#3a2a22', stroke=OUT, stroke_width=1.8))
        s.append(R(x + w - 24, yb - h + 12, 14, 18, '#3a2a22', stroke=OUT, stroke_width=1.8))
    s.append(roof(x, yb - h, w, rh, rcol))
    return G(*s)


def temple(x, yb, w, h, stone='#f1e6cf', shade='#d9c9a6'):
    s = []
    s.append(R(x - 10, yb - 8, w + 20, 8, shade, stroke=OUT, stroke_width=1.8))
    s.append(R(x - 4, yb - 16, w + 8, 8, stone, stroke=OUT, stroke_width=1.8))
    n = 6
    cw = 8
    colh = h - 16 - 14 - 26
    for i in range(n):
        cx = x + 6 + i * (w - 12 - cw) / float(n - 1)
        s.append(R(cx, yb - 16 - colh, cw, colh, stone, stroke=OUT, stroke_width=1.6))
        s.append(L(cx + 3, yb - 16 - colh + 2, cx + 3, yb - 18, shade, 1.2))
        s.append(R(cx - 2, yb - 16 - colh - 3, cw + 4, 4, shade, stroke=OUT, stroke_width=1.2))
    s.append(R(x - 2, yb - 16 - colh - 14, w + 4, 11, stone, stroke=OUT, stroke_width=1.8))
    s.append(P('M%s %s L%s %s L%s %s Z' % (f(x - 8), f(yb - 16 - colh - 14), f(x + w + 8), f(yb - 16 - colh - 14), f(x + w / 2.0), f(yb - h)), '#e6d3ab', stroke=OUT, stroke_width=2))
    s.append(P('M%s %s L%s %s L%s %s Z' % (f(x + 14), f(yb - 16 - colh - 17), f(x + w - 14), f(yb - 16 - colh - 17), f(x + w / 2.0), f(yb - h + 8)), '#c8683f', stroke='none'))
    return G(*s)


def bridge(x1, x2, yd, hd, yw, n, stone='#d9c7a0', wat='#4a9aa8', line='#a89874'):
    s = []
    wid = (x2 - x1) / float(n)
    s.append(R(x1, yd + hd, x2 - x1, yw - yd - hd, stone, stroke=OUT, stroke_width=2.4))
    r = wid * 0.36
    ya = yw - r * 1.3
    for i in range(n):
        cx = x1 + wid * (i + 0.5)
        s.append(P('M%s %s L%s %s A%s %s 0 0 1 %s %s L%s %s Z' % (f(cx - r), f(yw), f(cx - r), f(ya), f(r), f(r), f(cx + r), f(ya), f(cx + r), f(yw)), wat, stroke=OUT, stroke_width=2.4))
        for k in range(7):
            ang = math.pi * (k + 0.5) / 7
            s.append(L(cx - (r + 1) * math.cos(ang), ya - (r + 1) * math.sin(ang), cx - (r + 9) * math.cos(ang), ya - (r + 9) * math.sin(ang), line, 1.4))
    s.append(R(x1 - 6, yd, x2 - x1 + 12, hd, '#e6d6b0', stroke=OUT, stroke_width=2.4))
    s.append(R(x1 - 6, yd - 8, x2 - x1 + 12, 8, '#cdb98e', stroke=OUT, stroke_width=2))
    xx = x1
    while xx < x2:
        s.append(L(xx, yd - 8, xx, yd, line, 1.2))
        xx += 22
    return G(*s)


def amphora(x, y, sc=1, col='#c47a45'):
    body = P('M0 0 Q-12 -10 -12 -26 Q-12 -38 -5 -42 L-5 -50 L5 -50 L5 -42 Q12 -38 12 -26 Q12 -10 0 0 Z', col)
    lip = E(0, -50, 7, 2.6, '#a85d2f')
    hd = P('M-5 -47 Q-17 -46 -11 -33 M5 -47 Q17 -46 11 -33', stroke_width=2.4)
    band = P('M-11 -30 Q0 -26 11 -30', stroke='#a85d2f', stroke_width=1.8)
    return G(hd, body, band, lip, stroke=OUT, stroke_width=2, stroke_linejoin='round', stroke_linecap='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def sack(x, y, sc=1, col='#e0cfa0'):
    return G(P('M-14 0 Q-18 -14 -10 -24 L-4 -28 L4 -28 L10 -24 Q18 -14 14 0 Z', col), P('M-4 -28 Q0 -24 4 -28', stroke_width=1.8),
             stroke=OUT, stroke_width=2, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(y), f(sc)))


def barge(x, y, w, cargo=True, sc=1.0, seed=3):
    rnd = random.Random(seed)
    s = []
    if cargo:
        xx = x + 22
        while xx < x + w - 20:
            if rnd.random() < 0.6:
                s.append(amphora(xx, y + 3, 0.9 * sc, rnd.choice(['#c47a45', '#b8683a', '#d08a52'])))
                xx += 18 * sc
            else:
                s.append(sack(xx, y + 3, 0.9 * sc))
                xx += 26 * sc
    s.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(x), f(y), f(x + w), f(y), f(x + w - 18), f(y + 24 * sc), f(x + 18), f(y + 24 * sc)), '#8b5a35', stroke=OUT, stroke_width=2.4, stroke_linejoin='round'))
    s.append(P('M%s %s L%s %s' % (f(x + 6), f(y + 8 * sc), f(x + w - 6), f(y + 8 * sc)), stroke='#6e3a1c', stroke_width=1.8))
    return G(*s)


def cypress(x, yb, h=60, w=14):
    return G(R(x - 1.5, yb - 8, 3, 8, '#6e4a2c', stroke='none'), E(x, yb - 8 - h / 2.0, w / 2.0, h / 2.0, '#5a7a45', stroke=OUT, stroke_width=1.8))


def roman(x, yb, sc=1, col='#d1a85a', flip=False, hair='#3a2a20', arms='down', carry=None):
    b = []
    b.append(limb(-5, -8, -6, 0, SK, 8, hand=None) + limb(5, -8, 6, 0, SK, 8, hand=None))
    b.append(E(-6, 1, 5, 2.5, '#7a4a26') + E(6, 1, 5, 2.5, '#7a4a26'))
    b.append(P('M-9 -34 Q0 -40 9 -34 L11 -10 L-11 -10 Z', col))
    b.append(L(-10.5, -13, 10.5, -13, '#8b4a30', 2))
    if arms == 'up':
        b.append(limb(-8, -32, -16, -44, col, 6, hand=SK, hr=3.5) + limb(8, -32, 16, -44, col, 6, hand=SK, hr=3.5))
    elif arms == 'carry':
        b.append(limb(-8, -32, -10, -22, col, 6, hand=SK, hr=3.5) + limb(8, -32, 10, -22, col, 6, hand=SK, hr=3.5))
    else:
        b.append(limb(-9, -33, -13, -20, col, 6, hand=SK, hr=3.5) + limb(9, -33, 13, -20, col, 6, hand=SK, hr=3.5))
    b.append(C(0, -45, 8, SK))
    b.append(P('M-8 -46 Q-8 -54 0 -54 Q8 -54 8 -46 Q3 -50 0 -50 Q-4 -50 -8 -46 Z', hair))
    b.append(C(-2.6, -45, 1.1, '#2a1a10', stroke='none') + C(2.6, -45, 1.1, '#2a1a10', stroke='none'))
    return G(*b, stroke=OUT, stroke_width=1.8, stroke_linejoin='round', stroke_linecap='round', transform=xf(x, yb, sc, 0, flip))


def stall(x, yb, w, h=90, cloths=None):
    s = []
    posts = [R(x, yb - h, 6, h, '#8b5a35'), R(x + w - 6, yb - h, 6, h, '#8b5a35')]
    s.extend(posts)
    s.append(R(x - 4, yb - 40, w + 8, 40, '#b9783f', stroke=OUT, stroke_width=2.2))
    cl = cloths or ['#e2573a', '#4f74a8', '#f2c043', '#7fa05a', '#b86aa0', '#fbfaf4', '#d98a3a']
    n = len(cl)
    cwd = (w - 8) / float(n)
    for i, c in enumerate(cl):
        cx = x + 4 + i * cwd
        for k in range(3):
            s.append(R(cx, yb - 40 - 10 * (k + 1) - (i % 2) * 3, cwd - 3, 11, c, rx=3, stroke=OUT, stroke_width=1.8))
        s.append(L(cx + 3, yb - 52, cx + cwd - 8, yb - 52, '#ffffff', 1.4, opacity=0.6))
    nst = 8
    sw = (w + 16) / float(nst)
    for i in range(nst):
        c = '#e2573a' if i % 2 == 0 else '#fbfaf4'
        s.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(x - 8 + i * sw), f(yb - h - 14), f(x - 8 + (i + 1) * sw), f(yb - h - 14), f(x - 11 + (i + 1) * sw), f(yb - h + 12), f(x - 11 + i * sw), f(yb - h + 12)), c, stroke=OUT, stroke_width=2))
    return G(*s)


def pot(x, yb, sc=1):
    return G(P('M-9 0 L-11 -14 L11 -14 L9 0 Z', '#c8683f'), R(-12, -17, 24, 4, '#a8502e'),
             C(-5, -24, 6, '#6a9a4a'), C(5, -26, 6, '#7fb05a'), C(0, -32, 6, '#6a9a4a'),
             stroke=OUT, stroke_width=1.8, stroke_linejoin='round', transform='translate(%s %s) scale(%s)' % (f(x), f(yb), f(sc)))


def glow(cx, cy, r, gid):
    return '<defs><radialGradient id="%s" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff6cf" stop-opacity="1"></stop><stop offset="0.5" stop-color="#ffe9a3" stop-opacity="0.6"></stop><stop offset="1" stop-color="#ffe9a3" stop-opacity="0"></stop></radialGradient></defs>' % gid


# ---------------------------------------------------------------- HTML scaffolding
HEAD = '''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bangers&amp;family=Comic+Neue:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
body{margin:0}
a{color:#7a3e1d}a:hover{color:#4a2410}
.balloon{position:absolute;background:#fffdf7;border:2.5px solid #3b2416;border-radius:50%%;display:flex;align-items:center;justify-content:center;text-align:center;box-sizing:border-box;font-family:'Comic Neue',sans-serif;font-weight:700;color:#2a1a10;line-height:1.2}
.balloon::after{content:"";position:absolute;width:18px;height:18px;background:#fffdf7;border-right:2.5px solid #3b2416;border-bottom:2.5px solid #3b2416}
.tail-bl::after{left:22%%;bottom:-10px;transform:rotate(55deg) skewX(20deg)}
.tail-br::after{right:22%%;bottom:-10px;transform:rotate(35deg) skewX(-20deg)}
</style>
</helmet>
'''

TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":794,"height":1123}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
'''


def balloon(text, left, top, w, h, tail='bl', fs=16, pad=8):
    return '<div class="balloon tail-%s" style="left: %spx; top: %spx; width: %spx; height: %spx; font-size: %spx; padding: 0 %spx">%s</div>' % (tail, f(left), f(top), f(w), f(h), f(fs), f(pad), text)


def caption(text, pos='tl'):
    if pos == 'tl':
        edge = 'left: 0; top: 0; border-right: 3px solid #3b2416; border-bottom: 3px solid #3b2416;'
    else:
        edge = 'right: 0; bottom: 0; border-left: 3px solid #3b2416; border-top: 3px solid #3b2416;'
    return '<div style="position: absolute; %s background: #fbe7a6; padding: 6px 14px; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 20px; color: #2a1a10">%s</div>' % (edge, text)


def sfx(text, left, top, size=84, rot=-8):
    return '<div style="position: absolute; left: %spx; top: %spx; transform: rotate(%sdeg); font-family: \'Bangers\', \'Comic Neue\', sans-serif; font-size: %spx; letter-spacing: 3px; color: #e2573a; -webkit-text-stroke: 3px #3b2416; line-height: 1">%s</div>' % (f(left), f(top), f(rot), f(size), text)


def panel(w, h, body, label, overlays='', bg='#f6ead2', height=None, flex=False, defs=''):
    svg = '<svg viewBox="0 0 %s %s" preserveAspectRatio="xMidYMid slice" style="width: 100%%; height: 100%%; display: block" role="img" aria-label="%s">%s%s</svg>' % (f(w), f(h), label, defs, body)
    hs = ''
    if flex:
        hs = 'flex: 1; min-height: 0; '
    elif height:
        hs = 'height: %spx; ' % f(height)
    return '<div style="position: relative; %sbox-sizing: border-box; border: 3px solid #3b2416; border-radius: 4px; overflow: hidden; background: %s">\n%s\n%s\n</div>' % (hs, bg, svg, overlays)


def row2(a, b, height=None, flex=False):
    hs = 'flex: 1; min-height: 0' if flex else 'height: %spx' % f(height)
    return '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; %s">\n%s\n%s\n</div>' % (hs, a, b)


def row3(a, b, c, height):
    return '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; height: %spx">\n%s\n%s\n%s\n</div>' % (f(height), a, b, c)


def footer(n):
    return '<div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: 700; color: #7a5a3e; margin-top: -4px">\n<span>Leoni di Laguna · Ep. 2 – Amici di Roma</span>\n<span>%s</span>\n</div>' % n


def page(title, rows, n):
    root = '<div style="width: 794px; height: 1123px; box-sizing: border-box; padding: 28px; background: #fdf8ee; display: flex; flex-direction: column; gap: 14px; font-family: \'Comic Neue\', sans-serif">\n\n%s\n\n%s\n\n</div>' % ('\n\n'.join(rows), footer(n))
    return HEAD % title + root + '\n' + TAIL


def gid_defs(*items):
    """items: (id, type, stops) ; type 'v' vertical linear or 'r' radial; stops list of (offset,color,opacity)"""
    s = ['<defs>']
    for gid, typ, stops in items:
        st = ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%s"></stop>' % (f(o), c, f(op)) for o, c, op in stops)
        if typ == 'v':
            s.append('<linearGradient id="%s" x1="0" y1="0" x2="0" y2="1">%s</linearGradient>' % (gid, st))
        else:
            s.append('<radialGradient id="%s" cx="0.5" cy="0.5" r="0.5">%s</radialGradient>' % (gid, st))
    s.append('</defs>')
    return ''.join(s)


def write(path, html):
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
