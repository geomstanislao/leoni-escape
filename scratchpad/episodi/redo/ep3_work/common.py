import re, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/redo/ep3_work')
from lib import *

OUTDIR = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escape/project/'
W = 215

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

TYPES = {'LUOGO': '#5f9a5a', 'OGGETTO ROSSO': '#d9472f', 'OGGETTO BLU': '#4f74a8', 'PERSONAGGIO': '#c99a2e',
         'INDIZIO': '#7a5a3e', 'ENIGMA': '#8a5fb0', 'COMBINAZIONE': '#e39a3b', 'RISPOSTA': '#e39a3b',
         'SBAGLIATO': '#8d9097', 'SPECIALE': '#3b2416'}

GRID_L, GRID_T, CW, CH, GAP = 30, 52, 238, 333, 10


def tx(s, x, y, size=10, fill='#2a1a10', anchor='middle', font='Comic Neue', weight=700, **kw):
    return T('text', s, x=x, y=y, text_anchor=anchor, font_family=font, font_weight=weight, font_size=size, fill=fill, stroke='none', **kw)


def hid(x, y, n):
    return G(C(x, y, 9, '#f4c64e', stroke=OUT, stroke_width=1.5),
             T('text', str(n), x=x, y=y + 3.6, text_anchor='middle', font_family='Comic Neue', font_weight=700,
               font_size=10, fill='#2a1a10', stroke='none'))


def star_gold(cx, cy, r, fill='#f4c64e'):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append('%s,%s' % (f(round(cx + rr * math.cos(a), 2)), f(round(cy + rr * math.sin(a), 2))))
    return T('polygon', points=' '.join(pts), fill=fill, stroke=OUT, stroke_width=1.6, stroke_linejoin='round')


def svg(H, body, aria, defs=''):
    return T('svg', defs, body, viewBox='0 0 %s %s' % (W, f(H)), preserveAspectRatio='xMidYMid meet',
             style='width: 100%%; height: %spx; display: block' % f(H), role='img', aria_label=aria)


def rgrad_def(gid, c='#fff2b8', o=1):
    return T('radialGradient', T('stop', offset=0, stop_color=c, stop_opacity=o) + T('stop', offset=1, stop_color=c, stop_opacity=0),
             id=gid, cx=0.5, cy=0.5, r=0.5)


def fmt_text(t):
    return re.sub(r'\*\*(.+?)\*\*', r'<b style="color: #a8322a">\1</b>', t)


def band_circle(num, typ):
    if num is None:
        inner = '<svg viewBox="0 0 20 20" style="width: 16px; height: 16px; display: block">%s</svg>' % star_gold(10, 10.5, 9)
        return '<div style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 50%%; background: #ffffff; border: 2px solid #3b2416; display: flex; align-items: center; justify-content: center">%s</div>' % inner
    if typ == 'OGGETTO ROSSO' or typ == 'OGGETTO BLU':
        col = '#d9472f' if typ == 'OGGETTO ROSSO' else '#4f74a8'
        return '<div style="width: 30px; height: 30px; box-sizing: border-box; border-radius: 50%%; background: %s; border: 2px solid #3b2416; display: flex; align-items: center; justify-content: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 16px; color: #ffffff; line-height: 1">%s</div>' % (col, num)
    return '<div style="width: 24px; height: 24px; box-sizing: border-box; border-radius: 50%%; background: #ffffff; border: 2px solid #3b2416; display: flex; align-items: center; justify-content: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 13px; color: #2a1a10; line-height: 1">%s</div>' % num


def card_front(typ, num, title, H, svgs, text=None, strip=None, text_html=None):
    col = TYPES[typ]
    out = ['<div style="width: 238px; height: 333px; box-sizing: border-box; border: 2px solid #3b2416; border-radius: 10px; background: #fdf8ee; overflow: hidden; display: flex; flex-direction: column; font-family: \'Comic Neue\', sans-serif">']
    out.append('<div style="height: 30px; flex: none; box-sizing: border-box; background: %s; display: flex; align-items: center; justify-content: space-between; padding: 0 8px"><span style="font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 11px; color: #ffffff; text-transform: uppercase; letter-spacing: 0.5px">%s</span>%s</div>' % (col, typ, band_circle(num, typ)))
    if strip:
        out.append('<div style="flex: none; background: #fbe7a6; border-bottom: 1.5px solid #3b2416; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 11px; text-align: center; padding: 3px; color: #2a1a10">%s</div>' % strip)
    out.append('<div style="flex: none; font-family: \'Bangers\', sans-serif; font-size: 21px; color: #2a1a10; text-align: center; margin: 6px 6px 2px; line-height: 1">%s</div>' % title)
    out.append('<div style="flex: none; margin: 0 8px; box-sizing: border-box; height: %spx; border: 1.5px solid #3b2416; border-radius: 6px; overflow: hidden; background: #f6ead2">%s</div>' % (f(H + 3), svgs))
    if text_html is None:
        text_html = fmt_text(text)
    out.append('<div style="flex: 1; min-height: 0; box-sizing: border-box; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 11.5px; line-height: 1.25; color: #2a1a10; padding: 6px 10px 8px">%s</div>' % text_html)
    out.append('</div>')
    return '\n'.join(out)


