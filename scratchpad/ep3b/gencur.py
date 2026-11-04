import re
D = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/fumetto/project/'
s = open(D + 'Ep2_Curiosita.dc.html', encoding='utf-8').read()
s = s.replace('Ep. 2 – Le curiosità del Leone', 'Ep. 3 – Le curiosità del Leone')
s = s.replace('Ep. 2 – Amici di Roma', 'Ep. 3 – Fuga in laguna')
s = s.replace('Quei rotoli <br>erano miei!', 'Il martello <br>mi serviva!')
old = [("Patavium", "Perché nella laguna?"), ("Veneti e Romani", "Attila"), ("Tito Livio", "Case sui pali"), ("Le strade romane", "L'oro bianco")]
for a, b in old:
    s = s.replace('color: #2a1a10">%s</div>' % a, 'color: #2a1a10">%s</div>' % b, 1)
texts = [
 ("Così i Romani chiamavano Padova. Era una delle città più ricche dell'Italia romana.", "Quando arrivavano eserciti nemici, la gente della terraferma si rifugiava sulle isole: l'acqua bassa e i canali la proteggevano."),
 ("I Veneti diventarono alleati dei Romani e, col tempo, anche cittadini romani.", "Era il re degli Unni. Nel 452 distrusse Aquileia e molte persone fuggirono verso la laguna."),
 ("Nato a Patavium, scrisse una grandissima storia di Roma, dalla sua fondazione. Era divisa in ben 142 libri!", "Il fondo della laguna è fangoso, così si piantavano pali di legno. Anche Venezia oggi poggia su milioni di pali!"),
 ("La Via Annia univa Patavium ad altre città del Veneto, fino ad Aquileia.", "Nella laguna si produceva il sale facendo evaporare l'acqua del mare. Era preziosissimo per conservare il cibo."),
 ("Al Museo Archeologico degli Eremitani, a Padova, puoi vedere tanti oggetti dell'epoca romana.", "Torcello è una delle prime isole abitate della laguna. Lì puoi visitare l'antica basilica e il Museo di Torcello."),
]
for a, b in texts:
    assert a in s, a
    s = s.replace(a, b, 1)
icons = [
 '<path d="M5 38 Q14 34 24 38 Q34 42 43 38"></path><path d="M13 30 L24 16 L35 30 Z"></path><path d="M16 30 V36 M32 30 V36"></path><path d="M22 36 V30 H26 V36"></path>',
 '<path d="M7 40 L24 10 L41 40 Z"></path><path d="M19 40 L24 27 L29 40"></path><path d="M24 10 V4 M24 4 L32 7 L24 10"></path>',
 '<path d="M8 24 H40"></path><path d="M11 24 L24 11 L37 24"></path><path d="M13 24 V42 M24 24 V42 M35 24 V42"></path><path d="M6 40 Q12 37 18 40 M30 40 Q36 37 42 40"></path>',
 '<path d="M24 7 L39 19 L24 41 L9 19 Z"></path><path d="M9 19 H39"></path><path d="M24 7 L17 19 L24 41 L31 19 L24 7"></path>',
 '<path d="M17 42 V17 H31 V42"></path><path d="M17 17 L24 6 L31 17"></path><path d="M21 24 H27 V31 H21 Z"></path><path d="M9 42 H39"></path>',
]
parts = re.split(r'(<svg viewBox="0 0 48 48"[^>]*>)(.*?)(</svg>)', s, flags=re.S)
# parts: pre, open, inner, close, pre, ...
assert (len(parts) - 1) // 4 == 5, len(parts)
out = [parts[0]]
for i in range(5):
    out += [parts[1 + 4 * i], '\n' + icons[i] + '\n', parts[3 + 4 * i], parts[4 + 4 * i]]
s = ''.join(out)
open(D + 'Ep3_Curiosita.dc.html', 'w', encoding='utf-8').write(s)
print('ok')
