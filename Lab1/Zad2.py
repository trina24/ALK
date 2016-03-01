# -*- coding: utf-8 -*-
class Generator:

    def __init__(self, n, k):
        self.n = n #maksymalna wartość w ciągu
        self.counter = k-1 #ustawiamy licznik na koniec wektora
        self.vector = [i+1 for i in range(k)] #inicjujemy wektor
        self.stop = False

    def complete(self, n, vector, counter):
        #zwiększa elementy na końcu wektora
        while(vector[counter] < n - len(vector) + counter + 1):
            vector[counter] += 1
            print vector
        self.vector = vector

    def reset(self, n, vector, counter):
        #przesuwa licznik w lewo, tak długo, jak od końca do licznika wszystko jest "zrobione"
        while (vector[counter] == n - len(vector) + counter + 1):
            counter -= 1
            #jeśli przejdziemy cały wektor, to koniec
            if (counter < 0):
                return True
        #w przeciwnym wypadku zwiększamy bieżący element, a na prawo od niego wstawiamy kolejne liczby naturalne
        vector[counter] += 1
        for i in range(len(vector) - counter):
            vector[counter + i] = vector[counter] + i
        print vector
        self.vector = vector
        return False

    def generate(self):
        print self.vector
        stop = self.stop
        while (stop == False):
            self.complete(self.n, self.vector, self.counter)
            stop = self.reset(self.n, self.vector, self.counter)
            print self.counter

class Main:
    n = int(raw_input('Podaj n: \n'))
    k = int(raw_input('Podaj k: \n'))
    gen = Generator(n, k)
    gen.generate()
