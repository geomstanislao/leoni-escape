import sys, re, math
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escB')
from lib import *

OUTDIR = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escape/project/'
W = 215
DARK = '#2a1a10'
TYPES = {'LUOGO': '#5f9a5a', 'OGGETTO ROSSO': '#d9472f', 'OGGETTO BLU': '#4f74a8', 'PERSONAGGIO': '#c99a2e',
         'INDIZIO': '#7a5a3e', 'ENIGMA': '#8a5fb0', 'COMBINAZIONE': '#e39a3b', 'RISPOSTA': '#e39a3b',
         'SBAGLIATO': '#8d9097', 'SPECIALE': '#3b2416'}


# ------------------------------------------------------------ small helpers
def ink(*ch, w=2, **kw):
    return G(*ch, stroke=OUT, stroke_width=w, stroke_linejoin='round', stroke_linecap='round', **kw)


def tr(x, y, s=1, rot=0):
    return 'translate(%s %s) rotate(%s) scale(%s)' % (f(x), f(y), f(rot), f(s))


def txt(s, x, y, size=10, fill=DARK, font='Comic Neue', weight=700, anchor='middle', **kw):
    return T('text', s, x=x, y=y, text_anchor=anchor, font_family=font + ', sans-serif', font_weight=weight,
             font_size=size, fill=fill, stroke='none', **kw)


def hid(x, y, n):
    return C(x, y, 9, '#f4c64e', stroke=OUT, stroke_width=1.5) + txt(str(n), x, y + 3.6, 10)


def rect_bg(H, col):
    return R(0, 0, W, H, col)


def water(y, H, col='#6fb3c4', wave='#8fcad8'):
    s = R(0, y, W, H - y, col, stroke='none')
    for i, (wx, wy) in enumerate([(20, 12), (80, 24), (150, 10), (40, 38), (120, 36), (180, 28)]):
        if y + wy < H - 4:
            s += P('M%s %s q6 -4 12 0 q6 4 12 0' % (f(wx), f(y + wy)), stroke=wave, stroke_width=2, stroke_linecap='round')
    return s


def reeds(x, yb, n=3, h=60, spread=10, seed=1):
    s = ''
    for i in range(n):
        dx = (i - (n - 1) / 2.0) * spread
        hh = h - (i % 2) * 10 - (i * 3) % 7
        lean = dx * 0.5
        s += P('M%s %s Q%s %s %s %s' % (f(x + dx), f(yb), f(x + dx + lean * 0.3), f(yb - hh * 0.5), f(x + dx + lean), f(yb - hh)),
               stroke='#4f7f36', stroke_width=2.4, stroke_linecap='round')
        s += E(x + dx + lean, yb - hh - 2, 2.8, 8, '#8a5a2b', stroke=OUT, stroke_width=1.2, transform='rotate(%s %s %s)' % (f(lean * 2), f(x + dx + lean), f(yb - hh)))
        s += P('M%s %s q-8 -14 -14 -26' % (f(x + dx), f(yb - 6)), stroke='#6a9a4a', stroke_width=2, stroke_linecap='round')
    return s


def boat(x, y, s=1, flip=False, oar=False):
    hull = (P('M-32 -6 L32 -6 L23 13 L-23 13 Z', '#b57a3e') + P('M-26 1 L26 1 M-23 7 L23 7', stroke='#8a5a2b', stroke_width=1.3)
            + R(-33, -9, 66, 4, '#8a5a2b', rx=2))
    return ink(hull, w=1.8, transform='translate(%s %s) scale(%s %s)' % (f(x), f(y), f(-s if flip else s), f(s)))


def post(x, y, h):
    return ink(R(x - 3.5, y, 7, h, '#7a5230', rx=2), E(x, y, 3.5, 2, '#9a6a3e'), w=1.8)


def feather(x, y, rot=0, col='#8d9097', s=1):
    return ink(P('M0 -18 Q10 -6 5 16 L0 24 L-5 16 Q-10 -6 0 -18 Z', col),
               P('M0 -16 L0 26', stroke='#ffffff' if col == '#8d9097' else '#8d9097', stroke_width=1, opacity=0.8),
               P('M0 -4 L6 -8 M0 4 L7 0 M0 -4 L-6 -8 M0 4 L-7 0', stroke='#ffffff' if col == '#8d9097' else '#8d9097', stroke_width=0.8, opacity=0.7),
               w=1.5, transform=tr(x, y, s, rot))


