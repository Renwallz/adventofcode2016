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

totalSectorSum = 0

def isValidRoom(name, checksum):
    name = name.replace('-', '')
    counter = collections.Counter(name)
    lists = sorted(counter.items(), key=lambda x: x[0]) # Sort alphabetically
    lists.sort(key=lambda x: x[1], reverse=True)        # Sort by count
    generatedChecksum = ''.join(x[0] for x in lists[:5])
    return generatedChecksum == checksum

for room in ROOMS:
    m = PARSER.match(room)
    if m:
        name, number, checksum = m.groups()
        number = int(number)
        if isValidRoom(name, checksum):
            totalSectorSum += number
    else:
        raise ValueError("Unexpected Value: {}".format(room))
        
print("The sum of the sector IDs is {}".format(totalSectorSum))