# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.

import random

list = int(input('Введит едлину списка: '))
random_list = [random.randint(1, 5) for _ in range(list)]
print(random_list)

i = 0
while i < len(random_list):
    if random_list[i] == 4 or random_list[i] == 5:
        random_list[i] = 1
    i += 1
print(random_list)

'''max_count = max(random_list)
min_count = min(random_list)
print(max_count)
print(min_count)

for i in range(len(random_list)):
    if random_list[i] == max_count:
        random_list[i] = min_count
print(random_list)
'''