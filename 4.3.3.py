# Гонка спидстеров
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без причины,
# и узнать у своего друга Циско Рамона есть ли смысл принимать вызов.
# Циско получил данные, что скорость Зума равна nn, а скорость Флэша равна kk.
# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.
# Формат входных данных. На вход программе подаётся два целых числа nn и kk, скорость Зума и Флэша.
# Формат выходных данных. Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES»,
# если их скорости равны нужно вывести "Don't know".

nn = int(input())   # Зум
kk = int(input())   # Флэш

if nn > kk:
    print('NO')
elif kk > nn:
    print('YES')
elif nn == kk:
    print("Don't know")
