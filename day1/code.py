#!/usr/bin/env python

file_results = 'input'

f = open(file_results, 'r')
lines = list(f)

point = 50
res = 0
res2 = 0

for line in lines:
    rotations = int(line[1:])
    if line[0] == 'L':
        rotations = -rotations
    new_point = point + rotations

    nb_zeros = abs(new_point // 100)

    if (point == 0 and new_point < 0 and nb_zeros > 0):
        nb_zeros -= 1

    point = (new_point) % 100
    if (point == 0):
        res += 1
        if (new_point > 0 and nb_zeros > 0):
            nb_zeros -= 1

    print(rotations, point, nb_zeros)
    res2 += nb_zeros




# Part 1
print("res part 1: ", res)

# Part 2
print("res part 2: ", res+res2)
