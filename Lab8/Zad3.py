# -*- coding: utf-8 -*-

import math

class PermutationFinder:

    def __init__(self, n, rank):
        self.rank = rank
        self.n = n

    def par_unrank(self, n, r):
        perm = [0 for i in range(n)]
        perm[n-1] = 1
        for j in range(n):
            d = (r % math.factorial(j+1))/math.factorial(j)
            r = r - d * math.factorial(j)
            perm[n-j-1] = d + 1
            for i in range(n-j+1,n+1):
                 if (perm[i-1] > d):
                     perm[i-1] += 1
        return perm
                 
    def unrank(self):
        return self.par_unrank(self.n, self.rank)
    

class Main:
    
    n = int(raw_input("Podaj n: \n"))
    r = int(raw_input("Podaj rangę: \n"))
    pf = PermutationFinder(n,r)
    print pf.unrank()
