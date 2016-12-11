#!/usr/bin/env python3

HEIGHT = 6
WIDTH  = 50


class Screen(object):
    
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.screen = [ list( '.' * width ) for _ in range(height) ]
        self.width  = width
        self.height = height
        
        self.ON  = '#'
        self.OFF = '.'
        
    def printScreen(self):
        print('-'*20, '\n')
        for row in self.screen:
            print(''.join(row))
        print('\n', '-'*19)
            
    def rect(self, width, height):
        """ turns on all of the pixels in a rectangle at the top-left of the screen """
        if width <= 0 or height <= 0:
            return
        for row in self.screen[:height]:
            for i in range(width):
                row[i] = self.ON

    def rotateColumn(self, colNum, amount):
        """ shifts column col amount right, wrapping to the left"""
        amount %= self.height
        col = [ x[colNum] for x in self.screen ]
        
        for i in range( self. height ):
            self.screen[i][colNum] = col[ (i - amount) % self.height ]
        
    def rotateRow(self, rowNum, amount):
        """ shifts row row amount down, wrapping to the top"""
        amount %= self.width
        amount = self.width - amount
        row = self.screen[rowNum]
        
        self.screen[rowNum] = row[amount:] + row[:amount]
        
    def numLitPixels(self):
        total = 0
        for row in self.screen:
            total += row.count(self.ON)
        return total
        

def testScreen():
    screen = Screen(7, 3)
    screen.printScreen()
    screen.rect(3,2)
    screen.printScreen()
    screen.rotateColumn(1,1)
    screen.printScreen()
    screen.rotateRow(0, 4)
    screen.printScreen()
    screen.rotateColumn(1, 1)
    screen.printScreen()

    
    
screen = Screen(WIDTH, HEIGHT)

with open('day08.in') as f:
    for line in f:
        line = line.rstrip()
        line = line.split()
        if line[0] == 'rect':
            # rect 3x2
            args = line[1].split('x')
            width  = int(args[0])
            height = int(args[1])
            screen.rect(width, height)
        elif line[0] == 'rotate':
            number = int(line[2][2:])
            amount = int(line[-1])
            if line[1] == 'row':
                screen.rotateRow(number, amount)
            elif line[1] == 'column':
                screen.rotateColumn(number, amount)
            else:
                raise ValueError(" Unexpected Argument to rotate: {}".format( line ) )
        else:
            raise ValueError("Unknown instruction: {}".format( line ) )
            
print( "There are {} pixels lit".format( screen.numLitPixels() ) )
screen.printScreen()