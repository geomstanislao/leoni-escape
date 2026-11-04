from common import *
import math

P_ = 'c1f'


def bq(a, b, c, t):
    return (1 - t) ** 2 * a + 2 * t * (1 - t) * b + t * t * c


def wall(H, yf, wallc='#ecd2a2', floorc='#c79a64', lines=True):
    s = [R(0, 0, W, yf, wallc, stroke='none'), R(0, yf, W, H - yf, floorc, stroke='none')]
    if lines:
        y = 20
        while y < yf:
            s.append(L(0, y, W, y, '#dcbf8c', 1))
            y += 22
    s.append(L(0, yf, W, yf, OUT, 2))
    for yy in range(int(yf) + 13, int(H), 13):
        s.append(L(0, yy, W, yy, '#a77a48', 1, opacity=0.7))
    return G(*s)


def sparkles(pts):
    return ''.join(star(x, y, r, '#f4b942') for x, y, r in pts)


# ------------------------------------------------------------- TITOLO
def art_titolo():
    H = 170
    g = P_ + '_t_glow'
    d = T('defs', rgrad_def(g, '#fff2b8', 1))
    b = [R(0, 0, W, H, '#fbeec8'), C(150, 100, 80, 'url(#%s)' % g, stroke='none'),
         C(107, 70, 70, 'url(#%s)' % g, stroke='none'),
         R(0, 140, W, 30, '#c9b07a'), L(0, 140, W, 140, OUT, 2)]
    for xx in range(10, 215, 26):
        b.append(L(xx, 146, xx + 8, 146, '#a89874', 1.5))
        b.append(L(xx + 12, 158, xx + 22, 158, '#a89874', 1.5))
    b.append(sparkles([(18, 30, 6), (200, 22, 5), (60, 22, 4), (150, 26, 5), (20, 80, 4)]))
    # Becco peeking from the right edge
    b.append(becco(208, 62, 0.4))
    b.append(horse(172, 148, 0.95, fill='#f4c64e', dark='#d99a2b'))
    b.append(sparkles([(150, 100, 5), (204, 104, 5), (176, 90, 4)]))
    b.append(sofia(80, 112, 0.58, expr='smile'))
    b.append(nico(38, 117, 0.58, expr='dot'))
    b.append(toni(124, 119, 0.58, expr='dot', la=(-30, 10), ra=(30, 10)))
    b.append(leo(100, 50, 0.5, wing='open', la=(-34, -10), ra=(34, -10), mouth='smile'))
    return H, svg(H, ''.join(b), 'Leo con ali dorate vola sopra Nico, Sofia e Toni, accanto al cavallino d\'oro che brilla; Becco spunta da dietro', d)


# ------------------------------------------------------------- 1 INIZIO
def art_1():
    H = 120
    b = [wall(H, 92)]
    b.append(altar(58, 106, 56, 30))
    b.append(leo(145, 66, 0.72, wing='small', la=(-30, 26), ra=(44, -28), mouth='smile'))
    b.append(sparkles([(116, 20, 5), (196, 30, 4)]))
    return H, svg(H, ''.join(b), 'Leo saluta con la zampa davanti a un altare vuoto')


