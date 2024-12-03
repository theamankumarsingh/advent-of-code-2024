import os
import sys
import math

f = open("input.txt", "r")
data = [list(map(int, line.split())) for line in f.readlines()]

count=0

for report in data:
    diff_list = [(report[i] - report[i+1]) for i in range(len(report)-1)]
    if all([abs(diff) in [1, 2, 3] for diff in diff_list]) and (all(diff<0 for diff in diff_list) or all(diff>0 for diff in diff_list)):
        count += 1
    else:
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            diff_list = [(new_report[i] - new_report[i+1]) for i in range(len(new_report)-1)]
            if all([abs(diff) in [1, 2, 3] for diff in diff_list]) and (all(diff<0 for diff in diff_list) or all(diff>0 for diff in diff_list)):
                count += 1
                break

print(count)
