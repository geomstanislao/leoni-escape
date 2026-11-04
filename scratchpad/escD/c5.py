import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escD')
from b45 import *

gen.ARIA.update({
    72: 'Baio salta il fossato con Nico, Sofia e Toni in groppa, Leo vola accanto e l\'acqua schizza',
    74: 'Il cancello di legno del santuario chiuso con un grosso lucchetto di bronzo; Becco bagnato e imbronciato siede sopra con una chiave di bronzo al collo',
    76: 'Tre oggetti con un cartello bianco sotto ciascuno: una tavoletta di bronzo con segni angolari (81), il cavallino d\'oro (84), un secchio di bronzo decorato (86)',
    81: 'Becco brontola mentre la chiave gli cade dal collo',
    84: 'Becco ride tenendosi la pancia con le ali',
    86: 'Becco scuote la testa',
    20: 'Una grossa chiave antica di bronzo appesa a una cordicella, ancora bagnata',
    26: 'Un grosso lucchetto di bronzo sul cancello di legno',
    46: 'Il cancello si apre, i bambini corrono dentro con il cavallino d\'oro, Leo esulta e Becco è imbronciato sul muro',
})


def il72(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(40, 20, 0.5) + cloud(176, 14, 0.45)
    s += sanctuary_far(166, 74)
    s += R(0, 80, W, 40, '#9ac17a', stroke='none') + P('M0 80 L215 80', stroke=OUT, stroke_width=1.8)
    s += water(94, H)
    s += P('M0 94 Q20 90 40 94 L40 120 L0 120 Z', '#8ab463', stroke=OUT, stroke_width=1.8)
    s += P('M215 94 Q196 90 176 94 L176 120 L215 120 Z', '#8ab463', stroke=OUT, stroke_width=1.8)
    s += bhorse(106, 52, 0.9, blaze=True, braid=True, tail='long', rot=-16)
    p = wpt(106, 52, 0.9, -16)
    for (lx, who) in ((-8, 'n'), (3, 's'), (14, 't')):
        qx, qy = p(lx, -14)
        if who == 'n':
            s += nico(qx, qy, 0.27, rot=-16, expr='wow', la=(-14, 12), ra=(14, 8), pack=False)
        elif who == 's':
            s += sofia(qx, qy, 0.27, rot=-16, expr='happy', la=(-14, 8), ra=(14, 8))
        else:
            s += toni(qx, qy, 0.27, rot=-16, expr='happy', la=(-20, 0), ra=(20, 0))
    s += leo(172, 36, 0.3, wing='open', eyes='closed', mouth='smile', la=(-34, -24), ra=(34, -24))
    s += drops([(98, 90, 1.1), (116, 88, 1.3), (128, 94, 0.9), (86, 96, 0.8), (140, 90, 0.8)])
    s += P('M82 104 q8 -10 16 0 M112 106 q8 -12 16 0 M130 104 q6 -8 12 0', stroke='#ffffff', stroke_width=2.4, stroke_linecap='round')
    s += bang('HOP!', 44, 54, 26, '#d9472f', -8)
    return s


def il74(H=175):
    s = rect_bg(H, '#d6ecee') + cloud(36, 20, 0.5) + cloud(180, 30, 0.45)
    s += ink(R(0, 62, W, H - 62, '#e3d4b2'), w=1.8)
    for yy in (80, 100, 120, 140, 160):
        s += P('M0 %s L215 %s' % (f(yy), f(yy)), stroke='#c9b58a', stroke_width=1)
    for xx in (14, 30, 186, 200):
        s += P('M%s 62 L%s 175' % (f(xx), f(xx)), stroke='#c9b58a', stroke_width=1)
    # pillars + lintel
    s += ink(R(38, 44, 18, 131, '#cdbb92'), R(159, 44, 18, 131, '#cdbb92'), R(34, 40, 26, 8, '#b9a577'), R(155, 40, 26, 8, '#b9a577'), w=1.8)
    s += ink(R(38, 80, 139, 14, WOOD_D, rx=2), w=2)
    # gate leaves
    s += gate_wood(56, 94, 51, 81) + gate_wood(107, 94, 51, 81)
    s += ink(R(56, 110, 102, 7, BRONZE), R(56, 152, 102, 7, BRONZE), w=1.6)
    for xx in (64, 90, 124, 150):
        s += C(xx, 113.5, 1.6, BRONZE_D, stroke=OUT, stroke_width=0.8) + C(xx, 155.5, 1.6, BRONZE_D, stroke=OUT, stroke_width=0.8)
    s += P('M107 94 L107 175', stroke=OUT, stroke_width=2)
    # padlock
    s += lock_body(107, 136, 1.0, w=36, h=30)
    s += C(107, 136, 9, '#f4c64e', stroke=OUT, stroke_width=1.5) + txt('26', 107, 139.6, 10)
    # Becco on top, wet and sulky
    s += becco(107, 60, 0.5, legs_on=False)
    s += P('M100 52 Q93 68 94 72 M114 52 Q108 66 96 71', stroke=OUT, stroke_width=1.4, stroke_linecap='round')
    s += small_key(93, 86, 0.2, 90)
    s += C(111, 66, 9, '#f4c64e', stroke=OUT, stroke_width=1.5) + txt('76', 111, 69.6, 10)
    s += drops([(80, 40, 1.0), (134, 46, 1.1), (128, 26, 0.8), (84, 66, 0.8), (140, 70, 0.8)])
    s += P('M104 82 q3 6 0 10 M120 82 q3 6 0 10', stroke='#9fd0e3', stroke_width=2, stroke_linecap='round')
    return s


def il76(H=120):
    s = rect_bg(H, '#efdcbc') + R(0, 74, W, 46, '#e0cba0', stroke='none') + P('M0 74 L215 74', stroke=OUT, stroke_width=1.4)
    # tablet
    cx = 36
    s += ink(R(cx - 21, 8, 42, 58, BRONZE, rx=4), R(cx - 21, 8, 42, 8, '#e8b469', rx=4), w=2)
    s += P('M%s 24 l5 9 l5 -9 M%s 24 l0 12 M%s 38 l9 -4 l0 12 M%s 52 l6 -8 l6 8 M%s 52 l10 0' % (f(cx - 14), f(cx + 4), f(cx - 14), f(cx + 2), f(cx - 14)),
           stroke='#5e381c', stroke_width=2.2, stroke_linecap='round', stroke_linejoin='round')
    # golden horse
    cx = 107
    s += glow_(cx, 38, gid(76), 30)
    s += horse(cx - 2, 36, 1.5)
    s += sparkles([(cx - 28, 14, 5), (cx + 30, 18, 4), (cx + 22, 56, 4)])
    # situla
    cx = 179
    s += P('M%s 24 Q%s -2 %s 24' % (f(cx - 17), f(cx), f(cx + 17)), stroke=OUT, stroke_width=3.4, stroke_linecap='round')
    s += P('M%s 24 Q%s 0 %s 24' % (f(cx - 17), f(cx), f(cx + 17)), stroke='#e8b469', stroke_width=1.6, stroke_linecap='round')
    s += ink(P('M%s 22 L%s 22 L%s 62 Q%s 68 %s 62 Z' % (f(cx - 21), f(cx + 21), f(cx + 14), f(cx), f(cx - 14)), BRONZE), w=2)
    s += ink(E(cx, 22, 21, 5, '#e8b469'), w=2)
    s += P('M%s 34 L%s 34 M%s 52 L%s 52' % (f(cx - 19), f(cx + 19), f(cx - 15), f(cx + 15)), stroke='#5e381c', stroke_width=1.6)
    s += P('M%s 43 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6' % f(cx - 17), stroke='#5e381c', stroke_width=1.5, stroke_linejoin='round')
    for k in range(5):
        s += C(cx - 12 + k * 6, 58, 1.3, '#5e381c', stroke='none')
    # signs
    s += sign(36, 80, 81, w=44, h=34, fs=22) + sign(107, 80, 84, w=44, h=34, fs=22) + sign(179, 80, 86, w=44, h=34, fs=22)
    return s


def il81(H=120):
    s = rect_bg(H, '#f1e4d0') + cloud(176, 22, 0.4)
    s += becco(96, 70, 0.7, legs_on=False)
    s += P('M60 92 q-8 -2 -12 -10', stroke='#8d9097', stroke_width=2, stroke_linecap='round') if False else ''
    s += P('M82 38 Q76 30 70 34 M102 34 Q106 26 112 28', stroke=OUT, stroke_width=1.6, stroke_linecap='round') if False else ''
    s += P('M138 50 L140 64', stroke='#9a7a4a', stroke_width=1.6, stroke_dasharray='3 2')
    s += small_key(150, 88, 0.36, 40)
    s += P('M168 72 L164 86 M174 82 L170 96 M160 66 L158 78', stroke='#bfa77a', stroke_width=1.8, stroke_linecap='round')
    s += bang('UFFA!', 164, 34, 28, '#d9472f', 8)
    return s


def il84(H=120):
    s = rect_bg(H, '#f1e4d0')
    s += becco(100, 70, 0.7, legs_on=False)
    p = wpt(100, 70, 0.7)
    ex, ey = p(-6, -50)
    s += C(ex, ey, 4.6, '#fafaf7', stroke='none')
    s += P('M%s %s Q%s %s %s %s' % (f(ex - 4.5), f(ey + 1), f(ex), f(ey - 6), f(ex + 4.5), f(ey + 1)), stroke=OUT, stroke_width=1.8, stroke_linecap='round')
    s += becco_wing_belly(100, 70, 0.7)
    s += drops([(ex - 10, ey + 8, 0.9), (ex + 4, ey + 12, 0.9)])
    s += bang('HA HA!', 160, 36, 26, '#d9472f', 10)
    s += P('M146 56 Q156 58 158 68 M142 74 Q152 78 152 90', stroke=OUT, stroke_width=1.8, stroke_linecap='round')
    return s


def il86(H=120):
    s = rect_bg(H, '#f1e4d0')
    s += becco(104, 70, 0.7, rot=-6, legs_on=False)
    s += P('M52 24 q-10 12 0 26 M44 20 q-16 18 0 36', stroke='#7a5a3e', stroke_width=2, stroke_linecap='round')
    s += P('M156 24 q10 12 0 26 M164 20 q16 18 0 36', stroke='#7a5a3e', stroke_width=2, stroke_linecap='round')
    s += bang('NO NO!', 160, 100, 24, '#d9472f', -8)
    return s


def il20(H=120):
    s = rect_bg(H, '#e9dcc0') + E(108, 108, 80, 6, '#cdbb92', stroke='none')
    # string
    s += G(P('M-52 -14 Q-70 -58 -22 -62 Q30 -66 44 -40', stroke=OUT, stroke_width=6, stroke_linecap='round'),
           P('M-52 -14 Q-70 -58 -22 -62 Q30 -66 44 -40', stroke=STRAW, stroke_width=3.4, stroke_linecap='round'), transform=xfm(104, 66, 0.82, -30))
    s += small_key(104, 66, 0.82, -30)
    s += drops([(150, 98, 1.0), (62, 100, 0.9), (136, 104, 0.7)])
    s += sparkles([(172, 40, 5), (40, 40, 4)], '#fff2b8')
    return s


def il26(H=120):
    s = rect_bg(H, '#a8703a')
    for k in range(1, 20):
        s += P('M%s 0 L%s 120' % (f(k * 11), f(k * 11)), stroke='#7a4a26', stroke_width=1.2)
    s += ink(R(0, 54, W, 12, BRONZE), w=1.8)
    for xx in (10, 40, 70, 150, 180, 205):
        s += C(xx, 60, 2, BRONZE_D, stroke=OUT, stroke_width=0.9)
    s += lock_body(108, 70, 1.5, w=62, h=50)
    s += R(0, 0, 0, 0, 'none') if False else ''
    s += ink(C(108, 66, 7, '#2a1a10'), P('M105 70 L111 70 L113 84 L103 84 Z', '#2a1a10'), w=1.2)
    s += C(84, 52, 2.2, BRONZE_D, stroke=OUT, stroke_width=0.9) + C(132, 52, 2.2, BRONZE_D, stroke=OUT, stroke_width=0.9)
    s += C(84, 88, 2.2, BRONZE_D, stroke=OUT, stroke_width=0.9) + C(132, 88, 2.2, BRONZE_D, stroke=OUT, stroke_width=0.9)
    return s


def il46(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(40, 14, 0.45)
    # interior glow
    s += R(60, 44, 95, 74, '#fbe7a6', stroke=OUT, stroke_width=1.8)
    s += R(60, 100, 95, 18, '#e3d4b2', stroke='none') + P('M60 100 L155 100', stroke=OUT, stroke_width=1.2)
    s += ink(R(97, 72, 22, 6, '#d9d0bd', rx=2), R(101, 78, 14, 22, '#cfc4ac'), w=1.4)
    # walls
    s += ink(R(0, 40, 60, 80, '#e3d4b2'), R(155, 40, 60, 80, '#e3d4b2'), w=1.8)
    for yy in (60, 80, 100):
        s += P('M0 %s L60 %s M155 %s L215 %s' % (f(yy), f(yy), f(yy), f(yy)), stroke='#c9b58a', stroke_width=1)
    # open leaves
    s += ink(P('M60 44 L38 54 L38 120 L60 112 Z', '#a8703a'), P('M155 44 L177 54 L177 120 L155 112 Z', '#a8703a'), w=1.8)
    s += P('M48 50 L48 117 M166 50 L166 117', stroke='#7a4a26', stroke_width=1.2)
    s += ink(R(36, 62, 24, 6, BRONZE), R(155, 62, 24, 6, BRONZE), w=1.2)
    # kids running in
    s += toni(84, 88, 0.3, expr='happy', run=6, la=(-20, -10), ra=(20, -10))
    s += nico(112, 88, 0.3, expr='happy', run=6, la=(-24, 0), ra=(24, 0), pack=False)
    s += glow_(141, 66, gid(46), 20)
    s += sofia(136, 86, 0.3, expr='happy', run=6, la=(-14, 8), ra=(14, -34))
    s += horse(141, 66, 0.4)
    s += sparkles([(122, 50, 4), (160, 48, 4)])
    # Leo cheering
    s += leo(108, 26, 0.26, wing='open', eyes='closed', mouth='smile', la=(-34, -24), ra=(34, -24))
    # Becco sulking on the wall
    s += becco(192, 28, 0.26, legs_on=False)
    s += P('M180 36 q-6 4 -10 0', stroke='none') if False else ''
    return s


def gid(n):
    return 'Carte5_g%s' % n


# ---------------------------------------------------------------- build sheet 5
c5 = [
    card('COMBINAZIONE', 72, 'AL GALOPPO!', 'Hop! Baio salta il fossato con tutti e tre in groppa. Eccovi davanti al santuario… ma il cancello è chiuso! Prendete la carta **74**. Scartate le carte 14, 52 e 58.', il72(120), 120, strip='Combinazione: BAIO + FOSSATO'),
    card('LUOGO', 74, 'IL CANCELLO', 'Il cancello del santuario è chiuso con un lucchetto. E guardate chi c\'è seduto sopra, con la chiave al collo!', il74(175), 175),
    card('ENIGMA', 76, 'L\'INDOVINELLO DI BECCO', '«La chiave? Ve la do solo se indovinate! Sono di bronzo e piena di segni, su di me gli allievi imparavano a scrivere. Chi sono?» Il numero sotto la risposta giusta è la carta da prendere.', il76(120), 120),
    card('RISPOSTA', 81, 'GIUSTO!', '«Uffa! È la tavoletta…» Becco lascia cadere la chiave. Prendete la carta **20**. Scartate le carte 76, 84 e 86.', il81(120), 120, strip='Risposta a: L\'INDOVINELLO DI BECCO'),
    card('SBAGLIATO', 84, 'SBAGLIATO!', '«Ah ah! Il cavallino è d\'oro, mica pieno di segni!» Perdete 1 piuma, rimettete giù la carta e riprovate.', il84(120), 120, strip='Risposta a: L\'INDOVINELLO DI BECCO'),
    card('SBAGLIATO', 86, 'SBAGLIATO!', '«No no! La situla è un secchio di bronzo: ci si mette l\'acqua, non ci si scrive!» Perdete 1 piuma, rimettete giù la carta e riprovate.', il86(120), 120, strip='Risposta a: L\'INDOVINELLO DI BECCO'),
    card('OGGETTO ROSSO', 20, 'LA CHIAVE DI BRONZO', 'Una grossa chiave di bronzo, ancora un po\' bagnata. Chissà cosa apre…', il20(120), 120),
    card('OGGETTO BLU', 26, 'IL LUCCHETTO', 'Un lucchetto di bronzo pesante. Senza la sua chiave non si apre.', il26(120), 120),
    card('COMBINAZIONE', 46, 'APERTO!', 'Clack! Il cancello si apre. Correte all\'altare con il cavallino d\'oro: prendete la carta **39**. Scartate tutte le carte tranne la carta 2.', il46(120), 120, strip='Combinazione: CHIAVE + LUCCHETTO'),
]
write('Carte5_Fronte.dc.html', 'Carte 5 – Fronte', 'Leoni di Laguna – Escape · Carte foglio 5 · FRONTE · pagina 11 (ritaglia lungo i bordi)', c5)
