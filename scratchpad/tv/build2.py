import json, os, re
SD='/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/'
TV=SD+'tv/'

def ep1():
    c=json.load(open(TV+'cards.json')); c.pop('SEGNA',None); c.pop('TITOLO',None)
    obj={7:['r','il remo'],12:['r','il panino'],15:['r','la corda'],14:['r','Baio'],20:['r','la chiave'],
         18:['b','Becco'],22:['b','la barca'],35:['b','le bolle'],58:['b','il fossato'],26:['b','il lucchetto']}
    req={2:[1],3:[1],4:[1],5:[2],8:[2],7:[4],11:[4],12:[4],16:[5],9:[16],10:[16],15:[16],19:[10],22:[10],
      29:[7,22],24:[9],27:[9],31:[9],18:[27],30:[12,18],35:[30],50:[15,35],52:[50],53:[52],58:[52],56:[53],
      61:[56],64:[56],68:[56],71:[56],14:[68],72:[14,58],74:[72],26:[74],76:[74],81:[76],84:[76],86:[76],
      20:[81],46:[20,26],39:[46],43:[39]}
    hints=[
     dict(done=[5,8],t="All'inizio",h=["Cercate nei disegni i cerchietti dorati con un numero.","Nella carta 2, il santuario, ci sono due numeri nascosti.","Prendete le carte 5 e 8."]),
     dict(done=[16],t="La cassa (carta 5)",h=["Trovate i due segni del lucchetto sulla tavoletta (carta 8).","Leggete il taccuino di Sofia (carta 11): in che verso scrivevano i Veneti?","Da destra a sinistra: il primo segno vale 1, il secondo 6. Carta 16."]),
     dict(done=[29],t="Come si parte?",h=["Nel disegno del fiume (carta 10) ci sono due numeri nascosti.","Premete «Combina»: un oggetto rosso e un oggetto blu.","Il remo (7) + la barca (22) = carta 29."]),
     dict(done=[27],t="I tre rami (carta 9)",h=["Leggete la piuma grigia (carta 19).","Contate solo le piume grigie, non quelle bianche.","Il ramo di mezzo ha 3 piume grigie: carta 27."]),
     dict(done=[30],t="Becco non molla",h=["Nel disegno del canneto c'è un numero nascosto su Becco.","Becco ha fame… Combinate il panino con Becco.","Il panino (12) + Becco (18) = carta 30."]),
     dict(done=[50],t="Il cavallino in acqua",h=["Cercate il numero vicino alle bolle (carta 30).","Serve un oggetto rosso trovato nella cassa.","La corda (15) + le bolle (35) = carta 50."]),
     dict(done=[56],t="Il fossato (carta 52)",h=["Nel disegno del villaggio ci sono due numeri nascosti.","L'uomo vicino al recinto vi dirà cosa cercare.","Prendete le carte 53 e 58, poi la 56."]),
     dict(done=[68],t="Il recinto (carta 56)",h=["Controllate tre cose: la fronte, la criniera, la coda.","Baio ha la macchia bianca, la criniera intrecciata e la coda lunga.","È il cavallo numero 68."]),
     dict(done=[72],t="Come passare il fossato",h=["Baio è un oggetto rosso, il fossato è blu.","Premete «Combina» e scegliete Baio e il fossato.","Baio (14) + il fossato (58) = carta 72."]),
     dict(done=[81],t="Il cancello e Becco (carta 74)",h=["Nel disegno del cancello ci sono due numeri nascosti: prendeteli tutti e due.","Per l'indovinello di Becco (carta 76) ripensate alla carta 8.","Prendete 26 e 76. La risposta è la tavoletta: carta 81."]),
     dict(done=[46],t="Il cancello chiuso",h=["Becco vi ha dato qualcosa…","La chiave è rossa, il lucchetto è blu.","La chiave (20) + il lucchetto (26) = carta 46."]),
     dict(done=[43],t="L'altare (carta 39)",h=["Guardate di nuovo la carta 2, il santuario.","Prima cifra: i cavallini di bronzo. Seconda cifra: le torce accese.","4 cavallini e 3 torce: carta 43."]),
    ]
    tessere={
     'veneti':("I Veneti antichi","Quasi 3.000 anni fa nel Nord-Est d'Italia viveva un popolo chiamato Veneti, oggi detti anche Paleoveneti. Este era una delle loro città più importanti."),
     'reitia':("La dea Reitia","A Este c'era un grande santuario dedicato alla dea Reitia. La gente le offriva piccoli doni di bronzo, come cavallini e guerrieri."),
     'alfabeto':("L'alfabeto dei Veneti","I Veneti avevano un loro alfabeto e spesso scrivevano da destra verso sinistra. Nel santuario sono state trovate tavolette di bronzo per imparare le lettere."),
     'cavalli':("I cavalli dei Veneti","I cavalli dei Veneti erano famosi anche fuori dall'Italia: perfino i Greci li ammiravano per le corse dei carri."),
     'museo':("Il Museo Atestino","Molti bronzetti e tavolette dei Veneti antichi si possono vedere al Museo Nazionale Atestino di Este."),
    }
    return dict(id='ep1',title="Il cavallino d'oro",place="Este, quasi 3.000 anni fa",
      intro="Il gabbiano Becco ha rubato il cavallino d'oro della dea Reitia! Riportatelo sull'altare: la puntata più lunga, con 45 carte.",
      cards=c,obj=obj,wrong=[24,31,61,64,71,84,86],req=req,
      disc={16:[5,8,11],27:[9,19,22],68:[53,56],72:[14,52,58],81:[76]},keep={50:[2,50],46:[2,46]},
      next={1:[2,3,4],4:[7,12,11],16:[9,15,10],50:[52],53:[56],68:[14],72:[74],81:[20],46:[39]},
      tess={1:'veneti',3:'reitia',8:'alfabeto',53:'cavalli',43:'museo'},final=43,hints=hints,tessere=tessere)

