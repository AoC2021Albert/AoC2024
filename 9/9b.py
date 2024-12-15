#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('9/in.raw', 'r')
#f = open('9/sample.raw', 'r')
lines = f.read().splitlines()

line=lines[0]+'0'

M=[]
id=0
for i in range(0,len(line),2):
    for j in range(int(line[i])):
        M.append(id)
    id+=1
    for j in range(int(line[i+1])):
        M.append(-1) #space

head=0
tail=len(M)-1
res=0
while head<=tail:
    if M[head]==-1:
        while M[tail]==-1:
            tail -=1
        v=M[tail]
        tail-=1
    else:
        v=M[head]
    if head<=tail:
        res+=v*head
    head+=1
print(res)


