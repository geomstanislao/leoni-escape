import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/g2611_work')
from h10 import *
from r10a import sandwich2, sad_leo_overlay, backpack
from r10b import cheese_t
from r10c import brick_wall

GLOW = [(0, '#fff6c0', .95), (.35, '#ffb43c', .6), (1, '#ff7a20', 0)]


def glow_def(i):
    return RGd(i, [(0, '#fff6c0', .95), (.35, '#ffb43c', .6), (1, '#ff7a20', 0)])


def goblet(x, y, s=1, rot=0, tint='#dff3f8', op=.8):
    b = [P('M-10 -26 Q-11 -8 0 -6 Q11 -8 10 -26 Z', tint, opacity=op),
         R(-1.4, -6, 2.8, 8, tint, opacity=op), E(0, 3, 8, 2.4, tint, opacity=op),
         P('M-7 -24 Q-8 -12 -3 -9', 'none', stroke='#ffffff', stroke_width=2, opacity=.95),
         P('M-9 -26 Q0 -23 9 -26', 'none', stroke='#ffffff', stroke_width=1, opacity=.8),
         P('M5 -20 Q6 -14 3 -11', 'none', stroke='#9ad0e0', stroke_width=1.2, opacity=.8)]
    return ink(*b, transform=T_(x, y, s, rot), sw=1.5)


def sparks(x, y, n=3):
    return ''.join(sparkle4(x + dx, y + dy, r) for (dx, dy, r) in [(0, 0, 4), (9, -6, 2.6), (-8, -8, 2.2)][:n])


def man(x, y, s=1, flip=False, rot=0, la=(-22, 24), ra=(22, 24), expr='smile', look=0, kind='master', hold_l='', hold_r='', cap=True):
    master = kind == 'master'
    tun = '#5f7894' if master else '#efe1c0'
    tun2 = '#475c78' if master else '#d6c49a'
    b = []
    b.append(E(-10, 61, 9, 4.5, '#5a3a22') + E(10, 61, 9, 4.5, '#5a3a22'))
    b.append(P('M-19 -14 Q0 -25 19 -14 L26 58 Q0 65 -26 58 Z', tun))
    b.append(P('M-19 -14 Q-24 20 -26 58 L-14 60 Q-14 20 -12 -12 Z', tun2, stroke='none', opacity=.5))
    b.append(P('M-24 52 Q0 59 24 52', 'none', stroke=tun2, stroke_width=2))
    # arms (sleeves)
    b.append(limb(-17, -8, la[0], la[1], tun, 14, hand=SK, hr=6))
    # apron
    if master:
        b.append(P('M-13 -12 L13 -12 L18 56 Q0 62 -18 56 Z', '#9a6638'))
        b.append(P('M-13 -12 L-18 56 L-8 58 L-6 -12 Z', '#7a4a26', stroke='none', opacity=.5))
        b.append(P('M-8 -14 L-14 -22 M8 -14 L14 -22', 'none', stroke='#6b3f1e', stroke_width=2.2))
        b.append(R(-8, 6, 16, 11, '#8a5a30', rx=2, stroke_width=1.4))
    else:
        b.append(P('M-12 -10 L12 -10 L15 44 Q0 48 -15 44 Z', '#8a5a30'))
        b.append(P('M-8 -12 L-13 -20 M8 -12 L13 -20', 'none', stroke='#6b3f1e', stroke_width=2.2))
        b.append(P('M-9 8 L-4 14 M6 22 L10 28', 'none', stroke='#3a2a20', stroke_width=2, opacity=.5))
    b.append(R(-21, 15, 42, 5, '#4a3020', rx=2, stroke_width=1.4))
    b.append(limb(17, -8, ra[0], ra[1], tun, 14, hand=SK, hr=6))
    if hold_l:
        b.append(G(hold_l, transform='translate(%s %s)' % (f(la[0]), f(la[1]))))
    if hold_r:
        b.append(G(hold_r, transform='translate(%s %s)' % (f(ra[0]), f(ra[1]))))
    # head
    b.append(R(-5, -20, 10, 8, '#e9c6a4', stroke_width=1.5))
    if master:
        b.append(C(-19, -37, 6, '#cfcfd2') + C(19, -37, 6, '#cfcfd2'))
    b.append(C(0, -36, 19, SK))
    if not master:
        b.append(P('M-20 -38 Q-22 -55 -6 -57 Q8 -62 18 -52 Q23 -46 20 -38 Q10 -47 0 -45 Q-12 -47 -20 -38 Z', '#6b3f1e'))
        b.append(P('M-4 -56 L0 -63 L5 -56', '#6b3f1e', stroke_width=1.6))
        b.append(P('M-16 -26 Q-12 -22 -8 -25', 'none', stroke='#3a2a20', stroke_width=3, opacity=.55, stroke_linecap='round'))
    b.append(face(0, -35, expr, my=-25, look=look, sp=7))
    if master:
        b.append(P('M-15 -27 Q-16 -4 0 -2 Q16 -4 15 -27 Q9 -19 0 -19 Q-9 -19 -15 -27 Z', '#d2d2d6'))
        b.append(P('M-7 -22 Q0 -19 7 -22 Q0 -25 -7 -22 Z', '#d2d2d6', stroke_width=1.4))
        b.append(P('M-9 -14 Q0 -9 9 -14', 'none', stroke='#9a9aa2', stroke_width=1.2))
        b.append(P('M-21 -44 Q-19 -64 0 -64 Q19 -64 21 -44 Q0 -53 -21 -44 Z', '#a8322a'))
        b.append(P('M-21 -44 Q0 -53 21 -44 L21 -39 Q0 -48 -21 -39 Z', '#7a1f1a'))
        b.append(P('M-13 -60 Q-6 -64 0 -63', 'none', stroke='#e07a68', stroke_width=2, opacity=.8))
    return ink(*b, transform=T_(x, y, s, rot) if not flip else 'translate(%s %s) rotate(%s) scale(%s %s)' % (f(x), f(y), f(rot), f(-s), f(s)))


