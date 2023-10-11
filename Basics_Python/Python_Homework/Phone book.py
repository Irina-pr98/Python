# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def menu():
    dict_phonebook = {}
    while True:
        function = int(input('Введите запрос: 1 - Сохранить телефонную книгу, 2 - Показать все контакты, 3 - Найти контакт, 4 - Добавить контакт, 5 - Изменить контакт,  6 - Удалить контакт, 7 - Выход: '))
        if function == 1:
            save_dir(dict_phonebook)
            print('Save')
        elif function == 2:
            if len(dict_phonebook) == 0:
                dict_phonebook = open_read_dir()
            if len(dict_phonebook) == 0:
                print('Телефонная книга пуста')
            else:
                print(dict_phonebook)
        elif function == 3:
            contact_find(dict_phonebook)
        elif function == 4:
            value_new_contact = add_contact(dict_phonebook)
            print(value_new_contact)
            dict_phonebook.update(value_new_contact)
            print('Сохрани!')
        elif function == 5:
            new_contact = contact_find(dict_phonebook)
            add_contact(dict_phonebook, new_contact)
        elif function == 6:
            new_contact = contact_find(dict_phonebook)
            print(f'Удалили контант: {new_contact[0]}: {dict_phonebook.pop(new_contact[0])}')
            print('Сохрани!')
        elif function == 7:
            print('End')
            break
        else:
            print('Введите ещё раз')


def open_read_dir():
    dict_phonebook = {}
    with open('Python-Homework\Phonebook.txt', 'r', encoding='UTF-8') as f:
        for line_contact in f.readlines():
            key, value = line_contact.split(':')
            dict_phonebook[key] = value
        return dict_phonebook


def save_dir(dict_phonebook):
    str_phonebook = ''
    print(dict_phonebook)
    for key, value in dict_phonebook.items():
        str_phonebook += f'{key}:{value} \n'
    with open('Python-Homework\Phonebook.txt', 'w', encoding='UTF-8') as f:
        f.write(str_phonebook)


def add_contact(dict_phonebook, new_contact_in = [0]):
    if len(new_contact_in) < 2:
        name_contact = input('Введите Имя и Фамилию: ')
        phone_contact = input('Введите телефон: ')
        comment_contact = input('Введите комментарий: ')
        contact_list = [phone_contact, comment_contact]
    else:
        name_contact, contact_list = tuple(new_contact_in)
    dict_phonebook.setdefault(name_contact, contact_list)
    print(f'{name_contact}, {dict_phonebook[name_contact]}')
    return dict_phonebook


def contact_find(dict_phonebook):
    name_contact = input('Введите Имя и Фамилию: ')
    if name_contact in dict_phonebook:
        print(f'{name_contact}: {dict_phonebook[name_contact]}')
        return [name_contact, dict_phonebook[name_contact]]
    else:
        print(f'Результаты отсутствуют')
        
menu()