#!/usr/bin/env python
f = open('4/in.raw', 'r')
lines = f.read().splitlines()

m = ['#'*(len(lines[0])+2)]
for line in lines:
    m.append('#'+line+'#')
m.append('#'*(len(lines[0])+2))


def xmas(m, y, x):
    res = 0
    for d in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        if m[y+1*d[0]][x+1*d[1]] == "M":
            if m[y+2*d[0]][x+2*d[1]] == "A":
                if m[y+3*d[0]][x+3*d[1]] == "S":
                    res += 1
    return (res)


def masx(m, y, x):
    res = 0
    if m[y+1][x+1]+m[y-1][x-1] in ('MS', 'SM'):
        if m[y+1][x-1]+m[y-1][x+1] in ('MS', 'SM'):
            res += 1
    return (res)


p1 = 0
p2 = 0
for y in range(1, len(m)-1):
    for x in range(1, len(m[0])-1):
        if m[y][x] == 'X':
            p1 += xmas(m, y, x)
        if m[y][x] == 'A':
            p2 += masx(m, y, x)
print(p1, p2)
