#!/usr/bin/env python
from collections import defaultdict

f = open('8/in.raw', 'r')
# f = open('8/sample.raw', 'r')
lines = f.read().splitlines()

MAXY = len(lines)
MAXX = len(lines[0])

M = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            M[c].append(x+y*1j)


def pair_antinodes(ans, a, b):
    for an in [a+(a-b), b+(b-a)]:
        print((a-b))
        if an.real in range(0, MAXX) and an.imag in range(0, MAXY):
            ans[0].add(an)
    for start, inc in ((a, (a-b)), (b, (b-a))):
        an = start
        while an.real in range(0, MAXX) and an.imag in range(0, MAXY):
            ans[1].add(an)
            an += inc


def all_antinodes(ans, l):
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            pair_antinodes(ans, l[i], l[j])


ans = [set(), set()]
for freq, l in M.items():
    all_antinodes(ans, l)
print(len(ans[0]), len(ans[1]))
