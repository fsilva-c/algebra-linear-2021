#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
# ./carros.py

import sys
sys.path.append('../gauss')

from gElm import G_Elm

a = [
    [1, 0, 1, 0, 0, 0, 0],   # nó 1
    [-1, 1, 0, -1, 0, 0, 0], # nó 2
    [0, -1, 0, 0, 1, 0, 0],  # nó 3
    [0, 0, -1, 0, 0, -1, 0], # nó 4
    [0, 0, 0, 1, 0, 1, -1],  # nó 5
    [0, 0, 0, 0, -1, 0, 1]   # nó 6
]

#b = [800, -200, -500, -750, 600, 50]
b = [27, -8, -4, -13, 10, -12]
#c = [150, -220, 560, 300, -600, -190]

def concatenar_matriz(A, B):
    for i in range(len(A)):
        A[i].append(B[i])

    return A

matriz = concatenar_matriz(a, b)
gauss = G_Elm(matriz)

gauss.gauss_elm()