with open('Day2/input.txt') as f:
    data = [value.rstrip().split(' ') for value in f.readlines()]

data = [(value[0], int(value[1])) for value in data]

def dot_mult(coordinates, value):
    global aim
    coordinates[0] = coordinates[0] + value
    coordinates[1] = coordinates[1] + aim * value

def increase_aim(_, value):
    global aim
    aim += value

def decrease_aim(_, value):
    global aim
    aim -= value

commands = {'forward': dot_mult,
            'down': increase_aim,
            'up': decrease_aim}

coordinates = [0,0]
aim = 0

for command, value in data:
    commands[command](coordinates, value)

print(coordinates)
print(coordinates[0] * coordinates[1])
