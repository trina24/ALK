# -*- coding: utf-8 -*-

class SuccessorFinder:
    def __init__(self,vec):
        self.perm = vec
        self.n = len(vec)

    def find_index(self):
        i = self.n - 1
        while (i>0 and self.perm[i] < self.perm[i-1]):
            i -= 1
        if (i == 0):
            return "koniec"
        else:
            return i-1

    def find_last_greater(self, index):
        i = self.n - 1
        while (self.perm[i] < self.perm[index]):
            i -= 1
        return i

    def change(self, vec, index1, index2):
        temp = vec[index1]
        vec[index1] = vec[index2]
        vec[index2] = temp
        return vec

    def sublist(self,vec,index):
        list1 = [vec[i] for i in range(index+1)]
        list2 = [vec[i] for i in range(index+1,self.n)]
        list2.reverse()
        return list1+list2

    def successor(self):
        index = self.find_index()
        if (index == "koniec"):
            return "brak następnika"
        else:
            index2 = self.find_last_greater(index)
            changedlist = self.change(self.perm,index,index2)
            successor = self.sublist(changedlist,index)
            return successor

class Main():
    vector = raw_input("Podaj elementy permutacji: \n").split()
    permutation = []
    for element in vector:
        permutation.append(int(element))
    sf = SuccessorFinder(permutation)
    print sf.successor()
