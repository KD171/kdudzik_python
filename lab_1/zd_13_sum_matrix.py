#! /usr/bin/env python3
import random
import numpy as np

matrix1 = [[random.randint(0, 100) for x in range(128)] for y in range(128)]
matrix2 = [[random.randint(0, 100) for x in range(128)] for y in range(128)]
#ver1
matrix = [[matrix1[x][y] + matrix2[x][y] for y in range(len(matrix1))] for x in range(len(matrix2))]
print(matrix)
#ver2
reference = np.add(np.array(matrix1), np.array(matrix2))
print(reference)
matrix = np.array(matrix)

if np.array_equal(matrix, reference):
    print('Both matrices are the same')


