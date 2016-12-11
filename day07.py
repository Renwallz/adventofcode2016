#!/usr/bin/env python3

import re

searchNotWithinBrackets = re.compile(r'''
    \[ [^ \] ]*     # keep looking until the next closing bracket    
        (\w)        
        (.(?!\1))   # look ahead for not group 1, and if so grab next char and store into group 2
        \2          
        \1          
    .*\]''', re.VERBOSE)
searchPairs = re.compile(r'(\w)(.(?!\1))\2\1') # See regex above for the explanation of (.(?!\1))

total = 0

test = '''abba[mnop]qrst
abcd[bddb]xyyx 
aaaa[qwer]tyui 
ioxxoj[asdfgh]zxcvbn'''.split()

def checkIP(ip):
    if not searchNotWithinBrackets.search(ip):
        if searchPairs.search(ip):
            return True
    return False

    
for t in test:
    print(t, checkIP(t))


    
with open('day07.in') as f:
    for line in f:
        line = line.rstrip()
        if checkIP(line):
            total += 1
                
print("There are {} IPs vulnerable".format(total))