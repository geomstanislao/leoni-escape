CARDS={}
def card(n):
    def deco(fn):
        CARDS[n]=fn
        return fn
    return deco
