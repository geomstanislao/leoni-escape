import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/escB')
from gen import *

PFX = {'v': ''}


def gid(n):
    return '%s_g%s' % (PFX['v'], n)


def il10(H=175):
    s = rect_bg(H, '#d6ecee')
    s += cloud(150, 24, 0.7) + cloud(40, 40, 0.5)
    s += water(96, H)
    s += P('M0 92 Q50 84 84 100 Q98 128 82 %d L0 %d Z' % (H, H), '#79a85a', stroke=OUT, stroke_width=2)
    s += ink(P('M30 118 L34 60 L44 60 L48 118 Z', '#8a5a2b'), C(24, 42, 22, '#5f9a5a'), C(52, 36, 24, '#6bab62'), C(38, 22, 20, '#5f9a5a'),
             P('M44 78 Q64 70 80 74', stroke='#6a4220', stroke_width=5), w=2)
    s += feather(78, 80, 70, '#8d9097', 0.8)
    s += hid(100, 66, 19)
    s += reeds(100, 150, 3, 56, 9) + reeds(206, 120, 3, 50, 8) + reeds(14, 170, 3, 50, 9)
    s += post(128, 104, 42)
    s += P('M131 112 Q140 122 150 126', stroke='#c9a96a', stroke_width=2.5)
    s += boat(158, 138, 1.2)
    s += hid(158, 142, 22)
    s += P('M100 160 q8 -4 16 0 t16 0', stroke='#cfeaf0', stroke_width=2, stroke_linecap='round')
    return s


def il18(H=120):
    s = rect_bg(H, '#d6ecee')
    s += cloud(40, 22, 0.6) + cloud(180, 34, 0.5)
    s += post(108, 98, 24)
    s += nest(108, 98, 84, 12)
    s += becco(108, 62, 0.5, legs_on=False)
    s += horse(110, 90, 0.5)
    s += ink(P('M68 98 Q108 118 148 98', '#b98a4a'), w=1.8)
    s += sparkles([(70, 74, 5), (146, 70, 4)])
    return s


def il39(H=120):
    s = rect_bg(H, '#efdcbc')
    s += R(0, 96, W, 24, '#cdb98c', stroke='none') + P('M0 96 L215 96', stroke=OUT, stroke_width=1.8)
    s += ink(R(14, 42, 108, 12, '#d9d0bd', rx=2), R(20, 54, 96, 42, '#cfc4ac'), w=2)
    s += R(26, 60, 84, 28, '#b9ad92', stroke=OUT, stroke_width=1.4)
    s += P('M32 82 L38 66 L44 82 L50 66 M56 66 L56 82 L66 82 M72 66 L84 66 L72 82 L86 82 M92 66 L92 82 M92 74 L102 74 M102 66 L102 82', stroke='#5e4a30', stroke_width=2, stroke_linecap='round', stroke_linejoin='round')
    s += sofia(158, 66, 0.55, expr='happy', la=(-24, 16), ra=(22, -44))
    s += glow_(171, 34, gid(39))
    s += horse(171, 34, 0.5)
    s += sparkles([(150, 18, 5), (196, 26, 4), (184, 10, 3)])
    return s


def il43(H=110):
    s = rect_bg(H, '#efdcbc')
    s += R(0, 90, W, 20, '#cdb98c', stroke='none') + P('M0 90 L215 90', stroke=OUT, stroke_width=1.8)
    s += glow_(96, 50, gid(43), 36)
    s += ink(R(68, 64, 56, 8, '#d9d0bd', rx=2), R(74, 72, 44, 18, '#cfc4ac'), w=1.8)
    s += horse(96, 52, 0.6)
    s += sparkles([(70, 38, 5), (124, 36, 5), (96, 14, 4)])
    s += priestess(34, 60, 0.52)
    s += leo(150, 68, 0.42, wing='open', eyes='closed', mouth='smile', la=(-34, -24), ra=(34, -24))
    s += becco(196, 80, 0.27, legs_on=False)
    s += ink(P('M-8 0 Q0 -8 8 0 Z', '#d9a05a'), R(-8, 0, 16, 2.5, '#7ec060'), P('M-8 2 L8 2 L6 6 L-6 6 Z', '#e8b469'), w=1.2, transform=tr(181, 70, 0.8, -10))
    return s


def il50(H=120):
    s = rect_bg(H, '#d6ecee')
    s += cloud(150, 16, 0.5)
    s += water(84, H)
    s += P('M0 62 L100 62 Q104 90 96 %d L0 %d Z' % (H, H), '#8ab463', stroke=OUT, stroke_width=1.8)
    s += toni(20, 40, 0.4, expr='smile', la=(-14, 10), ra=(18, 14))
    s += P('M30 52 q-8 -16 4 -18 q12 0 6 16', stroke=OUT, stroke_width=5, stroke_linecap='round') + P('M30 52 q-8 -16 4 -18 q12 0 6 16', stroke='#d8b574', stroke_width=3, stroke_linecap='round')
    s += nico(54, 40, 0.4, expr='det', la=(-14, 12), ra=(24, 16))
    s += sofia(88, 36, 0.4, expr='happy', la=(-14, 12), ra=(24, 14))
    s += P('M64 46 Q80 44 98 50 Q130 52 144 66 L150 86', stroke=OUT, stroke_width=5, stroke_linecap='round') + P('M64 46 Q80 44 98 50 Q130 52 144 66 L150 86', stroke='#d8b574', stroke_width=3, stroke_linecap='round')
    s += horse(152, 94, 0.55, rot=-12)
    s += P('M144 108 q-2 6 0 9 M160 106 q2 6 0 9', stroke='#9fb5c0', stroke_width=1.8, stroke_linecap='round')
    s += sparkles([(180, 80, 5), (130, 82, 4)])
    return s


