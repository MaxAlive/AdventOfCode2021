with open('Day8/input.txt') as f:
    data = [value.rstrip().split() for value in f.readlines()]

outputs = [d[-4:] for d in data]

# flattened list of output --> shows number of activated segments of digits
flat_outputlist = [len(digit) for output in outputs for digit in output]

# list of number of activated segements of the numbers: 1, 4, 7, 8
activated_segments = [2, 4, 3, 7]

print(len([digit for digit in flat_outputlist
           if digit in activated_segments]))
