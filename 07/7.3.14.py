# Only even numbers 🌶
# Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет.
# Формат входных данных
# На вход программе подаются 10 целых чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

flag = True
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        flag *= True
    elif n % 2 == 1:
        flag *= False
if flag == 1:
    print('YES')
else:
    print('NO')