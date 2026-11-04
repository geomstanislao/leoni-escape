import sys, math, random
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep2a')
from lib import *

OUTD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'
OCHRE, OLIVE, TERRA, WHITE = '#d1a85a', '#9a9a5a', '#c8683f', '#efe6d0'

W, H = 794, 1123
b = []
defs = gid_defs(('e2cg1', 'v', [(0, '#4fa8e6', 1), (0.55, '#9fd6f0', 1), (1, '#fdf0c8', 1)]),
                ('e2cg2', 'v', [(0, '#7fd0cc', 1), (0.4, '#45a9b2', 1), (1, '#1f6e82', 1)]),
                ('e2cg3', 'r', [(0, '#fff6cf', 1), (0.4, '#ffe9a3', 0.6), (1, '#ffe9a3', 0)]),
                ('e2cg4', 'r', [(0, '#fff8d8', 0.9), (0.5, '#ffe9a3', 0.4), (1, '#ffe9a3', 0)]))
b.append(R(0, 0, W, 650, 'url(#e2cg1)'))
b.append(C(150, 520, 240, 'url(#e2cg3)', stroke='none'))
b.append(C(150, 520, 50, '#fff7c4', stroke='none'))
b.append(cloud(640, 380, 1.3, 0.9) + cloud(380, 360, 0.9, 0.85) + cloud(60, 340, 1.0, 0.85) + cloud(720, 560, 0.8, 0.8))
b.append(P('M0 600 Q140 560 300 590 Q460 552 620 588 Q720 566 794 584 L794 660 L0 660 Z', '#a9bc98', stroke='none'))
# far town
far = [(0, 70, 60, '#e8d5b0'), (76, 60, 76, '#d9c29a'), (140, 74, 54, '#efe0c2'), (220, 64, 70, '#e0c9a0'), (290, 70, 56, '#e8d5b0'), (362, 56, 66, '#d9c29a'), (430, 70, 52, '#efe0c2'), (500, 66, 62, '#e0c9a0')]
for (x, w, h, wall) in far:
    b.append(house(x, 640, w, h, wall, TERRA, door=False, win=(w > 60)))
b.append(temple(572, 650, 190, 150))
b.append(cypress(560, 650, 90, 20) + cypress(772, 650, 100, 22) + cypress(204, 650, 70, 16) + cypress(470, 650, 60, 14))
# water
b.append(R(0, 640, W, 300, 'url(#e2cg2)'))
b.append(L(0, 640, W, 640, '#ffe9b0', 2, opacity=0.7))
# bridge
b.append(bridge(30, 530, 626, 16, 716, 5))
# reflections / glints
gl = []
for (x, y, w) in [(60, 730, 120), (300, 740, 100), (600, 700, 140), (150, 880, 120), (520, 890, 150), (360, 900, 90), (700, 760, 80), (30, 800, 90)]:
    gl.append(P('M%s %s Q%s %s %s %s' % (f(x), f(y), f(x + w / 2.0), f(y - 7), f(x + w), f(y)), stroke='#ffffff', stroke_width=3, opacity=0.4, stroke_linecap='round'))
b.append(G(*gl))
gl2 = []
for k, y in enumerate(range(660, 700, 10)):
    gl2.append(L(120 - k * 10, y, 190 + k * 10, y, '#ffe08a', 5, stroke_linecap='round'))
b.append(G(*gl2, opacity=0.6))
# barges
b.append(barge(40, 770, 230, True, 1.35, 31))
b.append(roman(120, 793, 1.4, OLIVE, arms='up'))
b.append(L(130, 690, 112, 840, '#8b5a35', 5))
b.append(barge(520, 820, 250, True, 1.35, 32))
b.append(roman(700, 845, 1.4, OCHRE, flip=True))
# near bank
b.append(P('M0 905 Q100 888 200 902 Q320 886 440 900 Q580 886 700 900 Q760 890 794 898 L794 1123 L0 1123 Z', '#86c26a', stroke=OUT, stroke_width=3))
b.append(paving(0, 940, W, 183, 24, 50, '#d3c3a0', '#a89874', 81))
b.append(P('M0 940 Q200 930 400 940 Q600 930 794 940', stroke=OUT, stroke_width=3))
gr = []
for x in range(10, 790, 70):
    gr.append(P('M%s 912 Q%s 898 %s 886' % (f(x), f(x - 2), f(x + 8)), stroke='#5e9b48', stroke_width=3, stroke_linecap='round'))
