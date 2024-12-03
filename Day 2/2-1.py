import os
import sys

f = open("input.txt", "r")
data = [list(map(int, line.split())) for line in f.readlines()]

count=0

for report in data:
    if sorted(report) == report or sorted(report, reverse=True) == report:
        count += 1
        for i in range(len(report)-1):
            diff = abs(report[i] - report[i+1])
            if not(diff >= 1 and diff <= 3):
                count -= 1
                break

print(count)
