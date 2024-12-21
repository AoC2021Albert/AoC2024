#!/usr/bin/env python
from functools import cache
import math


f = open('21/in.raw', 'r')
# f = open('21/sample.raw', 'r')
lines = f.read().splitlines()

DIR = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
NUMKEYPAD = [['7', '8', '9'],
             ['4', '5', '6'],
             ['1', '2', '3'],
             ['X', '0', 'A']]
DIRKEYPAD = [['X', '^', 'A'],
             ['<', 'v', '>']]
INVALID = {}

KNUMS = {}
for y, row in enumerate(NUMKEYPAD):
    for x, val in enumerate(row):
        KNUMS[val] = y*1j+x
        if val == 'X':
            INVALID['numeric'] = y*1j+x

KDIRS = {}
for y, row in enumerate(DIRKEYPAD):
    for x, val in enumerate(row):
        KDIRS[val] = y*1j+x
        if val == 'X':
            INVALID['direction'] = y*1j+x


def valid_path(a, path, kind):
    p = a
    for step in path:
        p += DIR[step]
        if p == INVALID[kind]:
            return False
    return True


def sign(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


@cache
def path_len(a, b, kind, depth):
    match sign(a.real, b.real):
        case 0:
            hor = ''
        case 1:
            hor = '<'*int(abs(a.real-b.real))
        case -1:
            hor = '>'*int(abs(a.real-b.real))
    match sign(a.imag, b.imag):
        case 0:
            ver = ''
        case 1:
            ver = '^'*int(abs(a.imag-b.imag))
        case -1:
            ver = 'v'*int(abs(a.imag-b.imag))
    min_path = math.inf
    for path in ('A'+hor+ver+'A', 'A'+ver+hor+'A'):
        if valid_path(a, path[1:-1], kind):
            if depth == 0:
                min_path = min(min_path, len(path)-1)
            else:
                min_path = min(min_path, sum(path_len(
                    KDIRS[path[i]], KDIRS[path[i+1]], 'direction', depth-1) for i in range(len(path)-1)))
    return min_path


def solve(lines, depth):
    res = 0
    for path in lines:
        value = int(path[:-1])
        ext_path = 'A'+path
        path_lens = [path_len(KNUMS[ext_path[i]], KNUMS[ext_path[i+1]],
                              'numeric', depth) for i in range(len(ext_path)-1)]
        len_path = sum(path_lens)
        res += value * len_path
    return res


print(solve(lines, 2))
print(solve(lines, 25))