b.append(G(*gr))
b.append(amphora(40, 960, 1.4) + amphora(76, 960, 1.4, '#b8683a'))
# Leo
b.append(C(397, 470, 230, 'url(#e2cg4)', stroke='none'))
b.append(leo(397, 508, 2.1, rot=-4, wing='open', eyes='open'))
# Becco
b.append(becco(700, 470, 1.5, rot=-12, wings='up', scroll=True, legs_on=False))
# kids running
g = 1038
b.append(nico(110, g - 62 * 1.65, 1.65, rot=6, run=16, la=(-30, 14), ra=(32, -22), expr='dot'))
b.append(sofia(290, g - 72 * 1.65, 1.65, rot=6, run=16, la=(-30, -16), ra=(30, 14), expr='dot'))
b.append(toni(470, g - 72 * 1.5, 1.5, rot=6, run=14, la=(-32, 10), ra=(34, -22), expr='dot'))
b.append(tito(650, g - 63 * 1.7 * 1.05, 1.7, rot=6, run=16, la=(-30, -14), ra=(32, 14), expr='dot'))
for (x, y, r) in [(40, 480, 9), (754, 400, 9), (240, 590, 8), (560, 560, 8), (330, 380, 8), (520, 380, 7), (90, 1000, 7)]:
    b.append(star(x, y, r, '#f4b942'))
svg = '<svg viewBox="0 0 794 1123" preserveAspectRatio="xMidYMid slice" style="position: absolute; left: 0; top: 0; width: 794px; height: 1123px; display: block" role="img" aria-label="Patavium romana in una giornata di sole: il ponte di pietra, i barconi sul fiume, i tetti di tegole e un tempio lontano; Nico, Sofia, Toni e Tito corrono lungo la riva, Leo vola in alto e Becco in alto a destra tiene un rotolo nel becco">' + defs + ''.join(b) + '</svg>'

title = '<div style="position: absolute; left: 0; top: 22px; width: 794px; text-align: center; transform: rotate(-3deg); font-family: \'Bangers\', \'Comic Neue\', sans-serif; font-size: 110px; letter-spacing: 3px; line-height: 0.92; color: #f4c64e; -webkit-text-stroke: 4px #3b2416; paint-order: stroke fill; text-shadow: 3px 5px 0 #3b2416">LEONI DI<br>LAGUNA</div>'

banner = '''<div style="position: absolute; left: 87px; top: 262px; width: 620px; height: 72px; transform: rotate(-2deg)">
<svg viewBox="0 0 620 72" width="620" height="72" style="position: absolute; left: 0; top: 0; display: block" aria-hidden="true">
<path d="M2 20 L66 20 L66 68 L2 68 L20 44 Z" fill="#e9d3a0" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M618 20 L554 20 L554 68 L618 68 L600 44 Z" fill="#e9d3a0" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M48 56 L66 56 L66 68 Z" fill="#bfa468" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M572 56 L554 56 L554 68 Z" fill="#bfa468" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<rect x="48" y="4" width="524" height="52" fill="#fff3d6" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></rect>
</svg>
<div style="position: absolute; left: 56px; top: 4px; width: 508px; height: 52px; display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Comic Neue', sans-serif; font-weight: 700; font-size: 26px; color: #3b2416; white-space: nowrap">Episodio 2 – Amici di Roma</div>
</div>'''

strip = '<div style="position: absolute; left: 0; bottom: 0; width: 794px; height: 64px; box-sizing: border-box; background: #3b2416; border-top: 4px solid #f4c64e; display: flex; align-items: center; justify-content: center; text-align: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 20px; letter-spacing: 0.5px; color: #fdf3d6">Avventure nella storia di Venezia e dei Veneti</div>'

root = '<div style="width: 794px; height: 1123px; position: relative; overflow: hidden; background: #5d86b8; font-family: \'Comic Neue\', sans-serif">\n\n' + svg + '\n\n' + title + '\n\n' + banner + '\n\n' + strip + '\n\n</div>'
write(OUTD + 'Ep2_Copertina.dc.html', HEAD % 'Copertina Ep. 2 – Amici di Roma' + root + '\n' + TAIL)
print('ok')
