# -*- coding: utf-8 -*-

# Napisz program wyznaczający kod Prufera długości n−2 o randze r.

import math

class PruferUnrank:

    def __init__(self, n, rank):
        self.n = n
        self.rank = rank

    def unrank(self):
        r = self.rank
        prufer = []
        while (len(prufer) < self.n - 2):
            i = len(prufer)
            prufer.append(int(r // math.pow(self.n,self.n - 3 - i)) + 1)
            r = r % math.pow(self.n, self.n - 3 - i)
        return prufer

class Main:

    n = int(raw_input("Podaj n: "))
    r = int(raw_input("Podaj r: "))
    pu = PruferUnrank(n, r)
    print pu.unrank()
