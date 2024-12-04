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

matrix =[[''] * (len(matrix[0]) + 2 * 3) for _ in range(3)] + [[''] * 3 + row + [''] * 3 for row in matrix] + [[''] * (len(matrix[0]) + 2 * 3) for _ in range(3)]

s = 0

for i in range(3, r+3):
    for j in range(3, c+3):
        words = [
            matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+3][j],
            matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i][j+3],
            matrix[i][j]+matrix[i-1][j]+matrix[i-2][j]+matrix[i-3][j],
            matrix[i][j]+matrix[i][j-1]+matrix[i][j-2]+matrix[i][j-3],
            matrix[i][j]+matrix[i+1][j+1]+matrix[i+2][j+2]+matrix[i+3][j+3],
            matrix[i][j]+matrix[i-1][j-1]+matrix[i-2][j-2]+matrix[i-3][j-3],
            matrix[i][j]+matrix[i+1][j-1]+matrix[i+2][j-2]+matrix[i+3][j-3],
            matrix[i][j]+matrix[i-1][j+1]+matrix[i-2][j+2]+matrix[i-3][j+3],
        ]
        s+=words.count('XMAS')

print(s)
