# -*- coding: utf-8 -*-

# Napisz program generujący podział zbioru {1,...,n} odpowiadający
# zadanej funkcji RGF f : {1,...,n} -> Z+.

class partitionGenerator:

    def __init__(self, n, func):
        self.n = n
        self.func = func
        self.blocks = []

    def generate(self):
        k = 1
        for element in self.func:
            if (element > k):
                k = element
        for i in range(k):
            self.blocks.append([])
        for j in range(1,self.n+1):
            self.blocks[self.func[j-1]-1].append(j)
            self.blocks[self.func[j-1]-1].sort()
        print self.blocks

class Main:

    n = int(raw_input("Podaj n: "))
    spl = raw_input("Podaj wartości funkcji: ").split()
    func = [int(element) for element in spl]
    pg = partitionGenerator(n, func)
    pg.generate()
