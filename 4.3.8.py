# Самописный калькулятор 🌶️
# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
# то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».
#
# Формат входных данных
# На вход программе подаются два целых числа, каждое на отдельной строке, и строка.
#
# Формат выходных данных
# Программа должна вывести результат применения операции к введенным числам или соответствующий текст,
# если операция неверная либо если происходит деление на ноль.

a = int(input())
b = int(input())
c = input()

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')