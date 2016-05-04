# -*- coding: utf-8 -*-

# Napisz program obliczający za pomocą programowania dynamicznego
# wartości liczb Strilinga pierwszego rodzaju ze wzoru:
# s(n,k) = s(n-1,k-1) - (n-1)*s(n-1,k)
# gdzie s(n,n+1) = 0 dla n >= 0, s(n,0) = 0 dla n >= 1 i s(0,0) = 1.

class Stirling1:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = [[-1 for j in range(k+1)] for i in range(n)]

    
    # buduje trójkąt liczb Strilinga I rodzaju (o n-1 wierszach)

    def build(self, matrix):
        # warunek początkowy s(0,0) = 1
        matrix[0][0] = 1
        # warunek początkowy s(n,0) = 0
        for i in range(1,self.n):
            matrix[i][0] = 0
        # warunek początkowy s(n,n+1) = 0
        for i in range(0,self.k):
            matrix[i][i+1] = 0
        # wzór stosujemy w dwóch różnie iterowanych pętlach, żeby nie
        # wyjść poza listę i nie wskazywać na wartości puste (tu: -1)
        for i in range(1,self.k):
            for j in range(1,i+1):
                matrix[i][j] =  matrix[i-1][j-1] - (i-1)*matrix[i-1][j]
        for i in range(self.k,self.n):
            for j in range(1,self.k+1):
                matrix[i][j] =  matrix[i-1][j-1] - (i-1)*matrix[i-1][j]
        return matrix


    # wyznacza wartość liczby Stirlinga s(n,k) na podstawie n-1-szego
    # wiersza w trójkącie

    def calculate(self,n,k):
        if (k > n or n == 0):
            return 0
        else:
            matrix = self.build(self.matrix)
            return matrix[n-1][k-1] - (n-1)*matrix[n-1][k]

    def get(self):
        return self.calculate(self.n,self.k)


class Main:
    n = int(raw_input("Podaj n: "))
    k = int(raw_input("Podaj k: "))
    strl = Stirling1(n,k)
    print "s(n,k) = " + str(strl.get())
