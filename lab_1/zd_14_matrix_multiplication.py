#! /usr/bin/env python3

import random
import numpy as np

matrix1 = [[random.randint(0, 10) for x in range(8)] for y in range(8)]
matrix2 = [[random.randint(0, 10) for x in range(8)] for y in range(8)]
matrix = [[0 for y in range(len(matrix1))] for x in range(len(matrix1))]

#ver1
if len(matrix1[0]) == len(matrix2):
    for x in range(len(matrix1)):
        for y in range(len(matrix1)):
            for k in range(len(matrix1)):
                matrix[x][y] += matrix1[x][k] * matrix2[k][y]

#ver2
reference = np.matmul(np.array(matrix1), np.array(matrix2))
print(reference)
matrix = np.array(matrix)
if np.array_equal(matrix, reference):
    print("Both matrices are the same")

