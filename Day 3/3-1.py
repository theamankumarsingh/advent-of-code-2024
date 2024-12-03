import os
import sys
import re

f = open("input.txt", "r")
input_text = f.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

match = re.findall(pattern, input_text)

s = 0
for m in match:
    s += int(m[0]) * int(m[1])

print(s)
