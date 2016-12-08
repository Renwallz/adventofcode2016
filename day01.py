#!/usr/bin/env python3

class Compass(object):  
    
    def __init__(self):
        self.directions = [('n', 1), ('e', 1), ('s', -1), ('w', -1)]
        self.currentDirection = 0
    
    def getNewDirection(self, turnDirection):
        if turnDirection == 'L':
            self.currentDirection = (self.currentDirection - 1) % len(self.directions)
        else:
            self.currentDirection = (self.currentDirection + 1) % len(self.directions)
        return self.directions[self.currentDirection]
        

class VisitedLocationException(Exception):
    pass
    
def checkCurrentLocation(coords):
    if coords in seenLocations:
        raise VisitedLocationException
    seenLocations.add(coords)
        
xpos = ypos = 0
compass = Compass()

# record visited locations, to know when we arrive somewhere we've already been
seenLocations = set((0, 0))

with open('day01.in') as f:
    inp = f.read()
directions = inp.split(', ')


try:
    for direction in directions:
        currentDirection = compass.getNewDirection(direction[0])
        
        speed = int(direction[1:])
    
        if currentDirection[0] in ('n', 's'):   #moving vertically
            for _ in range(speed):
                ypos += 1 * currentDirection[1]
                checkCurrentLocation((xpos,ypos))
                
        else:                                   #moving horizontally
            for _ in range(speed):
                xpos += 1 * currentDirection[1]
                checkCurrentLocation((xpos,ypos))
    
        print(xpos, ypos, speed, currentDirection[0])
        
        
except VisitedLocationException:
    pass
        
        
# We are now at the destination
# Calculate distance

# Normalise
if xpos < 0:
    xpos *= -1
if ypos < 0:
    ypos *= -1
    
distance = xpos + ypos
print("The total distance is {}".format(distance))