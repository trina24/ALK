# -*- coding: utf-8 -*-

# Napisz program wyznaczający podzbiór T o randze r w porządku
# minimalnych zmian k-elementowych podzbiorów zbioru {1,...,n}.

class SubsetFinder:

    def __init__(self, n, k, r):
        self.n = n
        self.k = k
        self.rank = r
        self.binomials = self.pascal_triangle()

    def pascal_triangle(self):
        # zwraca listę kolejnych wierszy trójkąta Pascala
        pt = []
        pt.append([1])
        currentline = [pt[0]]
        for i in range(1, self.n + 1):
            newline = [1]
            for j in range(1, len(currentline)):
                newline.append(currentline[j - 1] + currentline[j])
            newline.append(1)
            pt.append(newline)
            currentline = newline
        return pt

    def binomial(self, n, k):
        # wyznacza z trójkąta Pascala współczynnik dwumianowy C(n, k)
        if (n >= k):
            return self.binomials[n][k]
        else:
            return 0

    def unrank(self):
        # wyznacza podzbiór na podstawie rangi
        r = self.rank
        subset = []
        candidate = self.n - 1
        for i in range(self.k, 0, -1):
            while (self.binomial(candidate, i) > r):
                candidate -= 1
            subset.insert(0, candidate + 1)
            r = self.binomial(candidate + 1, i) - r - 1
            candidate -=1
        return subset
    
class Main:

    n = int(raw_input("Podaj n: \n"))
    k = int(raw_input("Podaj k: \n"))
    r = int(raw_input("Podaj r: \n"))
    sf = SubsetFinder(n, k, r)
    print sf.unrank()
