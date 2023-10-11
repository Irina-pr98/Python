my_string = 'qwerty'
my_string = list(my_string)
print(my_string)

for i in range(len(my_string)):
    print(f'{i}. {my_string[i]}')
    
# С помощью функции enumerate

my_string = 'asdfgh'
my_string = list(my_string)
print(my_string)

for i, item in enumerate(my_string, 1):
    print(f'{i}. {item}')