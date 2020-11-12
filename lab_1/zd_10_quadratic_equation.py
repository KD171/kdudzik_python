#! /usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        delta = b ** 2 - 4 * a * c
        x1 = (- b + delta ** (1 / 2)) / (2 * a)
        x2 = (- b - delta ** (1 / 2)) / (2 * a)
        x_np = np.roots([a, b, c])
        print("Numpy:", "\nx1 = ", x_np[0], "\nx2 = ", x_np[1])
        print("Normal:", '\nx1 =', x1, '\nx2 =', x2)
    except Exception as e:
        print(e)

