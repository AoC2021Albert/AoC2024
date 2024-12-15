#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('15/in.raw', 'r')
#f = open('15/sample2.raw', 'r')
lines = f.read().splitlines()
MAPLINES=lines.index('')
MOVE={'^':-1j,'v':1j,'<':-1,'>':1}

walls=[]
boxes=[]
for y in range(MAPLINES):
    for x, c in enumerate(lines[y]):
        if c == '#':
            walls.append(x+y*1j)
        elif c == 'O':
            boxes.append(x+y*1j)
        elif c == '@':
            p = x+y*1j
        else:
            assert(c == '.')

moves=[]
for i in range(MAPLINES+1,len(lines)):
    moves+=list(lines[i])

#print(len(walls),len(boxes),p)
#print(moves)

for move in moves:
    dir=MOVE[move]
    new_p=p+dir
    if new_p not in walls+boxes:
        p=new_p
    else:
        while new_p in boxes:
            new_p+=dir
        if new_p not in walls:
            new_p-=dir
            while new_p in boxes:
                boxes[boxes.index(new_p)]+=dir
                new_p-=dir
            p+=dir
    #print(dir,p,boxes)
res = 0
for box in boxes:
    res+=abs(box.imag)*100
    res+=abs(box.real)
print(res)
#print(len(walls),len(boxes),p)
#print(boxes)



