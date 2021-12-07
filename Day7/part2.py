#Definitely the right solution, mathematical explanation follows soon.

from statistics import mean
from math import ceil


def fuel_consumption(data, middle):
    return sum(
        [(abs(position - middle) ** 2 + abs(position-middle)) // 2
         for position in data]
    )


with open('Day7/input.txt') as f:
    data = [int(value) for value in f.readlines()[0].rstrip().split(',')]

print(min(
    fuel_consumption(data, ceil(mean(data))),
    fuel_consumption(data, int(mean(data)))
))