def blowpipe(x1, y1, x2, y2, gather=None, r=7, gid=None):
    d = 'M%s %s L%s %s' % (f(x1), f(y1), f(x2), f(y2))
    b = [P(d, 'none', stroke=OUT, stroke_width=4.4, stroke_linecap='round'), P(d, 'none', stroke='#9aa0a8', stroke_width=2.4, stroke_linecap='round'),
         P(d, 'none', stroke='#e4e8ec', stroke_width=.8, stroke_linecap='round', opacity=.8)]
    if gather:
        b.append(C(x2, y2, r * 2.6, U(gid), stroke='none', opacity=.8) if gid else '')
        b.append(ink(C(x2, y2, r, gather[0]), sw=1.6))
        b.append(C(x2 - r * .3, y2 - r * .3, r * .38, gather[1], stroke='none', opacity=.9))
    return G(*b)


def furnace(p, x, yb, s=1, lit_=True, tag='f', crucible=False, big=False):
    """returns (defs, svg). origin: bottom centre. width 84, height ~96"""
    d = LGd(p + 'fb' + tag, [(0, '#7a3a26'), (.5, '#c4764a'), (1, '#7a3a26')], 0, 0, 1, 0)
    d += RGd(p + 'fo' + tag, [(0, '#fffbd0'), (.3, '#ffd24a'), (.7, '#ff8a22'), (1, '#c8421a')])
    b = []
    b.append(E(0, 1, 52, 6, '#1f1008', stroke='none', opacity=.4))
    # body
    b.append(P('M-44 0 L-44 -40 Q-45 -94 0 -99 Q45 -94 44 -40 L44 0 Z', U(p + 'fb' + tag)))
    # light and shade on dome
    b.append(P('M-44 -40 Q-45 -92 -12 -98 Q-30 -80 -30 -40 Z', '#ffd9a0', stroke='none', opacity=.28))
    b.append(P('M44 -40 Q45 -92 12 -98 Q32 -80 30 -40 Z', '#3a1408', stroke='none', opacity=.28))
    # brick courses
    for k, yy in enumerate([-8, -18, -28, -38, -48, -58, -68, -78, -88]):
        wd = 44 if yy > -45 else 44 * math.sqrt(max(.05, 1 - ((abs(yy) - 45) / 56.) ** 2))
        b.append(PLn('M%s %s Q0 %s %s %s' % (f(-wd), f(yy), f(yy + 5), f(wd), f(yy)), '#4a1e10', 1, .75))
        off = 0 if k % 2 else 5
        for j in range(-int(wd // 10), int(wd // 10) + 1):
            xx = j * 10 + off
            if abs(xx) < wd - 2:
                b.append(PLn('M%s %s l0 -9' % (f(xx), f(yy)), '#4a1e10', .9, .6))
    b.append(R(-46, -4, 92, 6, '#5a2a18', rx=1.5, stroke_width=1.6))
    # mouths
    for mx in (-24, 0, 24):
        if big and mx == 0:
            continue
        b.append(P('M%s -4 L%s -26 Q%s -37 %s -26 L%s -4 Z' % (f(mx - 9), f(mx - 9), f(mx), f(mx + 9), f(mx + 9)), U(p + 'fo' + tag), stroke_width=2.2))
        b.append(P('M%s -4 L%s -26 Q%s -37 %s -26 L%s -4' % (f(mx - 9), f(mx - 9), f(mx), f(mx + 9), f(mx + 9)), 'none', stroke='#3a1408', stroke_width=3, opacity=.45))
        b.append(P('M%s -6 Q%s -20 %s -13 Q%s -22 %s -6 Z' % (f(mx - 4), f(mx - 6), f(mx), f(mx + 5), f(mx + 4)), '#fff3a0', stroke='none', opacity=.9))
    if big:
        b.append(P('M-21 -4 L-21 -50 Q-21 -68 0 -68 Q21 -68 21 -50 L21 -4 Z', U(p + 'fo' + tag), stroke_width=2.4))
        b.append(P('M-21 -4 L-21 -50 Q-21 -68 0 -68 Q21 -68 21 -50 L21 -4', 'none', stroke='#3a1408', stroke_width=3.5, opacity=.4))
        b.append(C(0, -34, 16, '#d8ff7a', stroke='none', opacity=.35))
        for fx in (-14, -6, 6, 14):
            b.append(P('M%s -4 Q%s -16 %s -26 Q%s -14 %s -4 Z' % (f(fx - 4), f(fx - 5), f(fx), f(fx + 5), f(fx + 4)), '#ffe36a', stroke='#e0731a', stroke_width=1))
        b.append(P('M-13 -8 L-16 -30 Q-16 -37 -10 -37 L10 -37 Q16 -37 16 -30 L13 -8 Z', '#a8643c', stroke_width=2))
        b.append(P('M-13 -10 L-14 -30', 'none', stroke='#d8905a', stroke_width=2))
        b.append(E(0, -37, 11.5, 3.8, '#a6d65c', stroke_width=1.6))
        b.append(E(0, -37.4, 8, 2.2, '#d8ff7a', stroke='none'))
        b.append(E(-4, -38, 2.6, .9, '#ffffff', stroke='none', opacity=.9))
        b.append(C(5, -37, 1.2, '#eaffb0', stroke='none'))
    # crown hole
    b.append(E(0, -99, 9, 3, '#3a1408', stroke_width=1.6))
    b.append(E(0, -99.5, 6, 1.8, '#ffb43c', stroke='none'))
    return d, ink(*b, transform=T_(x, yb, s), sw=2.2)


def bhouse(x, yb, w, h, seed=1, roof='#a8452c', chim=True, win=True, door=True, tag=''):
    rnd = random.Random(seed)
    b = []
    b.append(R(x, yb - h, w, h, '#b9704a', stroke=OUT, stroke_width=1.6))
    for r_ in range(int(h / 5)):
        yy = yb - h + r_ * 5
        b.append(L(x, yy, x + w, yy, '#7a3e24', .6, opacity=.55))
        for c_ in range(int(w / 9)):
            xx = x + (4.5 if r_ % 2 else 0) + c_ * 9
            if xx < x + w:
                b.append(L(xx, yy, xx, yy + 5, '#7a3e24', .5, opacity=.45))
    b.append(R(x, yb - h, w * .22, h, '#ffe0b0', stroke='none', opacity=.14))
    b.append(R(x + w * .78, yb - h, w * .22, h, '#2a1008', stroke='none', opacity=.2))
    b.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(x - 3), f(yb - h), f(x + w * .12), f(yb - h - 12), f(x + w * .88), f(yb - h - 12), f(x + w + 3), f(yb - h)), roof, stroke=OUT, stroke_width=1.6))
    for k in range(5):
        xx = x + w * (.14 + k * .17)
        b.append(PLn('M%s %s L%s %s' % (f(xx), f(yb - h - 11), f(xx - 2), f(yb - h)), '#6a2a18', .8, .6))
    if chim:
        cx = x + w * rnd.choice([.3, .7])
        b.append(P('M%s %s L%s %s L%s %s L%s %s Z' % (f(cx - 3), f(yb - h - 8), f(cx - 2), f(yb - h - 26), f(cx + 2), f(yb - h - 26), f(cx + 3), f(yb - h - 8)), '#c98260', stroke=OUT, stroke_width=1.3))
        b.append(P('M%s %s L%s %s L%s %s Z' % (f(cx - 4.5), f(yb - h - 26), f(cx), f(yb - h - 31), f(cx + 4.5), f(yb - h - 26)), '#8a4a30', stroke=OUT, stroke_width=1.2))
    if win:
        wx = x + w * .15
        b.append(P('M%s %s L%s %s Q%s %s %s %s L%s %s Z' % (f(wx), f(yb - h * .3), f(wx), f(yb - h * .62), f(wx + 5), f(yb - h * .75), f(wx + 10), f(yb - h * .62), f(wx + 10), f(yb - h * .3)), '#ffb43c', stroke=OUT, stroke_width=1.3))
        b.append(R(wx + 2, yb - h * .6, 6, 6, '#fff0a0', stroke='none', opacity=.8))
    if door:
        dx = x + w * .6
        b.append(P('M%s %s L%s %s Q%s %s %s %s L%s %s Z' % (f(dx), f(yb), f(dx), f(yb - h * .42), f(dx + 5.5), f(yb - h * .56), f(dx + 11), f(yb - h * .42), f(dx + 11), f(yb)), '#5a3a22', stroke=OUT, stroke_width=1.3))
    return G(*b)


