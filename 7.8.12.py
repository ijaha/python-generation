# Старинная задача
# Имеется 100 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и
# надо купить голов 100 скота?
# Примечание. Используйте вложенный цикл for

for x in range(1, 11):
    for y in range(1, 21):
        for z in range(1, 201):
            if (10 * x + 5 * y + 0.5 * z == 100) and (x + y + z == 100):
                print('быки', x)
                print('коровы', y)
                print('телята', z)
                print('*' * 10)
    