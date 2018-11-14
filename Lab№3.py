"""KubSU Python Lab№3"""
print('Exercise 1.')
book = input('Что за книга?')
author = input('Кто ее автор')
print('Писатель', author, ' - автор книги', book)

print('Exercise 2.')
city1 = input('Название первого города - ')
city2 = input('Название второго города - ')
city3 = input('Название третьего города - ')

listcities = [city1, city2, city3]

longestword = 0
for i in range(len(listcities)):
    if len(listcities[longestword]) < len(listcities[i]):
        longestword = i
print('Длиннейшее название - ', listcities[longestword])

shortestword = 0
for i in range(len(listcities)):
    if len(listcities[shortestword]) > len(listcities[i]):
        shortestword = i
print('Кратчайшее название - ', listcities[shortestword])

print('Exercise 3.')
word = input('Введите ваше слово - ')
a = list(word)
print(a[2])
print(a[-1])
k = int(input('Какой еще элемент вам нужен? - '))
b = a[(k-1):k]
print(b)

print('Exercise 4.')
word = 'Информатика'
informatika = list(word)
print(informatika)
forma = ''.join(informatika[2:7])
tik = ''.join(informatika[7:10])
print(forma)
print(tik)

print('Exercise 5.')
symbol = input('Ваш символ - ')
number = int(input('Сколько раз повторить? - '))
print(symbol*number)

print('Exercise 6.')
sentence = input('Введите текст - ')
symbol = input('Какой символ вы ищете? - ')
number = []
for i in range(len(sentence)):
    if symbol in sentence[i]:
        number.append(symbol)
print(number)

print('Exercise 7.')
sentence = input('Введите текст - ')
print(sentence.title())

print('Exercise 8.')
sentence = input('Введите предложение - ')
symbol = input('Какие буквы считаем? - ')
count = 0
if symbol in sentence[0]:
    count += 1
for i in range(len(sentence)):
    if symbol in sentence[i] and sentence[i - 1] == ' ':
        count += 1
print('Данный символ встречается в начале слов', count, 'раз(а)')

print('Exercise 9.')
sentence = input('Введите предложение - ')
symbol = input('Какие буквы считаем? - ')
count = 0
for i in range(len(sentence)):
    if symbol in sentence[i]:
        count += 1
print('Данный символ встречается', count, 'раз(а)')

print('Exercise 10.')
text = input('Введите текст - ')
count = 0
symbol = '.'
for i in range(len(text)):
    if symbol in text[i]:
        count += 1
print('В вашем тексте', count, 'предложения(ий)')

print('Exercise 11.')
text = input('Введите текст - ')
for i in range(len(text)):
    if ('ж' in text[i] and 'ы' in text[i+1]) or ('ш' in text[i] and 'ы' in text[i+1]):
        print(text.replace('жы', 'жи') and text.replace('шы', 'ши'))

print('Exercise 12.')
word = input('Введите слово - ')
if word == word[::-1]:
    print('Перевертыш!')
else:
    print('Не перевертыш')

print('Exercise 13.')
sentense = 'А РОЗА УПАЛА НА ЛАПУ АЗОРА'
sentense = ''.join(sentense.split())
if sentense == sentense[::-1]:
    print('Перевертыш!')
else:
    print('Не перевертыш')
print(sentense)

print('Exercise 14.')
symbol = input('Введите символ - ')
if symbol.isdigit():
    print('Это цифра!')
else:
    print('Это не цифра')

print('Exercise 15.')
text = input('Введите текст - ')
count = 0
digits = []
for i in range(len(text)):
    if text[i].isdigit():
        count += 1
        digits.append(text[i])
print('В тексте ', count, 'цифр')
print('Вот они - ', digits)

print('Exercise 16.')
text = input('Введите текст - ')
digits = []
for i in range(len(text)):
    if text[i].isdigit():
        digits.append(int(text[i]))
print(digits)
b = sum(digits)
print('Полученная сумма - ', b)

print('Exercise 17.')
sentence = input('Введите текст - ')
count = 0
list = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
for i in range(len(sentence)):
    if sentence[i] in list:
        count += 1
print('В предложении', count, 'гласных')

print('Exercise 18.')
sentence = input('Введите текст - ')
spaces = ' '
count = 0
for i in range(len(sentence)):
    if not sentence[i].isdigit() and not sentence[i] in spaces:
        count += 1
print('В предложении -', count, 'букв')

print('Exercise 19.')
inputtext = 'ilmujcbec gq y rpcyqspc, zsr npyargac gq rfc icw rm gr'
input_list = list(inputtext)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
spaces = ' '
for i in range(len(input_list)):
    if input_list[i] not in spaces:
        input_list[i]