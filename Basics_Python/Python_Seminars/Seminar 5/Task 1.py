# Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

fib_1 = int(input('Введите номер числа Фибоначчи: '))
def fibonacci(fib_1):
    if fib_1 == 0:
        return 0
    elif fib_1 == 1:
        return 1
    else:
        return fibonacci(fib_1 - 1) + fibonacci(fib_1 - 2)
print(fibonacci(fib_1)) 