def horse(x, y, s=1, rot=0, col='#f4c64e', flip=False):
    legs_ = 'M-11 4 L-12 20 M-5 5 L-5 20 M6 5 L7 20 M12 4 L14 19'
    b = P(legs_, stroke=OUT, stroke_width=5.5) + P(legs_, stroke=col, stroke_width=2.6)
    b += P('M-14 -3 Q-25 2 -20 15', stroke=OUT, stroke_width=4.5) + P('M-14 -3 Q-25 2 -20 15', stroke=col, stroke_width=2)
    b += E(0, 0, 15, 8, col) + P('M8 -4 L14 -20 L21 -18 L18 -2 Z', col)
    b += P('M13 -21 L29 -17 L28 -10 L19 -10 Z', col) + P('M15 -21 L16 -28 L20 -21 Z', col)
    b += P('M13 -20 Q9 -12 7 -5', stroke='#d99a2b', stroke_width=2) + C(22, -16, 1.2, OUT, stroke='none')
    return ink(b, w=1.6, transform='translate(%s %s) rotate(%s) scale(%s %s)' % (f(x), f(y), f(rot), f(-s if flip else s), f(s)))


def sparkles(pts, col='#fff2b8'):
    s = ''
    for (x, y, r) in pts:
        s += star(x, y, r, col).replace('<path ', '<path stroke="#d99a2b" stroke-width="1" stroke-linejoin="round" ')
    return s


def nest(x, y, w=44, h=12):
    s = E(x, y, w / 2.0, h, '#b98a4a')
    for i in range(-4, 5):
        s += P('M%s %s l%s -%s' % (f(x + i * w / 9.5), f(y + h * 0.5), f(i * 1.2), f(h * 0.9)), stroke='#7a5230', stroke_width=1.2)
    return ink(s, w=1.8)


def priestess(x, y, s=1):
    b = [P('M-15 -2 L15 -2 L22 54 L-22 54 Z', '#d08a45'),
         P('M-17 20 L17 20 L18 26 L-18 26 Z', '#8a3a22'),
         P('M-12 22 l4 3 M-4 22 l4 3 M4 22 l4 3 M12 22 l-2 3', stroke='#f4c64e', stroke_width=1.2),
         limb(-14, 2, -20, 24, '#d08a45', 10, hand=TSK, hr=5), limb(14, 2, 20, 24, '#d08a45', 10, hand=TSK, hr=5),
         C(0, -22, 4, '#6a3a24') if False else C(0, -38, 9, '#3a2a20'),
         C(0, -18, 15, TSK),
         P('M-16 -20 Q-16 -36 0 -36 Q16 -36 16 -20 Q8 -28 0 -27 Q-8 -28 -16 -20 Z', '#3a2a20'),
         C(-15, -14, 3, '#c9803a', stroke_width=1.2), C(15, -14, 3, '#c9803a', stroke_width=1.2),
         face(0, -17, 'smile', my=-8, sp=6)]
    return ink(*b, transform=tr(x, y, s))


# ------------------------------------------------------------ illustrations
def il10(P_, H=175):
    s = rect_bg(H, '#d6ecee')
    s += R(0, 0, W, 70, '#cfe6ea', stroke='none') + cloud(150, 24, 0.7) + cloud(40, 40, 0.5)
    s += water(96, H)
    s += P('M0 96 Q40 86 80 98 L0 98 Z', '#8ab463') + P('M0 90 L0 H' .replace('H', str(H)) + ' L78 ' + str(H) + ' Q60 130 70 100 Q40 88 0 90 Z', '#79a85a', stroke=OUT, stroke_width=2)
    # tree on bank
    s += ink(P('M30 118 L34 60 L44 60 L48 118 Z', '#8a5a2b'), C(24, 42, 22, '#5f9a5a'), C(52, 36, 24, '#6bab62'), C(38, 22, 20, '#5f9a5a'),
             P('M44 78 Q64 70 80 74', stroke='#6a4220', stroke_width=5), w=2)
    s += feather(76, 82, 70, '#8d9097', 0.8)
    s += hid(98, 68, 19)
    s += reeds(180, 130, 4, 62, 9) + reeds(14, 160, 3, 50, 9) + reeds(200, 168, 3, 70, 8)
    s += post(135, 106, 38)
    s += P('M138 112 Q150 120 160 124', stroke='#c9a96a', stroke_width=2.5)
    s += boat(150, 134, 1.25)
    s += hid(150, 140, 22)
    s += P('M105 150 q6 -4 12 0 q6 4 12 0', stroke='#8fcad8', stroke_width=2, stroke_linecap='round')
    return s


