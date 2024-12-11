import os
import sys

f_id = open("input.txt", "r")
input_text = list(map(int,list(f_id.read().split()[0])))

disk = []
file_id = 0
file_size = []
for i in range(len(input_text)):
    if i%2:
        disk += ['.']*input_text[i]
    else:
        disk += [file_id]*input_text[i]
        file_id += 1
        file_size.append(input_text[i])

checksum = 0

for f_id in range(file_id -1, -1, -1):
    index = disk.index(f_id)
    count = file_size[f_id]

    disk = disk[:index]
    space_index = next((i for i in range(len(disk) - len(['.']*count) + 1) if disk[i:i+len(['.']*count)] == ['.']*count), None)

    if space_index is not None:
        disk[space_index:space_index+count] = [f_id]*count
        checksum += sum([f_id*(space_index+i) for i in range(count)])
    else:
        checksum += sum([f_id*(index+i) for i in range(count)])

print(checksum)
