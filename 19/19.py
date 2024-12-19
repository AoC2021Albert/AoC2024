#!/usr/bin/env python
from functools import cache


f = open('19/in.raw', 'r')
# f = open('19/sample.raw', 'r')
lines = f.read().splitlines()

available_patterns = lines[0].split(', ')


@cache
def solve(line):
    if len(line) == 0:
        return (1)
    res = 0
    for pattern in available_patterns:
        if line.startswith(pattern):
            res += solve(line[len(pattern):])
    return (res)


res = 0
res2 = 0
for line in lines[2:]:
    ways = solve(line)
    if ways > 0:
        res += 1
    res2 += ways
    print(ways, line)
print(res, res2)
