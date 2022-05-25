# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
count = 0
for letter in word:
    if letter in 'ауеыоэяию':
        count += 1
print(count)
print()


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'.split(' ')
count = 0
for word in sentence:
    count += 1
print(count)
print()

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'.split(' ')
for letter in sentence:
    print(letter[0])
print()

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'.split(' ')
total_len = 0
for word in sentence:
    total_len += len(word)
print(total_len/len(sentence))