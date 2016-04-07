# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie k-elementowe podzbiory zbioru
# {1,...,n} w porządku minimalnych zmian (revolving door).

class Generator:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.vector = [i + 1 for i in range(k)]

    def num_of_least(self, vector):
        # zwraca liczbę pozycji, na których stoi najmniejszy możliwy
        # element, powiększoną o 1
        j = 0
        while (j < len(vector) and vector[j] == j + 1):
            j += 1
        j += 1
        return j

    def successor(self, vector):
        # wyznacza następnika
        vector.append(self.n + 1)  # wartownik
        j = self.num_of_least(vector)
        # jeżeli ciąg jest postaci 1, 2, ..., k - 1, n, to koniec
        if (j == self.k and vector[self.k - 1] == self.n):
            return []
        # jeżeli różnica k - j jest nieparzysta, to zwiększamy dwa
        # ostatnie elementy z tych, których nie dałoby się zmniejszyć
        # lub, jeśli takich nie ma, zmniejszamy pierwszy
        elif ((self.k - j) % 2 == 1):
            if (j == 1):
                vector[0] -= 1
            else:
                vector[j - 2] = j
                vector[j - 3] = j - 1
        # jeżeli różnica k - j jest parzysta, rozważamy dwa przypadki
        else:
            # j-ta i następna pozycja różnią się o 1:
            # wtedy j-ty element przesuwamy na następną pozycję
            # a na j-tej wstawiamy możliwie najmniejszy
            if (vector[j] == vector[j - 1] + 1):
                vector[j] = vector [j - 1]
                vector[j - 1] = j
            # w przeciwnym przypadku:
            # j-ty element wstawiamy na poprzednią pozycję
            # na j-tej pozycji zwiększamy o 1
            else:
                vector[j - 2] = vector[j - 1]
                vector[j - 1] += 1
        vector.pop()
        return vector

    def generate(self):
        vector = self.vector
        while (len(vector) > 0):
            print vector
            vector = self.successor(vector)

class Main:

    n = int(raw_input("Podaj n: \n"))
    k = int(raw_input("Podaj k: \n"))
    gen = Generator(n, k)
    gen.generate()