def card_back(num):
    if num is None:
        mid = '<svg viewBox="0 0 80 80" style="width: 80px; height: 80px; display: block">%s</svg>' % star_gold(40, 42, 36)
    else:
        mid = '<span style="font-family: \'Bangers\', sans-serif; font-size: 74px; color: #3b2416; line-height: 1; margin-top: 4px">%s</span>' % num
    return ('<div style="position: relative; width: 238px; height: 333px; box-sizing: border-box; border: 2px solid #3b2416; border-radius: 10px; overflow: hidden; background-color: #f6ead2; background-image: radial-gradient(circle, #e6c874 1.4px, transparent 2px); background-size: 14px 14px">\n'
            '<div style="position: absolute; left: 0; top: 18px; width: 100%%; text-align: center; font-family: \'Bangers\', sans-serif; font-size: 18px; letter-spacing: 1px; color: #7a5a3e; line-height: 1">LEONI DI LAGUNA</div>\n'
            '<div style="position: absolute; left: 41px; top: 88px; width: 152px; height: 152px; box-sizing: border-box; border-radius: 50%%; border: 3px dotted #e2b24a"></div>\n'
            '<div style="position: absolute; left: 57px; top: 104px; width: 120px; height: 120px; box-sizing: border-box; border-radius: 50%%; background: #fdf8ee; border: 2px solid #3b2416; display: flex; align-items: center; justify-content: center">%s</div>\n'
            '<div style="position: absolute; left: 0; bottom: 18px; width: 100%%; text-align: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 10px; color: #7a5a3e; line-height: 1">Escape · Il cavallino d\'oro</div>\n'
            '</div>') % mid


def sheet(title, header, cards, footer=None):
    """cards: list of 9 html strings (row-major)."""
    o = ['<div style="position: relative; width: 794px; height: 1123px; background: #ffffff; overflow: hidden; font-family: \'Comic Neue\', sans-serif">']
    o.append('<div style="position: absolute; left: 0; top: 19px; width: 794px; text-align: center; font-family: \'Comic Neue\', sans-serif; font-size: 11px; color: #7a5a3e; line-height: 14px">%s</div>' % header)
    for i, c in enumerate(cards):
        r, k = divmod(i, 3)
        o.append('<div style="position: absolute; left: %spx; top: %spx; width: 238px; height: 333px">\n%s\n</div>' % (GRID_L + k * (CW + GAP), GRID_T + r * (CH + GAP), c))
    if footer:
        o.append('<div style="position: absolute; left: 0; top: 1087px; width: 794px; text-align: center; font-family: \'Comic Neue\', sans-serif; font-size: 11px; color: #7a5a3e; line-height: 14px">%s</div>' % footer)
    o.append('</div>')
    return HEAD % title + '\n'.join(o) + '\n' + TAIL


def write(name, html):
    with open(OUTDIR + name, 'w', encoding='utf-8') as fh:
        fh.write(html)


# ------------------------------------------------------------------ props
def ink(*ch, **kw):
    sw = kw.pop('sw', 2)
    return G(*ch, stroke=OUT, stroke_width=sw, stroke_linejoin='round', stroke_linecap='round', **kw)


def horse(x, y, s=1, fill='#6f9a84', dark='#47705e', flip=False):
    b = []
    b.append(P('M-14 -24 Q-28 -23 -24 -5 Q-19 -14 -14 -17 Z', dark))
    for lx in (-13, -5.5, 6, 13):
        b.append(R(lx, -14, 5.5, 15, fill if lx in (-5.5, 13) else dark))
    b.append(E(0, -20, 17, 8.5, fill))
    b.append(P('M8 -24 L12 -42 L21 -40 L17 -20 Z', fill))
    b.append(P('M12 -42 L20 -47 L23 -43 L31 -35 L29 -31 L22 -33 L17 -34 Z', fill))
    b.append(P('M18 -46 L19.5 -53 L23 -45 Z', fill))
    b.append(P('M10 -43 Q3 -35 7 -25', 'none', stroke=dark, stroke_width=4))
    b.append(C(24.5, -39.5, 1.3, '#2a1a10', stroke='none'))
    return ink(*b, transform=xf(x, y, s, 0, flip))


