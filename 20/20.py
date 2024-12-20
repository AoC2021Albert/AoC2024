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

#better part 2
res=0
for steps, cheat_start in enumerate(path[:-2]):
    for extra_steps, cheat_end in enumerate(path[steps+1:]):
        cheat=cheat_end-cheat_start
        euclidean_distance = abs(cheat.real)+abs(cheat.imag)
        if euclidean_distance <= 20 and extra_steps +1 - euclidean_distance >= 100:
            res+=1
print(res)
exit()
 # part 2, also works, but has finished AFTER I've written the better solution
def add_cheats(cheats, p, depth):
    if depth == 0:
        return
    for d in (1,1j,-1,-1j):
        if cheats[p+d] > 20-depth+1:
            cheats[p+d] = 20-depth+1
            add_cheats(cheats, p+d, depth-1)

cheats = defaultdict(lambda: math.inf)
add_cheats(cheats,0,20)
print(cheats)

print(len(path))
shortcuts = []
for steps, p in enumerate(path[:-2]):
    print(steps)
    for d, walked in cheats.items():
        try:
            if (SAVE:=path.index(p+d)-steps-walked) > 0:
                shortcuts.append((SAVE,p,d))
        except:
            pass

print(sorted(shortcuts,key=lambda x: x[0]))
print(len(list(x for x in shortcuts if x[0] >= 100)))

#961805
