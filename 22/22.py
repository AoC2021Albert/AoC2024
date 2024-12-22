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