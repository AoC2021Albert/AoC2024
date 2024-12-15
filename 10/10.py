#!/usr/bin/env python
f = open('10/in.raw', 'r')
# f = open('10/sample.raw', 'r')
lines = f.read().splitlines()

M = [[11]*(len(lines[0])+2)]
for y, line in enumerate(lines):
    M.append([11]+[int(c) for c in line]+[11])
M.append([11]*(len(lines[0])+2))


def follow_trail(M, p, res):
    v = M[int(p.imag)][int(p.real)]
    if v == 9:
        res[0].add(p)
        res[1] += 1
    for d in (1, -1, 1j, -1j):
        np = p+d
        nv = M[int(np.imag)][int(np.real)]
        if nv == v+1:
            follow_trail(M, np, res)


def trail_score(M, y, x):
    v = M[y][x]
    if v != 0:
        return (0, 0)
    p = x+y*1j
    res = [set(), 0]
    follow_trail(M, p, res)
    return (len(res[0]), res[1])


p1 = 0
p2 = 0
for y in range(1, len(M)-1):
    for x in range(1, len(M[0])-1):
        pp1, pp2 = trail_score(M, y, x)
        p1 += pp1
        p2 += pp2
print(p1, p2)
