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


res = 0
for path in lines:
    print(path)
    value = int(path[:-1])
    ext_path = 'A'+path
    path_lens = [path_len(KNUMS[ext_path[i]], KNUMS[ext_path[i+1]],
                          'numeric', 25) for i in range(len(ext_path)-1)]
    len_path = sum(path_lens)
    res += value * len_path
    print(res)

print(res)
