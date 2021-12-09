with open('Day8/input.txt') as f:
    data = [value.rstrip().split() for value in f.readlines()]

def get_wiring(digits):
    four = list(filter(lambda x: len(x) == 4, digits))[0]
    flattened_digits = [segment for digit in digits for segment in digit]
    segment_count = {segment: flattened_digits.count(segment)
                        for segment in set(flattened_digits)}
    translation = {}

    for key, value in segment_count.items():
        if value == 8 and key not in four:
            translation[key] = 'a'
        if value == 6:
            translation[key] = 'b'
        if value == 8 and key in four:
            translation[key] = 'c'
        if value == 7 and key in four:
            translation[key] = 'd'
        if value == 4:
            translation[key] = 'e'
        if value == 9:
            translation[key] = 'f'
        if value == 7 and key not in four:
            translation[key] = 'g'

    return translation

def translate(output_number, translation, numbers):
    result = []
    for digit in output_number:
        activated_segments = []
        for letter in digit:
            activated_segments.append(translation[letter])
        result.append(numbers[('').join(sorted(activated_segments))])

    return int(('').join(result))

inputs = [d[:d.index('|')] for d in data]
outputs = [d[d.index('|') + 1:] for d in data]
numbers = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
            'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
final_sum = 0

for i, digits in enumerate(inputs):
    translation = get_wiring(digits)
    final_sum += translate(outputs[i], translation, numbers)

print(final_sum)