# ------------------------------------------------------------- 2 IL SANTUARIO
def art_2():
    H = 175
    g = P_ + '_s_glow'
    d = T('defs', rgrad_def(g, '#ffd36a', 0.8))
    b = [wall(H, 128)]
    # tablet
    b.append(R(82, 8, 52, 36, '#bdb5a5', stroke=OUT, stroke_width=2, rx=3))
    b.append(P('M90 17 L95 25 L100 17 L105 25 L110 17 M116 16 L122 16 L122 22 L128 22 M90 38 L96 31 L102 38 M104 31 L110 31 L110 38', 'none', stroke='#4a4a4a', stroke_width=2, stroke_linecap='round', stroke_linejoin='round'))
    b.append(hid(123, 33, 8))
    # shelves + bronze horses (exactly four)
    for sx, sy, fl in ((4, 64, False), (4, 108, False), (161, 64, True), (161, 108, True)):
        b.append(ink(R(sx, sy, 50, 6, '#8b5a2b'), P('M%s %s L%s %s L%s %s Z' % (f(sx + 8), f(sy + 6), f(sx + 8), f(sy + 14), f(sx + 16), f(sy + 6)), '#6b4428'),
                     P('M%s %s L%s %s L%s %s Z' % (f(sx + 42), f(sy + 6), f(sx + 42), f(sy + 14), f(sx + 34), f(sy + 6)), '#6b4428')))
        b.append(horse(sx + 25, sy, 0.62, flip=fl))
    # torches (exactly three)
    b.append(torch(66, 86, 1.1))
    b.append(torch(149, 86, 1.1))
    b.append(torch(107, 80, 1.1))
    # altar (empty)
    b.append(altar(107, 134, 42, 26))
    b.append(E(107, 138, 30, 3.5, '#a77a48', stroke='none'))
    # chest bottom-left
    b.append(ink(R(8, 146, 56, 22, '#9a6338'),
                 P('M8 146 L8 140 Q36 122 64 140 L64 146 Z', '#b9783f'),
                 R(20, 140, 6, 28, '#6b4428', stroke_width=1.5), R(46, 140, 6, 28, '#6b4428', stroke_width=1.5),
                 R(31, 146, 10, 10, '#c9922e', stroke_width=1.8), C(36, 150.5, 1.6, '#3b2416', stroke='none')))
    b.append(hid(54, 158, 5))
    return H, svg(H, ''.join(b), 'Interno del santuario: altare di legno vuoto, quattro cavallini di bronzo sulle mensole, tre torce accese, una cassa con lucchetto e una tavoletta di pietra', d)


# ------------------------------------------------------------- 3 LA SACERDOTESSA
def art_3():
    H = 120
    b = [wall(H, 100)]
    b.append(ink(P('M150 100 L150 40 Q150 22 170 22 Q190 22 190 40 L190 100 Z', '#a98458'), P('M158 100 L158 42 Q158 30 170 30 Q182 30 182 42 L182 100 Z', '#6b4428')))
    b.append(priestess(107, 70, 0.82))
    b.append(P('M135 20 Q139 27 135 31 Q131 27 135 20 Z', '#bfe3f2', stroke=OUT, stroke_width=1.4))
    b.append(P('M78 24 Q82 31 78 35 Q74 31 78 24 Z', '#bfe3f2', stroke=OUT, stroke_width=1.4))
    return H, svg(H, ''.join(b), 'La sacerdotessa preoccupata, con tunica ocra e terracotta, cintura decorata, chignon scuro e orecchini di bronzo')


# ------------------------------------------------------------- 4 GLI ZAINI
def sandwich(x, y, s=1):
    b = []
    b.append(P('M-30 4 L30 4 Q30 14 22 14 L-22 14 Q-30 14 -30 4 Z', '#d9a066'))
    b.append(P('M-32 -2 L32 -2 L30 5 L20 3 L10 9 L-2 3 L-14 9 L-30 4 Z', '#f4c64e'))
    b.append(P('M-32 -7 Q-25 -1 -17 -7 Q-9 -1 0 -7 Q9 -1 17 -7 Q25 -1 32 -7 L32 -1 L-32 -1 Z', '#7fb04a'))
    b.append(P('M-33 -8 Q-36 -36 0 -36 Q36 -36 33 -8 Z', '#e0a96a'))
    for cx, cy in ((-14, -24), (-2, -28), (12, -24), (-8, -16), (8, -15)):
        b.append(E(cx, cy, 2.4, 1.3, '#fff2c8', stroke='none'))
    return ink(*b, transform=xf(x, y, s, 0, False))


def bag(x, yb, col, dk):
    b = [P('M-24 0 L-24 -36 Q-24 -52 0 -52 Q24 -52 24 -36 L24 0 Z', col),
         E(0, -49, 17, 5.5, '#2a1a10'),
         R(-16, -26, 32, 22, dk, rx=4), L(-16, -20, 16, -20, OUT, 1.6),
         R(-5, -33, 10, 5, '#e9c46a', stroke_width=1.5)]
    return b


