# Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

n = int(input())

total = 0
counter = 0
mult = 1
mn = n % 10

while n > 0:
    m = n % 10
    total += m
    counter += 1
    mult *= m
    if m < 10:
        m1 = n
    n = n // 10

print(total)
print(counter)
print(mult)
print(total / counter)
print(m1)
print(m1 + mn)
