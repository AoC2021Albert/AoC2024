#!/usr/bin/env python
f = open('15/in.raw', 'r')
# f = open('15/sample.raw', 'r')
lines = f.read().splitlines()
TALL = lines.index('')
WIDE = len(lines[0])
MOVE = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
VIEW = True
walls = []
boxes = []
# w_ prefix is for Wide on second part
w_walls = []
w_boxes = []
# Read input map
for y in range(TALL):
    for x, c in enumerate(lines[y]):
        if c == '#':
            walls.append(x+y*1j)
            w_walls += [x*2+y*1j, x*2+1+y*1j]
        elif c == 'O':
            boxes.append(x+y*1j)
            w_boxes += [x*2+y*1j, x*2+1+y*1j]
        elif c == '@':
            initial_p = x+y*1j
        else:
            assert (c == '.')
# Read moves
moves = []
for i in range(TALL+1, len(lines)):
    moves += list(lines[i])

# START PART 1
p = initial_p
if VIEW:
    print("\033[?25l", end="")  # hide cursor
    print("\033[2J\033[H", end="")  # clear screen
for move in moves:
    dir = MOVE[move]
    new_p = p+dir
    if new_p not in walls+boxes:
        p = new_p
    else:
        while new_p in boxes:
            new_p += dir
        if new_p not in walls:
            new_p -= dir
            while new_p in boxes:
                boxes[boxes.index(new_p)] += dir
                new_p -= dir
            p += dir
    if VIEW:
        screen = f"\033[1;1H"
        for y in range(TALL):
            for x in range(WIDE):
                pos = x+y*1j
                if pos in boxes:
                    c = 'O'
                elif pos in walls:
                    c = '#'
                elif pos == p:
                    c = '@'
                else:
                    c = '.'
                screen += c
            screen += "\n"
        print(screen, end="")
if VIEW:
    print("\033[?25h", end="")  # show cursor
    print(f"\033[{TALL+1};{1}H#", end="")  # move cursor to the bottom

print(sum(abs(box.imag) * 100 + abs(box.real) for box in boxes))

if VIEW:
    input("Press Enter for part 2")

# START PART 2


def move_boxes_v(p, dir, w_walls, w_boxes, do_move):
    new_p = p+dir
    if new_p in w_walls:
        return False
    if new_p in w_boxes:
        first_box_idx = w_boxes.index(new_p)
        second_box_idx = first_box_idx ^ 1  # xor 1 to get the other box side
        if (move_boxes_v(new_p, dir, w_walls, w_boxes, do_move) and
                move_boxes_v(w_boxes[second_box_idx], dir, w_walls, w_boxes, do_move)):
            if do_move:
                w_boxes[first_box_idx] += dir
                w_boxes[second_box_idx] += dir
        else:
            return False
    return True


if VIEW:
    print("\033[?25l", end="")  # hide cursor
    print("\033[2J\033[H", end="")  # clear screen
p = initial_p + initial_p.real  # double the x coordinate
for move in moves:
    dir = MOVE[move]
    new_p = p+dir
    if new_p not in w_walls+w_boxes:
        p = new_p
    else:
        if dir.imag == 0:  # same as before
            while new_p in w_boxes:
                new_p += dir
            if new_p not in w_walls:
                new_p -= dir
                while new_p in w_boxes:
                    w_boxes[w_boxes.index(new_p)] += dir
                    new_p -= dir
                p += dir
        else:  # vertical gets more complicated
            if move_boxes_v(p, dir, w_walls, w_boxes, False):
                move_boxes_v(p, dir, w_walls, w_boxes, True)
                p = new_p
    if VIEW:
        screen = f"\033[1;1H"
        left_box = True
        for y in range(TALL):
            for x in range(WIDE * 2):
                pos = x + y * 1j
                if pos in w_boxes:
                    c = '[' if left_box else ']'
                    left_box = not left_box
                elif pos in w_walls:
                    c = '#'
                elif pos == p:
                    c = '@'
                else:
                    c = '.'
                screen += c
            screen += "\n"
        print(screen, end="")

if VIEW:
    print("\033[?25h", end="")  # show cursor
    print(f"\033[{TALL+1};{1}H#", end="")

print(sum(abs(box.imag) * 100 + abs(box.real) for box in w_boxes[::2]))
