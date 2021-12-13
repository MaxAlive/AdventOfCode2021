from parse import parse

with open('Day13/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

dots = {tuple(parse('{:d},{:d}', d)) for d in data[:data.index('')]}
instructions = [tuple(parse('fold along {}={:d}', d))
                for d in data[data.index('')+1:]]

def fold(dots, axis, line):
    new_dot = [0,0]

    if axis == 'x':
        i=0
    else:
        i=1

    for dot in list(filter(lambda x: x[i] > line, dots)):
        dots.remove(dot)
        new_dot[i] = 2*line - dot[i]
        new_dot[1-i] = dot[i-1]
        dots.add(tuple(new_dot))

instruction_1 = instructions[0]

fold(dots, *instruction_1)
print(len(dots))
