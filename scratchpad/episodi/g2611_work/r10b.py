from h10 import *
from r10a import sandwich2, sad_leo_overlay


def curtain(x0, x1, y0, y1, side, p, tag):
    """red velvet drape with folds; side 'l' or 'r'"""
    w = x1 - x0
    b = [R(x0, y0, w, y1 - y0, U(p + 'cu'), stroke=OUT, stroke_width=1.6)]
    n = 4
    for i in range(1, n):
        xx = x0 + w * i / n
        b.append(P('M%s %s Q%s %s %s %s' % (f(xx), f(y0), f(xx + (4 if side == 'l' else -4)), f((y0 + y1) / 2), f(xx), f(y1)), 'none', stroke='#7a1a18', stroke_width=1.6, opacity=.7))
        b.append(P('M%s %s Q%s %s %s %s' % (f(xx + 2.5), f(y0), f(xx + 2.5 + (4 if side == 'l' else -4)), f((y0 + y1) / 2), f(xx + 2.5), f(y1)), 'none', stroke='#f08a7a', stroke_width=1.2, opacity=.5))
    return G(*b)


# ------------------------------------------------------------------ 11
@card(11)
def c11(p):
    H = 110
    d = lit_defs(p)
    dd, wp = wood_planks(p, 0, 0, 215, 110, '#c79a62', '#9a6c3e', 36, 0)
    d += dd + LGd(p + 'pg', [(0, '#fffefa'), (1, '#f4ecd2')])
    b = [wp]
    b += [R(0, 0, 215, 110, '#2a1a10', stroke='none', opacity=.12)]
    b += [R(13, 9, 195, 98, '#2a1a10', stroke='none', opacity=.25, rx=5)]
    b += [R(10, 6, 195, 98, U(p + 'pg'), stroke=OUT, stroke_width=2, rx=4)]
    for yy in (22, 34, 46, 58, 70, 82, 94):
        b += [L(12, yy, 203, yy, '#bcd3e6', 1.3)]
    b += [L(26, 7, 26, 103, '#e07a6a', 1.6)]
    for yy in (18, 52, 86):
        b += [C(18, yy, 3, '#8a7a5a', stroke_width=1.2), C(17.4, yy - .6, 1, '#cfc2a0', stroke='none')]
    # washi tape on top corners
    b += [ink(P('M178 2 L206 8 L202 18 L174 12 Z', '#8fc9a8', fill_opacity=.85), sw=1.2)]
    # timeline arrow
    b += [P('M44 65.5 L190 65.5', 'none', stroke='#8aa0c8', stroke_width=5, stroke_linecap='round', opacity=.35)]
    b += [P('M44 64 L190 64', 'none', stroke='#2a4a8a', stroke_width=3.2, stroke_linecap='round'),
          P('M180 56 L196 64 L180 72', 'none', stroke='#2a4a8a', stroke_width=3.2, stroke_linecap='round', stroke_linejoin='round')]
    for xx in (70, 95, 120, 145):
        b += [P('M%s 59 L%s 69' % (f(xx), f(xx)), 'none', stroke='#2a4a8a', stroke_width=2, stroke_linecap='round')]
    for xx in (44, 166):
        b += [C(xx, 64, 6, '#c0392b', stroke_width=1.6), C(xx - 1.8, 62, 1.8, '#f08a7a', stroke='none')]
    b += [T('text', '697', x=46, y=48, text_anchor='middle', font_family='Bangers', font_weight=700, font_size=22, fill='#2a4a8a', stroke='none'),
          T('text', 'primo doge', x=50, y=90, text_anchor='middle', font_family='Comic Neue', font_weight=700, font_size=12, fill='#2a1a10', stroke='none'),
          T('text', '1797', x=156, y=48, text_anchor='middle', font_family='Bangers', font_weight=700, font_size=22, fill='#2a4a8a', stroke='none'),
          T('text', 'fine', x=164, y=90, text_anchor='middle', font_family='Comic Neue', font_weight=700, font_size=12, fill='#2a1a10', stroke='none')]
    # pencil resting at the bottom right corner on the desk edge
    b += [ink(P('M150 106 L204 98', 'none', stroke_width=5.5), P('M150 106 L204 98', 'none', stroke='#e9c46a', stroke_width=3.4), P('M150 106 L144 107', 'none', stroke='#f2c9a0', stroke_width=3.4),
              P('M204 98 L209 97.3', 'none', stroke='#e07a8a', stroke_width=3.4), sw=1.2)]
    b += [sparkle4(112, 20, 3), sparkle4(196, 44, 2.6)]
    H, d, body = finish(p, H, d, b, .22)
    d = d.replace('url(#', 'url(#')
    return H, d, body, ''


