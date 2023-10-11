#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

first_digit = number % 10
second_digit = number % 100 // 10
third_digit = number // 100

print(f'Сумма числа {number}: {first_digit + second_digit + third_digit}')