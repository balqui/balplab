
class Store(dict):
    """
    Stores the letter sequence towards the palindrom.
    Implemented as a dict: position to pair (letter, repr).
    The 2nd component takes care of upper case, spaces, and 
    punctuation, and some day must care for accent marks.
    Stores explicitly the size for easier code reading.
    """
    def __init__(self):
        super().__init__()
        self.sz = 0
    
    def put(self, pos, ch):
        """center addition: allowed unduplicated if old length 
        is even, and also if old length is odd - then the new 
        central character must be correct, otherwise a correct
        central one is put additionally to the ch given
        """
        if ch.isupper() and self[pos][0] == ch.lower():
            "change to upper, preserve punctuation"
            self[pos][1] = ch + self[pos][1][1:]
        elif not ch.isalnum():
            "spaces and punctuation"
            self[pos - 1][1] += ch.strip(' _') + ' '
        elif 2*pos == self.sz:
            "center addition becoming odd size"
            self._shift(pos)
            self[pos] = [ch, ch]
        elif 2*pos == self.sz + 1:
            """odd size to grow at center by duplicating 
            if ch correct, otherwise duplicate correctly 
            then put new ch 
            """
            self._shift(pos)
            self[pos] = [ self[pos-1][0], self[pos-1][0] ]
            if ch != self[pos][0]:
                self.put(pos, ch)
        elif ch.islower():
            if 2*pos > self.sz: 
                "current arith needs reference in first half"
                pos = self.sz - pos
            self._shift(pos)
            self[pos] = [ch, ch]
            self._shift(self.sz - pos)
            self[self.sz - pos - 1] = [ch, ch]
        else:
            "flag untreated case at some point"
            pass

    def _shift(self, pos):
        self.sz += 1
        for i in reversed(range(pos+1, self.sz)):
            self[i] = self[i-1]
        self[pos] = '_'
            
    def _dump(self):
        r = ''
        for i in range(self.sz):
            r += self[i][0]
        return r
    
    def writ(self):
        r = ''
        for i in range(self.sz):
            r += self[i][1]
        return r
    
    def _p(self):
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

