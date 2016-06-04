# -*- coding: utf-8 -*-

# Napisz program obliczający rangę kodu Prufera L.

import math

class PruferRank:

    def __init__(self, prufer):
        self.prufer = prufer

    def rank(self):
        pr = self.prufer
        pr.reverse()
        for i in range(len(pr)):
            pr[i] -= 1
        n = len(pr) + 2
        r = 0
        for i in range(len(pr)):
            r += pr[i] * math.pow(n,i)
        return int(r)

class Main:

    spl = raw_input("Podaj elementy kodu: ").split()
    prufer = [int(element) for element in spl]
    pr = PruferRank(prufer)
    print pr.rank()
