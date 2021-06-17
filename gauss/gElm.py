#! /usr/bin/env python3
# -*- coding: utf-8 -*- 

import math
import sys

# ./gElm.py

class G_Elm:

    def __init__(self, matrix):
        self.matrix = matrix
        self.LINES = matrix.__len__()
        self.COLUMNS = matrix[0].__len__()

    def elimin_system(self):
        for line in range(self.LINES - 1):

            ''' pivoteamento parcial '''
            pivot = self.matrix[line][line]
            for part_pivot in range(line, self.LINES): # percorre todas as colunas abaixo do pivô
                candidate = self.matrix[part_pivot][line]
                if math.fabs(candidate) > math.fabs(pivot): # novo pivo com maior módulo
                    temp = self.matrix[line]
                    self.matrix[line] = self.matrix[part_pivot]
                    self.matrix[part_pivot] = temp

                    pivot = candidate
            
            if pivot == 0:
                print("Pivô é Zero!")
                sys.exit()

            ''' cálculo das linhas '''
            for next_line in range(line + 1, self.LINES):
                w = self.matrix[next_line][line] / pivot

                for c in range(self.COLUMNS):
                    self.matrix[next_line][c] -= self.matrix[line][c] * w

    def gauss_jordan(self):
        for line in range(self.LINES):
            
            ''' pivoteamento parcial '''
            pivot = self.matrix[line][line]
            for part_pivot in range(line, self.LINES): # percorre todas as colunas abaixo do pivô
                candidate = matrix[part_pivot][line]
                if math.fabs(candidate) > math.fabs(pivot): # novo pivo com maior módulo
                    temp = matrix[line]
                    matrix[line] = matrix[part_pivot]
                    matrix[part_pivot] = temp

                    pivot = candidate
            
            if pivot == 0:
                print("Pivô é Zero!")
                sys.exit()
                
            ''' cálculo das linhas '''
            for i in range(self.LINES):
                w = self.matrix[i][line] / pivot
                    
                for c in range(self.COLUMNS):
                    self.matrix[i][c] -= self.matrix[line][c] * w

    def solver_system(self):
        # populando a lista de variáveis do sistema
        l_system = []
        for el in range(self.LINES):
            l_system.append(0)

        for i in range(self.LINES, 0, -1):
            sum = 0.

            for j in range(i, self.LINES):
                sum += self.matrix[i - 1][j] * l_system[j]
            
            if self.matrix[i - 1][i - 1] == 0:
                print("Pivô é Zero! Impossível Resolver!")
                self.print_matrix()
                sys.exit()

            l_system[i - 1] = ((self.matrix[i - 1][self.LINES] - sum) / self.matrix[i - 1][i - 1])

        print("Solução do sistema: S = {" + str(l_system) + "}")

    def gauss_elm(self):
        self.elimin_system()
        self.solver_system()

    def print_matrix(self):
        for i in self.matrix:
            print(i)

if __name__ == '__main__':
    '''
    matrix = [
                [2, 1, -3, -1], 
                [-1, 3, 2, 12],
                [3, 1, -3, 0]
            ]
    '''
    '''
    matrix = [
                [3, -5, 1, 12],
                [3, -55, 5, 1],
                [5, 12, 1, -1]
            ]
    '''

    matrix = [
                [1, 2, 1, 2], 
                [3, 8, 1, 12],
                [0, 4, 1, 2]
            ]
    

    '''
    matrix = [
                [0.8, -0.2, -0.2, -0.3, 0.5],
                [-0.2, 0.9, -0.2, -0.3, 0.4],
                [-0.3, -0.3, 0.8, -0.2, 0.3],
                [-0.2, -0.2, -0.4, 0.8, 0]
            ]
    '''
    '''
    matrix = [
                [1, 5, 7],  
                [2, 0, 3],
                [2, 2, 4]
            ]
    '''
    
    
    gauss = G_Elm(matrix)
    #gauss.elimin_system()
    gauss.gauss_elm()
    gauss.print_matrix()
    