with open('Day6/input.txt') as f:
    data = f.readlines()[0].rstrip().split(',')

# fishies index = how many days to hatch
# value = how many lanternfish in the state of index
fishies = [data.count(str(i)) for i in range(9)]

for days in range(256):
    fishies = fishies[1:] + [fishies[0]]
    fishies[6] += fishies[8]
    
print(sum(fishies))
