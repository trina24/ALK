# -*- coding: utf-8 -*-

# Napisz program obliczający rangę podzbioru T ⊂ {1,...,n} w upo-
# rządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1,...,n}.

import math

class RankFinder:

    def __init__(self, n, subset):
        self.n = n
        self.subset = subset
        
    def gray_sequence(self):
        # znajduje wektor charakterystyczny dla podzbioru
        grayseq = [0 for i in range(self.n)]
        for element in self.subset:
            ind = int(element) - 1
            grayseq[ind] = 1
        return grayseq

    def binary_rank(self):
        # zamienia wektor charakterystyczny na rangę binarną
        vector = self.gray_sequence()
        vector.reverse()
        binary_rank = []
        for j in range(self.n):
            b = 0
            for i in range(j, self.n):
                b += vector[i]
            b %= 2
            binary_rank.append(b)
        binary_rank.reverse()
        return binary_rank

    def rank(self):
        # zamienia rangę binarną na postać dziesiątkową
        binary = self.binary_rank()
        binary.reverse()
        r = 0
        for i in range(len(binary)):
            r += binary[i] * pow(2, i)
        return r

class Main:
    
    n = int(raw_input("Podaj n: \n"))
    subset = raw_input("Podaj elementy podzbioru: \n").split()
    rf = RankFinder(n, subset)
    print "rank = " + str(rf.rank())