def il11(P_, H=120):
    s = rect_bg(H, '#e8d9b8')
    s += R(0, 0, W, H, '#d9c59a', stroke='none') + R(10, 8, 195, 104, '#c9a96a', stroke=OUT, stroke_width=2, rx=4)
    s += ink(P('M107 14 L107 108', stroke=OUT), P('M107 16 Q60 8 16 16 L16 104 Q60 98 107 108 Z', '#fffdf3'),
             P('M107 16 Q154 8 198 16 L198 104 Q154 98 107 108 Z', '#fffdf3'), w=1.8)
    for yy in (34, 48, 62, 76, 90):
        s += P('M24 %s Q60 %s 100 %s' % (f(yy), f(yy - 3), f(yy)), stroke='#bcd3e6', stroke_width=1)
        s += P('M114 %s Q154 %s 190 %s' % (f(yy), f(yy - 3), f(yy)), stroke='#bcd3e6', stroke_width=1)
    s += ink(P('M92 56 L30 56 M44 40 L28 56 L44 72', stroke='#d9472f'), w=4)
    s += P('M122 36 q8 -6 12 2 t14 0 t12 -2 M122 52 q10 6 20 -2 t22 4 M122 70 q6 -8 14 0 t12 2 M150 84 q10 4 20 -2', stroke='#4f74a8', stroke_width=2, stroke_linecap='round')
    s += P('M40 90 q8 -8 16 0 t16 0', stroke='#7a5a3e', stroke_width=1.6, stroke_linecap='round')
    return s


def il12(P_, H=120):
    s = rect_bg(H, '#f1e2c0')
    s += E(108, 104, 76, 7, '#d8c49a', stroke='none')
    s += ink(P('M28 70 Q22 36 66 30 Q108 18 150 30 Q194 36 188 70 Z', '#d9a05a'),
             P('M30 70 L186 70 L180 78 L36 78 Z', '#ffe27a'),
             P('M48 80 Q60 86 72 80 Q84 90 96 80 Q110 88 124 80 Q138 90 150 80 Q162 86 172 80 L172 82 L48 82 Z', '#7ec060'),
             P('M30 82 L186 82 Q192 100 170 104 L48 104 Q24 100 30 82 Z', '#e8b469'), w=2.2)
    s += P('M52 44 Q60 36 76 36 M120 34 Q140 30 156 38', stroke='#f4d598', stroke_width=3, stroke_linecap='round')
    s += C(82, 52, 1.6, '#a8702f', stroke='none') + C(110, 46, 1.6, '#a8702f', stroke='none') + C(138, 52, 1.6, '#a8702f', stroke='none') + C(100, 58, 1.6, '#a8702f', stroke='none')
    for hx in (62, 110, 150):
        s += C(hx, 76, 3, '#f7e49a', stroke=OUT, stroke_width=1)
    return s


def il15(P_, H=120):
    s = rect_bg(H, '#e9dcc0')
    s += E(108, 100, 70, 8, '#cdbb92', stroke='none')
    ropecol, dark = '#d8b574', '#a8803f'
    rings = [(52, 12, 8), (46, 10, 4), (40, 8, 0), (34, 7, -4)]
    b = ''
    for rx, ry, dy in [(60, 24, 24), (52, 21, 14), (44, 18, 4), (34, 14, -6)]:
        b += E(108, 66 + dy * 0.5, rx, ry, 'none', stroke=OUT, stroke_width=11) + E(108, 66 + dy * 0.5, rx, ry, 'none', stroke=ropecol, stroke_width=8)
    for k in range(18):
        a = k * 20 * math.pi / 180
        b += P('M%s %s l3 4' % (f(108 + 60 * math.cos(a)), f(76 + 24 * math.sin(a))), stroke=dark, stroke_width=1.5)
    s += b
    s += P('M120 94 Q150 100 168 86 Q184 76 176 64', stroke=OUT, stroke_width=11, stroke_linecap='round') + P('M120 94 Q150 100 168 86 Q184 76 176 64', stroke=ropecol, stroke_width=8, stroke_linecap='round')
    s += P('M160 92 l3 4 M174 80 l4 2 M178 68 l2 4', stroke=dark, stroke_width=1.5)
    return s


