# -*- coding: utf-8 -*-

# Napisz program obliczający metodą programowania dynamicznego liczbę
# podziałów liczby n na k składników, korzystając ze wzoru:
# P(n, k) = P(n−1, k−1) + P(n−k, k) dla k <= n,
# gdzie P(0,0) = 1 oraz P(i,0) = 0 dla i > 0.

class PartitionGenerator:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.partition = [[None for j in range(k+1)] for i in range(n+1)]
        self.partition[0][0] = 1  # warunek początkowy P(0,0) = 1
        for i in range(1,n+1):
            self.partition[i][0] = 0  # warunek początkowy P(i,0) = 0

    def generate(self):
        for i in range(1,self.n+1):
            for j in range(1, min(i,self.k) + 1):  # unikamy wyjścia z tablicy
                if (i < 2*j):  # unikamy dodawania wartości pustych
                    self.partition[i][j] = self.partition[i-1][j-1]
                else:
                    self.partition[i][j] = self.partition[i-1][j-1] + \
                                           self.partition[i-j][j]
        return self.partition[self.n][self.k]

class Main:

    n = int(raw_input("Podaj n: "))
    k = int(raw_input("Podaj k: "))
    pg = PartitionGenerator(n,k)
    print pg.generate()
