# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

number = int(input('Введите число: '))

fibonacci_one = 0 
fibonacci_two = 1 
fibonacci_cur = 0 #текущее число фибоначчи
count = 1

while fibonacci_cur < number:
    fibonacci_cur = fibonacci_one + fibonacci_two
    fibonacci_one, fibonacci_two = fibonacci_two, fibonacci_cur
    count += 1
    
# print(count if number == fibonacci_cur else '-1')
    
if number == fibonacci_cur:
    print(count)
else:
    print(-1)