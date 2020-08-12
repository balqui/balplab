
from store import Store
    # ~ def put(self, pos, ch):
    # ~ def shift(self, pos):
    # ~ def dump(self):
    # ~ def writ(self):
    # ~ def p(self):

class Chann:
    """
    Communication and user-friendliness between Store and web page
    """

    def __init__(self):
        "position - also, keep a list of Store's for history and back and such"
        self.p = 0
        self.st = Store()

    def move(self, how):
        q = self.p
        if how == 37 and self.p > 0:
            self.p -= 1
        elif how == 38:
            self.p = 0
        elif how == 39 and self.p < self.st.sz:
            self.p += 1
        elif how == 40:
            self.p = self.st.sz
        return str(q) + " > " + str(self.p)

    def put(self, ch):
        w = self.st.put(self.p, ch)
        self.p += 1
        return str(self.p) + ", " + w + "; " + self.st.writ()

    def wh(self):
        return str(self.p)

if __name__ == "__main__":
    ch = Chann()
    for c in "aeiou":
        ch.put(c)
        print(ch.st.writ())
    print("p: ", ch.p)
    ch.move(37)
    ch.move(37)
    print("p: ", ch.p)
    ch.put('w')
    print(ch.st.writ())
    
