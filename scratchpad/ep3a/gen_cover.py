import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/ep3a')
from lib3 import *

W, H = 794, 1123
b = []
defs = gid_defs(('e3cg1', 'v', [(0, '#f08a5d', 1), (0.35, '#f7b87a', 1), (0.75, '#fcdc9e', 1), (1, '#fff1c9', 1)]),
                ('e3cg2', 'v', [(0, '#f6c98a', 1), (0.25, '#8cc4b4', 1), (0.6, '#3f9aa2', 1), (1, '#1f6a7e', 1)]),
                ('e3cg3', 'r', [(0, '#fff6cf', 1), (0.4, '#ffe3a0', 0.6), (1, '#ffe3a0', 0)]),
                ('e3cg4', 'r', [(0, '#fff8d8', 0.9), (0.5, '#ffe9a3', 0.4), (1, '#ffe9a3', 0)]))
b.append(R(0, 0, W, 660, 'url(#e3cg1)'))
b.append(C(170, 600, 260, 'url(#e3cg3)', stroke='none'))
b.append(C(170, 600, 54, '#fff7c4', stroke='none'))
b.append(cloud(640, 380, 1.3, 0.75, '#ffe6c4') + cloud(380, 372, 0.9, 0.7, '#ffe6c4') + cloud(70, 350, 1.0, 0.7, '#ffe6c4') + cloud(720, 560, 0.8, 0.7, '#ffe6c4'))
# water
b.append(R(0, 640, W, 483, 'url(#e3cg2)'))
b.append(L(0, 640, W, 640, '#ffe9b0', 2, opacity=0.7))
# sun reflection
for k, y in enumerate(range(655, 760, 12)):
    b.append(L(170 - 14 - k * 5, y, 170 + 14 + k * 5, y, '#ffe9a3', 4, opacity=0.65, stroke_linecap='round'))
# low far islands with huts
b.append(mound(120, 700, 300, 46, '#c2ae7e', '#8fa860'))
b.append(hut(70, 690, 0.62))
b.append(hut(160, 694, 0.55))
b.append(mound(690, 696, 280, 40, '#c2ae7e', '#8fa860'))
b.append(hut(660, 688, 0.5))
b.append(hut(730, 692, 0.58))
b.append(mound(430, 668, 150, 18, '#c2ae7e', '#8fa860'))
b.append(reeds(380, 668, 6, 26, 3, 20) + reeds(500, 668, 5, 24, 4, 16))
b.append(reeds(30, 700, 6, 40, 5, 24) + reeds(280, 706, 5, 34, 6, 18) + reeds(560, 704, 6, 36, 7, 20))
for (x, y, w) in [(330, 730, 100), (520, 760, 120), (30, 790, 120), (650, 800, 110), (200, 840, 140), (560, 870, 140), (60, 900, 100), (700, 930, 80)]:
    b.append(ripple(x, y, w, '#ffffff', 0.4, 3))
# egrets and gulls
b.append(egret(110, 440, 1.1, True, False, 'up') + egret(190, 480, 0.9, True, False, 'down') + egret(615, 640, 0.8, True, True, 'up'))
b.append(gull(260, 560, 1.0) + gull(300, 530, 0.8) + gull(560, 600, 0.9))
# Leo
b.append(C(397, 520, 230, 'url(#e3cg4)', stroke='none'))
b.append(leo(397, 522, 2.0, rot=-4, wing='open', eyes='open'))
# Becco with mallet
b.append(becco_mallet(700, 466, 1.45, rot=-12, wings='up'))
# boat with people
GY = 940
b.append(E(397, 990, 320, 16, '#1f6a7e', stroke='none', opacity=0.45))
b.append(papa(185, GY - 40 * 1.55, 1.55, la=(-28, 30), ra=(34, 26), expr='smile'))
b.append(toni(305, GY - 24 * 1.35, 1.35, la=(-26, -4), ra=(32, -40), expr='happy'))
b.append(sofia(405, GY - 20 * 1.45, 1.45, la=(-24, 14), ra=(24, 14), expr='smile'))
b.append(elena(512, GY - 22 * 1.5, 1.5, la=(-34, -40), ra=(24, 14), expr='happy'))
b.append(nico(625, GY - 22 * 1.5, 1.5, la=(-20, 16), ra=(38, -26), expr='happy', pack=False))
b.append(boat(397, GY, 600, 48))
b.append(oar(238, 920, 330, 1000, 40))
b.append(oar(142, 923, 62, 1002, 40))
b.append(ripple(280, 1008, 120, '#ffffff', 0.55, 3) + ripple(20, 1014, 90, '#ffffff', 0.5, 3) + ripple(500, 1014, 220, '#ffffff', 0.4, 3))
# foreground reeds
b.append(reeds(30, 1130, 9, 250, 11, 34) + reeds(110, 1130, 7, 190, 12, 30) + reeds(770, 1130, 9, 270, 13, 34) + reeds(690, 1130, 7, 200, 14, 28))
b.append(reeds(400, 1130, 6, 110, 15, 40))
for (x, y, r) in [(40, 520, 9), (754, 400, 9), (250, 640, 7), (540, 540, 8), (330, 400, 8), (520, 390, 7), (90, 790, 7), (730, 760, 7)]:
    b.append(star(x, y, r, '#fff0b0'))
