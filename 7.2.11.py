# Таблица умножения
# Дано натуральное число . Напишите программу, которая выводит таблицу умножения на .
# Формат входных данных
# На вход программе подается натуральное число.
# Формат выходных данных
# Программа должна вывести таблицу умножения на введенное число.
# Примечание. В качестве знака умножения используйте английскую букву x.

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n*i)