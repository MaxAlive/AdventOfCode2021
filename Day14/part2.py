from parse import parse
from collections import defaultdict

with open('Day14/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

insertion_rules = [parse('{} -> {}', d) for d in data[data.index('')+1:]]
insertion_rules = {
    key: [f'{key[0]}{value}', f'{value}{key[1]}'] for key, value in insertion_rules}

polymer_pairs = {key: 0 for key in insertion_rules}
polymer = data[0]

# original polymer
for i in range(len(polymer)-1):
    polymer_pairs[polymer[i:i+2]] += 1

# insertion
steps = 40
for step in range(steps):
    new_pairs = polymer_pairs.copy()
    for key in polymer_pairs:
        new_pairs[key] -= polymer_pairs[key]
        for pair in insertion_rules[key]:
            new_pairs[pair] += polymer_pairs[key]
    polymer_pairs = new_pairs

element_count = defaultdict(int)

for pair, count in polymer_pairs.items():
    element_count[pair[0]] += count
    element_count[pair[1]] += count

element_count[polymer[0]] += 1
element_count[polymer[-1]] += 1

min_count = element_count[min(element_count, key=element_count.get)] // 2
max_count = element_count[max(element_count, key=element_count.get)] // 2

print(max_count - min_count)
