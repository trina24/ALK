# -*- coding: utf-8 -*-

# Napisz program obliczający pozycję podzbioru T ⊂ {1,...,n} w upo-
# rządkowaniu leksykograficznym (według wektorów charakterystycznych)
# podzbiorów zbioru {1,...,n}.

import math

class RankFinder:
    
    def __init__(self, n, subset):
        self.subset = subset
        self.indicator = [0 for i in range(n)]        

    def indicator_vector(self, vector):
        # wypełnia wektor charakterystyczny jedynkami tam, gdzie
        # występuje dana liczba
        for element in vector:
            number = int(element) - 1 
            self.indicator[number] = 1
        return self.indicator

    def find_rank(self):
        rank = 0
        ind = self.indicator_vector(self.subset)
        # odwracamy wektor charakterystyczny, bo powinien być
        # indeksowany od n-1 do 0
        ind.reverse()
        # obliczamy rangę ze wzoru
        for i in range(len(ind)):
            if (ind[i] == 1):
                rank += pow(2,i)
        return rank

class Main:

    n = int(raw_input('Podaj n: \n'))
    subset = raw_input('Podaj elementy podzbioru: \n').split()
    rf = RankFinder(n, subset)
    print rf.find_rank()
