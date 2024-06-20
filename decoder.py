with open('data/coded.dat') as data:
    lines = [line[:-1] for line in data]

text = ""
for line in lines:
    for character in line:
        if character.isalnum():
            text += character.lower()

dic = {}

def countLetters(text):
    for letter in text:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    return dic

print(countLetters(text))

