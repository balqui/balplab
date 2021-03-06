
class Store(dict):
    """
    Stores explicitly the size self.sz for easier code reading.
    Stores the letter sequence towards the palindrom
    and the current change position in range(0, self.sz + 1).
    Implemented as a dict: position to pair (letter, repr).
    The 2nd component takes care of upper case, spaces, and 
    punctuation, and some day will care for accent marks.
    """
    def __init__(self):
        super().__init__()
        self.sz = 0
        self.p = 0

    def move(self, d):
        "move current change position by d or to the extreme"
        if 0 <= self.p + d <= self.sz + 1:
            self.p = self.p + d
        elif d < 0:
            self.p = 0
        else:
            "d > 0"
            self.p = self.sz + 1

    def put(self, ch):
        """center addition: allowed unduplicated if old length 
        is even, and also if old length is odd - then the new 
        central character must be correct, otherwise a correct
        central one is put additionally to the ch given
        """
        pos = self.p
        if ch.isupper() and pos > 0 and self[pos-1][0] == ch.lower():
            "change to upper, preserve punctuation"
            self[pos-1][1] = ch + self[pos-1][1][1:]
        elif not ch.isalnum() and pos > 0:
            "spaces and punctuation"
            self[pos - 1][1] += ch.strip(' _') + ' '
        elif 2*pos == self.sz:
            "center addition becoming odd size"
            self._shift(pos)
            self[pos] = [ch, ch]
        elif 2*pos == self.sz - 1 and ch.lower() == self[pos][0]:
            """odd size to grow at center by correctly duplicating 
            the next ch
            """
            self._shift(pos)
            self[pos] = [ch.lower(), ch]
        elif 2*pos == self.sz + 1:
            """odd size to grow at center by duplicating next ch
            if new ch is correct, otherwise duplicate correctly 
            then put new ch 
            """
            self._shift(pos)
            self[pos] = [ self[pos-1][0], self[pos-1][0] ]
            if ch != self[pos][0]:
                self._shift(pos)
                self[pos] = [ch, ch]
            self.p -= 1
        elif ch.islower():
            if 2*pos > self.sz: 
                "current arith needs reference in first half"
                pos = self.sz - pos
            self._shift(pos)
            self[pos] = [ch, ch]
            self._shift(self.sz - pos)
            self[self.sz - pos - 1] = [ch, ch]
        else:
            "flag untreated case maybe at some point"
            pass
        return self.writ()

    def delete(self):
        "delete whatever is to the left of the current position"
        if self.p == 0:
            "silently do nothing"
            return
        pos = self.p - 1
        # ~ print("pos, sz: ", pos, self.sz)
        if len(self[pos][1]) > 1:
            "delete space and/or punctuation"
            self[pos][1] = self[pos][1][:-1]
        elif 2*pos == self.sz - 1:
            "odd length, middle char, remove it"
            self._unshift(pos)
        elif 2*pos == self.sz - 2 or 2*pos == self.sz:
            "even length, one of central chars, remove only one"
            self._unshift(pos)
        else:
            "must remove two chars - NOT SURE p IS LEFT IN CORRECT PLACE"
            if 2*pos > self.sz: 
                "current arith needs reference in first half - case '==' covered above"
                pos = self.sz - pos - 1
            # ~ print(pos, self.sz - pos - 1)
            self._unshift(pos)
            self._unshift(self.sz - pos - 1)

    def _shift(self, pos):
        self.sz += 1
        for i in reversed(range(pos+1, self.sz)):
            self[i] = self[i-1]
        self[pos] = '_'
        if pos <= self.p: 
            self.p += 1

    def _unshift(self, pos):
        # ~ print("unshift", pos, self._dump())
        self.sz -= 1
        for i in range(pos, self.sz):
            # ~ print(i, self._dump())
            self[i] = self[i+1]
        if pos <= self.p: 
            self.p -= 1

    def _dump(self):
        r = ''
        for i in range(self.sz):
            r += self[i][0]
        return r

    def writ(self, mark=True):
        "may mark the current change position"
        r = ''
        for i in range(self.sz):
            if i == self.p and mark: r += '|'
            r += self[i][1]
        if self.sz == self.p and mark: r += '|'
        return r

    def _p(self):
        print('===')
        print('|' + s.dump() + '| , size: ' + str(self.sz))
        print('===')

    def g(self):
        return ':::' + str(self.sz)



if __name__ == "__main__":
    from jutge import read

    s = Store()
    while True:
        ch = read(str)
        if ch is None: break
        if ch == '<': 
            s.move(-1)
        elif ch == '>': 
            s.move(1)
        elif ch == '!': 
            s.delete()
        else:
            s.put(ch)
        print(s.writ())

