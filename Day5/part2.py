import re
from collections import defaultdict

with open('Day5/input.txt') as f:
    data = [re.split('->|,', value.rstrip().replace(' ', ''))
            for value in f.readlines()]

#helper functions
def draw_line(points):
    x1, y1, x2, y2 = [int(coordinate) for coordinate in points]
    x, y = x1, y1
    result = [(x, y)]
    while x != x2 or y != y2:
        if x1 < x2:
            x += 1
        elif x1 > x2 :
            x -= 1
        if y1 < y2:
            y += 1
        elif y1 > y2 :
            y -= 1
        result.append((x, y))

    return result


#all  targeted points
points = defaultdict(int)

for d in data:
    for point in draw_line(d):
        points[point] += 1

print(sum(value > 1 for value in points.values()))