def window_arch(x, y, w, h, p, sky='#bfe6f4', bars=True, tag='w'):
    b = [P('M%s %s L%s %s Q%s %s %s %s L%s %s Z' % (f(x), f(y + h), f(x), f(y + w / 2), f(x), f(y), f(x + w / 2), f(y), f(x + w), f(y + w / 2)), sky)]
    b = [P('M%s %s L%s %s Q%s %s %s %s Q%s %s %s %s L%s %s Z' % (f(x), f(y + h), f(x), f(y + w * .5), f(x), f(y - w * .1), f(x + w / 2), f(y - w * .1), f(x + w), f(y - w * .1), f(x + w), f(y + w * .5), f(x + w), f(y + h)), U(p + 'sk' + tag), stroke_width=2)]
    b.append(P('M%s %s l%s %s l%s %s' % (f(x + 3), f(y + h * .5), f(w * .3), f(-h * .35), f(w * .2), f(-h * .0)), 'none', stroke='#ffffff', stroke_width=2.4, opacity=.6))
    if bars:
        b.append(L(x + w / 2, y - 1, x + w / 2, y + h, OUT, 1.6))
        b.append(L(x, y + h * .45, x + w, y + h * .45, OUT, 1.6))
    b.append(R(x - 3, y + h, w + 6, 4, '#c9a878', stroke_width=1.6))
    return G(*b, stroke=OUT, stroke_width=2, stroke_linejoin='round')


