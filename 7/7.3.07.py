# Асимптотическое приближение
# На вход программе подается натуральное число . Напишите программу, которая вычисляет значение выражения
# Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n) , которая находится в модуле math .

from math import *

n = int(input())

sum = 0
for i in range(1, n + 1):
    sum = sum + 1 / i
total = sum - log(n)
print(total)