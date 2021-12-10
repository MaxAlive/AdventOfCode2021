with open('Day10/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

def getScore(line, scores, partners):
    index = 0
    closing_letters = partners.keys()
    
    while index < len(line):
        letter = line[index]
        if letter in closing_letters:
            if line[index-1] == partners[letter]:
                line = line[:index-1] + line[index+1:]
                index -= 2
            else:
                return scores[letter]
        index += 1

    return 0


scores = {')':3, ']':57, '}':1197, '>':25137}
partners = {')':'(', '}':'{', ']':'[', '>':'<'}
final_score = 0

for line in data:
    final_score += getScore(line, scores, partners)

print(final_score)