def sky_def(p, tag='w', c0='#7ec4ea', c1='#e8f4e0'):
    return LGd(p + 'sk' + tag, [(0, c0), (1, c1)])


def shelf(x, y, w, p=None):
    return ink(R(x, y, w, 5, '#b98a55', stroke_width=1.6), R(x + 1, y + 1, w - 2, 1.4, '#e4b27a', stroke='none', opacity=.8),
               P('M%s %s L%s %s L%s %s Z' % (f(x + 6), f(y + 5), f(x + 6), f(y + 12), f(x + 13), f(y + 5)), '#8a5a30', stroke_width=1.2),
               P('M%s %s L%s %s L%s %s Z' % (f(x + w - 6), f(y + 5), f(x + w - 6), f(y + 12), f(x + w - 13), f(y + 5)), '#8a5a30', stroke_width=1.2), sw=1.6)


def cup(x, y, s=1, tint='#cfe9f0', op=.85):
    return ink(P('M-5 -9 Q-5 0 0 1 Q5 0 5 -9 Z', tint, opacity=op), P('M-3 -8 Q-3 -2 -1 -1', 'none', stroke='#ffffff', stroke_width=1.4), transform=T_(x, y, s), sw=1.2)


def bucket(x, yb, s=1):
    b = [E(0, 1, 13, 3, '#1f1008', stroke='none', opacity=.3),
         P('M-11 -22 L11 -22 L9 0 L-9 0 Z', '#8a5a30'), E(0, -22, 11, 3, '#4a8aa8'), E(0, -22, 11, 3, 'none', stroke=OUT, stroke_width=1.6),
         P('M-10 -15 Q0 -12 10 -15 M-9 -7 Q0 -4 9 -7', 'none', stroke='#4a4a52', stroke_width=1.8),
         P('M-5 -22 L-4 0', 'none', stroke='#c99a62', stroke_width=1, opacity=.7),
         P('M-11 -22 Q0 -42 11 -22', 'none', stroke=OUT, stroke_width=1.4),
         PLn('M-6 -22 q3 -1.4 6 0 q3 1.4 6 0', '#e8f6fa', 1.2, .9)]
    return ink(*b, transform=T_(x, yb, s), sw=1.6)