def il16(P_, H=105):
    s = rect_bg(H, '#efe0bd')
    s += E(108, 96, 80, 7, '#d0bc92', stroke='none')
    s += ink(P('M50 30 L38 4 L176 4 L164 30 Z', '#9a6638'), P('M44 18 L170 18', stroke='#5e381c', stroke_width=2), w=2) if False else ''
    # open lid behind
    s += ink(R(48, 6, 120, 30, '#a56f3d', rx=4), P('M48 14 L168 14 M48 28 L168 28', stroke='#5e381c', stroke_width=1.4), w=2)
    # contents
    s += ink(R(66, 24, 70, 14, '#f1e2b8', rx=7), E(66, 31, 3.5, 7, '#d9c08a'), E(136, 31, 3.5, 7, '#d9c08a'),
             R(98, 23, 6, 16, '#c8483a'), w=1.6, transform='rotate(-8 100 31)')
    s += ink(E(150, 34, 18, 8, 'none', stroke='#d8b574', stroke_width=7), E(150, 34, 18, 8, 'none', stroke=OUT, stroke_width=1.2), w=1) if False else ''
    s += P('M134 36 Q150 26 166 36 Q150 44 134 36', stroke=OUT, stroke_width=9) + P('M134 36 Q150 26 166 36 Q150 44 134 36', stroke='#d8b574', stroke_width=6)
    # chest body
    s += ink(R(40, 40, 136, 52, '#b57a3e', rx=4), R(40, 40, 136, 10, '#8a5a2b'), R(40, 62, 136, 4, '#8a5a2b'),
             R(50, 40, 8, 52, '#7a5a3e'), R(158, 40, 8, 52, '#7a5a3e'), R(100, 48, 16, 20, '#e0b13c', rx=3), w=2)
    s += C(108, 56, 2.4, OUT, stroke='none') + P('M108 56 L108 62', stroke=OUT, stroke_width=2)
    s += sparkles([(90, 14, 5), (152, 12, 4), (120, 6, 3)])
    return s


def il18(P_, H=120):
    s = rect_bg(H, '#d6ecee')
    s += cloud(40, 22, 0.6) + cloud(180, 34, 0.5)
    s += post(108, 98, 24)
    s += nest(108, 96, 80, 13)
    s += becco(108, 62, 0.5, flip=False, legs_on=False)
    s += horse(88, 82, 0.55)
    s += P('M82 38 Q90 50 104 46', stroke=OUT, stroke_width=2.4, stroke_linecap='round') if False else ''
    s += sparkles([(66, 70, 5), (142, 76, 4)])
    s += P('M72 90 Q108 100 144 90 Q144 104 108 106 Q72 104 72 90 Z', '#b98a4a', stroke=OUT, stroke_width=1.8) if False else ''
    s += nest(108, 100, 84, 11)
    # grin
    s += P('M80 40 Q86 47 94 41', stroke=OUT, stroke_width=1.6, stroke_linecap='round', opacity=0)
    return s


def il19(P_, H=120):
    s = rect_bg(H, '#e5efe0')
    s += R(0, 88, W, 32, '#9ac17a', stroke='none') + P('M0 88 L215 88', stroke=OUT, stroke_width=1.8)
    s += feather(138, 52, 38, '#8d9097', 2.1)
    s += leo(54, 72, 0.5, rot=0, eyes='closed', mouth='oh', wing='small')
    s += P('M82 70 q4 -4 8 0 M84 78 q5 -2 9 2', stroke='#7a5a3e', stroke_width=1.6, stroke_linecap='round')
    return s


def il22(P_, H=120):
    s = rect_bg(H, '#d6ecee')
    s += cloud(170, 20, 0.6)
    s += water(70, H)
    s += R(0, 60, 54, 60, '#8ab463', stroke=OUT, stroke_width=1.8) if False else ''
    s += post(150, 56, 58)
    s += P('M150 66 Q130 76 118 82', stroke='#c9a96a', stroke_width=2.8) + P('M150 66 Q130 76 118 82', stroke=OUT, stroke_width=0.8, opacity=0)
    s += boat(96, 82, 1.55)
    s += P('M40 94 q8 -4 16 0 t16 0 M120 104 q8 -4 16 0 t16 0', stroke='#cfeaf0', stroke_width=2, stroke_linecap='round')
    return s


