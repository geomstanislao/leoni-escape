# Level versions (Bambini k / Adulti a) of episodes 1-3, built as patches over the family episodes.
# Output: levels.json = {id: patch}, and <id>_cards.json with re-wrapped card HTML (art reused).
import json, re, sys
SD='/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/'
sys.path.insert(0, SD+'escA')
from common import card_front

def base_cards(ep):
    return json.load(open(SD+('tv/cards.json' if ep=='ep1' else 'episodi/%s_cards.json'%ep)))

def parse(h):
    typ=re.search(r'<span[^>]*>([^<]+)</span>',h).group(1)
    m=re.search(r'background: #fbe7a6[^>]*>(.*?)</div>',h); strip=m.group(1) if m else None
    m=re.search(r"font-family: 'Bangers'[^>]*>(.*?)</div>",h,re.S); title=m.group(1); te=m.end()
    s=h.index('<svg',te); depth=0; i=s
    while True:
        a=h.find('<svg',i+1); b=h.find('</svg>',i+1)
        if a!=-1 and a<b: depth+=1; i=a
        else:
            if depth==0: e=b+6; break
            depth-=1; i=b
    svg=h[s:e]
    vb=re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',svg); H=float(vb.group(2))
    m=re.search(r'<div style="flex: 1;[^>]*>(.*)</div>\s*</div>\s*$',h,re.S); text_html=m.group(1)
    band=h[:h.index(title)]
    star='<svg' in band[band.index('</span>'):]
    mnum=re.search(r'>(\d+)</div></div>',band); num=None if star or not mnum else int(mnum.group(1))
    return dict(typ=typ,strip=strip,title=title,svg=svg,H=H,text_html=text_html,num=num)

def norm_svg(svg,H):
    head=svg[:svg.index('>')+1]; rest=svg[len(head):]
    head=re.sub(r'\s(width|height|style|preserveAspectRatio)="[^"]*"','',head)
    head=head[:-1]+' preserveAspectRatio="xMidYMid meet" style="width: 100%%; height: %spx; display: block">'%(int(H) if H==int(H) else H)
    return head+rest

def rewrap(src_html,n=None,typ=None,title=None,text=None,strip=False,H=None,keepnum=True):
    p=parse(src_html)
    H=H or p['H']
    num=(p['num'] if n is None else n)
    if p['num'] is None and n is None: num=None
    st=p['strip'] if strip is False else strip
    return card_front(typ or p['typ'], num, title or p['title'], H, norm_svg(p['svg'],H),
                      text=text, strip=st, text_html=None if text else p['text_html'])

# ---------------------------------------------------------------- patches
# drop: cards removed; text/title: overrides; rules: req/next/disc/keep overrides (None deletes);
# clone: new card numbers made from another card's art {new:(src, typ, title, strip, text)}
P={}

