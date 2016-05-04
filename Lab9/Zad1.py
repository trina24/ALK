# -*- coding: utf-8 -*-

# Napisz program obliczający za pomocą programowania dynamicznego
# wartości liczb Strilinga drugiego rodzaju ze wzoru:
# S(n,k) = k*S(n-1,k) + S(n-1,k-1),
# gdzie S(n,n+1) = 0 dla n >= 0, S(n,0) = 0 dla n >= 1 i S(0,0) = 1.

class Stirling2:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = [[-1 for j in range (k+1)] for i in range(n)]


    # buduje trójkąt liczb Stirlinga II rodzaju (o n-1 wierszach)

    def build(self,matrix):
        # warunek początkowy S(0,0) = 1
        matrix[0][0] = 1
        # warunek początkowy S(n,0) = 0
        for i in range(1,self.n):
            matrix[i][0] = 0
        # warunek początkowy S(n,n+1) = 0
        for i in range(0,self.k):
            matrix[i][i+1] = 0
        # wzór stosujemy w dwóch różnie iterowanych pętlach, żeby nie
        # wyjść poza listę i nie wskazywać na wartości puste (tu: -1)
        for i in range(1,self.k):
            for j in range(1,i+1):
                matrix[i][j] = j*matrix[i-1][j] + matrix[i-1][j-1]
        for i in range(self.k,self.n):
            for j in range(1,self.k+1):
                matrix[i][j] = j*matrix[i-1][j] + matrix[i-1][j-1]
        return matrix


    # wyznacza wartość liczby Stirlinga S(n,k) na podstawie n-1-szego
    # wiersza w trójkącie

    def calculate(self,n,k):
        if (k > n or n == 0):
            return 0
        else:
            matrix = self.build(self.matrix)
            return k*matrix[n-1][k] + matrix[n-1][k-1]

    def get(self):
        return self.calculate(self.n,self.k)


class Main:
    n = int(raw_input("Podaj n: "))
    k = int(raw_input("Podaj k: "))
    strl = Stirling2(n,k)
    print "S(n,k) = " + str(strl.get())
