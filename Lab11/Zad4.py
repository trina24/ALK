# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie podziały liczby n na k
# składników. Wykorzystaj algorytmy z zadań 2 i 3.

import SelfConjugatePartition as conj
import PartitionGenerator as gen

class ParticularPartition(gen.PartitionGenerator):

    # przeciążenie konstruktora
    
    def __init__(self,n,k):
        super(ParticularPartition,self).__init__(n)
        self.k = k
        self.temp_part[0] = k

    # przeciążenie metod
    
    def prepare_partition(self, m):
        temp = self.temp_part[:m]
        scp = conj.SelfConjugatePartition(temp)
        return scp.conversion()

    def generate_partitions(self):
        if (self.k == 0):
            return [[]]
        elif (self.n == 0):
            return [[0]]
        else:
            self.part(self.n-self.k,self.k,1)
            return self.partitions

class Main:

    n = int(raw_input("Podaj n: "))
    k = int(raw_input("Podaj k: "))
    pp = ParticularPartition(n,k)
    parts = pp.generate_partitions()
    for element in parts:
        print element
