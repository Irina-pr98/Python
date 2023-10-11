# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса 
# формата _n.

string = input('Введите строку: ')
dictionary = {}

for i in string:
    dictionary[i] = dictionary.get(i, 0) + 1
    
    if dictionary[i] == 1:
        print(i, end=", ")
    else:
        print(f'{i}_{dictionary[i] - 1}', end=", ")