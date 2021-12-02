with open('Day1/input.txt') as f:
    data = [int(value.rstrip()) for value in f.readlines()]

print(
    len(
        [1 for i, _ in enumerate(data[:-3])
        if sum(data[i:i+3]) < sum(data[i+1:i+4])]
    )
)
