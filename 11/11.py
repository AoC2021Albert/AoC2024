#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce, cache
from operator import mul
import re
import math
from copy import deepcopy
import datetime


f = open('11/in.raw', 'r')
# f = open('11/sample.raw', 'r')
lines = f.read().splitlines()

stones=list(map(int,lines[0].split(" ")))
print(stones)


@cache
def evolve(stone, loop):
    if loop==0:
        return(1)
    res=0
    if stone==0:
        res=evolve(1,loop-1)
    elif len(sstone:=str(stone))%2==0:
        L=len(sstone)//2
        res+=evolve(int(sstone[:L]),loop-1)
        res+=evolve(int(sstone[L:]),loop-1)
    else:
        res+=evolve(stone*2024,loop-1)
    return(res)

res=0
for stone in stones:
    res+=evolve(stone,75)
print(res)


