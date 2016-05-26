# -*- coding: utf-8 -*-

# Napisz program generujący podział sprzężony do zadanego podziału
# (a1,...,am) liczby n.

import SelfConjugatePartition

class Main:

    spl = raw_input("Podaj liczby podziału: ").split()
    part = [int(element) for element in spl]
    scp = SelfConjugatePartition.SelfConjugatePartition(part)
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
