#!/usr/bin/env python
import numpy as np

file_results = 'input'

f = open(file_results, 'r')
lines = list(f)


def compute(lines, N):
    res = 0

    for line in lines:
        vec = [int(e) for e in line.rstrip()]
        shift = 0
        for i in range(0, N):
            if i < N-1:
                shift += np.argmax(vec[shift:-N+i+1]) + 1
            else:
                shift += np.argmax(vec[shift:]) + 1
            res += pow(10, N-i-1) * vec[shift-1]

    return res


print("res part 1: ", compute(lines, 2))
print("res part 2: ", compute(lines, 12))
