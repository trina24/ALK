# -*- coding: utf-8 -*-
class Generator:

    def __init__(self, n, k):
        self.n = n #maksymalna wartość w ciągu
        self.counter = k-1 #licznik ustawiamy na koniec wektora
        self.vector = [1 for i in range(k)] #inicjujemy jedynkami
        self.stop = False #warunek stopu

    def complete(self, n, vector, counter):
        #zwiększa elementy na końcu wektora
        while (vector[counter] < n):
            vector[counter] += 1
            print vector
        self.vector = vector

    def reset(self, n, vector, counter):
        #przesuwa licznik w lewo, tak długo, jak wszystko jest "zrobione"
        while (vector[counter] == n):
            counter -= 1
            #jeśli przejdziemy cały wektor, to koniec
            if (counter < 0):
                return True
        #w przeciwnym wypadku zwiększamy bieżący element i wstawiamy jedynki na prawo
        vector[counter] += 1
        for i in range(counter + 1, len(vector)):
            vector[i] = 1
        print vector
        self.vector = vector
        return False
    
    def generate(self):
        print self.vector
        stop = self.stop
        while (stop == False):
            self.complete(self.n, self.vector, self.counter)
            stop = self.reset(self.n, self.vector, self.counter)

class Main:
    n = int(raw_input('Podaj n: \n'))
    k = int(raw_input('Podaj k: \n'))
    gen = Generator(n, k)
    gen.generate()
