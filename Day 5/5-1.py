import os
import sys

f = open("input.txt", "r")
input_text = f.read().split('\n\n')

rules = input_text[0].split('\n')
dataset = list(filter(None, input_text[1].split('\n')))

rules_dict = {}

for rule in rules:
    key, value = rule.split('|')
    if key not in rules_dict:
        rules_dict[key] = []
    rules_dict[key].append(value)

s = 0

for data in dataset:
    data = data.split(',')
    flag = True
    prev_values = []

    for d in data:
        if d in rules_dict:
            common_set = set(rules_dict[d]).intersection(set(prev_values))
            if len(common_set) != 0:
                flag = False
                break
        prev_values.append(d)

    if flag:
        s += int(data[len(data)//2])

print(s)
