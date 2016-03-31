# -*- coding: utf-8 -*-

# Napisz program wyznaczający podzbiór T o randze r w uporządkowaniu
# antyleksykograficznym k-elementowych podzbiorów zbioru {1,...,n}.


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
        return self.binomials[n][k]

    def unrank(self):
        # wyznacza podzbiór na podstawie rangi
        r = self.rank
        subset = []
        candidate = self.n
        for i in range(self.k):
            while (self.binomial(candidate, self.k - i) > r and candidate > 0):
                candidate -= 1
                if (candidate < self.k - i):
                    break
            subset.append(candidate + 1)
            if (candidate >= self.k - i):
                r -= self.binomial(candidate, self.k - i)
            else:
                break
        return subset
    
class Main:

    n = int(raw_input("Podaj n: \n"))
    k = int(raw_input("Podaj k: \n"))
    r = int(raw_input("Podaj r: \n"))
    sf = SubsetFinder(n, k, r)
    print sf.unrank()
