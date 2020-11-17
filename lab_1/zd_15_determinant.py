#! /usr/bin/env python3


import random
import numpy as np
size_of_matrix = random.randint(2, 20)
matrix = [[random.randint(0, 10) for x in range(size_of_matrix)] for y in range(size_of_matrix)]

def det_of_matrix(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det_total = 0
        for x in range(len(matrix)):
            matrix_cp = matrix[1:]
            for y in range(len(matrix_cp)):
                matrix_cp[y] = matrix_cp[y][0:x] + matrix_cp[y][x+1:]
            det_total += (-1) ** (x % 2) * matrix[0][x] * det_of_matrix(matrix_cp)
        return det_total



matrix_np = np.array(matrix)
print(matrix_np)
print(det_of_matrix(matrix))
sign, logdet = np.linalg.slogdet(matrix_np)
print(sign * np.exp(logdet))
det = np.linalg.det(matrix_np)
print(det)
