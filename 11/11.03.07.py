# Список строк
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из указанных строк.

n = int(input())
list_ = []
for i in range(n):
    s = input()
    list_.append(s)
print(list_)