def art_4():
    H = 120
    b = [R(0, 0, W, 104, '#f3e2bd', stroke='none'), R(0, 104, W, 16, '#d9bf8c', stroke='none'), L(0, 104, W, 104, OUT, 2)]
    # bag 1 Nico (red) with oar keychain
    g1 = ink(*bag(0, 0, '#e2573a', '#c4452c'), transform='translate(38 104)')
    b.append(g1)
    b.append(ink(C(61, 80, 4, 'none', stroke='#8d9097', stroke_width=2), P('M60 83 L65 98', 'none', stroke='#8b5a2b', stroke_width=3),
                 P('M63 96 Q58 109 64 112 Q72 110 69 97 Z', '#f08a24'), P('M64 100 Q64 106 66 109', 'none', stroke='#fff2c8', stroke_width=1.5, stroke_linecap='round')))
    # bag 2 Toni (blue) with sandwich
    b.append(ink(*bag(0, 0, '#4f74a8', '#3d5d8a'), transform='translate(107 104)'))
    b.append(sandwich(107, 62, 0.58))
    b.append(ink(P('M91 58 Q107 70 123 58 L123 66 Q107 78 91 66 Z', '#4f74a8')))
    # bag 3 Sofia (yellow) with notebook
    b.append(ink(*bag(0, 0, '#f2c043', '#d9a526'), transform='translate(177 104)'))
    b.append(ink(G(R(-10, -24, 20, 28, '#7a5a3e', rx=2), R(-7, -21, 14, 22, '#fbfaf4'), L(-4, -15, 4, -15, '#6f8fc4', 1.2), L(-4, -10, 4, -10, '#6f8fc4', 1.2),
                   C(-6, -24, 1.5, '#8d9097', stroke_width=1), C(0, -24, 1.5, '#8d9097', stroke_width=1), C(6, -24, 1.5, '#8d9097', stroke_width=1),
                   transform='translate(177 59) rotate(-8)')))
    b.append(sparkles([(70, 40, 4), (146, 36, 4), (200, 30, 4)]))
    return H, svg(H, ''.join(b), 'Tre zaini aperti: un portachiavi a forma di remo arancione, un panino e un taccuino')


# ------------------------------------------------------------- 5 LA CASSA
def padlock_scene():
    b = [R(0, 0, W, 140, '#f3e2bd', stroke='none'), E(107, 134, 92, 5, '#d9bf8c', stroke='none')]
    b.append(ink(R(22, 74, 171, 58, '#9a6338'), P('M22 74 L22 66 Q22 42 107 42 Q193 42 193 66 L193 74 Z', '#b9783f'),
                 R(44, 42, 10, 90, '#6b4428', stroke_width=1.8), R(161, 42, 10, 90, '#6b4428', stroke_width=1.8), sw=2.5))
    b.append(ink(P('M88 72 L88 56 Q88 44 107 44 Q126 44 126 56 L126 72', 'none', stroke=OUT, stroke_width=10),
                 P('M88 72 L88 56 Q88 44 107 44 Q126 44 126 56 L126 72', 'none', stroke='#c9892e', stroke_width=5, stroke_linejoin='round'),
                 R(65, 70, 84, 56, '#e0b055', rx=9), sw=2.5))
    b.append(glyph(6, 91, 98, 28))
    b.append(glyph(1, 123, 98, 28))
    return b


def art_5():
    H = 140
    return H, svg(H, ''.join(padlock_scene()), 'Cassa di legno chiusa da un grande lucchetto di bronzo con due segni antichi: un cerchio con croce e una A senza barra')


# ------------------------------------------------------------- 7 IL REMO DI NICO
def art_7():
    H = 120
    b = [R(0, 0, W, H, '#f6ead2', stroke='none'), C(107, 66, 56, 'url(#%s)' % (P_ + '_r_glow'), stroke='none')]
    b.append(ink(C(107, 18, 11, 'none', stroke='#8d9097', stroke_width=5), C(107, 18, 11, 'none', stroke=OUT, stroke_width=1.2, opacity=0.5)))
    inner = [R(-4, -4, 8, 12, '#c9622a', rx=3), R(-3, 6, 6, 40, '#e8782a'), P('M-11 44 Q-12 82 0 86 Q12 82 11 44 Z', '#f08a24'),
             P('M-5 52 Q-6 72 -2 80', 'none', stroke='#ffd9a0', stroke_width=2.2, stroke_linecap='round')]
    b.append(ink(P('M107 29 L107 37', 'none', stroke='#8d9097', stroke_width=4)))
    b.append(ink(*inner, transform='translate(107 34) rotate(-14) scale(0.86)'))
    b.append(sparkles([(40, 40, 6), (176, 54, 5), (160, 22, 4), (50, 90, 4)]))
    d = T('defs', rgrad_def(P_ + '_r_glow', '#fff2b8', 1))
    return H, svg(H, ''.join(b), 'Il portachiavi a forma di piccolo remo arancione di Nico, appeso al suo anello', d)


