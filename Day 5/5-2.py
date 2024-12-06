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
    flag = False

    for i in range(len(data)):
        d = data[i]
        if d in rules_dict:
            common_set = [x for x in data[:i] if x in rules_dict[d]]
            if len(common_set) != 0:
                flag = True
                data = [item for item in data[:i] if item not in common_set] + [d] + common_set + data[i+1:]

    if flag:
        s += int(data[len(data)//2])

print(s)
