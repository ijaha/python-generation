# Диаграмма
# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.

n = input()
num = n.split()

for i in num:
    plus = '+' * int(i)
    print(plus, sep='\n')
