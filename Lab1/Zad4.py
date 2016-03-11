# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie podzbiory zbioru {1,2,...,n},
# wykorzystując bijekcję między ciągami binarnymi długości n, a tymi
# podzbiorami.

import math

class Generator:

    def __init__(self, n):
        self.n = n  # liczba elementów wyjściowego zbioru
        # inicjalizacja listy wektorów charakterystycznych
        self.ranklist = [0 for i in range(pow(2,n))]
    
    def fill_ranks(self, n):
        for i in range(len(self.ranklist)):
            # zamiana rangi na ciąg binarny
            binary = bin(i)[2:]
            # dopisanie zer z przodu
            for j in range(n-len(binary)):
                binary = '0' + binary
            # wypełnienie listy ciągami
            self.ranklist[i] = binary
        return self.ranklist
    
    def generate(self):
        for element in self.fill_ranks(self.n):
            binary = str(element)
            myset = []
            # jeżeli na dla danej liczby na jej pozycji w ciągu jest
            # jedynka, to wrzucamy ją do zbioru
            for i in range(len(binary)):
                if (int(binary[i]) == 1):
                    myset.append(i+1)
            print myset
                

class Main:

    n = int(raw_input('Podaj n: \n'))
    gen = Generator(n)
    gen.generate()