P['ep1k']=dict(base='ep1',level='k',title="Il cavallino d'oro",place="Este, quasi 3.000 anni fa",
 intro="Il gabbiano Becco ha rubato il cavallino d'oro della dea Reitia! Riportatelo sull'altare. Versione corta e facile, per i più piccoli.",
 drop=[14,20,26,46,52,53,56,58,61,64,68,71,72,74,76,81,84,86],
 text={
  1:"Il cavallino d'oro della dea Reitia è sparito: l'ha preso Becco! Aiutate Leo a riportarlo sull'altare. Prendete le carte **2**, **3** e **4**.",
  2:"Il santuario della dea Reitia. L'altare è vuoto! Cercate nel disegno i cerchietti dorati con un numero: sono le carte da prendere.",
  3:"«Becco ha chiuso la mia cassa con due segni antichi. Dentro c'è la mappa del fiume! I segni sono disegnati sulla tavoletta del santuario.»",
  5:"Sulla cassa ci sono due segni. Cercateli sulla tavoletta (carta 8): sotto ogni segno c'è un numero. Attenti: i Veneti leggevano da DESTRA a SINISTRA! Il numero che formate è la carta da prendere.",
  9:"Becco è passato da un solo ramo del fiume. Quale? Contate le piume grigie su ogni ramo. Il numero alla fine del ramo giusto è la carta da prendere.",
  19:"Leo annusa la piuma: «Becco ha perso TRE piume grigie sul ramo che ha preso. Le piume bianche non contano: sono degli aironi!»",
  50:"Ecco il cavallino d'oro! Leo lo prende tra le zampe e vi riporta in volo al santuario. Prendete la carta **39**.",
  39:"Sull'altare c'è scritto: PRIMA I CAVALLI DI BRONZO, POI I FUOCHI ACCESI. Guardate la carta 2: contate i cavallini, poi le torce accese. Il numero è la carta da prendere.",
  43:"Il cavallino d'oro è tornato sull'altare! Bravissimi! Contate le vostre piume: 9-10 LEONI D'ORO · 6-8 LEONI D'ARGENTO · 1-5 LEONI DI BRONZO.",
 },
 rules=dict(next={50:[39]},req={39:[50]},keep={50:[2,50],46:None}),
 tess={1:'veneti',3:'reitia',8:'alfabeto',43:'museo'},
 tessere={
  'veneti':("I Veneti antichi","Tanto tempo fa, qui vicino, viveva un popolo chiamato Veneti. Este era una delle loro città."),
  'reitia':("La dea Reitia","I Veneti pregavano la dea Reitia e le portavano piccoli regali di bronzo, come cavallini."),
  'alfabeto':("Scrivere al contrario","I Veneti avevano le loro lettere e spesso scrivevano da destra a sinistra."),
  'museo':("Il museo di Este","A Este c'è un museo dove si vedono i cavallini e le tavolette dei Veneti antichi."),
 },
 hints=[
  dict(done=[5,8],t="All'inizio",h=["Cercate nei disegni i cerchietti dorati con un numero.","Nella carta 2, il santuario, ci sono due numeri nascosti.","Prendete le carte 5 e 8."]),
  dict(done=[16],t="La cassa",h=["Trovate i due segni del lucchetto sulla tavoletta (carta 8).","Leggete da destra a sinistra.","Il primo segno vale 1, il secondo 6: carta 16."]),
  dict(done=[29],t="Come si parte?",h=["Nel disegno del fiume (carta 10) ci sono due numeri nascosti.","Premete «Combina»: un oggetto rosso e un oggetto blu.","Il remo (7) + la barca (22) = carta 29."]),
  dict(done=[27],t="I tre rami",h=["Leggete la piuma grigia (carta 19).","Contate solo le piume grigie, non quelle bianche.","Il ramo di mezzo ha 3 piume grigie: carta 27."]),
  dict(done=[30],t="Becco non molla",h=["Nel disegno del canneto c'è un numero nascosto su Becco.","Becco ha fame… Combinate il panino con Becco.","Il panino (12) + Becco (18) = carta 30."]),
  dict(done=[50],t="Il cavallino in acqua",h=["Cercate il numero vicino alle bolle (carta 30).","Serve la corda trovata nella cassa.","La corda (15) + le bolle (35) = carta 50."]),
  dict(done=[43],t="L'altare",h=["Guardate di nuovo la carta 2, il santuario.","Prima cifra: i cavallini. Seconda cifra: le torce accese.","4 cavallini e 3 torce: carta 43."]),
 ])

