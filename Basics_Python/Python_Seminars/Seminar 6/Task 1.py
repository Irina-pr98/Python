# Даны два массива чисел. Требуется вывести те элементы первого 
# массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит число 
# N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

import random

length_list_1 = int(input('Введите длину первого списка: '))
list_1 = [random.randint(1, 30) for _ in range(length_list_1)]
length_list_2 = int(input('Введите длину второго списка: '))
list_2 = [random.randint(1, 30) for _ in range(length_list_2)]
print(list_1)
print(list_2)
new_list = []

for i in list_1:
    if i not in list_2:
        new_list.append(i)
print(new_list)