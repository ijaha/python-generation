# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
# Примечание. Гарантируется, что длины названий всех трех городов различны.

c1 = input()
c2 = input()
c3 = input()

c1_l = len(c1)
c2_l = len(c2)
c3_l = len(c3)

min_c = min(c1_l, c2_l, c3_l)
max_c = max(c1_l, c2_l, c3_l)

if c1_l == min_c:
    print(c1)
elif c2_l == min_c:
    print(c2)
elif c3_l == min_c:
    print(c3)
if c1_l == max_c:
    print(c1)
elif c2_l == max_c:
    print(c2)
elif c3_l == max_c:
    print(c3)