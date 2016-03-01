# -*- coding: utf-8 -*-
import math

class Generator:

    def __init__(self, n):
        self.n = n
        self.ranklist = [0 for i in range(pow(2,n))]
    
    def fill_ranks(self, n):
        for i in range(len(self.ranklist)):
            binary = bin(i)[2:]
            for j in range(n-len(binary)):
                binary = '0' + binary
            self.ranklist[i] = binary
        return self.ranklist
    
    def printing(self):
        toprint = self.fill_ranks(self.n)
        print toprint

    def generate(self):
        for element in self.fill_ranks(self.n):
            binary = str(element)
            myset = []
            for i in range(len(binary)):
                if (int(binary[i]) == 1):
                    myset.append(i+1)
            print myset
                

class Main:
    n = int(raw_input('Podaj n: \n'))
    gen = Generator(n)
    gen.generate()
    #gen.printing()
