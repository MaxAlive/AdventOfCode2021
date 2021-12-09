from math import prod

with open('Day9/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

#drawing 9s around the input, to have no edge cases later on
columns = len(data[0])
data = [columns * '9'] + data[:] + [columns * '9']
data = ['9' + d + '9' for d in data]


def isLowPoint(x, y, data):
    current_height = data[x+1][y+1]

    if current_height == '9': return False    
    if data[x+1][y+2] < current_height: return False
    if data[x+2][y+1] < current_height: return False
    if data[x+1][y] < current_height: return False
    if data[x][y+1] < current_height: return False
    
    return True

def getBasinSize(x, y, data):
    explored_points = [(x, y)]
    points_to_explore = {(x+1, y), (x, y+1), (x-1, y), (x, y-1)}
    basin_size = 1

    while points_to_explore:
        current_point = points_to_explore.pop()
        explored_points.append(current_point)
        
        if data[current_point[0]][current_point[1]] == '9': continue

        basin_size += 1

        if (current_point[0]+1, current_point[1]) not in explored_points:
            points_to_explore.add((current_point[0]+1, current_point[1]))
        if (current_point[0], current_point[1]+1) not in explored_points:
            points_to_explore.add((current_point[0], current_point[1]+1))
        if (current_point[0]-1, current_point[1]) not in explored_points:
            points_to_explore.add((current_point[0]-1, current_point[1]))
        if (current_point[0], current_point[1]-1) not in explored_points:
            points_to_explore.add((current_point[0], current_point[1]-1))

    return basin_size

#calculating low Points
lowPoints = []

for x, row in enumerate(data[1:-1]):
    for y, height in enumerate(row[1:-1]):
        if isLowPoint(x, y, data):
            lowPoints.append((x+1, y+1))

#getting basin sizes from lowPoints
basins = []

for point in lowPoints:
    basins.append(getBasinSize(*point, data))

print(prod(sorted(basins)[-3:]))
