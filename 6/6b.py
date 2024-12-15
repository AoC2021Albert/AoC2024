#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('6/in.raw', 'r')
#f = open('6/sample.raw', 'r')
lines = f.read().splitlines()

DIRECTIONS = (-1j,1,1j,-1)
m = [['@']*(len(lines[0])+2)]
for y, line in enumerate(lines):
    new_line = list(line)
    for x, c in enumerate(line):
        if line[x] == '^':
            new_line=new_line[:x]+['.']+new_line[x+1:]
            INITIAL_GUARD=x+1+(y+1)*1j
            guard=INITIAL_GUARD
            guard_dir = 0
    m.append(['@']+new_line+['@'])
m.append(['@']*(len(lines[0])+2))

def check(m,guard,guard_dir):
    visited=defaultdict(set)
    while True:
        visited[guard].add(guard_dir)
        new_guard=guard+DIRECTIONS[guard_dir]
        match m[int(new_guard.imag)][int(new_guard.real)]:
            case '@':
                return(False,visited)
            case '#':
                guard_dir = (guard_dir + 1) % len(DIRECTIONS)
            case '.':
                guard = new_guard
                if guard_dir in visited[guard]:
                    return(True,visited)
                else:
                    visited[guard].add(guard_dir)
            case _:
                exit(1)

loop, visited = check(m,guard,guard_dir)
print(len(visited))
loops=0
for p in visited.keys():
    if p != INITIAL_GUARD:
        m[int(p.imag)][int(p.real)] = '#'
        loop, visited = check(m,guard,guard_dir)
        if loop:
            loops+=1
        m[int(p.imag)][int(p.real)] = "."
print(loops)