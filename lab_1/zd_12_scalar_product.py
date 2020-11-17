#! /usr/bin/env python3

import numpy as np


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

if len(a) == len(b):
    #ver 1
    c = 0
    for x, y in zip(a, b):
        c += x * y
    print('ver1', c)

    #ver 2
    d = sum(x * y for x, y in zip(a, b))
    print('ver2', d)
    if np.dot(a, b) == c == d:
        print("Same")
