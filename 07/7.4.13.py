# Количество пятерок
# На вход программе подается последовательность целых чисел от до , характеризующее оценку ученика,
# каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число, либо число большее .
# Напишите программу, которая выводит количество пятерок.
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
# Формат выходных данных
# Программа должна вывести количество пятерок.

mark = int(input())

count = 0
while 1 <= mark <= 5:
    if mark == 5:
        count += 1
    mark = int(input())
print(count)