def pincers(x, y, s=1, rot=0):
    b = [P('M-14 6 L0 -2 L14 6', 'none', stroke='#8a9098', stroke_width=3), P('M-14 6 L0 -2 L14 6', 'none', stroke='#d0d6dc', stroke_width=1),
         P('M0 -2 L-6 -22 M0 -2 L6 -22', 'none', stroke='#8a9098', stroke_width=3), C(0, -2, 2.2, '#4a4a52')]
    return ink(*b, transform=T_(x, y, s, rot), sw=1.4)


def shears(x, y, s=1, rot=0):
    b = [P('M-12 8 Q-18 0 -10 -6 Q-4 -4 0 0 L8 -22', 'none', stroke='#8a9098', stroke_width=3),
         P('M12 8 Q18 0 10 -6 Q4 -4 0 0 L-8 -22', 'none', stroke='#8a9098', stroke_width=3), C(0, 0, 2, '#4a4a52')]
    return ink(*b, transform=T_(x, y, s, rot), sw=1.4)


def bench(x, yb, w, h=22, p=''):
    b = [E(x + w / 2, yb + 2, w * .55, 4, '#1f1008', stroke='none', opacity=.35),
         R(x + 4, yb - h + 4, 6, h - 4, '#6b4426', stroke_width=1.6), R(x + w - 10, yb - h + 4, 6, h - 4, '#6b4426', stroke_width=1.6),
         R(x, yb - h, w, 6, '#b98a55', stroke_width=1.8), R(x + 1, yb - h + 1, w - 2, 1.6, '#e4b27a', stroke='none', opacity=.85),
         R(x, yb - h + 6, w, 2, '#6b4426', stroke='none', opacity=.5)]
    return ink(*b, sw=1.8)


def jar(p, x, yb, s=1, content='', tag='j', body='#c47a45', band='#3f6a98'):
    d = LGd(p + 'jb' + tag, [(0, '#8a4a2a'), (.4, '#d68a52'), (1, '#8a4a2a')], 0, 0, 1, 0)
    b = [E(0, 1, 24, 4, '#1f1008', stroke='none', opacity=.35)]
    b.append(P('M-15 0 Q-28 -16 -14 -37 Q-11 -42 -12 -46 L12 -46 Q11 -42 14 -37 Q28 -16 15 0 Z', U(p + 'jb' + tag)))
    b.append(P('M-12 -5 Q-21 -18 -12 -34', 'none', stroke='#f6c692', stroke_width=2.4, opacity=.7))
    b.append(P('M-26 -20 Q0 -14 26 -20 L25 -27 Q0 -21 -25 -27 Z', band, stroke_width=1.4))
    b.append(P('M-22 -8 Q0 -3 22 -8', 'none', stroke=band, stroke_width=1.6, opacity=.8))
    b.append(E(0, -47, 14.5, 4.8, '#e09a62', stroke_width=2))
    b.append(E(0, -47.5, 11.2, 3.3, '#2a1a10', stroke_width=1.2))
    b.append(content)
    b.append(P('M-14 -46 Q0 -41 14 -46', 'none', stroke=OUT, stroke_width=2))
    return d, ink(*b, transform=T_(x, yb, s), sw=2)


def sand_heap(w=14, top=-72, base=-47):
    return G(P('M%s %s C%s %s %s %s 0 %s C%s %s %s %s %s %s Z' % (f(-w - 2), f(base), f(-w - 3), f(top + 14), f(-w * .55), f(top), f(top), f(w * .55), f(top), f(w + 3), f(top + 14), f(w + 2), f(base)), '#f1d57a', stroke_width=1.6),
             P('M%s %s Q%s %s -1 %s' % (f(-w * .8), f(base - 2), f(-w * .5), f(top + 8), f(top + 2)), 'none', stroke='#fff0b4', stroke_width=2, opacity=.9),
             *[E(a, b_, 1, .7, '#b88a2c', stroke='none', opacity=.9) for (a, b_) in [(-6, -54), (2, -60), (7, -52), (-1, -51), (4, -66), (-9, -50), (0, -68)]])