def il24(P_, H=120):
    s = rect_bg(H, '#f1e4d0')
    s += becco(108, 62, 0.82, rot=-8, flip=False, wings='up', legs_on=False)
    s += txt('HA HA HA!', 160, 30, 20, '#d9472f', 'Bangers', 400, transform='rotate(10 160 30)') if False else T('text', 'HA HA!', x=160, y=34, text_anchor='middle', font_family='Bangers, sans-serif', font_size=22, fill='#d9472f', stroke=OUT, stroke_width=0.8, transform='rotate(12 160 34)')
    s += P('M96 20 q-3 6 0 10 q3 -4 0 -10 Z', '#bfe3f2', stroke=OUT, stroke_width=1) if False else ''
    s += P('M136 52 Q148 54 152 66 M140 70 Q150 74 150 86', stroke=OUT, stroke_width=2, stroke_linecap='round')
    return s


def il27(P_, H=150):
    s = rect_bg(H, '#d6ecee')
    s += cloud(40, 20, 0.5) + cloud(176, 26, 0.5)
    s += water(112, H)
    s += R(0, 98, W, 14, '#b9d6a0', stroke='none')
    s += reeds(26, 130, 5, 100, 10) + reeds(196, 132, 5, 96, 10) + reeds(58, 138, 3, 70, 9) + reeds(166, 140, 3, 74, 9)
    s += post(108, 80, 70)
    s += nest(108, 84, 70, 12)
    s += becco(108, 54, 0.46, legs_on=False)
    s += hid(108, 32, 18)
    # gleam
    s += horse(134, 78, 0.4)
    s += sparkles([(150, 64, 6), (124, 66, 4), (158, 80, 4)])
    return s


def il29(P_, H=110):
    s = rect_bg(H, '#d6ecee')
    s += cloud(50, 16, 0.5)
    s += water(78, H)
    s += toni(44, 56, 0.42, expr='happy') + nico(98, 58, 0.42, expr='happy', la=(-20, 24), ra=(30, 22), pack=False) + sofia(150, 52, 0.42, expr='smile')
    s += ink(P('M-8 0 L-30 24', stroke='#8a5a2b', stroke_width=3.5), E(-31, 25, 3, 9, '#c8854a'), w=1.4, transform='translate(118 74) rotate(10)') if False else ''
    s += boat(100, 90, 2.1)
    # oar
    s += ink(P('M112 66 L150 104', stroke='#8a5a2b', stroke_width=3.5), P('M148 98 L158 106 L152 112 L142 104 Z', '#c8854a'), w=1.4)
    s += P('M146 110 q6 -4 12 0 q6 4 12 0', stroke='#cfeaf0', stroke_width=2, stroke_linecap='round')
    s += leo(188, 30, 0.3, wing='open', eyes='open', mouth='smile')
    return s


def il30(P_, H=130):
    s = rect_bg(H, '#d6ecee')
    s += cloud(170, 18, 0.5)
    s += water(84, H, '#7a9a86', '#9ab8a2')
    s += post(66, 70, 20)
    s += nest(66, 68, 66, 11)
    s += becco(66, 40, 0.42, legs_on=False)
    # sandwich in beak
    s += ink(P('M-8 0 Q0 -8 8 0 Z', '#d9a05a'), R(-8, 0, 16, 2.5, '#7ec060'), P('M-8 2 L8 2 L6 6 L-6 6 Z', '#e8b469'), w=1.2, transform=tr(42, 28, 1.1, -10))
    # falling horse
    s += horse(112, 50, 0.45, rot=70)
    s += P('M104 62 l-3 10 M116 62 l1 10', stroke='#9fb5c0', stroke_width=1.6, stroke_linecap='round')
    s += T('text', 'PLOF!', x=158, y=60, text_anchor='middle', font_family='Bangers, sans-serif', font_size=24, fill='#e2573a', stroke=OUT, stroke_width=0.9, transform='rotate(-8 158 60)')
    # ring of bubbles
    for k in range(8):
        a = k * math.pi / 4
        s += C(134 + 16 * math.cos(a), 106 + 9 * math.sin(a), 3.2 + (k % 3), '#e9f6ee', stroke=OUT, stroke_width=1.2, fill_opacity=0.85)
    s += hid(178, 106, 35)
    return s


