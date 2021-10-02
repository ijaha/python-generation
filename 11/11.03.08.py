# Алфавит
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z.

abc = 'abcdefghijklmnopqrstuvwxyz'
list_ =[]
for i in range(26):
    symbol = abc[i] * (i+1)
    list_.append(symbol)
print(list_)
