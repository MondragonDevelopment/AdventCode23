from collections import defaultdict
from random import shuffle

with open('data/spanish.dat') as data:
    lines = [line[:-1] for line in data]

punctuation = [' ', '.', ',', ';', ':']

text = ""
for line in lines:
    for character in line:
        if character.isalnum():
            text += character.lower()
        if character in punctuation:
            text += character
        

text += 'f'
text = text.replace('ã', 'a').replace('³', 'e').replace('º', 'o')

alphabet = defaultdict()
abList = [i for i in range(ord('a'), ord('z') + 1)]
shuffle(abList)

for char in range(ord('a'), ord('z') + 1):
    alphabet[chr(char)] = chr(abList[char-ord('a') - 1])

print(alphabet)

lis = list(text)
newtext = ""
print(lis)

for letter in lis:
    if letter.isalnum():
        newtext += alphabet[letter]
    elif letter in punctuation:
        newtext += letter


print(newtext)
