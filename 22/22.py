#!/usr/bin/env python
from collections import defaultdict
import math
f = open('22/in.raw', 'r')
lines = f.read().splitlines()


p1 = 0
diffseq_value = defaultdict(int)
for num in map(int, lines):
    diffseq = []
    prev_value = math.inf
    local_diffseq_value = dict()
    for _ in range(2000):
        num ^= num << 6
        num %= (1 << 24)
        num ^= num >> 5
        num %= (1 << 24)
        num ^= num << 11
        num %= (1 << 24)
        value = num % 10
        diff = value - prev_value
        diffseq.append(diff)
        if tuple(diffseq[-4:]) not in local_diffseq_value:
            local_diffseq_value[tuple(diffseq[-4:])] = value
        prev_value = value
    for k, v in local_diffseq_value.items():
        diffseq_value[k] += v
    p1 += num
print(p1)

print(sorted([v for k, v in diffseq_value.items()
      if len(k) == 4 and k[0] != math.inf])[-1])
