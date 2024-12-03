import os
import sys

f = open("input.txt", "r")
data = f.readlines()

l_data=[]
r_data=[]

for line in data:
    l_data.append(int(line.split()[0]))
    r_data.append(int(line.split()[1]))

l_data.sort()
r_data.sort()

s=0

for i in range(len(l_data)):
    s+=abs(l_data[i]-r_data[i])

print(s)
