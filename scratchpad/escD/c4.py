import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escD')
from b45 import *

gen.ARIA.update({
    14: 'Baio, un cavallo baio tranquillo con una macchia bianca sulla fronte, la criniera intrecciata, la coda lunga e una coperta di lana',
    52: 'Villaggio di capanne di legno con tetti di paglia, un recinto con un uomo, un grande fossato pieno d\'acqua con un ponte rotto e il santuario lontano',
    53: 'Un allevatore veneto sorridente con barba corta e tunica marrone che tiene un cavezzo di corda',
    56: 'Quattro cavalli marroni in un recinto, ciascuno con un cartello bianco sotto: 61, 64, 68, 71. Differiscono per la macchia bianca, la criniera e la coda',
    58: 'Un fossato largo pieno d\'acqua con un ponte di legno rotto',
    61: 'Un cavallo con la coda corta che volta le spalle',
    64: 'Un cavallo che scuote la criniera sciolta',
    68: 'Baio coccola Toni mentre l\'allevatore porge il cavezzo a Nico',
    71: 'Un cavallo con la fronte tutta marrone che guarda perplesso',
})


def il14(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(40, 22, 0.6) + cloud(172, 30, 0.5)
    s += grass_ground(H, 92)
    s += E(104, 108, 62, 5, '#7fa862', stroke='none')
    s += bhorse(94, 70.2, 1.2, blaze=True, braid=True, tail='long', blanket=True)
    s += P('M20 106 q3 -9 6 0 M24 106 q1 -7 4 0 M184 108 q3 -9 6 0 M188 108 q1 -7 4 0', stroke='#5f9a5a', stroke_width=2, stroke_linecap='round')
    return s


def il52(H=175):
    s = rect_bg(H, '#d6ecee') + cloud(46, 18, 0.55) + cloud(150, 12, 0.45)
    s += P('M88 78 Q150 46 215 66 L215 92 L88 92 Z', '#b2cf94', stroke=OUT, stroke_width=1.6)
    s += sanctuary_far(166, 66)
    s += grass_ground(H, 84)
    s += hut(80, 106, 34, 22) + hut(124, 102, 30, 19)
    s += P('M150 118 Q172 108 205 114', stroke='#d9c59a', stroke_width=6, stroke_linecap='round')
    # corral with man
    s += fence(6, 66, 118, 22, 20)
    s += P('M6 118 L6 98', stroke=OUT, stroke_width=1) if False else ''
    s += man(36, 92, 0.42, expr='smile')
    s += hid(36, 98, 53)
    s += fence(6, 66, 121, 12, 20) if False else ''
    # ditch
    s += ditch_water(128, H)
    s += bridge_broken(120, 128, 154, H, 58)
    s += reeds(14, 175, 3, 36, 8) + reeds(204, 175, 3, 38, 8)
    return s


def il53(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(46, 20, 0.55) + cloud(168, 28, 0.5)
    s += P('M0 74 Q60 52 130 70 Q180 56 215 66 L215 120 L0 120 Z', '#b2cf94', stroke=OUT, stroke_width=1.6)
    s += grass_ground(H, 88)
    s += hut(150, 92, 40, 24)
    s += fence(4, 76, 96, 20, 24)
    s += man(98, 56, 0.9, expr='smile', ra=(30, 2), halter=True)
    return s


def il56(H=175):
    s = rect_bg(H, '#d6ecee') + cloud(60, 14, 0.45) + cloud(168, 18, 0.4)
    s += R(0, 52, W, H - 52, '#cdbb8a', stroke='none') + R(0, 52, W, 5, '#9ac17a', stroke='none') + P('M0 52 L215 52', stroke=OUT, stroke_width=1.8)
    s += fence(2, 214, 86, 36, 30)
    s += R(0, 120, W, H - 120, '#d9c79a', stroke='none') + P('M0 120 L215 120', stroke='#a8803f', stroke_width=1.2)
    spec = [(61, True, True, 'short'), (64, True, False, 'long'), (68, True, True, 'long'), (71, False, True, 'long')]
    for i, (n, bl, br, tl) in enumerate(spec):
        cx = 18.5 + 53.6 * i
        s += E(cx + 9, 123, 24, 3.5, '#b9a577', stroke='none')
        s += bhorse(cx, 123 - 31.5 * 0.78, 0.78, blaze=bl, braid=br, tail=tl)
    for i, n in enumerate((61, 64, 68, 71)):
        cx = 18.5 + 53.6 * i
        s += sign(cx + 3, 132, n, w=42, h=34, fs=23)
    return s


def il58(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(46, 16, 0.55) + cloud(170, 22, 0.5)
    s += R(0, 30, W, 30, '#9ac17a', stroke='none') + hut(150, 52, 34, 20) + hut(30, 50, 30, 18)
    s += ditch_water(58, H)
    s += bridge_broken(108, 58, 92, H, None)
    s += reeds(12, 120, 3, 34, 8) + reeds(204, 120, 3, 34, 8)
    return s


def il61(H=120):
    s = rect_bg(H, '#f1e4d0') + grass_ground(H, 96, '#b9d6a0')
    s += E(108, 104, 64, 5, '#8fb072', stroke='none')
    s += bhorse(108, 64, 1.25, blaze=True, braid=True, tail='short', flip=True, eye='closed')
    p = wpt(108, 64, 1.25, 0, True)
    tx, ty = p(-20, -1)
    s += dash_ring(tx, ty, 15, 13)
    s += bang('HMPF!', 52, 30, 24, '#8d9097', -8)
    return s


def il64(H=120):
    s = rect_bg(H, '#f1e4d0') + grass_ground(H, 96, '#b9d6a0')
    s += E(100, 104, 64, 5, '#8fb072', stroke='none')
    s += bhorse(96, 64, 1.2, blaze=True, braid=False, tail='long', rot=-4)
    p = wpt(96, 64, 1.2, -4)
    mx, my = p(4, -28)
    s += dash_ring(mx, my, 27, 22)
    s += P('M52 24 q-12 10 0 22 M44 18 q-18 16 0 34', stroke='#7a5a3e', stroke_width=2, stroke_linecap='round')
    s += bang('SBUF!', 172, 34, 24, '#d9472f', 8)
    return s


def il71(H=120):
    s = rect_bg(H, '#f1e4d0') + grass_ground(H, 96, '#b9d6a0')
    s += E(100, 104, 64, 5, '#8fb072', stroke='none')
    s += bhorse(96, 64, 1.2, blaze=False, braid=True, tail='long', eye='wide')
    p = wpt(96, 64, 1.2)
    fx, fy = p(32, -33)
    s += dash_ring(fx, fy, 15, 13)
    s += qmark(156, 40, 30, '#8a5fb0', 12) + qmark(178, 62, 20, '#8a5fb0', -10)
    return s


def il68(H=120):
    s = rect_bg(H, '#d6ecee') + cloud(40, 20, 0.5) + cloud(170, 16, 0.45)
    s += grass_ground(H, 100)
    s += bhorse(128, 108 - 31.5 * 0.74, 0.74, blaze=True, braid=True, tail='long', eye='closed')
    s += man(34, 108 - 62 * 0.42, 0.42, expr='happy', ra=(34, 2), halter=True)
    s += nico(64, 108 - 58 * 0.4, 0.4, expr='happy', la=(-30, 4), ra=(24, 16))
    s += toni(176, 108 - 54 * 0.4, 0.4, expr='happy', flip=True, la=(-14, 8), ra=(26, -8))
    s += hearts([(166, 50, 1.2), (154, 36, 0.9), (180, 38, 0.8)])
    return s


# ---------------------------------------------------------------- build sheet 4
PFX_ = 'Carte4'
c4 = [
    card('OGGETTO ROSSO', 14, 'IL CAVALLO BAIO', 'Baio, il cavallo più tranquillo del villaggio. È abituato a portare i bambini in groppa.', il14(120), 120),
    card('LUOGO', 52, 'IL VILLAGGIO', 'Il villaggio di Este. Tra voi e il santuario c\'è un fossato pieno d\'acqua, e il ponte è rotto! Guardate bene il disegno.', il52(175), 175),
    card('PERSONAGGIO', 53, 'L\'ALLEVATORE', '«I Veneti sono famosi per i cavalli! Il mio Baio vi porterà oltre il fossato. È nel recinto (carta **56**): ha una macchia bianca sulla fronte e la criniera intrecciata, ma NON ha la coda corta.»', il53(120), 120),
    card('ENIGMA', 56, 'IL RECINTO', 'Quale cavallo è Baio? Leggete bene le parole dell\'allevatore. Il numero sotto il cavallo giusto è la carta da prendere.', il56(175), 175),
    card('OGGETTO BLU', 58, 'IL FOSSATO', 'Un fossato largo e profondo. A piedi non si passa… ci vorrebbe qualcuno con quattro zampe buone!', il58(120), 120),
    card('SBAGLIATO', 61, 'SBAGLIATO!', 'Questo cavallo ha la coda corta! Perdete 1 piuma, rimettete giù la carta e riprovate.', il61(120), 120, strip='Risposta a: IL RECINTO'),
    card('SBAGLIATO', 64, 'SBAGLIATO!', 'Questo cavallo ha la criniera sciolta, non intrecciata! Perdete 1 piuma, rimettete giù la carta e riprovate.', il64(120), 120, strip='Risposta a: IL RECINTO'),
    card('RISPOSTA', 68, 'GIUSTO! È BAIO', 'Baio vi riconosce subito e nitrisce contento. L\'allevatore ve lo presta: prendete la carta **14**. Scartate le carte 53, 56, 61, 64 e 71.', il68(120), 120, strip='Risposta a: IL RECINTO'),
    card('SBAGLIATO', 71, 'SBAGLIATO!', 'Questo cavallo non ha la macchia bianca sulla fronte! Perdete 1 piuma, rimettete giù la carta e riprovate.', il71(120), 120, strip='Risposta a: IL RECINTO'),
]
write('Carte4_Fronte.dc.html', 'Carte 4 – Fronte', 'Leoni di Laguna – Escape · Carte foglio 4 · FRONTE · pagina 9 (ritaglia lungo i bordi)', c4)
