#!/usr/bin/env python

import collections
import logging
import random

d8 = random.randrange(8)
d12 = random.randrange(12)
d20 = random.randrange(20)

def backrow(d8,d12,d20):
    logging.debug((d8,d12,d20))
    logging.debug('01234567')
    row = ['_'] * 8
    row[d8] = 'Q'
    logging.debug(''.join(row))
    if d8&1:
        row[2*(d12%4)] = 'B'
        logging.debug(''.join(row))
        pos = 2*(d12%3)+1
        if pos >= d8:
            pos += 2
        row[pos] = 'B'
        logging.debug(''.join(row))
    else:
        row[2*(d12%4)+1] = 'B'
        logging.debug(''.join(row))
        pos = 2*(d12%3)
        if pos >= d8:
            pos += 2
        row[pos] = 'B'
        logging.debug(''.join(row))
    L = [-1]*8
    acc = 0
    for i in range(8):
        if row[i] == '_':
            L[i] = acc
            acc += 1
    pos = d20%5
    for i in range(8):
        if L[i] == pos:
            row[i] = 'N'
    logging.debug(''.join(row))
    L = [-1]*8
    acc = 0
    for i in range(8):
        if row[i] == '_':
            L[i] = acc
            acc += 1
    pos = d20%4
    for i in range(8):
        if L[i] == pos:
            row[i] = 'N'
    logging.debug(''.join(row))

    acc = 0
    for i in range(8):
        if row[i] == '_':
            if acc&1:
                row[i] = 'K'
            else:
                row[i] = 'R'
            acc += 1
            logging.debug(''.join(row))
    return row

# logging.basicConfig(level=logging.DEBUG)
print(backrow(d8,d12,d20))

d = {}
d['Q'] = [0]*8
d['K'] = [0]*8
d['N'] = [0]*8
d['B'] = [0]*8
d['R'] = [0]*8

left = collections.defaultdict(int)

for i in range(960):
    d8  = i%8
    d12 = i%12
    d20 = i%20
    row = backrow(d8,d12,d20)
    for i in range(8):
        d[row[i]][i] += 1
        if row[i] == 'K' and i<4:
            left[row[i+4]] += 1
print(d)
print(left)