P['ep1a']=dict(base='ep1',level='a',title="Il cavallino d'oro",place="Este, VI secolo a.C.",
 intro="Nel santuario della dea Reitia, a Este, i Veneti antichi offrivano statuette e lamine di bronzo. Becco ha rubato un cavallino d'oro. Versione con più storia vera e indizi meno espliciti.",
 drop=[43],
 clone={34:(43,None,None,None,"Il cavallino d'oro torna sull'altare. Per i Veneti il cavallo era simbolo di ricchezza e di prestigio: per questo lo offrivano agli dèi. Piume: 9-10 LEONI D'ORO · 6-8 D'ARGENTO · 1-5 DI BRONZO."),
        43:(24,'SBAGLIATO','SBAGLIATO!','Risposta a: L\'ALTARE',"Avete scritto il numero come lo scriviamo noi. Sull'altare c'è scritto di usare il verso dei Veneti! Perdete 1 piuma e riprovate.")},
 text={
  1:"Este, VI secolo a.C. Qui vivono i Veneti antichi, popolo di allevatori, artigiani del bronzo e commercianti. Dal santuario della dea Reitia è sparito un cavallino d'oro offerto in voto: l'ha rubato Becco! Prendete le carte **2**, **3** e **4**.",
  2:"Il santuario di Reitia, in località Baratella. Gli archeologi vi hanno trovato migliaia di offerte in bronzo: statuette, lamine, stili per scrivere. Guardate bene il disegno: i numeri nei cerchietti dorati sono carte.",
  3:"«Reitia protegge le nascite, la salute e la scrittura. Becco ha chiuso la mia cassa con un lucchetto di segni dell'alfabeto venetico: dentro c'è la mappa del fiume. I valori dei segni sono sulla tavoletta.»",
  8:"Una tavoletta alfabetica in bronzo: gli allievi del santuario vi copiavano lettere e gruppi di lettere per imparare a scrivere.",
  11:"Appunti di Sofia: «L'alfabeto venetico deriva da quello etrusco. Come gli Etruschi, i Veneti scrivevano spesso nel verso opposto al nostro.»",
  53:"«I cavalli veneti erano famosi anche in Grecia: il poeta Alcmane li lodava e Dionisio di Siracusa li comprava per le corse. Baio è nel recinto (carta **56**): macchia bianca in fronte, criniera intrecciata, ma NON coda corta.»",
  76:"«La chiave? Ve la do solo se indovinate! Sono di bronzo, ho righe di lettere e gruppi di lettere, e gli allievi mi copiavano per imparare a scrivere. Chi sono?» Il numero sotto la risposta giusta è la carta.",
  39:"Sull'altare è inciso: PRIMA I CAVALLI DI BRONZO, POI I FUOCHI ACCESI. SCRIVI COME I VENETI. Riprendete la carta 2 e contate: il numero, scritto nel verso giusto, è la carta da prendere.",
 },
 rules=dict(req={34:[39],43:[39]}),
 wrong_add=[43], final=34,
 tess={1:'veneti',3:'reitia',8:'alfabeto',53:'cavalli',34:'museo'},
 tessere={
  'veneti':("I Veneti antichi","Tra il IX e il I secolo a.C. il Nord-Est d'Italia era abitato dai Veneti, oggi detti Paleoveneti. Este, sull'Adige, fu uno dei loro centri principali; altri erano Padova, Oderzo, Vicenza e Treviso."),
  'reitia':("Il santuario di Reitia","Il santuario della dea Reitia, alla Baratella di Este, fu frequentato per secoli fino all'età romana. Vi sono state trovate migliaia di offerte in bronzo: statuette di cavalli, guerrieri e offerenti, lamine e stili per scrivere."),
  'alfabeto':("L'alfabeto venetico","I Veneti adattarono l'alfabeto etrusco alla loro lingua, di famiglia indoeuropea. Le iscrizioni corrono spesso da destra a sinistra. Le tavolette alfabetiche di Este servivano per insegnare la scrittura."),
  'cavalli':("I cavalli dei Veneti","I cavalli veneti erano celebri nel mondo greco: li cita il poeta Alcmane già nel VII secolo a.C., e lo storico Strabone racconta che Dionisio di Siracusa ne fece allevare per le corse."),
  'museo':("Il Museo Atestino","Molti reperti del santuario di Reitia e delle necropoli di Este, comprese le tavolette alfabetiche e le situle decorate, sono esposti al Museo Nazionale Atestino di Este."),
 },
 hints_replace={'L\'altare (carta 39)':dict(done=[34],t="L'altare (carta 39)",h=["Guardate di nuovo la carta 2: cavallini di bronzo e torce accese.","4 cavallini e 3 torce fanno 43… ma va scritto come i Veneti.","Da destra a sinistra: carta 34."])},
 hint_del=[])

