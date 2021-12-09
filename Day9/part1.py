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

lowPoints = []

for x, row in enumerate(data[1:-1]):
    for y, height in enumerate(row[1:-1]):
        if isLowPoint(x, y, data):
            lowPoints.append(int(data[x+1][y+1]))

print(sum(lowPoints) + len(lowPoints))
