#!/usr/bin/env python3

possibleCount = 0
with open('day03.in') as f:
    for line in f:
        line = line.rstrip()
        values = [int(x) for x in line.split()]
        values.sort()
        if values[0] + values[1] > values[2]:
            possibleCount += 1
            
print("There are {} Triangles that are possible".format(possibleCount))