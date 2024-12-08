import os
import sys
from itertools import product
f = open("input.txt", "r")
input_text = list(filter(None, f.read().split('\n')))

test_value = []
operands = []

for eq in input_text:
    eq = eq.split(':')
    test_value.append(int(eq[0]))
    operands.append(tuple(map(int,list(filter(None, eq[1].split(' '))))))

s = 0

for i in range(len(test_value)):
    operations = list(product([lambda x,y: x*y, lambda x,y: x+y],repeat = len(operands[i])-1))
    for operation in operations:
        res = operands[i][0]
        for j in range(len(operation)):
            res = operation[j](res,operands[i][j+1])
        if res == test_value[i]:
            s += res
            break

print(s)
