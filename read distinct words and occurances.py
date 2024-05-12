num = int(input('Enter number of words:'))

print(f'Enter the words {num} word: ')

words = []
distinct = []
output = {}


for i in range(0, num):

    word = input(f'Enter word {i}: ')

    words.append(word)


for word in words:

    if word not in distinct:

        distinct.append(word)

print(len(distinct))

for word in words:

    output[word] = words.count(word)

for i in output.values():
    print(i, end=' ')