P['ep2k']=dict(base='ep2',level='k',title="Amici di Roma",place="Patavium (Padova), circa 2.050 anni fa",
 intro="Becco ha preso i rotoli del giovane Tito! Ritrovateli nella Padova dei Romani. Versione corta e facile, per i più piccoli.",
 drop=[18,142],
 text={
  1:"Patavium, oggi Padova, tanto tempo fa. Qui vivono Veneti e Romani, amici. Il giovane Tito ha perso i suoi rotoli: li ha presi Becco! Prendete le carte **2**, **3** e **4**.",
  11:"«I Romani scrivevano i numeri con le lettere: I = 1, V = 5, X = 10, L = 50. Si sommano: XX = 20. Ma la I PRIMA della V toglie 1: IV = 4.»",
  6:"Sul miliario, la colonna di pietra della strada, c'è scritto XXIV. Usate il taccuino di Sofia (carta 11): XX = 20 e IV = 4. Quante miglia mancano al porto? Il numero è la carta da prendere.",
  5:"Leo annusa una piuma di Becco: «Sa d'olio!» Cercate l'anfora dell'olio, quella con le olive disegnate. Sotto c'è il suo numero romano: XL vale 40 e VI vale 6. Il numero è la carta da prendere.",
  46:"Nell'anfora dell'olio ci sono i rotoli di Tito, un po' unti ma salvi! Tito: «Da grande scriverò tanti libri sulla storia di Roma!» Quel ragazzo diventerà Tito Livio, un grande storico.",
 },
 title_over={46:"VITTORIA!"},
 rules=dict(next={46:None}),
 final=46,
 tess={2:'patavium',11:'numeri',6:'strade',46:'livio'},
 tessere={
  'patavium':("Patavium","Padova è una città antichissima: i Romani la chiamavano Patavium."),
  'numeri':("I numeri romani","I Romani scrivevano i numeri con le lettere: I, V, X, L, C…"),
  'strade':("Le strade romane","I Romani costruivano strade di pietra e mettevano colonne con le distanze."),
  'livio':("Tito Livio","Tito Livio, nato a Padova, scrisse la storia di Roma in tantissimi libri."),
 },
 hint_del_done=[142])

P['ep2a']=dict(base='ep2',level='a',title="Amici di Roma",place="Patavium, I secolo a.C.",
 intro="Patavium è una delle città più ricche dell'Italia romana. Il giovane Tito, futuro grande storico, ha perso i suoi rotoli. Versione con più storia vera e indizi meno espliciti.",
 text={
  1:"Patavium, I secolo a.C. I Veneti sono alleati di Roma da tempo, e verso il 49 a.C. gli abitanti diventano cittadini romani. Il giovane Tito ha perso i suoi rotoli: li ha presi Becco! Prendete le carte **2**, **3** e **4**.",
  2:"Il foro di Patavium. Il geografo greco Strabone racconta che la città era ricchissima e contava ben 500 cavalieri. Guardate bene il disegno!",
  3:"«Mi chiamo Tito. Un giorno scriverò tutta la storia di Roma, dalla fondazione ai giorni nostri! Becco ha portato via i miei rotoli verso il fiume.»",
  9:"«La lana di Patavium è famosa: tuniche e mantelli partono da qui fino a Roma. Becco è volato verso il porto sul fiume. Prendete il mio mulo col carretto (carta **22**)… ma si muove solo per qualcosa di buono!»",
  11:"Appunti di Sofia: «I Romani scrivevano i numeri con le lettere I, V, X, L, C, D e M, che valgono 1, 5, 10, 50, 100, 500 e 1000.»",
  6:"Lungo le strade i Romani posavano un miliario ogni mille passi, cioè circa un chilometro e mezzo. Quante miglia mancano al porto? Il numero è la carta da prendere.",
  24:"XXIV = 24 miglia, circa 35 km. Ecco il porto fluviale pieno di barche e di anfore: i fiumi collegavano Patavium al mare. Becco ha nascosto i rotoli in un'anfora! Prendete la carta **5**.",
  142:"CXLII = 142: tanti sono i libri della storia di Roma «dalla fondazione della città» che Tito Livio scrisse in più di quarant'anni. Di questi, ne sono arrivati a noi solo 35.",
 },
 tessere={
  'patavium':("Patavium","Patavium, l'odierna Padova, era tra le città più ricche dell'Italia romana. Strabone ricorda i suoi 500 cavalieri e il commercio di tessuti di lana verso Roma."),
  'numeri':("I numeri romani","Sette lettere: I, V, X, L, C, D, M. Si sommano da sinistra a destra, ma una lettera minore scritta prima di una maggiore si sottrae: IV = 4, XL = 40, CM = 900."),
  'strade':("Il miglio romano","Il miglio romano era di mille passi doppi, circa 1.480 metri. I miliari, colonne di pietra lungo le vie, indicavano la distanza e spesso il nome di chi aveva costruito o restaurato la strada."),
  'anfore':("Anfore e garum","Le anfore trasportavano olio, vino e garum, la salsa di pesce fermentato amatissima dai Romani. Sulle anfore si scrivevano spesso a pennello contenuto e provenienza."),
  'livio':("Tito Livio","Nato a Patavium nel 59 a.C., Tito Livio scrisse gli «Ab Urbe condita libri», 142 libri di storia di Roma. Se ne conservano 35. Morì nella sua città nel 17 d.C."),
 })

