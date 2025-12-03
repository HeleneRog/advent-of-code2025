#!/usr/bin/env python
import re

file = 'example'

f = open(file, 'r')
line = f.read()

res = 0
res2 = 0

for a, b in [e.split("-") for e in line.rstrip().split(",")]:
    for i in range(int(a), int(b)+1):
        i_str = str(i)
        if re.match(r"^(.*)\1$", i_str):
            res += i
        if re.match(r"^(.*)\1+$", i_str):
            res2 += i


print("res part 1: ", res)
print("res part 2: ", res2)
