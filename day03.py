#!/usr/bin/env python3

possibleCount = 0
with open('day03.in') as f:
    
    # now we need to be tricky; grab 3 lines at a time
    
    currentTriangles = []
    for line in f:
        line = line.rstrip()
        values = [int(x) for x in line.split()]
        currentTriangles.append(values)
        
        if len(currentTriangles) == 3:
            for i in range(3):
                values = [x[i] for x in currentTriangles]
                values.sort()
                if values[0] + values[1] > values[2]:
                    possibleCount += 1
            currentTriangles = []
            
print("There are {} Triangles that are possible".format(possibleCount))