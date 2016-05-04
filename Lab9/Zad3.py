# -*- coding: utf-8 -*-

# Napisz program obliczający za pomocą programowania dynamicznego
# wartości liczb Bella ze wzoru:
# B(n) = sum(k=0,n-1) (C(n-1,k)*B(k)),
# gdzie B(0) = 1.

class Bell:

    def __init__(self, n):
        self.n = n
        self.numbers = [1]  # warunek początkowy B(0) = 1
        self.binomials = self.pascal_triangle()


    # zwraca listę kolejnych wierszy trójkąta Pascala
    
    def pascal_triangle(self):
        pt = []
        pt.append([1])
        currentline = [pt[0]]
        for i in range(1, self.n + 1):
            newline = [1]
            for j in range(1, len(currentline)):
                newline.append(currentline[j - 1] + currentline[j])
            newline.append(1)
            pt.append(newline)
            currentline = newline
        return pt


    # wyznacza z trójkąta Pascala współczynnik dwumianowy C(n, k)

    def binomial(self, n, k):
        return self.binomials[n][k]

    
    # buduje listę liczb Bella

    def build(self, numbers):
        while (len(numbers) < self.n):
            bell_next = 0
            length = len(numbers)
            for i in range(length):
                bell_next += self.binomial(length-1,i) * numbers[i]
            numbers.append(bell_next)
        return numbers

        
    # zwraca n-tą liczbę Bella

    def get(self):
        return self.build(self.numbers)[-1]


class Main:

    n = int(raw_input("Podaj n: "))
    bell = Bell(n)
    print "B(n) = " + str(bell.get())
