# -*- coding: utf-8 -*-

# Zaimplementuj algorytm Trottera-Johnsona generowania wszystkich
# permutacji zbioru {1,...,n} w porządku minimalnych zmian.

import math

class TrotterJohnson:

    def __init__(self,n):
        self.n = n
        self.perms = [[1]]

    def algorithm(self):
        old_perms = self.perms
        new_perms = []
        i = 2
        while (i < self.n + 1):
            for k in range(len(old_perms)):
                for j in range(i):
                    new_perm = old_perms[k][:]
                    if (k % 2 == 0):
                        index = i - 1 - j
                    else:
                        index = j
                    new_perm.insert(index, i)
                    new_perms.append(new_perm)
            old_perms = new_perms
            new_perms = []
            i += 1
        return old_perms

class Main:

    n = int(raw_input("Podaj n: "))
    tj = TrotterJohnson(n)
    perms = tj.algorithm()
    for element in perms:
        print element
