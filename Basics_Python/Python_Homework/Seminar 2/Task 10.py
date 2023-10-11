#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
number_coins = int(input('Введите количество монет: '))
side_1_count = 0
side_0_count = 0

for i in range(number_coins):
    side = random.randint(0, 1)
    print(f'Монета под номером {i + 1} имеет сторону {side}')
    if side == 1:
        side_1_count += 1
    else:
        side_0_count += 1

if side_1_count < side_0_count:
    print(f'Количество монет, которые нужно перевернуть: {side_1_count}')
else:
    print(f'Количество монет, которые нужно перевернуть: {side_0_count}')
    
# Второй способ

import random

coins = [random.randint(0, 1) for _ in range(9)]
print(coins)
print('Перевернуть единички' if coins.count(1) < coins.count(0) else 'Перевернуть нолики')