import os
import sys

f = open("input.txt", "r")
input_text = list(map(int,list(f.read().split()[0])))

disk = []
file_id = 0
for i in range(len(input_text)):
    if i%2:
        disk += ['.']*input_text[i]
    else:
        disk += [file_id]*input_text[i]
        file_id += 1

start = 0
end = len(disk) - 1

while start < end and start < len(disk) and end >= 0:
    if disk[end] == '.':
        end -= 1
        continue
    if disk[start] != '.':
        start += 1
        continue
    disk[start], disk[end] = disk[end], disk[start]

checksum = sum([disk[i]*i for i in range(len(disk)) if disk[i] != '.'])
print(checksum)
