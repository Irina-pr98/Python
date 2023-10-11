# Дан список чисел. Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента, 
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

import random

list_1 = [random.randint(0, 20) for _ in range(int(input('Введите размер списка: ')))]
print(list_1)

count = 0
pairs_list = []
for item in set(list_1):
    pairs = list_1.count(item) // 2
    count += pairs
    if pairs:
        [pairs_list.append(item) for _ in range(pairs * 2)]
    [list_1.remove(item) for _ in range(pairs * 2)]
    
print(pairs_list)
print(list_1)
print(f'{count} пар элементов')