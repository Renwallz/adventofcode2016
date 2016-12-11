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



searchSSLWithinBracketsTemplate = r'''
    \[ 
        [^ \] ]*    # keep looking until the next closing bracket    
        {}          # where the value to search for will be placed
    .*\]'''

searchSSLPairs = re.compile(r'''
    (?:^|])             # start or after a closing ] (non capturing group)  
    [^ \[ ]*            # look for 0 or more not-[
    (?P<ABA>            # named group ABA
        (\w)            # group 2
        (?!\[|\]|\2)    # positive lookahead for not '[', ']' or group 2
        .               # take the middle char
        \2
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
    m = searchSSLPairs.finditer(ip)
    if m:
        for match in m:
            aba = match.group('ABA')
            bab = '{}{}{}'.format(aba[1], aba[0], aba[1])
            if re.search( searchSSLWithinBracketsTemplate.format(bab), ip, re.VERBOSE ): # too much java :(
                return True
    return False
    
    
for t in testSSL:
    print(t, checkIPForSSL(t))
    
 1/0

with open('day07.in') as f:
    for line in f:
        line = line.rstrip()
        if checkIPForSSL(line):
            total += 1
                
print("There are {} IPs vulnerable".format(total))