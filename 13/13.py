#!/usr/bin/env python
import re
import math


f = open('13/in.raw', 'r')
f = open('13/sample.raw', 'r')
lines = f.read().splitlines()


def solve(ax, ay, bx, by, fx, fy):
    min_price = math.inf
    # If same slope
    if ax/bx == ay/by:
        # check cheapest that is solveable
        if fx % ax == 0 and fy % ay == 0 and fx//ax == fy//ay:
            min_price = 3 * fx//ax
        if fx % bx == 0 and fy % by == 0 and fx//bx == fy//by:
            min_price = min(min_price, fx//bx)
    else:
        # solve equation
        A = (fx*by - bx*fy)/(ax*by - ay*bx)
        B = (fx*ay - ax*fy)/(bx*ay - by*ax)
        # Make sure it is solveable
        if A % 1 == 0 and B % 1 == 0:
            min_price = 3*A+B
    return (min_price if min_price != math.inf else 0)


res = 0
res2 = 0
i = 0
while i < len(lines):
    ax, ay = list(
        map(int, re.match(r'Button A: X\+(\d+), Y\+(\d+)', lines[i]).groups()))
    bx, by = list(
        map(int, re.match(r'Button B: X\+(\d+), Y\+(\d+)', lines[i+1]).groups()))
    fx, fy = list(
        map(int, re.match(r'Prize: X=(\d+), Y=(\d+)', lines[i+2]).groups()))
    i += 4
    res += solve(ax, ay, bx, by, fx, fy)
    res2 += solve(ax, ay, bx, by, fx+10000000000000, fy+10000000000000)
print(res, res2)