def il31(P_, H=120):
    s = rect_bg(H, '#e3eef0')
    s += water(76, H)
    heron = (P('M-6 24 L-6 44 M6 24 L6 44', stroke=OUT, stroke_width=3)
             + P('M-6 44 l-6 3 M6 44 l-6 3', stroke=OUT, stroke_width=2)
             + P('M-24 14 Q-34 -6 -18 -12 Q8 -22 28 -4 Q30 12 14 26 Q-6 32 -24 14 Z', '#ffffff')
             + P('M-4 4 Q8 -6 22 0', stroke='#cfd3da', stroke_width=1.6)
             + P('M22 -2 Q40 -10 34 -34 Q32 -46 40 -52', stroke=OUT, stroke_width=9) + P('M22 -2 Q40 -10 34 -34 Q32 -46 40 -52', stroke='#ffffff', stroke_width=5.5)
             + C(40, -54, 7, '#ffffff') + P('M46 -56 L74 -50 L46 -50 Z', '#f0c24a')
             + C(42, -56, 1.6, OUT, stroke='none')
             + P('M34 -60 Q24 -66 20 -58', stroke=OUT, stroke_width=2.4))
    s += ink(heron, w=2, transform=tr(98, 66, 1.05))
    s += P('M70 108 q8 -4 16 0 t16 0 M120 100 q8 -4 16 0 t16 0', stroke='#cfeaf0', stroke_width=2, stroke_linecap='round')
    s += E(100, 112, 24, 4, '#5a8fa0', stroke='none', opacity=0.5)
    return s


def il35(P_, H=120):
    s = rect_bg(H, '#c9ab7a')
    s += R(0, 0, W, 22, '#e3eef0', stroke='none')
    s += R(0, 22, W, 98, '#9a7c52', stroke='none')
    s += P('M0 24 q10 -4 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0', stroke='#cfeaf0', stroke_width=2.4)
    for (bx, by, br) in [(100, 76, 4), (108, 62, 5.5), (98, 46, 4.5), (112, 36, 6), (104, 24, 3.5), (84, 70, 3), (130, 56, 3.5), (120, 80, 3)]:
        s += C(bx, by, br, '#efe3c8', stroke=OUT, stroke_width=1.3, fill_opacity=0.8)
    s += ink(P('M0 120 L0 104 Q40 96 70 106 Q110 112 150 104 Q190 96 215 106 L215 120 Z', '#6e5538'), w=2)
    s += horse(108, 108, 0.55, rot=-10, col='#f4c64e') if False else ''
    s += ink(P('M92 106 Q100 96 108 100 Q118 92 126 106 Z', '#f4c64e'), w=1.6)
    s += sparkles([(116, 94, 4), (88, 98, 3)])
    s += E(40, 100, 14, 4, '#7d6445', stroke='none') + E(176, 98, 12, 4, '#7d6445', stroke='none')
    return s


def il39(P_, H=120):
    s = rect_bg(H, '#efdcbc')
    s += R(0, 96, W, 24, '#cdb98c', stroke='none') + P('M0 96 L215 96', stroke=OUT, stroke_width=1.8)
    s += ink(R(14, 42, 108, 12, '#d9d0bd', rx=2), R(20, 54, 96, 44, '#cfc4ac'), R(14, 96, 108, 4, '#b9ad92') if False else R(16, 96, 104, 4, '#b9ad92'), w=2)
    s += R(26, 60, 84, 28, '#b9ad92', stroke=OUT, stroke_width=1.4)
    s += P('M32 82 L38 66 L44 82 L50 66 M56 66 L56 82 L66 82 M72 66 L84 66 L72 82 L86 82 M92 66 L92 82 M92 74 L102 74 M102 66 L102 82', stroke='#5e4a30', stroke_width=2, stroke_linecap='round', stroke_linejoin='round')
    s += sofia(166, 66, 0.55, expr='happy', la=(-24, 16), ra=(22, -44))
    s += glow_(160, 33, 'g39')
    s += horse(172, 34, 0.5)
    s += sparkles([(150, 20, 5), (196, 26, 4), (180, 12, 3)])
    return s


def il43(P_, H=110):
    s = rect_bg(H, '#efdcbc')
    s += R(0, 88, W, 22, '#cdb98c', stroke='none') + P('M0 88 L215 88', stroke=OUT, stroke_width=1.8)
    s += glow_(108, 44, 'g43', 38)
    s += ink(R(76, 62, 64, 8, '#d9d0bd', rx=2), R(82, 70, 52, 20, '#cfc4ac'), w=1.8)
    s += horse(108, 50, 0.6)
    s += sparkles([(80, 36, 5), (136, 34, 5), (108, 18, 4)])
    s += priestess(44, 36, 0.52)
    s += leo(176, 56, 0.42, wing='open', eyes='closed', mouth='smile', la=(-34, -24), ra=(34, -24))
    s += becco(198, 90, 0.2, flip=False, legs_on=False) if False else ''
    s += becco(24, 98, 0.0001) if False else ''
    return s


