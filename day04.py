#!/usr/bin/env python3

import re
import collections

ROOMS = ['aaaaa-bbb-z-y-x-123[abxyz]', # is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
'a-b-c-d-e-f-g-h-987[abcde]', # is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
'not-a-real-room-404[oarel]', # is a real room.
'totally-real-room-200[decoy]', # is not
]

with open('day04.in') as f:
    ROOMS = f.readlines()

PARSER = re.compile(r'^([a-z\-]+)(\d+)\[(\w{5})\]$')
ALPHABET = [chr(x) for x in range(ord('a'), ord('z') + 1)]

def isValidRoom(name, checksum):
    name = name.replace('-', '')
    counter = collections.Counter(name)
    lists = sorted(counter.items(), key=lambda x: x[0]) # Sort alphabetically
    lists.sort(key=lambda x: x[1], reverse=True)        # Sort by count
    generatedChecksum = ''.join(x[0] for x in lists[:5])
    return generatedChecksum == checksum
    
def rotate(string, amount):
    newstring = []
    for c in string:
        if c in ALPHABET:
            # find the letter at {amount} offset in the ALPHABET list
            newstring.append( ALPHABET[(ord(c) - ord('a') + amount) % len(ALPHABET)] )
        else:
            newstring.append( c )
    return ''.join(newstring)

    
for room in ROOMS:
    m = PARSER.match(room)
    if m:
        name, number, checksum = m.groups()
        number = int(number)
        if isValidRoom(name, checksum):
            rotAmount = number % len(ALPHABET)
            decypheredName = rotate(name, rotAmount)
            if 'north' in decypheredName:
                print (decypheredName, number)
    else:
        raise ValueError("Unexpected Value: {}".format(room))