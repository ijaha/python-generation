# Факториал
# На вход программе подается натуральное число . Напишите программу, которая вычисляет .
# Входные данные
# На вход программе подается натуральное число .
# Выходные данные
# Программа должна вывести единственное число в соответствии с условием задачи.
# Примечание. Факториалом натурального числа , называется произведение всех натуральных чисел от до , то есть

n = int(input())

total = 1
if n <= 12:
    for i in range(1, n + 1):
        total *= i
    print(total)
