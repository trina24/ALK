# -*- coding: utf-8 -*-

# Napisz program realizujący iteracyjny algorytm generowania
# wszystkich podziałów zbioru {1,...,n} za pomocą przenoszenia między
# blokami elementu aktywnego.

class Generator:

    def __init__(self, n):
        self.n = n
        self.block = [1 for i in range(n)]
        self.PR = [True for i in range(n)]
        self.nex = [0 for i in range(n)]
        self.pre = [0 for i in range(n)]
        self.j = n

    def get_partition(self):
        list_of_blocks = []
        for i in range(1,self.n+1):
            num = self.block[i-1]
            flag = False
            for block in list_of_blocks:
                if (block.count(num) > 0):
                    block.append(i)
                    flag = True
            if (flag):
                pass
            else:
                list_of_blocks.append([i])
        return list_of_blocks

    def generate(self):
        print self.get_partition()
        while (self.j > 1):
            k = self.block[self.j-1]
            if (self.PR[self.j-1]):
                if (not self.nex[k-1]):
                    self.nex[k-1] = self.j
                    self.nex[self.j-1] = 0
                    self.pre[self.j-1] = k
                if (self.nex[k-1] > self.j):
                    self.pre[self.j-1] = k
                    self.nex[self.j-1] = self.nex[k-1]
                    self.pre[self.nex[self.j-1]-1] = self.j
                    self.nex[k-1] = self.j
                self.block[self.j-1] = self.nex[k-1]
            else:
                self.block[self.j-1] = self.pre[k-1]
                if (k == self.j):
                    if (not self.nex[k-1]):
                        self.nex[self.pre[k-1]-1] = 0
                    else:
                        self.nex[self.pre[k-1]-1] = self.nex[k-1]
                        self.pre[self.nex[k-1]-1] = self.pre[k-1]
            print self.get_partition()
            self.j = self.n
            while (self.j > 1 and ((self.PR[self.j-1] and self.block[self.j-1] == self.j) or (not self.PR[self.j-1] and self.block[self.j-1] == 1))):
                self.PR[self.j-1] = not self.PR[self.j-1]
                self.j -= 1

class Main:

    n = int(raw_input("Podaj n: "))
    gen = Generator(n)
    gen.generate()
