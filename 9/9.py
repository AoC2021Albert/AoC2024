#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


f = open('9/in.raw', 'r')
#f = open('9/sample.raw', 'r')
lines = f.read().splitlines()

line = lines[0]
assert (len(line) % 2 == 1)


def sorted_disk_blocks(line):
    left_block_num = 0
    right_block_num = len(line)//2
    left_i = 0
    right_i = len(line)-1
    right_block_left = int(line[right_i])
    left_block_left = int(line[left_i])
    while left_block_num < right_block_num:
        while left_block_left > 0:
            yield (left_block_num)
            left_block_left -= 1
        left_i += 1
        left_space = int(line[left_i])
        left_block_num += 1
        while left_space > 0 and left_block_num < right_block_num:
            while right_block_left > 0 and left_space > 0:
                yield (right_block_num)
                right_block_left -= 1
                left_space -= 1
            if right_block_left == 0:
                right_block_num -= 1
                right_i -= 2  # I don't care about empty at the end
                right_block_left = int(line[right_i])
        if left_block_num == right_block_num:
            while right_block_left > 0:
                yield (right_block_num)
                right_block_left -= 1
        left_i += 1
        left_block_left = int(line[left_i])


def sorted_files(line):
    res = 0

    POS = 0
    LONG = 1
    ID = 2
    spaces = []

    current_pos = 0
    current_id = 0
    file_long = int(line[0])
    files = [[0, file_long, current_id]]
    current_pos += file_long
    for i in range(1, len(line), 2):
        space_long = int(line[i])
        spaces.append([current_pos, space_long])
        current_pos += space_long
        file_long = int(line[i+1])
        current_id += 1
        files.append([current_pos, file_long, current_id])
        current_pos += file_long
    spaces.append([current_pos, 0])  # don't like bound checking...
    for i in range(1, len(files)):
        file = files[-i]
        file_long = file[LONG]
        dest_space = 0
        while spaces[dest_space][POS] < file[POS] and spaces[dest_space][LONG] < file_long:
            dest_space += 1
        if spaces[dest_space][POS] < file[POS]:
            files[-i][POS] = spaces[dest_space][POS]
            spaces[dest_space][POS] += file_long
            spaces[dest_space][LONG] -= file_long
        # file is in its final position
        for i in range(file_long):
            res += (file[POS]+i)*file[ID]
    return (res)


res = 0
for pos, num_block in enumerate(sorted_disk_blocks(line)):
    res += pos*num_block
print(res)
print(sorted_files(line))