# ------------------------------------------------------------- 8 LA TAVOLETTA
def art_8():
    H = 150
    b = [R(0, 0, W, H, '#f3e2bd', stroke='none')]
    b.append(ink(R(10, 8, 195, 134, '#c9984f', rx=10), R(16, 14, 183, 122, '#d9ac62', rx=7, stroke_width=1.5), sw=2.5))
    b.append(L(77, 14, 77, 136, '#8b5a2b', 2) + L(138, 14, 138, 136, '#8b5a2b', 2) + L(16, 75, 199, 75, '#8b5a2b', 2))
    cols = (46.5, 107.5, 168.5)
    for r in range(2):
        for k in range(3):
            n = r * 3 + k + 1
            cx = cols[k]
            cy = 38 + r * 61
            b.append(glyph(n, cx, cy, 28))
            b.append(tx(str(n), cx, cy + 36, 16))
    return H, svg(H, ''.join(b), 'Tavoletta di bronzo con una tabella di sei segni antichi e, sotto ciascuno, il suo numero da 1 a 6')


# ------------------------------------------------------------- 9 I TRE RAMI
def art_9():
    H = 175
    b = [R(0, 0, W, H, '#f1e0b5', stroke='none')]
    b.append(R(5, 5, 205, 165, 'none', stroke='#c9a06a', stroke_width=2, rx=6))
    # banks
    b.append(P('M0 118 Q40 108 70 150 L70 175 L0 175 Z', '#b9d18a', stroke='none') + P('M215 118 Q175 108 145 150 L145 175 L215 175 Z', '#b9d18a', stroke='none'))
    # river
    branches = [((107, 108), (52, 100), (36, 44)), ((107, 108), (107, 80), (107, 40)), ((107, 108), (162, 100), (178, 44))]
    paths = ['M107 172 L107 108']
    for p0, p1, p2 in branches:
        paths.append('M%s %s Q%s %s %s %s' % (p0[0], p0[1], p1[0], p1[1], p2[0], p2[1]))
    for d_ in paths:
        b.append(P(d_, 'none', stroke=OUT, stroke_width=29, stroke_linecap='round', stroke_linejoin='round'))
    for d_ in paths:
        b.append(P(d_, 'none', stroke='#8fd0e6', stroke_width=25, stroke_linecap='round', stroke_linejoin='round'))
    for d_ in paths:
        b.append(P(d_, 'none', stroke='#b6e3f2', stroke_width=2, stroke_dasharray='6 9', opacity=0.8))
    # signs
    for (cx, cy), txt in (((36, 28), '31'), ((107, 22), '27'), ((178, 28), '24')):
        b.append(ink(R(cx - 1.5, cy + 8, 3, 18, '#8b5a2b', stroke_width=1.4), C(cx, cy, 15, '#ffffff', stroke='#7a5a3e', stroke_width=2.5)))
        b.append(tx(txt, cx, cy + 5.5, 15))
    # feathers
    G_, Wt = '#8d9097', '#ffffff'
    Ed = '#7a5a3e'

    def fe(x, y, col, rot):
        return feather(x, y, 15, rot, col, OUT if col == G_ else Ed)
    # left: 1 grey + 2 white
    p0, p1, p2 = branches[0]
    for t, col, rot in ((0.28, Wt, 70), (0.55, G_, 35), (0.82, Wt, 10)):
        b.append(fe(bq(p0[0], p1[0], p2[0], t), bq(p0[1], p1[1], p2[1], t), col, rot))
    # middle: 3 grey + 2 white
    for yy, xx, col, rot in ((98, 101, G_, 80), (86, 113, Wt, 100), (74, 101, G_, 80), (62, 113, Wt, 100), (50, 101, G_, 80)):
        b.append(fe(xx, yy, col, rot))
    # right: 2 grey
    p0, p1, p2 = branches[2]
    for t, col, rot in ((0.38, G_, -60), (0.72, G_, -25)):
        b.append(fe(bq(p0[0], p1[0], p2[0], t), bq(p0[1], p1[1], p2[1], t), col, rot))
    # boat (top view)
    b.append(ink(P('M107 134 Q121 146 118 166 Q107 172 96 166 Q93 146 107 134 Z', '#b9783f'), P('M107 140 L107 164', 'none', stroke='#8b5a2b', stroke_width=1.5),
                 R(98, 150, 18, 3, '#8b5a2b', stroke_width=1.2)))
    # reeds on banks
    for rx_, ry_ in ((14, 150), (28, 156), (186, 152), (200, 158)):
        b.append(P('M%s %s Q%s %s %s %s' % (rx_, ry_, rx_ + 2, ry_ - 12, rx_ + 4, ry_ - 24), 'none', stroke='#5f8a3a', stroke_width=2.4, stroke_linecap='round'))
        b.append(E(rx_ + 4, ry_ - 28, 2.6, 6, '#8b5a2b', stroke=OUT, stroke_width=1))
    return H, svg(H, ''.join(b), 'Mappa del fiume vista dall\'alto: una barchetta in basso e il fiume che si divide in tre rami con piume grigie e bianche e un segno numerato in fondo a ogni ramo')


