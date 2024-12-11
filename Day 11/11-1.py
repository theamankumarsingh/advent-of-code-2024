import os
import sys

f = open("input.txt", "r")
input_text = list(map(int,list(f.read().split())))

arr = input_text
n_blinks = 25

for n in range(n_blinks):
    new_arr = []
    for ele in arr:
        if ele == 0:
            new_arr.append(1)
        elif len(str(ele)) % 2 == 0:
            new_arr.append(int(str(ele)[:len(str(ele))//2]))
            new_arr.append(int(str(ele)[len(str(ele))//2:]))
        else:
            new_arr.append(ele*2024)
    arr = new_arr

print(len(arr))
