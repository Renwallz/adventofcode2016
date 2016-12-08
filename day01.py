#!/usr/bin/env python3

COMPASS = [('n', 1), ('e', 1), ('s', -1), ('w', -1)]

with open('day01.in') as f:
    inp = f.read()
directions = inp.split(', ')

xpos = ypos = 0
currentFacingIndex = 0

for direction in directions:
    if direction[0] == 'L': #turn left
        currentFacingIndex = (currentFacingIndex - 1) % len(COMPASS)
    else: #turn right
        currentFacingIndex = (currentFacingIndex + 1) % len(COMPASS)
    
    speed = int(direction[1:])
    currentFacing = COMPASS[currentFacingIndex]
    
    if currentFacing[0] in ('n', 's'): #moving vertically
        ypos += speed * currentFacing[1]
    else:                           #moving horizontally
        xpos += speed * currentFacing[1]
        
        
# We are now at the destination
# Calculate distance

# Normalise
if xpos < 0:
    xpos *= -1
if ypos < 0:
    ypos *= -1
    
distance = xpos + ypos
print("The total distance is {}".format(distance))