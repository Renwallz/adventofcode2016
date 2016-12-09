#!/usr/bin/env python3

###########
## 1 2 3 ##
## 4 5 6 ##
## 7 8 9 ##
###########

with open('day02.in') as f:
    instructions = f.readlines()
    
directions = {  'U': (0, -1), 
                'L': (-1, 0),
                'D': (0, 1),
                'R': (1, 0),
             }
             
MAXHEIGHT = 2
MAXWIDTH  = 2
DOOR = [[1,2,3],[4,5,6],[7,8,9]]

curPos = (1,1) # in the middle

code = []

def move(direction, pos):
    if direction == 'U':
        pos = pos[0], max(pos[1] - 1, 0)
    elif direction == 'D':
        pos = pos[0], min(pos[1] + 1, MAXHEIGHT)
    elif direction == 'L':
        pos = max(pos[0] - 1, 0), pos[1]
    elif direction == 'R':
        pos = min(pos[0] + 1, MAXWIDTH), pos[1]
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
    code.append(DOOR[curPos[1]][curPos[0]])     # Beware the order here!
    print("Added {} at pos {}".format(code[-1], curPos))

print("The code is {}".format(''.join(str(x) for x in code)))