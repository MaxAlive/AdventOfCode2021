from statistics import median

with open('Day10/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

def getClosingString(line, partners, reversed_partners):
    index = 0
    closing_letters = partners.keys()
    
    while index < len(line):
        letter = line[index]
        if letter in closing_letters:
            if line[index-1] == partners[letter]:
                line = line[:index-1] + line[index+1:]
                index -= 2
            else:
                return ''
        index += 1

    return [reversed_partners[char] for char in reversed(line)]

def getScore(closing_string, scores):
    total = 0
    
    for letter in closing_string:
        total *= 5
        total += scores[letter]

    return total

scores = {')':1, ']':2, '}':3, '>':4}
partners = {')':'(', '}':'{', ']':'[', '>':'<'}
reversed_partners = {'(':')', '{':'}', '[':']', '<':'>'}
final_scores = []

for line in data:
    string = getClosingString(line, partners, reversed_partners)
    if string:
        final_scores.append(getScore(string, scores))

print(median(final_scores))