def torch(x, y, s=1):
    b = []
    b.append(C(0, -18, 17, '#ffe08a', stroke='none', opacity=0.5))
    b.append(P('M-9 12 L9 12 L9 17 L-9 17 Z', '#6b4428'))
    b.append(R(-3, -4, 6, 30, '#8b5a2b'))
    b.append(P('M-8 -7 L8 -7 L5 4 L-5 4 Z', '#6b4428'))
    b.append(P('M0 -36 Q10 -23 9 -15 Q8 -7 0 -7 Q-8 -7 -9 -15 Q-10 -25 0 -36 Z', '#f08a24'))
    b.append(P('M0 -26 Q5.5 -18 4.5 -13 Q3.5 -9 0 -9 Q-3.5 -9 -4.5 -13 Q-5 -19 0 -26 Z', '#ffe36a', stroke='none'))
    return ink(*b, transform=xf(x, y, s, 0, False))


def altar(x, yb, w=42, h=26, fill='#8b5a2b'):
    b = [R(x - w / 2, yb - h, w, h, fill), R(x - w / 2 - 5, yb - h - 8, w + 10, 8, '#a8703f')]
    for k in (-1, 0, 1):
        b.append(L(x + k * w / 4.0 + w / 8.0, yb - h + 2, x + k * w / 4.0 + w / 8.0, yb - 2, '#6b4428', 1.3))
    return ink(*b)


GL = {1: 'M4 20 L12 4 L20 20', 2: 'M12 3 L12 21 M6 5 L6 11 Q6 15 12 15 Q18 15 18 11 L18 5',
      3: 'M12 3 L21 12 L12 21 L3 12 Z', 4: 'M5 5 L19 19 M19 5 L5 19', 5: 'M2 5 L7 19 L12 8 L17 19 L22 5'}


def glyph(n, cx, cy, size=24):
    sc = size / 24.0
    if n == 6:
        inner = C(12, 12, 8, 'none') + P('M12 4 L12 20 M4 12 L20 12')
    else:
        inner = P(GL[n])
    return G(inner, transform='translate(%s %s) scale(%s) translate(-12 -12)' % (f(cx), f(cy), f(round(sc, 3))),
             fill='none', stroke=OUT, stroke_width=3, stroke_linecap='round', stroke_linejoin='round')


def feather(x, y, n=15, rot=0, col='#8d9097', edge=OUT):
    w = n * 0.3
    body = P('M0 %s Q%s %s %s %s Q0 %s %s %s Q%s %s 0 %s Z' % (
        f(-n / 2), f(w), f(-n * 0.15), f(w * 0.6), f(n * 0.35), f(n * 0.5), f(-w * 0.6), f(n * 0.35), f(-w), f(-n * 0.15), f(-n / 2)),
        col, stroke=edge, stroke_width=1.2, stroke_linejoin='round')
    q = L(0, -n / 2 + 2, 0, n / 2 + 3, edge, 1)
    return G(body, q, transform='translate(%s %s) rotate(%s)' % (f(x), f(y), f(rot)))


def priestess(x, y, s=1):
    b = []
    b.append(P('M-18 -14 Q-20 24 -27 58 L27 58 Q20 24 18 -14 Z', '#c8683f'))
    b.append(P('M-18 -14 Q0 -4 18 -14 L22 30 Q0 38 -22 30 Z', '#d9a441'))
    b.append(P('M-22 40 Q0 48 22 40', 'none', stroke='#7a3e1d', stroke_width=1.6))
    b.append(R(-21, 9, 42, 9, '#7a3e1d'))
    for i in range(5):
        cx = -16 + i * 8
        b.append(P('M%s 13.5 l3 -3.5 l3 3.5 l-3 3.5 Z' % f(cx), '#f4c64e', stroke='none'))
    b.append(limb(-16, -9, -6, 2, '#d9a441', 13))
    b.append(limb(16, -9, 6, 2, '#d9a441', 13))
    b.append(C(0, -37, 22, '#2a1a10'))
    b.append(C(0, -62, 9, '#2a1a10'))
    b.append(C(0, -36, 19, SK))
    b.append(P('M-20 -38 Q-18 -56 0 -56 Q18 -56 20 -38 Q10 -47 0 -47 Q-10 -47 -20 -38 Z', '#2a1a10'))
    b.append(P('M-17 -49 Q0 -56 17 -49', 'none', stroke='#d9a441', stroke_width=2.4))
    b.append(C(-19.5, -29, 3.2, '#b87a33', stroke_width=1.5) + C(19.5, -29, 3.2, '#b87a33', stroke_width=1.5))
    b.append(face(0, -35, 'worry', my=-24, sp=7))
    return ink(*b, transform=xf(x, y, s, 0, False))


def ptag(*a):
    return ''.join(a)
