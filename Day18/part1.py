import re
from math import ceil

with open('Day18/input.txt') as f:
    data = [d.rstrip() for d in f.readlines()]


def reduce_number(number):
    #print(number)
    nest_lvl = -1
    exploded, splitted = True, True

    while exploded or splitted:
        nest_lvl = -1
        exploded, splitted = False, False
        for i, letter in enumerate(number):
            #print(i, letter, nest_lvl)
            if letter == '[':
                nest_lvl += 1
            elif letter == ']':
                nest_lvl -= 1
            if nest_lvl == 4:
                number = explode(number, i+1)
                #print(number)
                exploded = True
                break
        if not exploded:
            for digits in list(map(int, re.findall(r'\d+', number))):
                if digits >= 10:
                    new_number = f'[{digits//2},{ceil(digits/2)}]'
                    number = number.replace(str(digits), new_number, 1)
                    splitted = True
                    break
                    #print(number)

    return number

def explode(number, index):
    #print(number)
    everything = list(re.findall(r'\d+|[\[\],]+', number))
    everything_indices = [m.start(0)
                          for m in re.finditer(r'\d+|[\[\],]+', number)]

    digits = list(map(int, re.findall(r'\d+', number)))
    digits_indices = [m.start(0) for m in re.finditer(r'\d+', number)]

    left_index = digits_indices.index(index)
    right_index = left_index+1
    #print(right_index, digits_indices)

    left_bracket_index = everything_indices.index(index) - 1
    right_bracket_index = everything_indices.index(digits_indices[right_index]) + 1

    everything[left_bracket_index] = everything[left_bracket_index][:-1]
    everything[right_bracket_index] = everything[right_bracket_index][1:]

    if left_index > 0:
        everything[everything_indices.index(
            digits_indices[left_index-1])] = str(digits[left_index] + digits[left_index-1])
    if right_index < len(digits_indices) - 1:
        everything[everything_indices.index(
            digits_indices[right_index+1])] = str(digits[right_index] + digits[right_index+1])
    

    everything = everything[:left_bracket_index+1] + ['0'] + everything[right_bracket_index:]
    everything = ('').join(everything)

    return everything

def add_numbers(number1, number2):
    return f"[{number1},{number2}]"

snail = data[0]
for number in data[1:]:
    snail = reduce_number(add_numbers(snail, number))

print(snail)
pairs = list(re.findall(r'\[\d,\d\]', snail))

while pairs:
    pairs = list(re.findall(r'\[\d+,\d+\]', snail))
    for pair in pairs:
        result = str(int(pair[1:pair.index(',')]) * 3 + int(pair[pair.index(',')+1:-1]) * 2)
        snail = snail.replace(pair, result, 1)

print(snail)