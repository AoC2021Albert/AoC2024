#!/usr/bin/env python
f = open('15/in.raw', 'r')
# f = open('15/sample.raw', 'r')
lines = f.read().splitlines()
TALL = lines.index('')
WIDE= len(lines[0])
MOVE = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
VIEW = True
walls = []
w_walls = []
boxes = []
w_boxes = []
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

moves = []
for i in range(TALL+1, len(lines)):
    moves += list(lines[i])

p = initial_p
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
res = 0
for box in boxes:
    res += abs(box.imag)*100
    res += abs(box.real)
print(res)


def move_boxes(p, dir, w_walls, w_boxes, do_move):
    new_p = p+dir
    if new_p in w_walls:
        return False
    if new_p in w_boxes:
        first_box_idx = w_boxes.index(new_p)
        second_box_idx = first_box_idx ^ 1
        if dir.imag == 0:
            if move_boxes(w_boxes[second_box_idx], dir, w_walls, w_boxes, do_move):
                w_boxes[first_box_idx] += dir
                w_boxes[second_box_idx] += dir
        elif (move_boxes(new_p, dir, w_walls, w_boxes, do_move) and
              move_boxes(w_boxes[second_box_idx], dir, w_walls, w_boxes, do_move)):
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
        if dir.imag == 0:
            while new_p in w_boxes:
                new_p += dir
            if new_p not in w_walls:
                new_p -= dir
                while new_p in w_boxes:
                    w_boxes[w_boxes.index(new_p)] += dir
                    new_p -= dir
                p += dir
        else:
            if move_boxes(p, dir, w_walls, w_boxes, False):
                move_boxes(p, dir, w_walls, w_boxes, True)
                p = new_p
    if VIEW:
        left_box = True
        for y in range(TALL):
            for x in range(WIDE*2):
                if x+y*1j in w_boxes:
                    if left_box:
                        c = '['
                    else:
                        c = ']'
                    left_box = not left_box
                elif x+y*1j in w_walls:
                    c = '#'
                elif x+y*1j == p:
                    c = '@'
                else:
                    c = '.'
                print(f"\033[{int(y)+1};{int(x)}H{c}", end="")

if VIEW:
    print("\033[?25h", end="")  # show cursor
    print(f"\033[{51};{1}H#", end="")
res = 0
for box in w_boxes[::2]:
    res += abs(box.imag)*100
    res += abs(box.real)

print(res)
