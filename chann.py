
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
        if how == 37 and self.p > 0:
            self.p -= 1
        elif how == 38:
            self.p = 0
        elif how == 39 and self.p < self.st.sz:
            self.p += 1
        elif how == 40:
            self.p = self.st.sz

    def put(self, ch):
        self.st.put(self.p, ch)

if __name__ == "__main__":
    pass
