from common import *
FR = {1: ['T', 1, 2, 3, 4, 5, 7, 8, 9], 2: [10, 11, 12, 15, 16, 18, 19, 22, 24], 3: [27, 29, 30, 31, 35, 39, 43, 50, 'S']}
for n, order in FR.items():
    back = []
    for r in range(3):
        row = order[r * 3:r * 3 + 3][::-1]
        back += row
    cards = [card_back(None if k in ('T', 'S') else k) for k in back]
    print(n, back)
    html = sheet('Carte foglio %d – Retro' % n, 'Leoni di Laguna – Escape · Carte foglio %d · RETRO (stampa fronte-retro, lato lungo)' % n, cards)
    write('Carte%d_Retro.dc.html' % n, html)
