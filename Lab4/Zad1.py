# -*- coding: utf-8 -*-

# Napisz program wyznaczający następnik k-elementowego podzbioru T    
# zbioru {1,...,n} w uporządkowaniu leksykograficznym podzbiorów
# k-elementowych.


class Successor:

    def __init__(self, n, subset):
        self.n = n
        self.k = len(subset)
        self.vector = [int(element) for element in subset]

    def successor(self):
        counter = self.k - 1
        vector = self.vector
        # przesuwa licznik w lewo, tak długo, aż będzie się dało
        # zwiększyć element na danej pozycji
        while (vector[counter] == self.n - self.k + counter + 1):
            counter -= 1
        # jeśli przejdziemy cały wektor, to koniec
        if (counter < 0):
            return 'Brak następnika'
        else:
        # w przeciwnym wypadku zwiększamy bieżący element
        # i wstawiamy kolejne liczby naturalne na prawo
            vector[counter] += 1
            for i in range(counter + 1, len(vector)):
                vector[i] = vector[i - 1] + 1
            return vector

class Main:

    n = int(raw_input('Podaj n: \n'))
    subset = raw_input('Podaj elementy podzbioru: \n').split()
    sc = Successor(n, subset)
    print sc.successor()
