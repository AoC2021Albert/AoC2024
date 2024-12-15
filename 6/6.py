#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('6/in.raw', 'r')
f = open('6/sample.raw', 'r')
lines = f.read().splitlines()

DIRECTIONS = (-1j,1,1j,-1)
m = ['@'*(len(lines[0])+2)]
for y, line in enumerate(lines):
    new_line = line
    for x, c in enumerate(line):
        if line[x] == '^':
            new_line=new_line[:x]+'.'+new_line[x+1:]
            INITIAL_GUARD=x+1+(y+1)*1j
            guard=INITIAL_GUARD
            guard_dir = 0
    m.append('@'+new_line+'@')
m.append('@'*(len(lines[0])+2))

def check_loop(m,guard,guard_dir, visited_with_dir_orig):
    visited_with_dir=deepcopy(visited_with_dir_orig)
    guard_dir = (guard_dir+1)%4
    while True:
        new_guard=guard+DIRECTIONS[guard_dir]
        match m[int(new_guard.imag)][int(new_guard.real)]:
            case '@':
                return(False)
            case '#':
                guard_dir = (guard_dir + 1) % len(DIRECTIONS)
            case '.':
                guard = new_guard
                if guard_dir in visited_with_dir[guard]:
                    return(True)
                visited_with_dir[guard].add(guard_dir)
            case _:
                exit(1)


visited=set([guard])
visited_with_dir=defaultdict(set)
makes_loops=set()
while True:
    new_guard=guard+DIRECTIONS[guard_dir]
    match m[int(new_guard.imag)][int(new_guard.real)]:
        case '@':
            break
        case '#':
            guard_dir = (guard_dir + 1) % len(DIRECTIONS)
        case '.':
            if new_guard!=INITIAL_GUARD and check_loop(m,guard,guard_dir, visited_with_dir):
                makes_loops.add(new_guard)
            guard = new_guard
            visited.add(guard)
            visited_with_dir[guard].add(guard_dir)
        case _:
            exit(1)
print(len(visited))
print(len(makes_loops))
'''
loops=0
for pos, dirs in visited_with_dir.items():
    for dir in dirs:
        if (dir+1)%len(DIRECTIONS) in dirs:
            block_pos = pos+DIRECTIONS[dir]
            if m[int(block_pos.imag)][int(block_pos.real)] !='@':
                loops+=1
                print(pos+DIRECTIONS[dir])
print(loops)
#5511
#1634
#1582
'''