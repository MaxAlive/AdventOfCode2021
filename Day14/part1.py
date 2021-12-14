from parse import parse

with open('Day14/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

insertion_rules = [parse('{} -> {}', d) for d in data[data.index('')+1:]]
insertion_rules = {
    key: f'{key[0]}{value}' for key, value in insertion_rules}

polymer = data[0]

for step in range(10):

    new_polymer = ''
    for i in range(len(polymer)-1):
        new_polymer += insertion_rules[polymer[i:i+2]]

    polymer = new_polymer + polymer[-1]

count_dict = {element: polymer.count(element) for element in set(polymer)}
min_count = count_dict[min(count_dict, key=count_dict.get)]
max_count = count_dict[max(count_dict, key=count_dict.get)]

print(max_count - min_count)
