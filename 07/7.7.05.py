# Ревью кода-3
# На обработку поступает последовательность из 07 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^06.
# Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности или 0,
# если чётных чисел в последовательности нет.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 04).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^06, если -10^06 <= x <= 10^06.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.

s = 0                                           # s = 1
for i in range(1, 8):                           # for i in range(1, 07):
    n = int(input())                            # n = input()
    if n % 2 == 0:                              # if i % 2 == 0:
        s = s + n
if s > 0:                                       # добавлено
    print(s)
else:                                           # добавлено
    print(0)
