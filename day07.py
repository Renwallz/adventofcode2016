#!/usr/bin/env python3

import re

searchTLSNotWithinBrackets = re.compile(r'''
    \[ [^ \] ]*     # keep looking until the next closing bracket    
        (\w)        
        (.(?!\1))   # look ahead for not group 1, and if so grab next char and store into group 2
        \2          
        \1          
    .*\]''', re.VERBOSE)
    
searchTLSPairs = re.compile(r'(\w)(.(?!\1))\2\1') # See regex above for the explanation of (.(?!\1))

supernetExtractor = re.compile(r'''
    (?:^|\])                    # start or ]
    (?P<content> [^ \[ ]+ )     # everything that's not a [
    (?:\[|$)                    # [ or end of line ]
    ''', re.VERBOSE )
    
hypernetExtractor = re.compile(r'''
    \[
        (?P<content> [^ \] ]+ )
    \]
    ''', re.VERBOSE )
    
tripletExtractor = re.compile(r'''
    (?=                     # positive lookahead without consuming
        (?P<triplet>        # capture the lookahead into <triplet>
            (\w)            # first letter
            (?!\2).         # second letter if it is not the same as the first
            \2              # first a second time
        )
    )''', re.VERBOSE)

total = 0

testTLS = '''abba[mnop]qrst
abcd[bddb]xyyx 
aaaa[qwer]tyui 
ioxxoj[asdfgh]zxcvbn'''.split()

testSSL = '''aba[bab]xyz 
xyx[xyx]xyx
aaa[kek]eke 
zazbz[bzb]cdb
'''.split()

def checkIPForTLS(ip):
    if not searchTLSNotWithinBrackets.search(ip):
        if searchTLSPairs.search(ip):
            return True
    return False

def checkIPForSSL(ip):
    supernet = '---'.join( x.group('content') for x in supernetExtractor.finditer(ip) ) 
    hypernet = '---'.join( x.group('content') for x in hypernetExtractor.finditer(ip) ) 
    
    for match in tripletExtractor.finditer(supernet):
        aba = match.group('triplet')
        bab = '{}{}{}'.format(aba[1], aba[0], aba[1])
        if bab in hypernet:
            return True
    return False
    
    
for t in testSSL:
    print(t, checkIPForSSL(t))
    

with open('day07.in') as f:
    for line in f:
        line = line.rstrip()
        if checkIPForSSL(line):
            total += 1
                
print("There are {} IPs vulnerable".format(total))