def glow_(cx, cy, gid, r=22):
    return ('<defs><radialGradient id="%s" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff6cf" stop-opacity="1"></stop>'
            '<stop offset="0.5" stop-color="#ffe9a3" stop-opacity="0.6"></stop><stop offset="1" stop-color="#ffe9a3" stop-opacity="0"></stop>'
            '</radialGradient></defs>' % gid) + C(cx, cy, r, 'url(#%s)' % gid, stroke='none')


def il50(P_, H=120):
    s = rect_bg(H, '#d6ecee')
    s += cloud(150, 16, 0.5)
    s += R(0, 58, 96, 62, '#8ab463', stroke=OUT, stroke_width=1.8)
    s += water(84, H)
    s += R(0, 58, 100, 30, '#8ab463', stroke=OUT, stroke_width=1.8)
    s += toni(22, 36, 0.4, expr='smile', la=(-14, 8), ra=(14, 8))
    s += ink(E(40, 38, 10, 7, 'none', stroke='#d8b574', stroke_width=4), w=1.2)
    s += nico(60, 38, 0.4, expr='det', la=(-14, 12), ra=(24, 16))
    # rope down
    s += P('M74 50 Q110 46 140 62 L148 86', stroke=OUT, stroke_width=5, stroke_linecap='round') + P('M74 50 Q110 46 140 62 L148 86', stroke='#d8b574', stroke_width=3, stroke_linecap='round')
    s += sofia(120, 32, 0.0001) if False else ''
    s += horse(150, 92, 0.55, rot=-12)
    s += P('M144 108 q-2 6 0 9 M158 104 q2 6 0 9', stroke='#9fb5c0', stroke_width=1.8, stroke_linecap='round')
    s += sparkles([(176, 80, 5), (130, 78, 4)])
    s += sofia(188, 54, 0.4, expr='happy', la=(-34, 10), ra=(-40, 0), flip=True) if False else ''
    s += sofia(104, 28, 0.0001) if False else ''
    return s


def il_segna(P_, H=150):
    s = rect_bg(H, '#fff6dc')
    for k in range(10):
        c, r = k % 5, k // 5
        cx, cy = 22 + c * 43, 36 + r * 74
        s += ink(P('M0 -26 Q14 -10 8 20 L0 32 L-8 20 Q-14 -10 0 -26 Z', '#f4c64e'),
                 P('M0 -24 L0 34', stroke='#d99a2b', stroke_width=1.6), P('M0 -8 L9 -14 M0 2 L10 -4 M0 12 L8 8 M0 -8 L-9 -14 M0 2 L-10 -4 M0 12 L-8 8', stroke='#d99a2b', stroke_width=1.2),
                 w=1.8, transform=tr(cx, cy, 1, 12))
        s += C(cx, cy + 40, 6.5, '#ffffff', stroke=OUT, stroke_width=1.8)
    return s


