# Количество цифр
# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.

s = input()
total = 0
for i in range(len(s)):
    if s[i].isdigit() == True:
        total += 1
print(total)