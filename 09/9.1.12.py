# Сколько раз?
# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести сколько раз встречаются символы  + и * в строке.

str_ = input()
plus = 0
star = 0
for i in range(len(str_)):
    if str_[i] in '+':
        plus += 1
    if str_[i] in '*':
        star += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')