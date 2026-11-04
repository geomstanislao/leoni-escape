import sys, re
from html.parser import HTMLParser

VOID = {'meta', 'link', 'br', 'img', 'hr', 'input'}


class H(HTMLParser):
    def __init__(self):
        super().__init__()
        self.st = []
        self.err = []
        self.ids = []

    def handle_starttag(self, t, a):
        for k, v in a:
            if k == 'id':
                self.ids.append(v)
        if t not in VOID:
            self.st.append(t)

    def handle_endtag(self, t):
        if t in VOID:
            return
        if not self.st or self.st[-1] != t:
            self.err.append('mismatch %s vs %s at %s' % (t, self.st[-1] if self.st else None, self.getpos()))
            if t in self.st:
                while self.st and self.st[-1] != t:
                    self.st.pop()
                self.st.pop()
        else:
            self.st.pop()


for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read()
    h = H()
    h.feed(s)
    dup = set(i for i in h.ids if h.ids.count(i) > 1)
    print(p.split('/')[-1], 'errs', h.err[:5], 'open', h.st, 'dupids', dup, 'slashgt', s.count('/>'))
    refs = set(re.findall(r'url\(#([^)]+)\)', s))
    print('  missing ids', refs - set(h.ids))
