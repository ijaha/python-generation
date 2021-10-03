# Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения
# по заданному числу градусов .

# Формат входных данных
# На вход программе подается одно вещественное число измеряемое в градусах.

# Формат выходных данных
# Программа должна вывести одно число – значение тригонометрического выражения.

# Примечание 1. Тригонометрические функции принимают аргумент в радианах.
# Чтобы перевести градусы в радианы, воспользуйтесь формулой
# Примечание 2. Модуль math содержит встроенную функцию radians() ,
# которая переводит угол из градусов в угол в радианах.

from math import *

x = float(input())

r = radians(x)
result = sin(r) + cos(r) + pow(tan(r), 2)
print(result)