#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('1/in.raw', 'r')
# f = open('sample.raw', 'r')
lines = f.read().splitlines()
l1=[]
l2=[]
for line in lines:
    a,b=list(map(int,line.split('   ')))
    l1.append(a)
    l2.append(b)

l1.sort()
l2.sort()

res=0
for i in range(len(lines)):
    res+=abs(l1[i]-l2[i])
print(res)

valid=set(l1)
res=0
for v in l2:
    if v in valid:
        res+=v
print(res)