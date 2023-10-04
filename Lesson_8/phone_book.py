# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.


def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выбертите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")

def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Изменить контакт\n"
              "5. Удалить контакт\n"
              "6. Выход\n")
        
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                edit_contact()
            case '5':
                delet_contact()    
            case '6':
                print('Всего доброго! ')


def delet_contact():
    name_deleted = input("Введите имя или фамилию контакта для удаления: \n").title

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

        found = False
    for i, item in enumerate(data):
        new_item = item.replace('\n', ' ').split()
        if name_deleted in new_item:
            found = True
            del data[i]

        
    if found:
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(data))
        print('Контакт успешно удален.\n')
                
    else:
        print('Контакт не найден.\n')
                               


def edit_contact():
    name_to_edit = input("Введите имя или фамилию контакта для редактирования: ").title()
    
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    
    found = False
    for i, item in enumerate(data):
        new_item = item.replace('\n', ' ').split()
        if name_to_edit in new_item:
            found = True
            # print(f'Контакт для редактирования:\n{item}')
            # index = int(input('Выберите поле для изменения: \n'
            #                 1. 'Имя\n' 
            #                 2. 'Фамилия\n'
            #                 3. 'Отчество\n' 
            #                 4. 'Телефон\n'
            #                 5. 'Адрес\n')) - 1
            print(f'Контакт для редактирования:\n{item}')
            index = int(input('Выберите поле для изменения:\n'
                            '1. Имя\n'
                            '2. Фамилия\n'
                            '3. Отчество\n'
                            '4. Телефон\n'
                            '5. Адрес\n')) - 1


            new_value = input('Введите новое значение: ').title()
            new_item[index] = new_value
            data[i] = ' '.join(new_item)
    
    if found:
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(data))
        print('Контакт успешно изменен.\n')
    else:
        print('Контакт не найден.\n')
    


interface()