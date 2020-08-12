# ~ from collections import defaultdict as dd

class Store(dict):
    
    def __init__(self):
        super().__init__()
        self.sz = 0
    
    def put(self, pos, ch):
        """center addition: allowed unduplicated if old length is even,
        and also if old length is odd and the central character 
        becomes correctly duplicated - actually forced to be so
        """
        if ch.isupper() and self[pos][0] == ch.lower():
            print("u", ch, pos, self.sz)
            self[pos][1] = ch + self[pos][1][1:]
        elif not ch.isalnum():
            "spaces and punctuation"
            self[pos - 1][1] += ch.strip(' _') + ' '
        elif 2*pos == self.sz:
            "center addition becoming odd size"
            print("!", ch, self.dump(), pos, self.sz)
            self.shift(pos)
            self[pos] = [ch, ch]
        elif 2*pos == self.sz + 1:
            """odd size to grow at center by duplicating if ch 
            correct, otherwise duplicate correctly then put ch 
            """
            self.shift(pos)
            self[pos] = [ self[pos-1][0], self[pos-1][0] ]
            if ch != self[pos][0]:
                self.put(pos, ch)
        elif ch.islower():
            if 2*pos > self.sz: 
                "need reference in first half"
                pos = self.sz - pos
            print("l", ch, pos, self.sz)
            self.shift(pos)
            self[pos] = [ch, ch]
            print("l", ch, pos, self.sz)
            self.shift(self.sz - pos)
            self[self.sz - pos - 1] = [ch, ch]
        else:
            "flag untreated case at some point"
            pass

    def shift(self, pos):
        print(">", pos, self.sz, s.dump())
        self.sz += 1
        for i in reversed(range(pos+1, self.sz)):
            self[i] = self[i-1]
        self[pos] = '_'
        print("|", pos, self.sz, s.dump())
            
    def dump(self):
        r = ''
        for i in range(self.sz):
            r += self[i][0]
        return r
    
    def writ(self):
        r = ''
        for i in range(self.sz):
            r += self[i][1]
        return r
    
    def p(self):
        print('===')
        print('|' + s.dump() + '| , size: ' + str(self.sz))
        print('===')



if __name__ == "__main__":
    from jutge import read

    s = Store()
    while True:
        i = read(int)
        if i is None: break
        ch = read(str)
        s.put(i, ch)
        print(s.writ())

