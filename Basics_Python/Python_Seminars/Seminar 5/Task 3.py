# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым
# 3 5 7 11 13 17 19 23

number = int(input('Введите число: '))

def is_simple(num: int):
    if not num % 2 and num != 2:
        for dev in range(3, num // 2, 2):
            if not num % dev:
                return False
    return True

print(is_simple(number))