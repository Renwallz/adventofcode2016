#!/usr/bin/env python3

from collections import Counter

message = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''.split()

with open('day06.in') as f:
    message = f.readlines()
    
message[0] = message[0].rstrip() # remove the first newline to skip that column

for i in range( len( message[0] ) ):
    col = [x[i] for x in message]
    c = Counter(col)
    # get the value of the most common letter
    print( c.most_common(1)[0][0], end='' )