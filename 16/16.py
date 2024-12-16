#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy
import sys


f = open('16/in.raw', 'r')
#f = open('16/sample.raw', 'r')
lines = f.read().splitlines()
sys.setrecursionlimit(len(lines)*len(lines[0]))

M=lines
OPT=[[[math.inf,math.inf,math.inf,math.inf] for _ in range(len(M[0]))] for _ in range(len(M))]

dir_idx={1:0,-1:1,1j:2,-1j:3}

def solve(p,score,dir,M,OPT):
    if M[int(p.imag)][int(p.real)]=='#':
        return
    if OPT[int(p.imag)][int(p.real)][dir_idx[dir]]<=score:
        return
    OPT[int(p.imag)][int(p.real)][dir_idx[dir]]=score
    solve(p+dir,score+1,dir,M,OPT)
    new_dir=dir*1j
    solve(p+new_dir,score+1001,new_dir,M,OPT)
    new_dir=dir*-1j
    solve(p+new_dir,score+1001,new_dir,M,OPT)

p=(len(M)-2)*1j+1
solve(p,0,1,M,OPT)
solve(p,1000,-1j,M,OPT)
print(min(OPT[1][-2]))
exit()
for y, line in enumerate(OPT):
    for x,c in enumerate(line):
        if c==math.inf:
            print('#',end='')
        else:
            if OPT[y][x-1]==c-1:
                print('<',end='')
            elif OPT[y][x+1]==c-1:
                print('>',end='')
            elif OPT[y-1][x]==c-1:
                print('^',end='')
            elif OPT[y+1][x]==c-1:
                print('v',end='')
            elif OPT[y][x-1]==c-1001:
                print('<',end='')
            elif OPT[y][x+1]==c-1001:
                print('>',end='')
            elif OPT[y-1][x]==c-1001:
                print('^',end='')
            elif OPT[y+1][x]==c-1001:
                print('v',end='')
            else:
                print('?',end='')
    print()

