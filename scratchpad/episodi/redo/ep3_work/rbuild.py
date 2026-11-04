import sys,json,re,importlib
sys.path.insert(0,'/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/redo/ep3_work')
from reg import CARDS
mods=[m for m in ['ra','rb','rc','rd'] if __import__('os').path.exists(m+'.py')]
for m in mods: importlib.import_module(m)
from common import svg
orig=json.load(open('../ep3_orig.json'))
only=sys.argv[1].split(',') if len(sys.argv)>1 else None
out={}
for k,h in orig.items():
    n=int(k)
    if n not in CARDS: continue
    if only and k not in only: continue
    p='r3c%d_'%n
    H,defs,body,aria=CARDS[n](p)
    m=re.search(r'<svg [^>]*>',h); old=m.group(0)
    hh=re.search(r'viewBox="0 0 215 ([\d.]+)"',old).group(1)
    assert float(hh)==float(H),(n,hh,H)
    ar=re.search(r'aria-label="([^"]*)"',old).group(1)
    new=svg(H,body,ar,defs)
    s=re.search(r'<svg .*?</svg>',h,re.S)
    html=h[:s.start()]+new+h[s.end():]
    assert '/>' not in html,n
    out[k]=html
fn='../ep3_new.json' if not only else 'part.json'
json.dump(out,open(fn,'w'),ensure_ascii=False)
print(len(out),'cards ->',fn)
