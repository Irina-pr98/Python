# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

count_day = int(input('Введите количество дней: '))
temperature = 0
count = 0
count_max = 0 #максимальное количество дней

for i in range(count_day):
    temperature += random.randint(-4, 4)
    print(temperature, end=", ")
    if temperature > 0:
        count += 1
    else:
        if count > 0:
            print(f'Количество теплых дней с температурой больше 0: {count}')
        count = 0
    
    if count > count_max:
        count_max = count

print('\n', f'Максимальное количество теплых дней: {count_max}')