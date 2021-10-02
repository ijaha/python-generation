# Дополните приведенный код, так чтобы элемент списка имеющий значение Green заменился
# на значение Зеленый, а элемент Violet на Фиолетовый.
# Далее необходимо вывести полученный список.

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

if 'Green' in rainbow:
    rainbow[3] = 'Зеленый'
if 'Violet' in rainbow:
    rainbow[-1] = 'Фиолетовый'
print(rainbow)