def ash_heap(w=14, top=-72, base=-47):
    g = [P('M%s %s C%s %s %s %s 0 %s C%s %s %s %s %s %s Z' % (f(-w - 2), f(base), f(-w - 3), f(top + 14), f(-w * .55), f(top), f(top), f(w * .55), f(top), f(w + 3), f(top + 14), f(w + 2), f(base)), '#a2a5a8', stroke_width=1.6),
         P('M%s %s Q%s %s -1 %s' % (f(-w * .8), f(base - 2), f(-w * .5), f(top + 8), f(top + 2)), 'none', stroke='#d6d8da', stroke_width=2, opacity=.9)]
    g += [E(a, b_, 1.1, .8, c, stroke='none') for (a, b_, c) in [(-6, -54, '#6f7276'), (2, -60, '#e4e6e8'), (7, -52, '#6f7276'), (-1, -51, '#e4e6e8'), (4, -64, '#6f7276'), (-9, -50, '#e4e6e8')]]
    # dry plant twig
    g.append(P('M4 -66 Q9 -78 14 -90 M9 -76 Q16 -78 19 -84 M7 -72 Q2 -76 1 -84 M11 -82 Q7 -86 6 -92', 'none', stroke='#6b5a2a', stroke_width=1.8))
    g.append(P('M14 -90 q3 -4 1 -8 M19 -84 q4 -2 5 -6 M1 -84 q-3 -3 -1 -7', 'none', stroke='#8a7a3a', stroke_width=1.4))
    return G(*g)


def lumps(w=11.5, base=-48):
    g = []
    for (a, b_, r, c) in [(-7, -52, 6.5, '#2d2c33'), (6, -52, 7, '#26252c'), (0, -62, 6.5, '#34333c'), (-11, -47, 4.5, '#2a2930'), (11, -47, 4.5, '#2a2930'), (-1, -49, 5, '#2d2c33'), (4, -68, 4.5, '#2a2930')]:
        pts = [(a + r * math.cos(t) * (1 + .25 * math.sin(3 * t)), b_ + r * .85 * math.sin(t)) for t in [i * math.pi / 3.5 for i in range(7)]]
        g.append(P('M' + ' L'.join('%s %s' % (f(px), f(py)) for px, py in pts) + ' Z', c, stroke_width=1.3))
        g.append(P('M%s %s L%s %s' % (f(a - r * .5), f(b_ - r * .3), f(a + r * .1), f(b_ - r * .6)), 'none', stroke='#8a8a9c', stroke_width=1.2, opacity=.9))
    return G(*g)


def label(x, y, w, h, num, size=16):
    return G(R(x - w / 2, y - h / 2, w, h, '#ffffff', rx=2, stroke=OUT, stroke_width=1.6),
             C(x - w / 2 + 3, y - h / 2 + 3, 1.4, '#8a5a30', stroke='none'),
             tx(str(num), x, y + size * .36, size, '#2a1a10'))


def glass_bead(x, y, r, col):
    return G(C(x, y, r, col, stroke=OUT, stroke_width=1.2), C(x - r * .3, y - r * .3, r * .35, '#ffffff', stroke='none', opacity=.8))


def feather_g(x, y, rot=0, n=16):
    return feather(x, y, n, rot, '#9a9da6')


def table_wood(p, y0, H, tag='t'):
    d, w = wood_planks(p + tag, 0, y0, 215, H - y0, '#c79a62', '#8a5c34', 34, 0)
    return d, G(w, R(0, y0, 215, 3, '#e4b27a', stroke='none', opacity=.7), R(0, y0 + 3, 215, 4, '#000000', stroke='none', opacity=.16), L(0, y0, 215, y0, OUT, 1.8))


def room_wall(p, H, y0=0, y1=80, c1='#b0694a', c2='#7a3e24', seed=2, tag='rw', glow=None):
    d = LGd(p + 'wd' + tag, [(0, '#2a1208', .55), (.55, '#2a1208', .1), (1, '#2a1208', .3)])
    b = [brick_wall(0, y0, 215, y1 - y0, c1, c2, seed, True), R(0, y0, 215, y1 - y0, U(p + 'wd' + tag), stroke='none')]
    return d, G(*b)
