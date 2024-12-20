#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('20/in.raw', 'r')
#f = open('20/sample.raw', 'r')
lines = f.read().splitlines()

M=[]
for y, line in enumerate(lines):
    if "S" in line:
        start = y*1j + line.index("S")
        line = line.replace("S", ".")
    if "E" in line:
        end = y*1j + line.index("E")
        line = line.replace("E", ".")
    M.append(list(line))

p=start
path=[p]
while p!=end:
    for d in [1,1j,-1,-1j]:
        new_p = p+d
        if M[int(new_p.imag)][int(new_p.real)]==".":
            assert path[-1] == p # The path has to be unique
            path.append(p+d)
    M[int(p.imag)][int(p.real)]="#"
    p=path[-1]

#print(path)

# part 1
shortcuts = []
for steps, p in enumerate(path[:-2]):
    for d1 in (1,1j,-1,-1j):
        if p+d1 not in (path[steps-1],path[steps+1]):
            for d2 in (d2c for d2c in (1,1j,-1,-1j) if d2c!=-d1):
                try:
                    if (SAVE:=path.index(p+d1+d2)-steps-2) > 0:
                        shortcuts.append((SAVE,p,d1,d2))
                except:
                    pass

print(sorted(shortcuts,key=lambda x: x[0]))
print(len(list(x for x in shortcuts if x[0] >= 100)))
exit()
# part 2
def add_cheats(cheats, p, depth):
    if depth == 0:
        return
    for d in (1,1j,-1,-1j):
        cheats.add(p+d)
        add_cheats(cheats, _p:=p+d, depth-1)

cheats = set()
add_cheats(cheats,0,20)
for i in range(20):
    for _ in range(i):
        for d in (1,1j,-1,-1j):
            if p+d in path:
                p+=d

