#!/usr/bin/env python
f = open('2/in.raw', 'r')
lines = f.read().splitlines()


def is_safe(nums):
    if nums[1]-nums[0] > 0:
        sign = 1
    else:
        sign = -1
    safe = True
    for i in range(1, len(nums)):
        d = (nums[i]-nums[i-1]) * sign
        if d < 1 or d > 3:
            safe = False
    return (safe)


res1 = 0
res2 = 0
for line in lines:
    nums = list(map(int, line.split(' ')))
    if is_safe(nums):
        res1 += 1
        res2 += 1
    else:
        safe = False
        # brute force is good enough and is way simpler
        for i in range(len(nums)):
            safe = safe or is_safe(nums[:i]+nums[i+1:])
        if safe:
            res2 += 1

print(res1, res2)