P['ep3k']=dict(base='ep3',level='k',title="Fuga in laguna",place="Altino e la laguna, tanto tempo fa",
 intro="Le famiglie di Altino scappano sulle isole della laguna. Aiutate Elena a costruire una casa sull'acqua. Versione facile, per i più piccoli.",
 text={
  1:"Altino, tanto tempo fa. Arriva un re cattivo, Attila, e la gente scappa in barca verso le isole della laguna. Aiutate Elena e la sua famiglia! Prendete le carte **2**, **3** e **4**.",
  3:"«Andiamo sulle isole: lì saremo al sicuro. Ma attenti, l'acqua è bassa: bisogna seguire i pali piantati nell'acqua!»",
  11:"«Nella laguna l'acqua profonda è segnata da gruppi di pali: le briccole. Seguite sempre le briccole, se no la barca si ferma nel fango!»",
  9:"Seguite con il dito la strada con le briccole fino alla fine, senza saltarne nessuna. Il numero dell'isola dove arrivate è la carta da prendere.",
  32:"La nonna: «Prima entra l'acqua del mare, poi il sole la asciuga, alla fine resta il sale.» Prima cifra: la vasca con l'acqua del mare. Seconda cifra: la vasca con il sale bianco.",
  50:"Bum, bum! I pali entrano nel fango e la casa sui pali è pronta. Leo: «Da queste casette sull'acqua nascerà una città bellissima: Venezia!»",
 },
 tessere={
  'briccole':("Le briccole","In laguna ci sono pali piantati nell'acqua: mostrano dove le barche possono passare."),
  'pali':("Case sui pali","Il fango è molle, così le case si costruiscono sopra tanti pali di legno."),
  'sale':("L'oro bianco","Con l'acqua del mare e il sole si fa il sale. Una volta valeva tantissimo!"),
  'venezia':("Nasce Venezia","Dalle casette sulle isole della laguna, piano piano, è nata Venezia."),
 })

