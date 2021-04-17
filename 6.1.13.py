# Сортировка трёх 🌶
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.


a = int(input())
b = int(input())
c = int(input())

d = (a + b + c) - min(a, b, c) - max(a, b, c)

print(max(a, b, c), d, min(a, b, c), sep='\n')
