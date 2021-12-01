with open('Day1/input.txt') as f:
    data = [int(value.rstrip()) for value in f.readlines()]

print(
    len(
        [1 for i, d in enumerate(data[1:])
        if (data[i] > data[i-1])]
    )
)
