#!/usr/bin/env python
import math

f = open('12/in.raw', 'r')
lines = f.read().splitlines()
# Surround the map with `#` to avoid boundary-checking
Map = [["#"]*(len(lines[0])+2)]
for line in lines:
    Map.append(["#"]+list(line)+["#"])
Map.append(["#"]*(len(lines[0])+2))

# I use an array for Min/Max Y/X so that I can pass it around
MIN_Y = 0
MAX_Y = 1
MIN_X = 2
MAX_X = 3


def get_plot(Map, point, value, plot, minmax):
    """Recursively get a plot"""
    if Map[int(point.imag)][int(point.real)] == value:
        plot.add(point)
        Map[int(point.imag)][int(point.real)] = '#'
        minmax[MIN_Y] = min(point.imag, minmax[MIN_Y])
        minmax[MAX_Y] = max(point.imag, minmax[MAX_Y])
        minmax[MIN_X] = min(point.real, minmax[MIN_X])
        minmax[MAX_X] = max(point.real, minmax[MAX_X])
        for d in (1, -1, 1j, -1j):
            get_plot(Map, point+d, value, plot, minmax)


def get_fences(plot, minmax):
    """Gets fences (p1) as a real number plus
    sides (p2) as an imaginary number"""
    fences = 0
    sides = 0
    in_plot = False
    old_sides = set()
    for y in range(minmax[MIN_Y], minmax[MAX_Y]+2):
        new_sides = set()
        for x in range(minmax[MIN_X], minmax[MAX_X]+2):
            if y*1j+x in plot:
                if not in_plot:
                    fences += 1
                    new_sides.add(x)
                in_plot = True
            else:
                if in_plot:
                    fences += 1
                    # trick, we add a sign to the "side"
                    # to know if we are going in->out
                    # or out->in
                    new_sides.add(-x)
                in_plot = False
        # Only new sides that were not in the old sides count
        sides += len(new_sides-old_sides)
        old_sides = new_sides
    old_sides = set()
    for x in range(minmax[MIN_X], minmax[MAX_X]+2):
        new_sides = set()
        for y in range(minmax[MIN_Y], minmax[MAX_Y]+2):
            if y*1j+x in plot:
                if not in_plot:
                    fences += 1
                    new_sides.add(y)
                in_plot = True
            else:
                if in_plot:
                    fences += 1
                    new_sides.add(-y)
                in_plot = False
        sides += len(new_sides-old_sides)
        old_sides = new_sides
    return (fences+sides*1j)


def calc_plot(Map, point, value):
    fences = 0
    plot = set()
    minmax = [math.inf, -math.inf, math.inf, -math.inf]
    get_plot(Map, point, value, plot, minmax)
    area = len(plot)
    if area > 0:
        minmax = [int(mm) for mm in minmax]
        fences = get_fences(plot, minmax)
    return (area*fences)


res = 0+0j
for y in range(len(Map)):
    for x in range(len(Map[0])):
        if (value := Map[y][x]) != "#":
            res += calc_plot(Map, y*1j+x, value)
print(res)
