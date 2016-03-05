# -*- coding: utf-8 -*-
import math

class Generator:

    def __init__(self, n):
        self.n = n #liczba elementów wyjściowego zbioru
        self.ranklist = [0 for i in range(pow(2,n))] #inicjalizacja listy wektorów charakterystycznych
    
    def fill_ranks(self, n):
        for i in range(len(self.ranklist)):
            #zamiana rangi na ciąg binarny
            binary = bin(i)[2:]
            #dopisanie zer z przodu
            for j in range(n-len(binary)):
                binary = '0' + binary
            #wypełnienie listy ciągami
            self.ranklist[i] = binary
        return self.ranklist

    def sort_ranks(self, n, somelist):
        #tworzy nową listę, przeglądając poprzednią i wybierając elementy o danej liczbie jedynek (kolejno)
        sortedlist = []
        for i in range(n+1):
            ones = 0
            for element in somelist:
                element_ones = element.count('1')
                if (element_ones == i):
                    sortedlist.append(element)
        return sortedlist

    def generate(self):
        sortedlist = self.sort_ranks(self.n, self.fill_ranks(self.n))
        for element in sortedlist:
            binary = str(element)
            myset = []
            #jeżeli na dla danej liczby na jej pozycji w ciągu jest jedynka, to wrzucamy ją do zbioru
            for i in range(len(binary)):
                if (int(binary[i]) == 1):
                    myset.append(i + 1)
            print sorted(myset)
                

class Main:
    n = int(raw_input('Podaj n: \n'))
    gen = Generator(n)
    gen.generate()
