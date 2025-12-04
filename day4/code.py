#!/usr/bin/env python
import numpy as np

file = 'input'

f = open(file, 'r')
lines = list(f)


def convert(e):
    if (e == '.'):
        return 0
    if (e == '@'):
        return 1


matrix = np.array([[convert(e) for e in line.rstrip()]
                  for line in lines])
N, M = np.shape(matrix)


def is_roll(mat, i, j):
    return 0 <= i < N and 0 <= j < M and mat[i, j]


delta = [-1, 0, 1]
neighboors = [[i, j] for i in delta for j in delta if (i != 0 or j != 0)]


def count_and_remove_rolls(matrix):
    nb_of_removals = 0
    result_mat = np.copy(matrix)
    for i in range(0, N):
        for j in range(0, M):
            if matrix[i, j] == 0:
                continue
            comp = 0
            for di, dj in neighboors:
                if is_roll(matrix, i+di, j+dj):
                    comp += 1
                    if (comp >= 4):
                        continue
            if comp < 4:
                result_mat[i, j] = 0
                nb_of_removals += 1
    return result_mat, nb_of_removals


res_matrix, nb_of_removals = count_and_remove_rolls(matrix)

print("Part1", nb_of_removals)

total_removals = nb_of_removals
while (nb_of_removals > 0):
    res_matrix, nb_of_removals = count_and_remove_rolls(res_matrix)
    total_removals += nb_of_removals

print("Part2", total_removals)
