#!/usr/bin/env python
file = 'input'

f = open(file, 'r')
lines = list(f)


class Range():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_in_range(self, x):
        return self.a <= x <= self.b


class Point():
    def __init__(self, x, side):
        self.x = x
        self.side = side

    def __str__(self):
        return "(%s, %s)" %(self.x, self.side)

    def __repr__(self):
        return "(%s, %s)" %(self.x, self.side)


first_part = True
ranges = []
points = []

res_part1 = 0

for line in lines:
    if line == "\n":
        first_part = False
        continue

    if first_part:
        a, b = line.rstrip().split("-")
        ranges.append(Range(int(a), int(b)))
        points.extend([Point(int(a), 1), Point(int(b), -1)])
    else:
        x = int(line)
        for a_range in ranges:
            if a_range.is_in_range(x):
                res_part1 += 1
                break


print("res part 1: ", res_part1)


# Part2 #
points.sort(key=lambda pt: pt.x)

res_part2 = 0
left_index = 0
index = 1
count = 1

while (True):
    count += points[index].side

    while (count > 0):
        index += 1
        count += points[index].side

    # do not update the result if the next range left value equals the
    # current right range value
    if (index < len(points)-1 and points[index].x == points[index+1].x):
        index += 1
        continue

    res_part2 += points[index].x - points[left_index].x + 1

    if (index == len(points) - 1):
        break

    left_index = index+1
    index += 2
    count = 1

print("res part 2: ", res_part2)
