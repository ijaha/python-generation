# Квадрат числа
# На вход программе подается натуральное число .
# Напишите программу, которая для каждого из чисел от до (включительно) выводит фразу:
# «Квадрат числа [число] равен [число]» (без кавычек).
# Формат входных данных
# На вход программе подается натуральное число .
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())

for _ in range(n + 1):
    print('Квадрат числа', _, 'равен', pow(_, 2))
