import os
import sys

f = open("input.txt", "r")
input_text = list(filter(None, f.read().split('\n')))
input_map = [list(s) for s in input_text]
antinode_map = [[0 for c in r] for r in input_map]

for r in range(len(input_map)):
    for c in range(len(input_map[r])):
        ele = input_map[r][c]
        if ele == "." or ele == "#":
            continue
        for rr in range(len(input_map)):
            for cc in range(len(input_map[rr])):
                ee = input_map[rr][cc]
                if rr == r and cc == c:
                    continue
                if ee == "." or ee == "#":
                    continue
                if ele == ee:
                    dr = rr - r
                    dc = cc - c
                    n = 0
                    while True:
                        if r - n*dr >= 0 and r - n*dr < len(input_map) and c - n*dc >= 0 and c - n*dc < len(input_map[rr]):
                            antinode_map[r - n*dr][c - n*dc] = 1
                        else:
                            break
                        n += 1
                    n = 0
                    while True:
                        if rr + n*dr >= 0 and rr + n*dr < len(input_map) and cc + n*dc >= 0 and cc + n*dc < len(input_map[rr]):
                            antinode_map[rr + n*dr][cc + n*dc] = 1
                        else:
                            break
                        n += 1

count = sum([sum(r) for r in antinode_map])
print(count)
