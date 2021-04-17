# Ход ладьи
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую,
# или «NO» в противном случае.
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# Примечание. Шахматная ладья ходит по горизонтали или вертикали.

a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())

if ((a_1 == a_2) and (b_1 != b_2)) or ((b_1 == b_2) and (a_1 != a_2)):
    print('YES')
else:
    print('NO')
