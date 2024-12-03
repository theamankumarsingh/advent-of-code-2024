import os
import sys
import re

f = open("input.txt", "r")
input_text = f.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"

match = re.findall(pattern, input_text)

s = 0
flag=1

for m in match:
    if m[2] == "do":
        flag = 1
        continue
    if m[3] == "don't":
        flag = 0
        continue
    if flag == 1:
        s += int(m[0]) * int(m[1])

print(s)
