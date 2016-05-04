# -*- coding: utf-8 -*-

import math

class RankFinder:

    def __init__(self, vec):
        self.perm = vec
        self.n = len(vec)

    def reduced_perm(self, vec):
        perm = []
        for i in range(len(vec)-1):
            if (vec[i+1] > vec[0]):
                perm.append(vec[i+1]-1)
            else:
                perm.append(vec[i+1])
        return perm

    def find_rank(self, vec, n):
        if (vec == [1] and n == 1):
            return 0
        else:
            return (vec[0]-1)*math.factorial(n-1) + self.find_rank(self.reduced_perm(vec),n-1)

    def rank(self):
        return self.find_rank(self.perm, self.n)

class Main:

    vector = raw_input("Podaj elementy permutacji: \n").split()
    permutation = []
    for element in vector:
        permutation.append(int(element))
    rf = RankFinder(permutation)
    print "ranga: " + str(rf.rank())
