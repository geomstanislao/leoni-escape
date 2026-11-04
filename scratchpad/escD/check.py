import sys
from html.parser import HTMLParser
V={'meta','link','br','img','input','hr'}
class H(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in V: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append((t,s.getpos(),s.st[-3:]))
        else: s.st.pop()
for fn in sys.argv[1:]:
    h=H(); h.feed(open(fn).read()); print(fn,h.err[:3],h.st)
