#!/usr/bin/env python
lines = open('20/in.raw', 'r').read().splitlines()

start = [y*1j + x for y, line in enumerate(lines)
         for x, c in enumerate(line) if c == "S"][0]
end = [y*1j + x for y, line in enumerate(lines)
       for x, c in enumerate(line) if c == "E"][0]

p = start
path = [p]
while p != end:
    p = [p+d for d in [1, 1j, -1, -1j]
         if p+d != path[-2:][0] and
         lines[int(p.imag+d.imag)][int(p.real+d.real)] != "#"][0]
    path.append(p)


def solve(path, picoseconds, minimum_saved):
    res = 0
    for steps, cheat_start in enumerate(path[:-picoseconds]):
        for extra_steps, cheat_end in enumerate(path[steps+1:]):
            cheat = cheat_end-cheat_start
            rectilinear_distance = abs(cheat.real)+abs(cheat.imag)
            if rectilinear_distance <= picoseconds and \
               extra_steps + 1 - rectilinear_distance >= minimum_saved:
                res += 1
    return (res)


# part 1
print(solve(path, 2, 100))
# part 2
print(solve(path, 20, 100))