svg = '<svg viewBox="0 0 794 1123" preserveAspectRatio="xMidYMid slice" style="position: absolute; left: 0; top: 0; width: 794px; height: 1123px; display: block" role="img" aria-label="La laguna veneta al tramonto: canneti, piccole isole con capanne su palafitte, una barca con Papà che rema, Elena, Nico, Sofia e Toni a bordo; Leo vola in alto e Becco in alto a destra tiene un grande martello di legno">' + defs + ''.join(b) + '</svg>'

title = '<div style="position: absolute; left: 0; top: 22px; width: 794px; text-align: center; transform: rotate(-3deg); font-family: \'Bangers\', \'Comic Neue\', sans-serif; font-size: 110px; letter-spacing: 3px; line-height: 0.92; color: #f4c64e; -webkit-text-stroke: 4px #3b2416; paint-order: stroke fill; text-shadow: 3px 5px 0 #3b2416">LEONI DI<br>LAGUNA</div>'
banner = '''<div style="position: absolute; left: 87px; top: 262px; width: 620px; height: 72px; transform: rotate(-2deg)">
<svg viewBox="0 0 620 72" width="620" height="72" style="position: absolute; left: 0; top: 0; display: block" aria-hidden="true">
<path d="M2 20 L66 20 L66 68 L2 68 L20 44 Z" fill="#e9d3a0" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M618 20 L554 20 L554 68 L618 68 L600 44 Z" fill="#e9d3a0" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M48 56 L66 56 L66 68 Z" fill="#bfa468" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<path d="M572 56 L554 56 L554 68 Z" fill="#bfa468" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></path>
<rect x="48" y="4" width="524" height="52" fill="#fff3d6" stroke="#3b2416" stroke-width="3" stroke-linejoin="round"></rect>
</svg>
<div style="position: absolute; left: 56px; top: 4px; width: 508px; height: 52px; display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Comic Neue', sans-serif; font-weight: 700; font-size: 26px; color: #3b2416; white-space: nowrap">Episodio 3 – Fuga in laguna</div>
</div>'''
strip = '<div style="position: absolute; left: 0; bottom: 0; width: 794px; height: 64px; box-sizing: border-box; background: #3b2416; border-top: 4px solid #f4c64e; display: flex; align-items: center; justify-content: center; text-align: center; font-family: \'Comic Neue\', sans-serif; font-weight: 700; font-size: 20px; letter-spacing: 0.5px; color: #fdf3d6">Avventure nella storia di Venezia e dei Veneti</div>'
root = '<div style="width: 794px; height: 1123px; position: relative; overflow: hidden; background: #f4a261; font-family: \'Comic Neue\', sans-serif">\n\n' + svg + '\n\n' + title + '\n\n' + banner + '\n\n' + strip + '\n\n</div>'
write(OUTD + 'Ep3_Copertina.dc.html', HEAD % 'Copertina Ep. 3 – Fuga in laguna' + root + '\n' + TAIL)
print('ok')
