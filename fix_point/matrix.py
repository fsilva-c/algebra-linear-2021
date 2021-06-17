#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
# ./matrix.py

# A * x = b; em que x e b são vetores
# ex. prof julian: A = [[5, 2], [3, 4]]; x = [[1], [2]], logo b = [[9], [11]]

# fómula ponto fixo:
# x = D^-1 *  (b - N * X)

import random
import numpy as np

class Matrix_OP:

    def __init__(self, _matrix):
        self.matrix = _matrix
        self.LINES = _matrix.__len__()
        self.COLUMNS = _matrix[0].__len__()

    ##### métodos principais #####
    def get_diags_matrix(self):
        mtrz_1, mtrz_2 = self.pop_matrix_zeros(self.LINES, self.COLUMNS), self.pop_matrix_zeros(self.LINES, self.COLUMNS)

        j = self.COLUMNS - 1
        for i in range(self.LINES):
            mtrz_1[i][i], mtrz_2[i][j] = self.matrix[i][i], self.matrix[i][j]

            j -= 1

        return mtrz_1, mtrz_2

    def get_fix_point(self, D, b, N, x, it = 800000):
        '''
        fómula ponto fixo:
        x = D^-1 *  (b - N * x); em que x não pode ser a solução de A * x = b
        '''
        inv_D = self.get_inv(D)

        i = 0
        stop = self.a_sub_b(self.a_mult_b(self.matrix, x), b) # A * x - b ~= [[0], [0]]
        err = 0.0000000001
        while np.linalg.norm(stop) > err and i < it:
            #self.print_matrix(x)
            #print("\n")
            x = self.a_mult_b(inv_D, (self.a_sub_b(b, self.a_mult_b(N, x))))
        
            stop = self.a_sub_b(self.a_mult_b(self.matrix, x), b)
            i += 1

        print("Iteracoes: ", i)

        return x

    ##### métodos úteis
    def pop_matrix_zeros(self, lines, columns):
        mtrz = []

        for i in range(lines):
            mtrz.append([0] * columns)

        return mtrz

    def a_mult_b(self, matrix_A, matrix_B):
        lines_matrix_A = len(matrix_A)
        columns_matrix_B = len(matrix_B[0])
        lines_matrix_B = len(matrix_B)

        ''' populando a matriz c '''
        matrix_C = self.pop_matrix_zeros(lines_matrix_A, columns_matrix_B)

        ''' multiplicação matrizA por matrizb linha e coluna '''
        for i in range(lines_matrix_A):
            for j in range(columns_matrix_B):
                for k in range(lines_matrix_B):
                    #print(str(matrix_A[i][k]) + " - " + str(matrix_B[k][j]))
                    matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

        return matrix_C


    def a_sub_b(self, matrix_A, matrix_B):
        lines_matrix = len(matrix_A)
        columns_matrix = len(matrix_A[0])

        ''' populando a matriz c '''
        matrix_C = self.pop_matrix_zeros(lines_matrix, columns_matrix)

        for l in range(lines_matrix):
            for c in range(columns_matrix):
                matrix_C[l][c] = matrix_A[l][c] - matrix_B[l][c]

        return matrix_C


    def get_inv(self, _matrix):
        # fazer com gauss-jordan.....
        return np.linalg.inv(_matrix)

    def print_matrix(self, _matrix = None):
        if _matrix is None:
            _matrix = self.matrix

        for i in range(_matrix.__len__()):
            print(_matrix[i])

    def truncate(self, n, decimals=0):
        multiplier = 10 ** decimals
        
        return int(n * multiplier) / multiplier


if __name__ == '__main__':

    matrix = [
                [5, 5],
                [3, 1]
            ]

    op = Matrix_OP(matrix)

    mts_diagonal = op.get_diags_matrix()
    D = mts_diagonal[0]
    N = mts_diagonal[1]
    b = [
        [9],
        [11]
    ]
    
    x_0, x_1 = random.random(), random.random()
    x = [
        [x_0],
        [x_1]
    ]
    #print("vetor x:")
    #op.print_matrix(x)
    #print("\n\n")

    fix_point = op.get_fix_point(D, b, N, x)
    print("Ponto fixo: ")
    op.print_matrix(fix_point)
    print("\n")
    
    print("Teste A * x (matrix * fix_point): ")
    test = op.a_mult_b(matrix, fix_point)
    op.print_matrix(test)
