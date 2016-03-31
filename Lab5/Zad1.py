# -*- coding: utf-8 -*-

# Napisz program wyznaczający następnik k-elementowego podzbioru T
# zbioru {1,...,n} w uporządkowaniu antyleksykograficznym podzbiorów
# k-elementowych.

class Successor:

    def __init__(self, n, subset):
        self.n = n
        self.k = len(subset)
        self.vector = [int(element) for element in subset]

    def successor(self):
        counter = self.k
        vector = self.vector
        vector.insert(0, self.n + 1)
        # przesuwa licznik w lewo, tak długo, aż będzie się dało
        # zwiększyć element na danej pozycji
        while (vector[counter - 1] - vector[counter] <= 1 and counter > 0):
            counter -= 1
        # jeśli przejdziemy cały wektor, to koniec
        if (counter == 0):
            return 'Brak następnika'
        else:
        # w przeciwnym wypadku zwiększamy bieżący element
        # i najmniejsze możliwe liczby na prawo
            vector[counter] += 1
            for i in range(counter + 1, len(vector)):
                vector[i] = self.k - i + 1
            vector.pop(0)
            return vector
        
class Main:

    n = int(raw_input('Podaj n: \n'))
    subset = raw_input('Podaj elementy podzbioru: \n').split()
    sc = Successor(n, subset)
    print sc.successor()
