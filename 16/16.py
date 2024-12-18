#!/usr/bin/env python
import math
import sys


f = open('16/in.raw', 'r')
# f = open('16/sample2.raw', 'r')
lines = f.read().splitlines()
sys.setrecursionlimit(len(lines)*len(lines[0]))

M = lines
OPT = [[[math.inf, math.inf, math.inf, math.inf]
        for _ in range(len(M[0]))] for _ in range(len(M))]

dir_idx = {1: 0, -1: 1, 1j: 2, -1j: 3}
inv_idx = [k for k in dir_idx]


def solve(p, score, dir, M, OPT):
    if M[int(p.imag)][int(p.real)] == '#':
        return
    if OPT[int(p.imag)][int(p.real)][dir_idx[dir]] <= score:
        return
    OPT[int(p.imag)][int(p.real)][dir_idx[dir]] = score
    solve(p+dir, score+1, dir, M, OPT)
    new_dir = dir*1j
    solve(p+new_dir, score+1001, new_dir, M, OPT)
    new_dir = dir*-1j
    solve(p+new_dir, score+1001, new_dir, M, OPT)


def solve2(p, score, dir, OPT, res):
    for arrival in OPT[int(p.imag)][int(p.real)]:
        if arrival == score:
            res.add(p)
            for possible_previous in [(p-dir, score-1, dir),
                                      (p-dir*1j, score-1, dir*1j),
                                      (p+dir*1j, score-1, -dir*1j),
                                      (p-dir, score-1001, dir),
                                      (p-dir*1j, score-1001, dir*1j),
                                      (p+dir*1j, score-1001, -dir*1j),
                                      ]:
                solve2(
                    possible_previous[0], possible_previous[1], possible_previous[2], OPT, res)


# PART1
p = (len(M)-2)*1j+1
solve(p, 0, 1, M, OPT)
solve(p, 1000, -1j, M, OPT)
res1 = min(OPT[1][-2])
print(res1)

# PART2
res2 = set()
solve2(1j+len(M[0])-2, res1, 1, OPT, res2)
solve2(1j+len(M[0])-2, res1, -1j, OPT, res2)
print(len(res2))
