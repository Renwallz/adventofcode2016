#!/usr/bin/env python3

# Lets verify some bitcoins!

import hashlib
import random

DOORID = b'ugkcyxxp'
PASSWORDLENGTH = 8

key = list('u' * PASSWORDLENGTH)
i = 0

HASHCODES = '123456789abcdef'

def animate(key):
    line = []
    for c in key:
        if c == 'u':
            line.append( random.choice( HASHCODES ) ) 
        else:
            line.append( c )
    print('\r Password: {}'.format(''.join(line) ), end='' )

while True:
    hash = hashlib.md5( DOORID + str(i).encode('ascii') ).hexdigest()
    if hash[:5] == '00000':
        pos = hash[5]
        value = hash[6]
        if pos.isnumeric():
            pos = int(pos)
            if pos < PASSWORDLENGTH and key[pos] == 'u':
                key[pos] = value
                if 'u' not in key:
                    print('\r '+' ' * 40 ) # clear the screen
                    break
    i += 1
    if i % 40000 == 0: # chosen by science to be the most exciting speed on  my cpu
        animate(key)
            
print ("The password is {}".format(''.join(key) ) )