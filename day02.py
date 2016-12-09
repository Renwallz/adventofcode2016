#!/usr/bin/env python3

###########
## 1 2 3 ##
## 4 5 6 ##
## 7 8 9 ##
###########


# lol, unexpected diamond
###############
##     1     ##
##   2 3 4   ##
## 5 6 7 8 9 ##
##   A B C   ##
##     D     ##
###############



with open('day02.in') as f:
    instructions = f.readlines()
    
directions = {  'U': (-1, 0), 
                'L': (0, -1),
                'D': (1, 0),
                'R': (0, 1),
             }
             
MAXHEIGHT = 2
MAXWIDTH  = 2
DOOR = [[1,2,3],[4,5,6],[7,8,9]]
DOOR = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]

curPos = (2,0) # Where the 5 is in the diamond

code = []
#instructions = '''ULL
#RRDDD
#LURDL
#UUUUD'''.split()

def isValid(pos):
    """ As this is now a diamond, some more smarts are needed """
    if not (0 <= pos[1] < len(DOOR)):
        return False
    if not (0 <= pos[0] < len(DOOR[0])): # This assumes it's still represented as a square
        return False
    if DOOR[pos[1]][pos[0]] == ' ':
        return False
    return True

def move(direction, pos):
    if direction in directions:
        move = directions[direction]
        newPos = (pos[0] + move[0], pos[1] + move[1])
        if isValid(newPos):
            return newPos
        return pos
    elif direction == '\n':
        return pos
    else:
        print("Error: Bad Instruction ({})".format(direction))
        raise ValueError
    return pos
    
    
for line in instructions:
    if line == '':
        continue
    for step in line:
        curPos = move(step, curPos)
        print(curPos, step, DOOR[curPos[0]][curPos[1]])
    code.append(DOOR[curPos[0]][curPos[1]])     # Beware the order here!
    print("Added {} at pos {}".format(code[-1], curPos))

print("The code is {}".format(''.join(str(x) for x in code)))