#! /usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys

class Matriz_Op:

    def __init__(self, matrixA, matrixB):
        self.matrixA = matrixA
        self.matrixB = matrixB
        self.LINES_MATRIX_A = matrixA.__len__()      # m
        self.COLUMNS_MATRIX_A = matrixA[0].__len__() # p
        self.LINES_MATRIX_B = matrixB.__len__()
        self.COLUMNS_MATRIX_B = matrixB[0].__len__() # n

    def validate(self):
        if self.COLUMNS_MATRIX_A != self.LINES_MATRIX_B:
            print("Formato de matrizes inválido!")
            sys.exit()

    def validate_mult_col_row(self):
        if self.LINES_MATRIX_A != self.COLUMNS_MATRIX_B:
            print("Formato de matrizes inválido!")
            sys.exit()
    
    def pop_matrix(self):
        matrix = []
        for i in range(self.LINES_MATRIX_A):
            matrix.append([0]*self.COLUMNS_MATRIX_B)

        return matrix

    def a_mult_b(self):
        self.validate()

        ''' populando a matriz c '''
        matrixC = self.pop_matrix()

        ''' multiplicação matrizA por matrizb linha e coluna '''
        for i in range(self.LINES_MATRIX_A):
            for j in range(self.COLUMNS_MATRIX_B):
                for k in range(self.LINES_MATRIX_B):
                    #print(str(matrixA[i][k]) + " - " + str(matrixB[k][j]))
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

        self.print_matrix(matrixC)

    def a_mult_b_col_row(self):
        self.validate_mult_col_row()

        ''' populando a matriz c '''
        matrixC = self.pop_matrix()

        ''' multiplicação matrizA por matrizb coluna e linha '''
        for k in range(self.LINES_MATRIX_B):
            for i in range(self.LINES_MATRIX_A):
                for j in range(self.COLUMNS_MATRIX_B):
                    print(str(matrixA[i][k]) + " " + str(matrixB[k][j]))
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]   

        self.print_matrix(matrixC)

    def print_matrix(self, matrix):
        for lines in range(matrix.__len__()):
            print(matrix[lines])

if __name__ == '__main__':
    matrixA = [
                [1, 5, 7],  
                [2, 0, 3],
                [2, 2, 4]
              ]

    matrixB = [
                [1.0, 0.0, 0.0],
                [0.0, -10.0, 0.0],
                [0.0, 0.0, -1.1999999999999993]
              ]

    op = Matriz_Op(matrixA, matrixB)
    op.a_mult_b()
    print("\n")
    #op.a_mult_b_col_row()