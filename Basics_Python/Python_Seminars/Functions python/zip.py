my_string = 'qwertyvidm'
my_list = [i for i in range(10)]
my_string = list(my_string)
print(my_string)
print(my_list)

new_list = []
for i , item in enumerate(my_string):
    new_list.append((my_string[i], my_list[i]))

print(new_list)

# С помощью функции zip

my_string = 'qwerty'
my_list = [i for i in range(10)]
my_string = list(my_string)
print(my_string)
print(my_list)

new_list = list(zip(my_string, my_list))

print(new_list)