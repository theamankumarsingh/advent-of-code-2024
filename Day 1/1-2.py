import os
import sys

f = open("input.txt", "r")
data = f.readlines()

l_data=[]
r_data=[]

for line in data:
    l_data.append(int(line.split()[0]))
    r_data.append(int(line.split()[1]))

s=0

for element in l_data:
    s+=element*r_data.count(element)

print(s)
