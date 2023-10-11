my_string = '112233445566778899'
my_string = list(my_string)
my_string = list(map(lambda x: int(x), my_string))
print(my_string)

def is_odd(num: int) -> bool:
    if num % 2 == 1:
        return True
    else:
        return False
    
my_string = list(filter(is_odd, my_string))
print(my_string)

# С помощью функции lambda

my_string = list(filter(lambda x: x % 2 == 0, my_string))
print(my_string)