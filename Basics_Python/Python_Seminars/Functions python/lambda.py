'''
lambda - это анонимная однострочная функция, которая обязательно что-то возвращает 
lambda используется при одноразовом использовании функции
Функцию lambda можно передать в качестве аргумента в какое-нибудь выражение

'''

operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y}

string = '3+2'
string = list(string)

print(string)

for i, item in enumerate(string):
    if string[i] in ['+', '-']:
        print(operation.get(string[i])(int(string[i - 1]), int(string[i + 1])))
        