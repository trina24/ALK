# -*- coding: utf-8 -*-

# Napisz  program  generujący  funkcję  RGF f: {1,...,n} -> Z+
# odpowiadającą  zadanemu podziałowi zbioru {1,...,n}.

class functionGenerator:

    def __init__(self,n,k,blocks):
        self.n = n
        self.k = k
        self.blocks = blocks
        self.func = [0 for i in range(n)]

    def generate(self):
        j = 1
        for i in range(self.k):
            while (self.func[j-1] != 0):
                j += 1
            h = 1
            while (self.blocks[h-1].count(j) == 0):
                h += 1
            for g in self.blocks[h-1]:
                self.func[g-1] = h
        print self.func

class Main:

    n = int(raw_input("Podaj n: "))
    k = int(raw_input("Podaj k: "))
    blocks = []
    for i in range(k):
        spl = raw_input("Podaj elementy bloku " + str(i+1) + ": ").split()
        block = [int(i) for i in spl]
        blocks.append(block)
    fg = functionGenerator(n,k,blocks)
    fg.generate()
