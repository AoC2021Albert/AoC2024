#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('22/in.raw', 'r')
#f = open('22/sample.raw', 'r')
#f = open('22/sample2.raw', 'r')
lines = f.read().splitlines()

res=0
for num in map(int, lines):
    for _ in range(2000):
        num ^= num << 6
        num %= (1 << 24)
        num ^= num >> 5
        num %= (1 << 24)
        num ^= num << 11
        num %= (1 << 24)
    res+=num
print(res)


res=0
seq_value=defaultdict(int)
for num in map(int, lines):
    ready = False
    seq = []
    prev = math.inf
    local_seq_value=dict()
    for _ in range(2000):
        num ^= num << 6
        num %= (1 << 24)
        num ^= num >> 5
        num %= (1 << 24)
        num ^= num << 11
        num %= (1 << 24)
        value= num %10
        diff = value - prev
        seq.append(diff)
        if tuple(seq[-4:]) not in local_seq_value:
            local_seq_value[tuple(seq[-4:])] = value
        prev = value
    for k,v in local_seq_value.items():
        seq_value[k]+=v
    res+=num
print(res)

print(sorted([v for k,v in seq_value.items() if len(k)==4])[-1])

#7372 too high