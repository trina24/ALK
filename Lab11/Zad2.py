# -*- coding: utf-8 -*-

# Napisz program generujący podział sprzężony do zadanego podziału
# (a1,...,am) liczby n.

class SelfConjugatePartition:
    
    def __init__(self, partition):
        self.part = partition

    def conversion(self):
        con_part = []
        m = len(self.part)
        new_len = self.part[0]
        for i in range(new_len):
            con_part.append(1)
        for j in range(2,m+1):
            for i in range(1,self.part[j-1]+1):
                con_part[i-1] += 1
        return con_part

class Main:

    spl = raw_input("Podaj liczby podziału: ").split()
    part = [int(element) for element in spl]
    scp = SelfConjugatePartition(part)
    conj = scp.conversion()
    print '\n' + 'Sprzężony podział: ' + str(conj) + '\n'


    print "Diagram Ferrersa-Younga - dany podział: \n"
    for element in scp.part:
        for i in range(element):
            print '*',
        print '\n'

    print "Diagram Ferrersa-Younga - sprzężony podział: \n"
    for element in conj:
        for i in range(element):
            print '*',
        print '\n'
