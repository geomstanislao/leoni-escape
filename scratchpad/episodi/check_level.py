import json,sys
SD='/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/'
spec={}
for f in ('spec.json','spec2.json','spec3.json'): spec.update(json.load(open(SD+'episodi/'+f)))
p=json.load(open(sys.argv[1]))
b=p['base']
if b=='ep1':
    sys.exit('ep1 not supported here')
E=spec[b]; cards={c['n']:dict(c) for c in E['cards']}
D=set(p.get('drop',[]))
for n in D: cards.pop(n,None)
for k,v in (p.get('clone') or {}).items():
    src=cards.get(v[0]) or {c['n']:c for c in E['cards']}[v[0]]
    c=dict(src); c['n']=int(k); c['typ']=v[1] or src['typ']; c['text']=v[4]
    for f in ('req','next','disc','keep','final','tess'): c.pop(f,None)
    cards[int(k)]=c
for f,d in (p.get('rules') or {}).items():
    for k,v in d.items():
        k=int(k)
        if v is None: cards[k].pop(f,None)
        else: cards[k][f]=v
for n,c in cards.items():
    for f in ('req','next','disc','keep'):
        if c.get(f): c[f]=[x for x in c[f] if x not in D]
wrong={n for n,c in cards.items() if c['typ']=='SBAGLIATO'}|set(p.get('wrong_add',[]))
final=p.get('final') or [c['n'] for c in E['cards'] if c.get('final')][0]
err=[]
if final not in cards: err.append('final card missing')
for n,t in p.get('text',{}).items():
    if int(n) not in cards: err.append('text for missing card %s'%n)
tess=p.get('tess') or {str(c['n']):c['tess'] for c in E['cards'] if c.get('tess')}
tk=set(p.get('tessere') or E['tessere'])
if set(tess.values())!=tk: err.append('tess keys mismatch %s'%(set(tess.values())^tk))
for n in tess:
    if int(n) not in cards: err.append('tess on missing card %s'%n)
seen={1}; got=set()
for s in p['test_path']:
    if isinstance(s,str) and s.startswith('C'):
        r,bb=map(int,s[1:].split('+')); n=r+bb
        if not (r in seen and bb in seen): err.append('combo %s without objects'%s)
        if cards.get(r,{}).get('typ')!='OGGETTO ROSSO' or cards.get(bb,{}).get('typ')!='OGGETTO BLU': err.append('combo %s not red+blue'%s)
    else: n=int(s)
    if n not in cards: err.append('path card %s missing'%n); break
    if n in wrong: err.append('path takes wrong card %s'%n)
    if not all(x in seen for x in cards[n].get('req',[])): err.append('card %s req %s not met'%(n,cards[n].get('req')))
    seen.add(n)
if final not in seen: err.append('path does not reach final %s'%final)
for n in tess:
    if int(n) not in seen: err.append('tessera card %s not on path'%n)
for h in p.get('hints',[]):
    for n in h['done']:
        if n not in cards: err.append('hint done %s missing'%n)
    if len(h['h'])!=3: err.append('hint needs 3 levels')
for k in ('title','place','intro','level','test_path'):
    if k not in p: err.append('missing '+k)
print('OK' if not err else '\n'.join(err))
