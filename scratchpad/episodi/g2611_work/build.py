import sys, json, importlib
sys.path.insert(0, '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/g2611_work')
from common import card_front, svg
import gc1
mods = [gc1]
try:
    import gc2; mods.append(gc2)
except ImportError: pass
CARDS = {}
for m in mods: CARDS.update(m.CARDS)
SD = '/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/'
spec = json.load(open(SD + 'spec4.json'))['g2611']['cards']
only = sys.argv[1].split(',') if len(sys.argv) > 1 else None
out = {}
for c in spec:
    n = c['n']
    if n not in CARDS: continue
    if only and str(n) not in only: continue
    p = 'g2611c%d_' % n
    H, defs, body, aria = CARDS[n](p)
    assert H == c.get('H', 120), (n, H, c.get('H', 120))
    s = svg(H, body, c['title'], defs)
    html = card_front(c['typ'], n, c['title'], H, s, text=c['text'], strip=c.get('strip'))
    if n > 999:
        html = html.replace('font-size: 13px; color: #2a1a10; line-height: 1">', 'font-size: 8.5px; letter-spacing: -0.3px; color: #2a1a10; line-height: 1">', 1)
    assert '/>' not in html, n
    out[str(n)] = html
fn = SD + 'g2611_cards.json' if not only else 'part.json'
json.dump(out, open(fn, 'w'), ensure_ascii=False)
print(len(out), '->', fn)
