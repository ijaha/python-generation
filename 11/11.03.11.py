# Суммы двух
# На вход программе подается натуральное число n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.

n = int(input())
list_1 = []
list_2 = []
if n >= 2:
    for i in range(n):
        s = int(input())
        list_1.append(s)
for i in range(len(list_1) - 1):
    k = list_1[i] + list_1[i+1]
    list_2.append(k)

print(list_2)