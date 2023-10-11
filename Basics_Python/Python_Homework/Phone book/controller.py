import phone_book

pb = phone_book.PhoneBook('Python-Homework\Phone book\phone.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите номер изменяемого контакта: '))
            name = input('Введите имя или нажмите Enter, если нет изменений: ')
            phone = input('Введите телефон или нажмите Enter, если нет изменений: ')
            comment = input('Введите комментарий или нажмите Enter, если нет изменений: ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите номер удаляемого контакта: '))
            pb.remove(index-1)
        case 6:
            pb.save()
        case 7:
            break