# -*- coding: utf-8 -*-

# Napisz program generujący wszystkie podziały liczby n w postaci
# normalnej za pomocą algorytmu rekurencyjnego.

import PartitionGenerator

class Main:

    n = int(raw_input("Podaj n: "))
    pg = PartitionGenerator.PartitionGenerator(n)
    parts = pg.generate_partitions()
    for element in parts:
        print element
