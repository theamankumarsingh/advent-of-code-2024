import os
import sys

f = open("input.txt", "r")
input_text = list(map(int,list(f.read().split())))

arrdict = {x:input_text.count(x) for x in set(input_text)}
n_blinks = 75

for n in range(n_blinks):
    new_arrdict = {}
    for ele in arrdict.keys():
        if ele == 0:
            new_arrdict[1] = arrdict[ele] if 1 not in new_arrdict.keys() else new_arrdict[1] + arrdict[ele]
        elif len(str(ele)) % 2 == 0:
            new_arrdict[int(str(ele)[:len(str(ele))//2])] = arrdict[ele] if int(str(ele)[:len(str(ele))//2]) not in new_arrdict.keys() else new_arrdict[int(str(ele)[:len(str(ele))//2])] + arrdict[ele]
            new_arrdict[int(str(ele)[len(str(ele))//2:])] = arrdict[ele] if int(str(ele)[len(str(ele))//2:]) not in new_arrdict.keys() else new_arrdict[int(str(ele)[len(str(ele))//2:])] + arrdict[ele]
        else:
            new_arrdict[ele*2024] = arrdict[ele] if ele*2024 not in new_arrdict.keys() else new_arrdict[ele*2024] + arrdict[ele]
    arrdict = new_arrdict

print(sum(arrdict.values()))
