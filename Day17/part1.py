from parse import parse

with open('Day17/input.txt') as f:
    data = f.readlines()[0].rstrip()

x_low, x_high, y_low, y_high = parse(
    'target area: x={:d}..{:d}, y={:d}..{:d}', data)


def inTarget(x, y):
    if x_low <= x <= x_high and y_low <= y <= y_high:
        return True
    return False


def step(x, y, v_x, v_y):
    if v_x == 0.0:
        return (x+v_x, y+v_y, 0.0, v_y-1)
    else:
        return (x+v_x, y+v_y, (abs(v_x)-1) * ((v_x) / abs(v_x)), v_y-1)


# brute force :(
highest_high = float('-inf')
for x in range(0, x_high):
    for y in range(0, x_high):
        x_pos, y_pos, v_x, v_y = 0, 0, x, y
        current_high = float('-inf')
        while y_pos > y_low and not inTarget(x_pos, y_pos):
            x_pos, y_pos, v_x, v_y = step(x_pos, y_pos, v_x, v_y)
            if y_pos > current_high:
                current_high = y_pos
        if inTarget(x_pos, y_pos):
            if current_high > highest_high:
                highest_high = current_high

print(highest_high)
