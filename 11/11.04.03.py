# Значение функции
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x^2 + 2*x + 1

# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.

n = int(input())
num = []
f = []
for i in range(n):
    k = int(input())
    num.append(k)
print(*num, sep='\n')
print()
for j in num:
    result = (j + 1) ** 2
    f.append(result)
print(*f, sep='\n')
