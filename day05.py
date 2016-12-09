#!/usr/bin/env python3

# Lets verify some bitcoins!

import hashlib


DOORID = b'ugkcyxxp'

key = []
i = 0

while True:
    hash = hashlib.md5( DOORID + str(i).encode('ascii') ).hexdigest()
    if hash[:5] == '00000':
        key.append(hash[5])
        print ("Found stage {}".format( len(key) ) )
        if len(key) == 8:
            break
    i += 1
            
print ("The password is {}".format(''.join(key) ) )