# ------------------------------------------------------------ card builder
def fmt(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<span style="color: #a8322a; font-weight: 700">\1</span>', text)


def card(typ, num, title, text, body, H=120, strip=None, label=None, star_=False):
    col = TYPES[typ]
    big = typ in ('OGGETTO ROSSO', 'OGGETTO BLU')
    if star_:
        circ = ('<div style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 50%; background: #ffffff; border: 2px solid #3b2416; display: flex; align-items: center; justify-content: center">'
                '<svg viewBox="0 0 16 16" width="14" height="14" role="img" aria-label="stella">' + star(8, 8, 7.5, '#f4c64e').replace('<path ', '<path stroke="#3b2416" stroke-width="1" stroke-linejoin="round" ') + '</svg></div>')
    elif big:
        circ = ('<div style="width: 30px; height: 30px; box-sizing: border-box; border-radius: 50%%; background: %s; border: 2px solid #3b2416; color: #ffffff; display: flex; align-items: center; justify-content: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 16px">%s</div>' % (col, num))
    else:
        circ = ('<div style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 50%%; background: #ffffff; border: 2px solid #3b2416; color: #2a1a10; display: flex; align-items: center; justify-content: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 13px">%s</div>' % num)
    h = '<div style="width: 238px; height: 333px; box-sizing: border-box; border: 2px solid #3b2416; border-radius: 10px; background: #fdf8ee; overflow: hidden; display: flex; flex-direction: column">\n'
    h += '<div style="height: 30px; flex-shrink: 0; background: %s; display: flex; align-items: center; justify-content: space-between; padding: 0 8px; font-family: \'Comic Neue\', sans-serif"><span style="font-weight: 700; font-size: 11px; color: #ffffff; text-transform: uppercase; letter-spacing: 0.5px">%s</span>%s</div>\n' % (col, label or typ, circ)
    if strip:
        h += '<div style="flex-shrink: 0; background: #fbe7a6; border-bottom: 1.5px solid #3b2416; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 11px; text-align: center; padding: 3px; color: #2a1a10">%s</div>\n' % strip
    h += '<div style="flex-shrink: 0; font-family: \'Bangers\', \'Comic Neue\', sans-serif; font-size: 21px; color: #2a1a10; text-align: center; margin: 6px 6px 2px; line-height: 1; letter-spacing: 0.3px">%s</div>\n' % title
    h += '<div style="flex-shrink: 0; margin: 4px 8px 0; border: 1.5px solid #3b2416; border-radius: 6px; overflow: hidden; line-height: 0; height: %dpx; box-sizing: content-box">' % H
    h += '<svg viewBox="0 0 215 %d" width="100%%" height="%d" preserveAspectRatio="xMidYMid slice" style="display: block" role="img" aria-label="%s">%s</svg></div>\n' % (H, H, ARIA[num] if num in ARIA else ARIA[title], body)
    h += '<div style="flex: 1; padding: 6px 10px 8px; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 11.5px; line-height: 1.25; color: #2a1a10">%s</div>\n' % fmt(text)
    h += '</div>'
    return h


ARIA = {
    10: 'Riva del fiume con canne, una barchetta legata a un palo e un albero con una piuma grigia su un ramo',
    11: 'Taccuino aperto con una freccia verso sinistra e alcuni scarabocchi',
    12: 'Un grosso panino con pane e formaggio',
    15: 'Una corda robusta arrotolata',
    16: 'La cassa aperta con dentro una mappa arrotolata e una corda',
    18: 'Becco su un nido in cima a un palo, con il cavallino d\'oro tra le zampe',
    19: 'Una piuma grigia e Leo che la annusa',
    22: 'Una barchetta di legno legata a un palo, senza remi',
    24: 'Becco che ride',
    27: 'Canneto con un palo e un nido; Becco col cappello da capitano sul nido e un luccichio dorato',
    29: 'Nico rema sulla barca con Sofia e Toni a bordo, Leo vola sopra',
    30: 'Becco mangia il panino sul nido; sotto, bolle in cerchio nell\'acqua dove è caduto il cavallino',
    31: 'Un airone bianco in piedi nell\'acqua',
    35: 'Bolle che salgono da acqua bassa e fangosa, con un luccichio dorato sul fondo',
    39: 'L\'altare vuoto con una fascia di segni incisi e Sofia che alza il cavallino d\'oro',
    43: 'Il cavallino d\'oro che brilla sull\'altare, la sacerdotessa sorride e Leo festeggia',
    50: 'Toni fa un cappio, Nico cala la corda, Sofia tira su il cavallino d\'oro',
    'LE VOSTRE PIUME': 'Dieci grandi piume dorate con un cerchietto da spuntare sotto ciascuna',
}

HEAD = '''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>%(title)s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bangers&amp;family=Comic+Neue:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
body{margin:0}
</style>
</helmet>
<div style="position: relative; width: 794px; height: 1123px; background: #ffffff; overflow: hidden; font-family: 'Comic Neue', sans-serif">
<div style="position: absolute; left: 0; top: 18px; width: 794px; height: 16px; line-height: 16px; text-align: center; font-family: 'Comic Neue', sans-serif; font-size: 11px; color: #7a5a3e">%(header)s</div>
<div style="position: absolute; left: 30px; top: 52px; width: 734px; height: 1019px; display: grid; grid-template-columns: 238px 238px 238px; grid-template-rows: 333px 333px 333px; gap: 10px">
'''
TAIL = '''</div>
<div style="position: absolute; left: 0; top: 1089px; width: 794px; height: 16px; line-height: 16px; text-align: center; font-family: 'Comic Neue', sans-serif; font-size: 11px; color: #7a5a3e">Chi ritaglia: cerca di non leggere le carte!</div>
</div>
</x-dc>
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


def write(name, title, header, cards):
    html = HEAD % {'title': title, 'header': header} + '\n'.join(cards) + '\n' + TAIL
    open(OUTDIR + name, 'w', encoding='utf-8').write(html)
