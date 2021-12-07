from statistics import median

with open('Day7/input.txt') as f:
    data = [int(value) for value in f.readlines()[0].rstrip().split(',')]

middle = int(median(data))

print(sum([abs(position - middle) for position in data]))
