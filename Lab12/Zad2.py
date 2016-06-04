# -*- coding: utf-8 -*-

# Napisz program wyznaczający drzewo odpowiadające zadanemu kodowi Prufera L.

class Tree:

    def __init__(self, prufer):
        self.n = len(prufer) + 2
        self.prufer = prufer
        self.vertices = [i+1 for i in range(self.n)]

    def choose_vertex(self, prufer, vertices):
        vrt = vertices
        vrt.sort()
        vrt.reverse()
        for element in vrt:
            if (prufer.count(element) == 0):
                return element

    def algorithm(self):
        prufer = self.prufer
        vertices = self.vertices
        edges = []
        while (len(prufer) > 0):
            vertex = self.choose_vertex(prufer, vertices)
            vertices.remove(vertex)
            edges.append((prufer.pop(0),vertex))
        edges.append((vertices[0],vertices[1]))
        return edges

class Main:
    
    spl = raw_input("Podaj elementy kodu: ").split()
    prufer = [int(element) for element in spl]
    tr = Tree(prufer)
    print tr.algorithm()
