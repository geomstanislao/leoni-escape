import re,sys
from html.parser import HTMLParser
VOID={'meta','link','br','img','hr','input'}
class H(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=0
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t:
            print('MISMATCH',t,s.st[-3:]); s.err+=1
            if t in s.st:
                while s.st.pop()!=t: pass
        else: s.st.pop()
for fn in sys.argv[1:]:
    h=H(); h.feed(open(fn,encoding='utf-8').read()); print(fn,'err',h.err,'left',h.st)