def from_spec(k,spec):
    e=spec[k]; cards=json.load(open(SD+'episodi/%s_cards.json'%k))
    obj={};wrong=[];req={};disc={};keep={};nxt={};tess={};final=None
    for c in e['cards']:
        n=c['n']
        assert str(n) in cards,(k,n)
        name=c['title'][0]+c['title'][1:].lower()
        name=name[0].lower()+name[1:] if not name.startswith(('Becco','Tito','Baio')) else name
        if c['typ']=='OGGETTO ROSSO':obj[n]=['r',name]
        if c['typ']=='OGGETTO BLU':obj[n]=['b',name]
        if c['typ']=='SBAGLIATO':wrong.append(n)
        for f,d in (('req',req),('disc',disc),('keep',keep),('next',nxt)):
            if c.get(f):d[n]=c[f]
        if c.get('tess'):tess[n]=c['tess']
        if c.get('final'):final=n
    return dict(id=k,adult=bool(e.get('adult')),title=e['title'],place=e['place'],intro=e['intro'],cards=cards,obj=obj,wrong=wrong,req=req,
                disc=disc,keep=keep,next=nxt,tess=tess,final=final,hints=e['hints'],
                tessere={kk:list(v) for kk,v in e['tessere'].items()})

spec=json.load(open(SD+'episodi/spec.json'));spec.update(json.load(open(SD+'episodi/spec2.json')));spec.update(json.load(open(SD+'episodi/spec3.json')))
base=[ep1()]+[from_spec(k,spec) for k in ('ep2','ep3','ep4','ep5','ep6','ep7','ep8','ep9','ep10','a1','a2','a3')]
for e in base: e['level']='a' if e.pop('adult',False) else 'f'
import glob as _g
spec4=json.load(open(SD+'episodi/spec4.json')) if os.path.exists(SD+'episodi/spec4.json') else {}
for k in sorted(spec4):
    if not os.path.exists(SD+'episodi/%s_cards.json'%k): continue
    e=from_spec(k,spec4); e.pop('adult',None); e['level']='g'; e['month']=spec4[k]['month']; e['map']=spec4[k].get('map') or ['laguna','venezia']; base.append(e)