# ------------------------------------------------------------------ 12
@card(12)
def c12(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'wl', [(0, '#fbe9c0'), (1, '#f0d29a')]) + LGd(p + 'bd', [(0, '#c99a62'), (1, '#8a5a30')])
    d += T('pattern', R(0, 0, 20, 20, '#fbf3e0', stroke='none') + R(0, 0, 10, 10, '#d94a3a', stroke='none') + R(10, 10, 10, 10, '#d94a3a', stroke='none'), id=p + 'ck', width=20, height=20, patternUnits='userSpaceOnUse', patternTransform='skewX(-8)')
    d += RGd(p + 'gl', [(0, '#fff3b8', .8), (1, '#fff3b8', 0)])
    b = [R(0, 0, 215, 60, U(p + 'wl'), stroke='none')]
    # window frame hint & shelf with jar
    b += [ink(R(14, 10, 34, 40, '#cfe9f4'), L(31, 10, 31, 50, OUT, 1.6), L(14, 30, 48, 30, OUT, 1.6), P('M16 12 L28 12 L16 28 Z', '#ffffff', stroke='none', opacity=.6), sw=2)]
    b += [ink(R(170, 26, 30, 4, '#b98a55'), P('M176 14 L194 14 L196 26 L174 26 Z', '#9fd2b8'), R(175, 10, 20, 5, '#d9a441'), sw=1.4)]
    b += [P('M177 17 L181 17 L181 24 L177 24 Z', '#ffffff', stroke='none', opacity=.5)]
    # table cloth
    b += [R(0, 58, 215, 62, U(p + 'ck'), stroke='none')]
    b += [P('M0 58 L215 58', 'none', stroke=OUT, stroke_width=2), R(0, 58, 215, 4, '#000000', stroke='none', opacity=.14)]
    b += [R(0, 58, 215, 62, '#2a1a10', stroke='none', opacity=.06)]
    # board
    b += [ink(P('M30 98 Q107 112 185 98 L190 108 Q107 122 25 108 Z', '#8a5a30'), P('M28 92 Q107 106 188 92 L190 100 Q107 114 26 100 Z', U(p + 'bd')), sw=2)]
    b += [P('M38 96 Q107 107 178 96', 'none', stroke='#e4b27a', stroke_width=1.4, opacity=.8)]
    b += [E(107, 98, 90, 8, '#2a1a10', stroke='none', opacity=.18)]
    b += [C(107, 56, 62, U(p + 'gl'), stroke='none')]
    b += [lit(p, sandwich2(107, 74, 1.62))]
    # crumbs, cheese, tomato slice on board
    b += [cheese_t(40, 94), E(58, 98, 3.6, 2, '#d9392e', stroke=OUT, stroke_width=1), E(182, 96, 3, 1.5, '#f3cf8a', stroke=OUT, stroke_width=1)]
    b += [ink(C(160, 100, 6, '#d9392e'), C(160, 100, 3.6, '#f08a7a', stroke='none'), P('M160 94 L160 106 M154 100 L166 100', 'none', stroke='#f6b09a', stroke_width=.8), sw=1.4)]
    for (cx, cy) in [(36, 104), (72, 108), (150, 110), (130, 106), (174, 107)]:
        b += [E(cx, cy, 1.5, 1, '#e8b25e', stroke='none')]
    b += [sparkle4(30, 56, 4), sparkle4(188, 62, 4), sparkle4(100, 6, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


def cheese_t(x, y):
    return ink(P('M%s %s L%s %s L%s %s Z' % (f(x), f(y), f(x + 20), f(y - 4), f(x + 18), f(y + 7)), '#f6cc4a'), C(x + 12, y, 1.5, '#e0a92a', stroke='none'), C(x + 8, y + 3, 1, '#e0a92a', stroke='none'), sw=1.4)


# ------------------------------------------------------------------ 5
@card(5)
def c5(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'cu', [(0, '#a02420'), (.5, '#d8423a'), (1, '#8c1c1a')], 0, 0, 1, 0)
    d += LGd(p + 'wl', [(0, '#f1e4c8'), (1, '#d9c79c')]) + RGd(p + 'gl', [(0, '#fff3b8', .8), (1, '#fff3b8', 0)])
    b = [R(0, 0, 215, 120, U(p + 'wl'), stroke='none')]
    # marble arch behind
    b += [ink(P('M52 100 L52 52 Q52 14 107 12 Q162 14 162 52 L162 100 Z', '#e6d6ae'), sw=2)]
    b += [P('M60 100 L60 54 Q60 22 107 20 Q154 22 154 54 L154 100 Z', '#c9a86a', stroke=OUT, stroke_width=1.4)]
    b += [P('M66 100 L66 56 Q66 28 107 26 Q148 28 148 56 L148 100 Z', '#f1e4c8', stroke=OUT, stroke_width=1.2)]
    for i in range(9):
        a = math.pi + i * math.pi / 8
        b += [C(107 + 47 * math.cos(a), 56 + 40 * math.sin(a), 1.8, '#f4c64e', stroke=OUT, stroke_width=.8)]
    b += [ink(E(107, 100, 52, 5, '#a98d62'), sw=1)] if False else []
    # floor checker
    b += [R(0, 98, 215, 22, '#d6c8a6', stroke='none')]
    for r_ in range(3):
        for c_ in range(14):
            if (r_ + c_) % 2:
                x_ = c_ * 17 - 8
                b += [R(x_, 98 + r_ * 8, 17, 8, '#9a8a66', stroke='none', opacity=.5)]
    b += [R(0, 98, 215, 2, OUT, stroke='none', opacity=.5)]
    # curtains
    b += [curtain(0, 40, 0, 100, 'l', p, 'l'), curtain(175, 215, 0, 100, 'r', p, 'r')]
    b += [P('M0 0 Q20 18 40 0', '#c8352a', stroke=OUT, stroke_width=1.6), P('M175 0 Q195 18 215 0', '#c8352a', stroke=OUT, stroke_width=1.6)]
    b += [R(0, 0, 215, 5, '#f4c64e', stroke=OUT, stroke_width=1.5)]
    for xx in (8, 215 - 8):
        b += [ink(C(xx, 6, 3, '#f4c64e'), sw=1)]
    # ties + tassels
    for (xx, sx) in ((40, 1), (175, -1)):
        b += [ink(P('M%s 62 Q%s 66 %s 70' % (f(xx), f(xx - 8 * sx), f(xx - 24 * sx)), 'none', stroke='#f4c64e', stroke_width=4), sw=1)]
        b += [ink(P('M%s 62 Q%s 66 %s 70' % (f(xx), f(xx - 8 * sx), f(xx - 24 * sx)), 'none', stroke='#f4c64e', stroke_width=2.2), sw=.1)] if False else []
        b += [ink(C(xx - 2 * sx, 62, 3.4, '#f4c64e'), P('M%s 65 L%s 76 M%s 65 L%s 76 M%s 65 L%s 77' % (f(xx - 3 * sx), f(xx - 5 * sx), f(xx - 2 * sx), f(xx - 2 * sx), f(xx - 1 * sx), f(xx + 1 * sx)), 'none', stroke='#d9a441', stroke_width=1.8), sw=1)]
    # throne chair at right
    b += [ink(R(166, 70, 8, 36, '#7a1a18'), sw=1.2)] if False else []
    b += [C(107, 56, 40, U(p + 'gl'), stroke='none')]
    b += [shadow(107, 112, 34, 5, .32)]
    b += [lit(p, doge(107, 72, .88, 'sad', True, la=(-13, 22), ra=(13, 22), cloth=(0, 22, 0)))]
    b += [sparkle4(60, 30, 2.6)]
    H, d, body = finish(p, H, d, b, .3)
    return H, d, body, ''


# ------------------------------------------------------------------ 6
@card(6)
def c6(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'pc', [(0, '#fbeec8'), (1, '#efd9a0')]) + LGd(p + 'ro', [(0, '#e8d49a'), (.5, '#fff3c8'), (1, '#c9a96a')], 0, 0, 1, 0)
    dd, wp = wood_planks(p, 0, 0, 215, 120, '#b98a55', '#8a5f36', 34, 0)
    d += dd
    b = [wp, R(0, 0, 215, 120, '#2a1a10', stroke='none', opacity=.1)]
    b += [P('M0 92 L215 92', 'none', stroke='#4a3020', stroke_width=1, opacity=.4)]
    b += [E(108, 100, 100, 6, '#2a1a10', stroke='none', opacity=.3)]
    # parchment
    b += [R(28, 28, 160, 68, U(p + 'pc'), stroke=OUT, stroke_width=2.2)]
    b += [R(28, 28, 160, 6, '#e8d49a', stroke='none'), R(28, 90, 160, 6, '#e8d49a', stroke='none')]
    b += [P('M36 42 Q60 38 90 44 M110 80 Q140 84 176 78', 'none', stroke='#d9b97a', stroke_width=1.2, opacity=.6)]
    for (cx, cy, r_) in [(150, 40, 5), (80, 84, 4)]:
        b += [C(cx, cy, r_, '#d9b97a', stroke='none', opacity=.35)]
    # rolls
    b += [ink(E(28, 62, 9, 36, U(p + 'ro')), E(28, 62, 4, 30, 'none'), E(188, 62, 9, 36, U(p + 'ro')), E(188, 62, 4, 30, 'none'), sw=2)]
    b += [P('M24 34 Q20 62 24 90', 'none', stroke='#fff8e0', stroke_width=2, opacity=.7)]
    # lion medallion
    b += [C(56, 62, 20, '#fffaf0', stroke=OUT, stroke_width=2), C(56, 62, 17, 'none', stroke='#d9a441', stroke_width=1.6)]
    b += [lion_wing_emblem(56, 64, 1.22)]
    # arrow with six ticks
    b += [P('M84 67 L138 67', 'none', stroke='#8aa0c8', stroke_width=5, stroke_linecap='round', opacity=.35)]
    b += [P('M84 66 L138 66', 'none', stroke='#2a4a8a', stroke_width=3.2, stroke_linecap='round'),
          P('M130 58 L142 66 L130 74', 'none', stroke='#2a4a8a', stroke_width=3.2, stroke_linecap='round', stroke_linejoin='round')]
    for xx in (90, 98, 106, 114, 122, 130):
        b += [P('M%s 61 L%s 71' % (f(xx), f(xx)), 'none', stroke='#2a4a8a', stroke_width=2, stroke_linecap='round')]
    b += [C(84, 66, 5, '#c0392b', stroke_width=1.5), C(82.6, 64.6, 1.4, '#f08a7a', stroke='none')]
    # sad doge cap at the end
    b += [shadow(166, 82, 16, 3, .25)]
    b += [corno(166, 62, .78, 24, sad=True)]
    # eyes + frown on the cap
    b += [ink(E(161.5, 44.4, 1.8, 2.6, '#2a1a10', stroke='none'), E(171, 42, 1.8, 2.6, '#2a1a10', stroke='none'), sw=1)] if False else []
    b += [T('text', 'FINE', x=158, y=88, text_anchor='middle', font_family='Bangers', font_weight=700, font_size=20, fill='#a8322a', stroke='none')]
    # ink pot and quill
    b += [ink(P('M196 104 L206 104 L208 114 L194 114 Z', '#2a2a4a'), E(201, 104, 5, 1.8, '#4a4a6a'), sw=1.3)]
    b += [ink(P('M204 104 Q212 84 206 70', 'none', stroke='#fbf8ee', stroke_width=3), P('M204 104 Q212 84 206 70', 'none', stroke_width=.1), sw=1.2)]
    b += [sparkle4(14, 20, 3), sparkle4(200, 22, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''


# ------------------------------------------------------------------ 1100
@card(1100)
def c1100(p):
    H = 120
    d = lit_defs(p) + LGd(p + 'sk', [(0, '#ffe6a8'), (.6, '#fbc98c'), (1, '#f7a97a')]) + RGd(p + 'gl', [(0, '#fff8d0', 1), (1, '#fff8d0', 0)])
    b = [R(0, 0, 215, 120, U(p + 'sk'), stroke='none')]
    # rays
    for k in range(14):
        a = -math.pi + k * math.pi / 13
        b += [P('M107 70 L%s %s L%s %s Z' % (f(107 + 160 * math.cos(a - .05)), f(70 + 160 * math.sin(a - .05)), f(107 + 160 * math.cos(a + .05)), f(70 + 160 * math.sin(a + .05))), '#fff3b8', stroke='none', opacity=.35 if k % 2 else .18)]
    b += [C(107, 66, 72, U(p + 'gl'), stroke='none')]
    # faded arcade
    for i in range(7):
        a = i * 31 - 6
        b += [P(pointed(a, a + 24, 82, 66, 100), '#d98a6a', stroke='none', opacity=.35)]
    b += [R(0, 98, 215, 22, '#e6c07a', stroke='none')]
    for r_ in range(3):
        for c_ in range(14):
            if (r_ + c_) % 2:
                b += [R(c_ * 17 - 8, 98 + r_ * 8, 17, 8, '#c9954a', stroke='none', opacity=.4)]
    b += [R(0, 98, 215, 2, OUT, stroke='none', opacity=.35)]
    b += [cloud2(30, 20, .55, .7, '#f6d9b0'), cloud2(190, 24, .5, .7, '#f6d9b0')]
    b += [shadow(70, 112, 28, 4, .28), shadow(150, 112, 30, 4, .28)]
    # doge smiling through tears
    b += [lit(p, doge(68, 66, .86, 'smile', True, la=(-26, 26), ra=(34, 14)))]
    # Leo hugging with wing
    b += [lit(p, leo(146, 62, .8, wing='open', la=(-34, 18), ra=(34, 22), mouth='smile'))]
    b += [sparkle4(30, 40, 4), sparkle4(112, 20, 4), sparkle4(190, 84, 4), sparkle4(100, 70, 3), sparkle4(46, 14, 3)]
    H, d, body = finish(p, H, d, b, .26)
    return H, d, body, ''
