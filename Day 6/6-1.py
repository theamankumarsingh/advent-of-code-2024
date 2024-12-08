import os
import sys

f = open("input.txt", "r")
input_text = list(filter(None, f.read().split('\n')))
input_map = [list(s) for s in input_text]
visited_map = [[False for _ in range(len(input_map[0]))] for _ in range(len(input_map))]

direction_orientation = ['^', '>', 'v', '<']
position = next(((i, row.index(x)) for i, row in enumerate(input_map) for x in row if x in direction_orientation), None)
direction = direction_orientation.index(input_map[position[0]][position[1]])
input_map[position[0]][position[1]] = '.'
visited_map[position[0]][position[1]] = True

exit_flag = False

while not exit_flag:
    match direction:
        case 0:
            new_position = (position[0] - 1, position[1])
            if input_map[new_position[0]][new_position[1]] == '#':
                direction += 1
            elif input_map[new_position[0]][new_position[1]] == '.':
                position = new_position
        case 1:
            new_position = (position[0], position[1] + 1)
            if input_map[new_position[0]][new_position[1]] == '#':
                direction += 1
            elif input_map[new_position[0]][new_position[1]] == '.':
                position = new_position
        case 2:
            new_position = (position[0] + 1, position[1])
            if input_map[new_position[0]][new_position[1]] == '#':
                direction += 1
            elif input_map[new_position[0]][new_position[1]] == '.':
                position = new_position
        case 3:
            new_position = (position[0], position[1] - 1)
            if input_map[new_position[0]][new_position[1]] == '#':
                direction = 0
            elif input_map[new_position[0]][new_position[1]] == '.':
                position = new_position

    if position[0] == 0 or position[0] == len(input_map) - 1 or position[1] == 0 or position[1] == len(input_map[0]) - 1:
        exit_flag = True
    visited_map[position[0]][position[1]] = True

print(sum(row.count(True) for row in visited_map))
