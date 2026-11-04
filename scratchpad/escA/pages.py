from common import *

def leo_svg(w, h, s, cx, cy, **kw):
    return T('svg', leo(cx, cy, s, **kw), viewBox='0 0 %s %s' % (w, h), style='width: %spx; height: %spx; display: block; flex: none' % (w, h), role='img', aria_label='Leo, il leoncino alato con le ali dorate')

CF = "font-family: 'Comic Neue', sans-serif"
HB = "font-family: 'Bangers', sans-serif"
ROOT = '<div style="width: 794px; height: 1123px; box-sizing: border-box; padding: 40px; background: #fdf8ee; display: flex; flex-direction: column; %s; color: #2a1a10">' % CF

def h2(t):
    return '<div style="%s; font-size: 24px; color: #a8322a; letter-spacing: 1px; line-height: 1; margin: 0 0 6px">%s</div>' % (HB, t)

def foot(n, extra=''):
    return '<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: 700; color: #7a5a3e"><span>Leoni di Laguna · Escape · pagina %s</span><span>%s</span></div>' % (n, extra)

# ---------------- Regole
legend = [('#5f9a5a', 'Luogo'), ('#c99a2e', 'Personaggio'), ('#7a5a3e', 'Indizio'), ('#d9472f', 'Oggetto rosso'), ('#4f74a8', 'Oggetto blu'),
          ('#8a5fb0', 'Enigma'), ('#e39a3b', 'Combinazione / Risposta'), ('#8d9097', 'Sbagliato')]
leg = ''.join('<div style="display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 700"><div style="width: 18px; height: 18px; flex: none; box-sizing: border-box; background: %s; border: 2px solid #3b2416; border-radius: 3px"></div><span>%s</span></div>' % (c, t) for c, t in legend)
prep = ['1. Stampate le pagine 2–7 fronte-retro (lato lungo). Se la stampante non fa il fronte-retro, stampate solo i fronti e scrivete il numero dietro ogni carta con la matita.',
        '2. Ritagliate le carte (meglio se lo fa un adulto senza leggerle!).',
        '3. Mettete le carte coperte in un mazzo, in ordine di numero.',
        '4. Tenete da parte il foglio «Gli aiuti di Leo».',
        '5. Mettete davanti a voi la carta «Le vostre piume»: partite con 10 piume.']
rules = [('NUMERI NASCOSTI', 'se in un disegno vedete un numero in un cerchietto dorato, prendete la carta con quel numero.'),
         ('COMBINARE', 'un oggetto ROSSO e un oggetto BLU si possono usare insieme. Sommate i loro numeri e prendete la carta con quel risultato. Se in alto c\'è scritto «Combinazione:» con i nomi dei vostri due oggetti, è giusto!'),
         ('ENIGMI', 'la soluzione è sempre un numero. Prendete la carta con quel numero: se in alto c\'è «Risposta a:» con il nome del vostro enigma, controllate se è GIUSTO o SBAGLIATO.'),
         ('ERRORI', 'se la carta non esiste, o è per un\'altra combinazione o un altro enigma, rimettetela subito nel mazzo senza leggerla e perdete 1 piuma.'),
         ('SCARTARE', 'quando una carta dice di scartare, mettete quelle carte da parte: non servono più.'),
         ('AIUTI', 'se siete bloccati, leggete un aiuto sul foglio «Gli aiuti di Leo». Ogni aiuto costa 1 piuma.')]
o = [ROOT]
o.append('<div style="position: relative; height: 128px; flex: none">%s<div class="balloon tail-bl" style="left: 128px; top: 8px; width: 330px; height: 84px; font-size: 17px; padding: 0 22px">Pax tibi! Aiutateci a ritrovare il cavallino d\'oro!</div></div>' % leo_svg(120, 128, 0.85, 62, 70, wing='small', la=(-34, 22), ra=(44, -28)))
o.append('<div style="%s; font-size: 54px; color: #2a1a10; line-height: 1; margin-top: 2px">LEONI DI LAGUNA – ESCAPE</div>' % HB)
o.append('<div style="%s; font-size: 30px; color: #e2573a; -webkit-text-stroke: 1px #3b2416; line-height: 1; margin-top: 2px; letter-spacing: 1px">Il cavallino d\'oro</div>' % HB)
o.append('<div style="font-size: 15px; font-weight: 700; color: #7a5a3e; margin: 8px 0 12px; padding: 6px 0; border-top: 2px solid #3b2416; border-bottom: 2px solid #3b2416">Gioco cooperativo · 2–6 giocatori · da 6 anni · 30–45 minuti · niente dadi, niente app</div>')
o.append(h2('PREPARAZIONE'))
o.append('<div style="font-size: 14px; line-height: 1.35; margin-bottom: 10px">%s</div>' % ''.join('<div style="margin-bottom: 2px">%s</div>' % t for t in prep))
o.append(h2('COME SI GIOCA'))
o.append('<div style="font-size: 14px; line-height: 1.35; margin-bottom: 10px">Si gioca tutti insieme. Girate la carta 1 e leggetela ad alta voce. Le carte vi diranno quali altre carte prendere.</div>')
o.append(h2('I TIPI DI CARTA'))
o.append('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px 10px; margin-bottom: 10px">%s</div>' % leg)
o.append(h2('LE REGOLE'))
o.append('<div style="font-size: 14px; line-height: 1.35; margin-bottom: 10px">%s</div>' % ''.join('<div style="display: flex; gap: 8px; margin-bottom: 4px"><span style="color: #a8322a; font-weight: 700">●</span><span><b>%s:</b> %s</span></div>' % (a, b) for a, b in rules))
o.append(h2('FINE'))
o.append('<div style="font-size: 14px; line-height: 1.35">Avete vinto quando trovate la carta VITTORIA! Contate le piume rimaste.</div>')
o.append(foot(1, 'Serve solo: forbici e una matita.'))
o.append('</div>')
write('Regole.dc.html', HEAD % 'Regole' + '\n'.join(o) + '\n' + TAIL)

