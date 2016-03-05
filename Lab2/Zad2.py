# -*- coding: utf-8 -*-
class Generator:

    def __init__(self, n, k):
        self.n = n #maksymalna wartość w ciągu
        self.counter = k-1 #licznik ustawiamy na koniec wektora
        self.vector = [1 for i in range(k)] #inicjujemy jedynkami

    def recursive_inc(self, n, vector, counter):
        if (vector[counter] < n and counter >= 0):
            #zwiększa bieżący element i wstawia jedynki na prawo
            vector[counter] += 1
            for i in range(counter + 1, len(vector)):
                vector[i] = 1
            print vector
            #zwiększa elementy na końcu wektora
            self.recursive_inc(n, vector, len(vector) - 1)
        elif (counter > 0):
            #przesuwa licznik w lewo
            self.recursive_inc(n, vector, counter - 1)

    def generate(self):
        print self.vector
        self.recursive_inc(self.n, self.vector, self.counter)

class Main:
    n = int(raw_input('Podaj n: \n'))
    k = int(raw_input('Podaj k: \n'))
    gen = Generator(n, k)
    gen.generate()
