import os
import sys
import re

f = open("input.txt", "r")
input_text = [x for x in f.read().split('\n') if x]

matrix = []
for line in input_text:
    matrix.append(list(line))

r = len(matrix)
c = len(matrix[0])

matrix =[[''] * (len(matrix[0]) + 2 * 1) for _ in range(1)] + [[''] * 1 + row + [''] * 1 for row in matrix] + [[''] * (len(matrix[0]) + 2 * 1) for _ in range(1)]

s = 0

for i in range(1, r+1):
    for j in range(1, c+1):
        x_shape_words = [matrix[i-1][j-1]+matrix[i][j]+matrix[i+1][j+1],matrix[i+1][j-1]+matrix[i][j]+matrix[i-1][j+1]]
        if (x_shape_words[0]=='MAS' or x_shape_words[0]=='SAM') and (x_shape_words[1]=='MAS' or x_shape_words[1]=='SAM'):
            s+=1

print(s)
