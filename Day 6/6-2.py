import os
import sys

def map_simulation(input_map):
    visited_map = [[False for _ in range(len(input_map[0]))] for _ in range(len(input_map))]
    direction_orientation = ['^', '>', 'v', '<']
    position = next(((i, row.index(x)) for i, row in enumerate(input_map) for x in row if x in direction_orientation), None)
    initial_position = position
    direction = direction_orientation.index(input_map[position[0]][position[1]])
    initial_direction = direction
    input_map[position[0]][position[1]] = '.'
    visited_map[position[0]][position[1]] = True
    visited_nodes_with_direction = set()
    exit_flag = False
    loop_flag = False

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
        if (position, direction) in visited_nodes_with_direction:
            exit_flag = True
            loop_flag = True
        if position[0] == 0 or position[0] == len(input_map) - 1 or position[1] == 0 or position[1] == len(input_map[0]) - 1:
            exit_flag = True
            loop_flag = False
        visited_map[position[0]][position[1]] = True
        visited_nodes_with_direction.add((position, direction))
    input_map[initial_position[0]][initial_position[1]] = direction_orientation[initial_direction]
    return visited_map, loop_flag

f = open("input.txt", "r")
input_text = list(filter(None, f.read().split('\n')))
input_map = [list(s) for s in input_text]

visited_map, loop_flag = map_simulation(input_map)

total_obstruction_points = 0
for i in range(len(visited_map)):
    for j in range(len(visited_map[0])):
        if visited_map[i][j] and input_map[i][j] == '.':
            input_map[i][j] = '#'
            v,l = map_simulation(input_map)
            total_obstruction_points += 1 if l else 0
            input_map[i][j] = '.'

print(total_obstruction_points)
