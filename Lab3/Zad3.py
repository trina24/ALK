# -*- coding: utf-8 -*-

# Napisz program wyznaczający podzbiór T o zadanej pozycji r w upo-
# rządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1,...,n}.


import math

class SubsetFinder:
    
    def __init__(self, n, r):
        self.n = n
        self.rank = r

    def binary_rank(self):
        # zamienia rangę na liczbę binarną
        binary = bin(self.rank)[2:]
        # dopełniamy zerami do ciągu (n+1)-elementowego
        for i in range(self.n - len(binary) + 1):
            binary = '0' + binary
        return binary

    def gray_sequence(self):
        # zamienia rangę binarną na wektor charakterystyczny
        grayseq = []
        binary = self.binary_rank()
        for i in range(self.n, 0, -1):
            a = int(binary[i]) + int(binary[i - 1])
            grayseq.append(a)
        grayseq.reverse()
        return grayseq

    def find_subset(self):
        # wyznacza elementy podzbioru wg wektora charakterystycznego
        grayseq = self.gray_sequence()
        subset = []
        for i in range(len(grayseq)):
            if (grayseq[i] == 1):
                subset.append(i+1)
        return subset

class Main:

    n = int(raw_input("Podaj n: \n"))
    r = int(raw_input("Podaj r: \n"))
    sf = SubsetFinder(n, r)
    print sf.find_subset()
