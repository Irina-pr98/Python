# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.

# Решение с помощью срезов
"""
numbers = int(input('Введите длину последовательности: '))
shift = int(input('Введите длину сдвига: '))

my_list = [i for i in range(numbers)]
print(my_list)

new_list = my_list[shift:] + my_list[:shift]
print(new_list)
"""

# Через цикл
import random

my_list = [random.randint(0, 10) for i in range(10)]
print(my_list)

shift = int(input('Введите размер сдвига: '))

for i in range(shift):
    my_list.insert(0, my_list.pop(-1))
print(my_list)