my_string = '55412697875130316539'
my_string = list(my_string)
print(my_string)

for i in range(len(my_string)):
    my_string[i] = int(my_string[i])

print(my_string)
print(sum(my_string))

# С помощью функции map

my_string = '1234567890123456789'
my_string = list(my_string)
print(my_string)

my_string = list(map(int, my_string))

print(my_string)
print(sum(my_string))

# С помощью функции lambda

my_string = '112233445566778899'
my_string = list(my_string)
print(my_string)

my_string = list(map(lambda x: int(x), my_string))

print(my_string)
print(sum(my_string))
