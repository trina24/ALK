# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie funkcje RGF f : {1,...,n} -> Z+
# w porządku leksykograficznym.

class Generator:

    def __init__(self,n):
        self.n = n
        self.func = [1 for i in range(n)]
        self.acc = [2 for i in range(n)]
        
    def generate(self):
        stop = False
        if (self.n == 0):
            print []
            stop = True
        while (not stop):
            print self.func
            j = self.n + 1
            while(True):
                j -= 1
                if (self.func[j-1] != self.acc[j-1]):
                    break
            if (j > 1):
                self.func[j-1] += 1
                for i in range(j+1,self.n+1):
                    self.func[i-1] = 1
                    if (self.func[j-1] == self.acc[j-1]):
                        self.acc[i-1] = self.acc[j-1] + 1
                    else:
                        self.acc[i-1] = self.acc[j-1]
            else:
                stop = True

class Main:

    n = int(raw_input("Podaj n: "))
    gen = Generator(n)
    gen.generate()
                        
