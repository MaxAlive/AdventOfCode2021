with open('Day11/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

for i, line in enumerate(data):
    data[i] = [int(octopus) for octopus in data[i]]

data = [['x'] * len(data[0])] + data + [['x'] * len(data[0])]
data = [['x'] + d + ['x'] for d in data]

def flash(data):
    neighbours = {(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)}
    flash_counter = 0

    for i, line in enumerate(data[1:-1]):
        for j in range(1, len(line)-1):
            if data[i+1][j] > 9:
                flash_counter += 1
                for x, y in neighbours:
                    if data[i+x+1][j+y] != 'x' and data[i+x+1][j+y] != 0:
                        data[i+x+1][j+y] += 1
                data[i+1][j] = 0

    return flash_counter

def raiseEnergy(data):
    for i, line in enumerate(data[1:-1]):
        for j in range(1, len(line)-1):
            data[i+1][j] += 1

def simultaneousFlash(data):
    for i, line in enumerate(data[1:-1]):
        for j in range(1, len(line)-1):
            if data[i+1][j] != 0:
                return False

    return True

steps = 0

while simultaneousFlash(data) == False:
    steps += 1
    raiseEnergy(data)
    while True:
        new_flashes = flash(data)
        if new_flashes == 0:
            break

print(steps)
