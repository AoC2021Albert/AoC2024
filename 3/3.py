#!/usr/bin/env python
import re

f = open('3/in.raw', 'r')
s = f.read()

res = 0
for m in re.findall(r'mul\([0-9]+,[0-9]+\)', s):
    a, b = list(map(int, m[4:-1].split(',')))
    res = res+a*b
print(res)


res = 0
d = True
for m in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s):
    if m == "do()":
        d = True
    elif m == "don't()":
        d = False
    else:
        if d:
            a, b = list(map(int, m[4:-1].split(',')))
            res = res+a*b
print(res)
