with open('Day3/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def get_count(data, index, value):
    counter = 0
    
    for d in data:
        if d[index] == value:
            counter += 1

    return counter

###oxygen generator rating
data_copy = data[:]
counter = 0

while len(data_copy) > 1:
    if get_count(data_copy, counter, '1') >= len(data_copy) / 2:
        data_copy = [value for value in data_copy if value[counter] == '1']
    else:
        data_copy = [value for value in data_copy if value[counter] == '0']
    counter += 1

oxygen_generator = int(data_copy[0], 2)

###CO2 Scrubber rating
data_copy = data[:]
counter = 0

while len(data_copy) > 1:
    if get_count(data_copy, counter, '1') < len(data_copy) / 2:
        data_copy = [value for value in data_copy if value[counter] == '1']
    else:
        data_copy = [value for value in data_copy if value[counter] == '0']
    counter += 1

co2_scrubber = int(data_copy[0], 2)

print(oxygen_generator * co2_scrubber)
