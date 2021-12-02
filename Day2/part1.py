with open('Day2/input.txt') as f:
    data = [value.rstrip().split(' ') for value in f.readlines()]

data = [(value[0], int(value[1])) for value in data]

def dot_mult(coordinates, direction, speed):
    coordinates[0] = coordinates[0] + commands[direction][0] * speed
    coordinates[1] = coordinates[1] + commands[direction][1] * speed

commands = {'forward': (1, 0),
            'down': (0,1),
            'up': (0,-1)}

coordinates = [0,0]

for direction, speed in data:
    dot_mult(coordinates, direction, speed)


print(coordinates)
print(coordinates[0] * coordinates[1])
