# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie podzbiory zbioru {1,...,n} w
# porządku minimalnych zmian (Graya), wykorzystując wagi Hamminga lub
# różnicę symetryczną zbiorów.

import math

class Generator:

    def __init__(self, n):
        self.n = n
        # inicjalizacja kodu Graya zerami
        self.vector = [0 for i in range(n)]

    def hamming(self, vector):
    # oblicza wagę hamminga i zwraca wynik modulo 2
        hamming = 0
        for element in vector:
            if (element == 1):
                hamming += 1
        hamming = hamming % 2
        return hamming
        
    def successor(self, vector):
        # znajduje następnik danego ciągu w kodzie Graya
        hamming = self.hamming(vector)
        # jeżeli waga Hamminga jest parzysta, zmienia ostatni bit
        if (hamming == 0):
            vector[self.n - 1] = (vector[self.n - 1] + 1) % 2
        # w przeciwnym przypadku szuka pierwszej od końca jedynki
        # i zmienia bit na lewo od niej
        else:
            i = self.n - 1
            while (vector[i] != 1):
                i -= 1
            if (i > 0):
                vector[i-1] = (vector[i-1] + 1) % 2
        return vector

    def subset(self, vector):
        # zwraca podzbiór odpowiadający wektorowi charakterystycznemu
        subset = []
        for i in range(len(vector)):
            if (vector[i] == 1):
                subset.append(i+1)
        return subset

    def generate(self):
        # wypisuje podzbiory dla kolejnych ciągów kodu Graya
        vector = self.vector
        print self.subset(vector)
        for i in range(pow(2,self.n)-1):
            vector = self.successor(vector)
            print self.subset(vector)

class Main:

    n = int(raw_input("Podaj n: \n"))
    gen = Generator(n)
    gen.generate()