P['ep3a']=dict(base='ep3',level='a',title="Fuga in laguna",place="Altino e la laguna, anno 452",
 intro="Dopo la distruzione di Aquileia da parte di Attila, gli abitanti di Altino cercano rifugio nella laguna. Versione con più storia vera e indizi meno espliciti.",
 text={
  1:"Altino, anno 452. Attila, re degli Unni, ha distrutto Aquileia, la grande città romana del Nord-Est. Gli abitanti di Altino caricano le barche e cercano rifugio tra le isole della laguna. Prendete le carte **2**, **3** e **4**.",
  3:"«Sulle isole saremo al sicuro: con l'acqua bassa né le navi né i cavalieri possono arrivarci. Ma chi non conosce i canali si incaglia. Molti torneranno ad Altino… e molti resteranno.»",
  11:"Appunti di Sofia: «I canali navigabili della laguna sono segnalati da gruppi di pali, le briccole. Fuori dai canali, a volte, l'acqua è alta una spanna.»",
  31:"«Facciamo il sale con l'acqua del mare.» Leo: «Tra ottant'anni Cassiodoro scriverà di voi: c'è chi può fare a meno dell'oro, ma nessuno può fare a meno del sale.» La nonna: «Capite le mie vasche (carta **32**)?»",
  32:"Il sale si ottiene facendo evaporare l'acqua di mare al sole, di vasca in vasca. Prima cifra: la vasca da cui si comincia. Seconda cifra: la vasca dove il sale è pronto.",
  50:"Bum, bum! I pali entrano nel fango fino allo strato duro, il «caranto». La casa è pronta. Su milioni di pali di legno, nei secoli, nascerà Venezia.",
 },
 tessere={
  'briccole':("Le briccole","Le briccole sono gruppi di pali che segnano i canali navigabili della laguna. Ancora oggi guidano le barche: fuori dai canali i bassifondi, le «barene» e le «velme», fanno incagliare."),
  'pali':("Il caranto","Sotto il fango della laguna c'è uno strato compatto di argilla, il caranto. I Veneziani vi piantarono milioni di pali di legno di larice e di rovere, su cui poggiano ancora le fondazioni della città."),
  'sale':("Il sale di Cassiodoro","Verso il 537 Cassiodoro, alto funzionario del regno dei Goti, scrisse ai «tribuni marittimi» della laguna: descriveva case simili a nidi di uccelli acquatici e la produzione del sale, più indispensabile dell'oro."),
  'venezia':("Dalle isole alla città","Dopo le invasioni nacquero centri come Grado, Torcello ed Eraclea. A Torcello la cattedrale fu fondata nel 639; secondo la tradizione nel 697 fu eletto il primo doge."),
 })

import glob,os
PATHS={}
for f in sorted(glob.glob(SD+'episodi/levels_extra/*.json')):
    pid=os.path.basename(f)[:-5]; q=json.load(open(f))
    PATHS[pid]=q.pop('test_path',None)
    for fld in ('text','title_over','tess'):
        if fld in q: q[fld]={int(k):v for k,v in q[fld].items()}
    if 'clone' in q: q['clone']={int(k):tuple(v) for k,v in q['clone'].items()}
    P[pid]=q
json.dump(PATHS,open(SD+'episodi/levels_paths.json','w'))
json.dump(P,open(SD+'episodi/levels.json','w'),ensure_ascii=False,indent=1)

def build_cards(pid,shrink={}):
    p=P[pid]; bc=base_cards(p['base']); out={}; changed=[]
    D=set(p.get('drop',[]))
    for k,h in bc.items():
        if not k.isdigit() or int(k) in D: continue
        n=int(k)
        if n in p.get('text',{}) or n in p.get('title_over',{}):
            H=shrink.get(n)
            out[k]=rewrap(h,title=p.get('title_over',{}).get(n),text=p.get('text',{}).get(n),H=H); changed.append(n)
        else: out[k]=h
    for n,(src,typ,title,strip,text) in p.get('clone',{}).items():
        out[str(n)]=rewrap(bc[str(src)],n=n,typ=typ,title=title,strip=strip if strip else False,text=text,H=shrink.get(n)); changed.append(n)
    return out,changed

if __name__=='__main__':
    import subprocess
    shr={pid:{} for pid in P}
    for it in range(6):
        allbad=0
        for pid in P:
            cards,ch=build_cards(pid,shr[pid])
            json.dump(cards,open(SD+'episodi/%s_cards.json'%pid,'w'),ensure_ascii=False)
            r=subprocess.run(['node',SD+'tv/overflow.js',SD+'episodi/%s_cards.json'%pid,','.join(map(str,ch))],capture_output=True,text=True)
            bad=json.loads(r.stdout or '{}')
            for k,H in bad.items():
                n=int(k); cur=shr[pid].get(n) or parse(cards[k])['H']
                shr[pid][n]=max(60,cur-15); allbad+=1
            if bad: print(it,pid,bad)
        if not allbad: break
    print('done',{k:v for k,v in shr.items() if v})
