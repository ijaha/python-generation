# Звездный треугольник
# На вход программе подается натуральное число – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# Формат входных данных
# На вход программе подается одно натуральное число .
# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием задачи.

n = int(input())

if n >= 2:
    for i in range(n):
        print((n - i) * '*')
