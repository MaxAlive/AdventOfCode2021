with open('Day3/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

input_length = len(data)
number_of_bits = len(data[0])
count = [0] * number_of_bits

for d in data:
    for i, bit in enumerate(d):
        count[i] += int(bit)

gamma = ('').join(['1' if c > input_length / 2 else '0' for c in count])
epsilon = ('').join(['1' if c < input_length / 2 else '0' for c in count])

print(gamma)
print(epsilon)

print(int(gamma, 2) * int(epsilon, 2))