BY={e['id']:e for e in base}
import copy
LV=json.load(open(SD+'episodi/levels.json'))
def apply(pid,p):
    E=copy.deepcopy(BY[p['base']]); E.update(id=pid,level=p['level'],title=p['title'],place=p['place'],intro=p['intro'])
    E['cards']=json.load(open(SD+'episodi/%s_cards.json'%pid))
    D=set(p.get('drop',[]))
    def filt(d):
        return {k:[x for x in v if x not in D] if isinstance(v,list) else v for k,v in d.items() if int(k) not in D}
    for f in ('req','disc','keep','next'): E[f]=filt(E[f])
    E['obj']={k:v for k,v in E['obj'].items() if int(k) not in D}
    E['wrong']=[x for x in E['wrong'] if x not in D]+p.get('wrong_add',[])
    for f,d in p.get('rules',{}).items():
        for k,v in d.items():
            k=int(k)
            if v is None: E[f].pop(k,None); E[f].pop(str(k),None)
            else: E[f][k]=v
    if 'tess' in p: E['tess']={int(k):v for k,v in p['tess'].items()}
    if 'tessere' in p: E['tessere']={k:list(v) for k,v in p['tessere'].items()}
    if 'final' in p: E['final']=p['final']
    if 'hints' in p: E['hints']=p['hints']
    else:
        bad=D|set(p.get('hint_del_done',[]))
        E['hints']=[h for h in E['hints'] if not set(h['done'])&bad]
        for t,h in p.get('hints_replace',{}).items():
            E['hints']=[h if x['t']==t else x for x in E['hints']]
    # normalise keys to int
    for f in ('req','disc','keep','next','obj'): E[f]={int(k):v for k,v in E[f].items()}
    for c in E['cards']: pass
    return E
lv=[apply(k,p) for k,p in LV.items()]
eps10=['ep%d'%i for i in range(1,11)]; sp=['a1','a2','a3']
order=[x+'k' for x in eps10+sp]+eps10+[x+'f' for x in sp]+[x+'a' for x in eps10]+sp
order=[x for x in order if x in BY or x in LV]+[e['id'] for e in base if e['level']=='g']
ALL={e['id']:e for e in base+lv}
eps=[ALL[k] for k in order if k in ALL]
pool=[];PI={};spool=[];SI={}
def svgsplit(h):
    out=[];i=0
    while True:
        s=h.find('<svg',i)
        if s<0: out.append(h[i:]);break
        d=0;j=s
        while True:
            x=h.find('<svg',j+1);y=h.find('</svg>',j+1)
            if x!=-1 and x<y: d+=1;j=x
            else:
                if d==0: e=y+6;break
                d-=1;j=y
        seg=h[s:e]
        if len(seg)>1500:
            hd=seg[:seg.index('>')+1]; inner=seg[len(hd):-6]
            if inner not in SI: SI[inner]=len(spool); spool.append(inner)
            out.append(h[i:s]+hd+'\x01%d\x02</svg>'%SI[inner])
        else: out.append(h[i:e])
        i=e
    return ''.join(out)
for e in eps:
    m={}
    for k,h in e['cards'].items():
        h=svgsplit(h)
        if h not in PI: PI[h]=len(pool); pool.append(h)
        m[k]=PI[h]
    e['cards']=m
MAPS=[]
if os.path.exists(SD+'maps/maps.json'):
    INFO=json.load(open(SD+'maps/info.json'))
    for m in json.load(open(SD+'maps/maps.json')):
        m.update(intro=INFO[m['id']]['intro'],time=INFO[m['id']]['time']); MAPS.append(m)
FBC=json.load(open(SD+'gara/firebase.json')) if os.path.exists(SD+'gara/firebase.json') else None
data=json.dumps({'episodes':eps,'pool':pool,'svgs':spool,'firebase':FBC,'maps':MAPS},ensure_ascii=False).replace('</','<\\/').replace('<!--','<\\!--')
t=open(TV+'template.html').read()
css=open(TV+'extra.css').read()
head=t[:t.index('<div class="app"')].replace('</style>',css+'</style>',1)
head=head.replace('<title>Leoni di Laguna Escape TV</title>','<title>Leoni di Laguna Escape</title>',1)
page=head+open(TV+'body2.html').read().replace('__DATA__',data)
open(TV+'leoni-escape-tv.html','w').write(page)
sa='<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
pwa_meta='''<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#1c130e">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Leoni Escape">
'''
i=page.index('<div class="app"')
body=page[i:]
open(TV+'download/leoni-escape-tv.html','w').write(sa+page[:i]+'</head>\n<body>\n'+body+'\n</body>\n</html>\n')
sw='<script>if("serviceWorker" in navigator){window.addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){});});}</script>\n'
open(SD+'pwa/index.html','w').write(sa+pwa_meta+page[:i]+'</head>\n<body>\n'+body+'\n'+sw+'</body>\n</html>\n')
open(TV+'game2.js','w').write(page[page.rindex('<script>')+8:page.rindex('</script>')])
print('ok',len(page),[ (e['id'],len(e['cards'])) for e in eps])
