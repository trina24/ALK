# -*- coding: utf-8 -*-

# Napisz program obliczający rangę k-elementowego podzbioru T zbioru
# {1,...,n} w uporządkowaniu leksykograficznym podzbiorów
# k-elementowych.

class RankFinder:

    def __init__(self, n, subset):
        self.n = n
        self.subset = subset
        self.k = len(subset)
        self.binomials = self.pascal_triangle()

    def pascal_triangle(self):
        # zwraca listę kolejnych wierszy trójkąta Pascala
        pt = []
        pt.append([1])
        currentline = [pt[0]]
        for i in range(1, self.n):
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
        subset.insert(0,0) #  zakładamy t_0 = 0
        for i in range(1, self.k+1):
            for j in range(subset[i - 1] + 1, subset[i]):
                rank += self.binomial(self.n - j, self.k - i)
        return rank

class Main:
    
    n = int(raw_input("Podaj n: \n"))
    subset = raw_input("Podaj elementy podzbioru: \n").split()
    for element in subset:
        element = int(element)
    rf = RankFinder(n, subset)
    print "rank = " + str(rf.rank())
