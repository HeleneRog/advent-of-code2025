#!/usr/bin/env python
import numpy as np
import math

file = 'input'

f = open(file, 'r')
lines = list(f)


def convert(c):
    if c == ' ':
        return 0
    return int(c)


def compute(sign, numbers):
    if sign == '+':
        return sum(numbers)
    if sign == '*':
        return math.prod(numbers)
    return 0


numbers_part1 = []
numbers_part2 = []

for line in lines[:-1]:
    numbers_part1.append([int(e) for e in line.rstrip().split()])
    numbers_part2.append([convert(e) for e in line.rstrip("\n")])

signs = (lines[-1]).rstrip().split()

res_part1 = 0
mat_part1 = np.array(numbers_part1)

for idx, sign in enumerate(signs):
    res_part1 += compute(sign, mat_part1[:, idx])

print("res part 1: ", res_part1)


res_part2 = 0
mat_part2 = np.array(numbers_part2)

sign_count = 0
numbers = []

for col in mat_part2.T:
    if sum(col) == 0:
        res_part2 += compute(signs[sign_count], numbers)
        sign_count += 1
        numbers = []
    else:
        nb = 0
        exp = 0
        for digit in col[::-1]:
            if (digit != 0):
                nb += pow(10, exp) * digit
                exp += 1
        numbers.append(nb)

res_part2 += compute(signs[sign_count], numbers)

print("res part 2: ", res_part2)
