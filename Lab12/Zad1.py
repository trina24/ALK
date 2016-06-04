# -*- coding: utf-8 -*-

# Napisz program generujący kod Prufera dla zadanego drzewa T o n wierzchołkach.

from ast import literal_eval as make_tuple

class Prufer:

    def __init__(self, list_of_edges):
        self.n = self.number_of_vertices(list_of_edges)
        self.neighbourhood_lists = self.build_neighbourhood_lists(list_of_edges)

    def number_of_vertices(self, list_of_edges):
        n = 0
        for edge in list_of_edges:
            m = max(edge[0], edge[1])
            if m > n:
                n = m
        return n

    def build_neighbourhood_lists(self, list_of_edges):
        nl = [[] for i in range(self.n)]
        for i in range(1,self.n+1):
            for edge in (list_of_edges):
                if (edge[0] == i):
                    nl[i-1].append(edge[1])
                elif (edge[1] == i):
                    nl[i-1].append(edge[0])
        return nl

    def min_degree_greatest(self, nl):
        min_vertices = []
        for i in range(len(nl)):
            if (nl[i] != None and len(nl[i]) == 1):
                min_vertices.append(i + 1)
        return max(vertex for vertex in min_vertices)

    def remove_vertex(self,vertex,nl):
        nl[vertex - 1] = None
        for neigh_list in nl:
            if (neigh_list != None and neigh_list.count(vertex) > 0):
                neigh_list.remove(vertex)
        return nl
                
    def algorithm(self):
        nl = self.neighbourhood_lists
        prufer = []
        for i in range(self.n - 2):
            vertex = self.min_degree_greatest(nl)
            prufer.append(nl[vertex - 1][0])
            self.remove_vertex(vertex,nl)
        return prufer
    
class Main:
    
    spl = raw_input("Podaj krawędzie drzewa w postaci (v1,v2), oddzielając je spacjami: ").split()
    edges = [make_tuple(element) for element in spl]
    pr = Prufer(edges)
    print pr.algorithm()