# ---------------- Aiuti
rows = [("All'inizio", "Cercate nei disegni i cerchietti dorati con un numero.", "Nella carta 2 ci sono due numeri nascosti.", "Prendete le carte 5 e 8."),
        ("La cassa (carta 5)", "Trovate i due segni del lucchetto sulla tavoletta (carta 8).", "Leggete il taccuino di Sofia (carta 11): in che verso scrivevano i Veneti?", "Da destra a sinistra: Λ = 1, ⊕ = 6 → carta 16."),
        ("Come si parte?", "Nel disegno del fiume (carta 10) c'è una barca con un numero.", "Un oggetto rosso + un oggetto blu: sommate i numeri.", "Remo 7 + Barca 22 = carta 29."),
        ("I tre rami (carta 9)", "Leggete la piuma grigia (carta 19).", "Contate solo le piume grigie, non quelle bianche.", "Il ramo di mezzo ha 3 piume grigie → carta 27."),
        ("Becco non molla", "Becco ha fame…", "Panino (rosso) + Becco (blu).", "12 + 18 = carta 30."),
        ("Il cavallino in acqua", "Cercate il numero vicino alle bolle (carta 30).", "Serve un oggetto rosso trovato nella cassa.", "Corda 15 + Bolle 35 = carta 50."),
        ("L'altare (carta 39)", "Riprendete la carta 2 e contate.", "Prima cifra: cavallini di bronzo. Seconda cifra: torce accese.", "4 cavallini e 3 torce → carta 43.")]
COLS = 'grid-template-columns: 138px 190px 190px 160px'
cell = 'box-sizing: border-box; padding: 8px 10px; border-right: 2px solid #3b2416; font-size: 13.5px; line-height: 1.3; font-weight: 700; display: flex; align-items: center'
o = [ROOT]
o.append('<div style="display: flex; align-items: center; gap: 14px; height: 120px; flex: none"><div style="flex: 1"><div style="%s; font-size: 48px; line-height: 1; color: #2a1a10">GLI AIUTI DI LEO</div><div style="font-size: 15px; font-weight: 700; color: #7a5a3e; margin-top: 8px; line-height: 1.3">Ogni aiuto costa 1 piuma. Leggete un aiuto alla volta e coprite il resto con un foglio!</div></div>%s</div>' % (HB, leo_svg(120, 120, 0.8, 60, 66, wing='small', la=(-34, 22), ra=(44, -28))))
o.append('<div style="margin-top: 14px; border: 2.5px solid #3b2416; border-radius: 8px; overflow: hidden; background: #fffdf7">')
o.append('<div style="display: grid; %s; background: #a8322a; color: #ffffff; %s; font-size: 20px; letter-spacing: 1px"><div style="padding: 6px 10px; border-right: 2px solid #3b2416">Dove siete bloccati</div><div style="padding: 6px 10px; border-right: 2px solid #3b2416">Aiuto 1</div><div style="padding: 6px 10px; border-right: 2px solid #3b2416">Aiuto 2</div><div style="padding: 6px 10px">Soluzione</div></div>' % (COLS, HB))
for i, (a, b, c, d) in enumerate(rows):
    bg = '#fffdf7' if i % 2 == 0 else '#f6ead2'
    o.append('<div style="display: grid; %s; height: 98px; background: %s; border-top: 2px solid #3b2416"><div style="%s; color: #a8322a">%s</div><div style="%s">%s</div><div style="%s">%s</div><div style="%s; border-right: 0"><div style="transform: rotate(180deg)">%s</div></div></div>' % (COLS, bg, cell, a, cell, b, cell, c, cell, d))
o.append('</div>')
o.append(foot(8))
o.append('</div>')
write('Aiuti.dc.html', HEAD % 'Gli aiuti di Leo' + '\n'.join(o) + '\n' + TAIL)