S = lambda f_: None

# ---------------------------------------------------------------- sheet 2
PFX['v'] = 'Carte2'
c2 = [
    card('LUOGO', 10, 'IL FIUME', 'Il fiume vicino al santuario. Becco è volato di qui… Guardate bene il disegno!', il10(175), 175),
    card('INDIZIO', 11, 'IL TACCUINO DI SOFIA', 'Appunti di Sofia: «I Veneti antichi spesso scrivevano da DESTRA verso SINISTRA, al contrario di noi!»', il11(P, 120), 120),
    card('OGGETTO ROSSO', 12, 'IL PANINO DI TONI', 'Pane e formaggio. Toni non lo darebbe a nessuno… o quasi.', il12(P, 120), 120),
    card('OGGETTO ROSSO', 15, 'LA CORDA', 'Una corda robusta, intrecciata con fibre di piante.', il15(P, 120), 120),
    card('RISPOSTA', 16, 'GIUSTO!', 'Click! Nella cassa ci sono la mappa del fiume (carta **9**) e una corda (carta **15**). La sacerdotessa: «Becco è volato verso il fiume!» Prendete anche la carta **10**. Scartate le carte 5, 8 e 11.', il16(P, 100), 100, strip='Risposta a: LA CASSA'),
    card('OGGETTO BLU', 18, 'BECCO', '«Mio! Tutto mio!» Becco non molla il cavallino… però gli brontola la pancia.', il18(120), 120),
    card('INDIZIO', 19, 'LA PIUMA GRIGIA', 'Leo annusa la piuma: «Becco ha perso tre piume grigie come questa sul ramo che ha preso. Attenti: le piume bianche sono degli aironi!»', il19(P, 120), 120),
    card('OGGETTO BLU', 22, 'LA BARCA', 'Una barchetta di legno legata alla riva. Pronta a partire… ma senza remi!', il22(P, 120), 120),
    card('SBAGLIATO', 24, 'SBAGLIATO!', 'Su questo ramo Becco non è passato: le piume grigie sono troppo poche! Perdete 1 piuma, rimettete giù la carta e riprovate.', il24(P, 120), 120, strip='Risposta a: I TRE RAMI'),
]
write('Carte2_Fronte.dc.html', 'Carte 2 – Fronte', 'Leoni di Laguna – Escape · Carte foglio 2 · FRONTE (ritaglia lungo i bordi)', c2)

# ---------------------------------------------------------------- sheet 3
PFX['v'] = 'Carte3'
c3 = [
    card('RISPOSTA', 27, 'GIUSTO! IL CANNETO', 'Il ramo di mezzo porta al canneto. In cima a un palo c\'è il nido di Becco… e qualcosa luccica! Scartate le carte 9, 19 e 22.', il27(P, 150), 150, strip='Risposta a: I TRE RAMI'),
    card('COMBINAZIONE', 29, 'SI PARTE!', 'Leo tocca il portachiavi: diventa un remo vero! «Finalmente il remo serve!» Ma il fiume si divide in tre rami… Guardate la mappa (carta **9**) e ricordate cosa avete trovato sull\'albero.', il29(P, 105), 105, strip='Combinazione: REMO + BARCA'),
    card('COMBINAZIONE', 30, 'PLOF!', '«Vuoi un po\' de formaio?» Becco afferra il panino e lascia cadere il cavallino… PLOF! È finito in acqua. Guardate dove fa le bolle!', il30(P, 130), 130, strip='Combinazione: PANINO + BECCO'),
    card('SBAGLIATO', 31, 'SBAGLIATO!', 'Qui due piume su tre sono bianche: sono di un airone! Perdete 1 piuma, rimettete giù la carta e riprovate.', il31(P, 120), 120, strip='Risposta a: I TRE RAMI'),
    card('OGGETTO BLU', 35, 'LE BOLLE', 'Il cavallino è sul fondo, proprio sotto le bolle. L\'acqua è bassa ma piena di fango: con le mani non ci si arriva!', il35(P, 120), 120),
    card('ENIGMA', 39, 'L\'ALTARE', 'Sull\'altare c\'è scritto: PRIMA I CAVALLI DI BRONZO, POI I FUOCHI ACCESI. Riprendete la carta **2** e guardate bene: il numero che trovate è la carta da prendere.', il39(120), 120),
    card('RISPOSTA', 43, 'VITTORIA!', 'Il cavallino d\'oro è tornato sull\'altare! Contate le vostre piume: 9-10 LEONI D\'ORO · 6-8 LEONI D\'ARGENTO · 1-5 LEONI DI BRONZO (riprovate!)', il43(110), 110, strip='Risposta a: L\'ALTARE'),
    card('COMBINAZIONE', 50, 'RIPESCATO!', 'Ecco il cavallino d\'oro! Ora tornate al santuario e prendete la carta **39**. Scartate le carte usate, ma tenete la carta 2.', il50(120), 120, strip='Combinazione: CORDA + BOLLE'),
    card('SPECIALE', None, 'LE VOSTRE PIUME', 'Iniziate con 10 piume. Ogni errore o aiuto di Leo: cancellate una piuma con la matita (oppure usate 10 monetine).', il_segna(P, 150), 150, label='SPECIALE', star_=True),
]
write('Carte3_Fronte.dc.html', 'Carte 3 – Fronte', 'Leoni di Laguna – Escape · Carte foglio 3 · FRONTE (ritaglia lungo i bordi)', c3)
