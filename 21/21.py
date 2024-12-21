#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce, cache
from operator import mul
import re
import math
from copy import deepcopy


f = open('21/in.raw', 'r')
# f = open('21/sample.raw', 'r')
lines = f.read().splitlines()

DIR = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
INVALID = {'numeric': 3j+0,
           'direction': 0}
KNUMS = {'7': 0,
         '8': 1,
         '9': 2,
         '4': 1j,
         '5': 1j+1,
         '6': 1j+2,
         '1': 2j,
         '2': 2j+1,
         '3': 2j+2,
         '0': 3j+1,
         'A': 3j+2}
KDIRS = {'^': 1,
         'A': 2,
         '<': 1j,
         'v': 1j+1,
         '>': 1j+2}


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
def shortest_paths(a, b, kind):
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
    paths = []
    if valid_path(a, hor+ver, kind):
        paths.append(hor+ver+'A')
        # return(frozenset(paths))
    if valid_path(a, ver+hor, kind):
        paths.append(ver+hor+'A')
    return frozenset(paths)


def solve_numeric(line):
    if len(line) == 1:
        return ['']
    else:
        res_paths = []
        curr_paths = shortest_paths(KNUMS[line[0]], KNUMS[line[1]], 'numeric')
        rem_paths = solve_numeric(line[1:])
        for curr_path in curr_paths:
            for rem_path in rem_paths:
                res_paths.append(curr_path+rem_path)
        return res_paths


def solve_direction(line):
    if len(line) == 1:
        return ['']
    else:
        res_paths = set()
        curr_paths = shortest_paths(
            KDIRS[line[0]], KDIRS[line[1]], 'direction')
        rem_paths = solve_direction(line[1:])
        for curr_path in curr_paths:
            for rem_path in rem_paths:
                res_paths.add(curr_path+rem_path)
        return res_paths


def solve_directions(lines):
    res_paths = set()
    for line in lines:
        res_paths = res_paths.union(solve_direction('A'+line))
    return res_paths


def solve(line):
    paths = (solve_directions(solve_directions(solve_numeric('A'+line))))
    return (len(sorted(paths, key=len)[0]))


res = 0
for line in lines:
    value = int(line[:-1])
    path = solve(line)
    print(line, value, path)
    res += value * path
    print(res)

print(res)
