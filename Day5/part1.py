import re
from collections import defaultdict

with open('Day5/input.txt') as f:
    data = [re.split('->|,', value.rstrip().replace(' ', ''))
            for value in f.readlines()]

#helper functions
def draw_line(x1, y1, x2, y2):
    if x1 == x2:
        if int(y1) > int(y2):
            return ((int(x1), y) for y in range(int(y2), int(y1)+1))
        else:
            return ((int(x1), y) for y in range(int(y1), int(y2)+1))
    elif y1 == y2:
        if int(x1) > int(x2):
            return ((x, int(y1)) for x in range(int(x2), int(x1)+1))
        else:
            return ((x, int(y1)) for x in range(int(x1), int(x2)+1))
    else:
        return ()


#all  targeted points
points = defaultdict(int)

for d in data:
    for point in draw_line(*d):
        points[point] += 1

print(sum(value > 1 for value in points.values()))
