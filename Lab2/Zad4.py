# -*- coding: utf-8 -*-

# Napisz program wyznaczający podzbiór T o zadanej pozycji r w upo-
# rządkowaniu leksykograficznym (według wektorów charakterystycznych)
# podzbiorów zbioru {1,...,n}.


class SubsetFinder:
    
    def __init__(self, n, r):
        self.n = n
        self.rank = r

    def find_binary(self):
        # zamienia rangę na liczbę binarną
        binary = bin(self.rank)[2:]
        # dopełniamy zerami do ciągu n-elementowego
        for i in range(self.n - len(binary)):
            binary = '0' + binary
        return binary

    def find_subset(self):
        # przegląda wektor charakterystyczny i wstawia do zbioru
        # numery pozycji, na których są jedynki
        subset = []
        binary = self.find_binary()
        for i in range(len(binary)):
            if (binary[i] == '1'):
                subset.append(i+1)
        return subset

class Main:

    n = int(raw_input('Podaj n: \n'))
    r = int(raw_input('Podaj r: \n'))
    sf = SubsetFinder(n, r)
    print sf.find_subset()
