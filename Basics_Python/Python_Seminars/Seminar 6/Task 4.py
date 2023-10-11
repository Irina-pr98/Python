# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое 
# из которых не превосходит k. Программа получает на вход одно 
# натуральное число k, не превосходящее 10^5. Программа должна 
# вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз 
# (перестановка чисел новую пару не дает).

'''def divisor(x):
    return sum([i for i in range(1, x // 2 + 1) if x % i == 0])

x = int (input('Введите предел: '))
for i in range(1, x):
    if divisor(divisor(i)) == i and i < divisor(i):
        print((i< divisor(i)))'''
        
len_arr = int(input('Введите k: '))

my_dict = {}
for i in range(1, len_arr):
    my_dict[i] = my_dict.get(i, 0)
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            my_dict[i] = my_dict.get(i, 0) + j
print(my_dict)

for key1, value1 in my_dict.items():
    for key2, value2 in my_dict.items():
        if key2 > key1:
            if key2 != key2 and value1 == key2 and value2 == key1:
                print(f'{key1} {key2}')