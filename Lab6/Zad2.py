# -*- coding: utf-8 -*-

# Napisz program obliczający rangę k-elementowego podzbioru T zbioru
# {1,...,n} w porządku minimalnych zmian podzbiorów k-elementowych.

import math

class RankFinder:

    def __init__(self, n, subset):
        self.n = n
        self.subset = subset
        self.binomials = self.pascal_triangle()

    def pascal_triangle(self):
        # zwraca listę kolejnych wierszy trójkąta Pascala
        pt = []
        pt.append([1])
        currentline = [pt[0]]
        last = int(self.subset[-1])
        for i in range(1, last + 1):
            newline = [1]
            for j in range(1, len(currentline)):
                newline.append(currentline[j - 1] + currentline[j])
            newline.append(1)
            pt.append(newline)
            currentline = newline
        return pt

    def binomial(self, n, k):
        # wyznacza z trójkąta Pascala współczynnik dwumianowy C(n, k)
        return self.binomials[n][k]

    def rank(self):
        # wyznacza rangę ze wzoru
        rank = 0
        subset = []
        for element in self.subset:
            subset.append(int(element))
        k = len(subset)
        for i in range(k):
            rank += pow(-1, k - i - 1) * (self.binomial(subset[i], i + 1) - 1)
        return rank

class Main:
    
    n = int(raw_input("Podaj n: \n"))
    subset = raw_input("Podaj elementy podzbioru: \n").split()
    for element in subset:
        element = int(element)
    rf = RankFinder(n, subset)
    print "rank = " + str(rf.rank())