def card(key):
    return {
        'T': lambda: card_front('SPECIALE', None, 'LEONI DI LAGUNA', *art_titolo(),
                                text_html='<div style="text-align: center; padding-top: 4px"><div style="font-family: \'Bangers\', sans-serif; font-size: 18px; color: #a8322a; line-height: 1.1; font-weight: 400">ESCAPE · Il cavallino d\'oro</div><div style="margin-top: 5px">Gioco di carte per tutta la famiglia</div></div>'),
        1: lambda: card_front('SPECIALE', 1, 'INIZIO', *art_1(), text='Este, quasi 3.000 anni fa. Il cavallino d\'oro della dea Reitia è sparito: l\'ha rubato Becco! Leo vi chiede aiuto: riportatelo sull\'altare. Prendete le carte **2**, **3** e **4**.'),
        2: lambda: card_front('LUOGO', 2, 'IL SANTUARIO', *art_2(), text='Il santuario della dea Reitia. L\'altare è vuoto! Guardate bene i disegni: i numeri nei cerchietti dorati sono carte da prendere.'),
        3: lambda: card_front('PERSONAGGIO', 3, 'LA SACERDOTESSA', *art_3(), text='«Becco ha chiuso la mia cassa con un lucchetto di segni antichi, e dentro c\'è la mappa del fiume! I nostri segni sono scritti sulla tavoletta del santuario.»'),
        4: lambda: card_front('SPECIALE', 4, 'GLI ZAINI', *art_4(), text='Aprite gli zaini! Il remo di Nico (carta **7**), il panino di Toni (carta **12**) e il taccuino di Sofia (carta **11**).'),
        5: lambda: card_front('ENIGMA', 5, 'LA CASSA', *art_5(), text='La cassa è chiusa da un lucchetto con due segni antichi. Che numero formano? Prendete la carta con quel numero.'),
        7: lambda: card_front('OGGETTO ROSSO', 7, 'IL REMO DI NICO', *art_7(), text='Il portachiavi a forma di remo di Nico. È piccolo… ma con la magia di Leo può diventare grande!'),
        8: lambda: card_front('INDIZIO', 8, 'LA TAVOLETTA', *art_8(), text='Su questa tavoletta gli allievi del santuario imparavano i segni antichi.'),
        9: lambda: card_front('ENIGMA', 9, 'I TRE RAMI', *art_9(), text='Becco è passato da un solo ramo. Quale? Il numero alla fine del ramo giusto è la carta da prendere.'),
    }[key]()


if __name__ == '__main__':
    order = ['T', 1, 2, 3, 4, 5, 7, 8, 9]
    html = sheet('Carte foglio 1 – Fronte', 'Leoni di Laguna – Escape · Carte foglio 1 · FRONTE (ritaglia lungo i bordi)',
                 [card(k) for k in order], 'Chi ritaglia: cerca di non leggere le carte!')
    write('Carte1_Fronte.dc.html', html)
    print(len(html))
