# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в 
# заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, 
# максимально близкое ему по значению

import random

length_list = int(input('Введите длину: '))
number = int(input('Введите искомое число: '))
random_array = [random.randint(1, 10) for _ in range(length_list)]
print(random_array)

min_delta = max(random_array)

for index in range(length_list):
    if abs(number - random_array[index]) < min_delta:
        min_delta = abs(number - random_array[index])
        search_number = random_array[index]

if number in random_array:
    print(f'Число {number} встречается {random_array.count(number)} раз')
else:
    print(f'Число {search_number} максимально близкое искомому числу {number}')