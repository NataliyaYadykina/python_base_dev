# Получение номера действия с телефонной книгой.
def get_action_type(text_choice):
    print('\n', text_choice, '\n')
    length = len(text_choice.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length:
            return int(choice)
        else:
            print(f'ОШИБКА! Введите значения от 1 до {length}.')    

# Добавление контакта в телефонную книгу
def get_data_contact():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    data_contact = [first_name, last_name, phone_number, comment]
    return data_contact

# Получение информации для поиска контакта
def get_search_text():
    return input('Введите информацию для поиска: ')

# Получение id контакта
def get_id_user(contacts_db):
    while True:
        id_user = input('Введите id контакта: ')
        if id_user in contacts_db.keys():
            return id_user
        else:
            print('Нет такого контакта. Укажите корректный id.')

# Получение номера телефона 
def get_phone_number(contacts_db, id_user):
    while True:
        phone_number = input('Введите номер телефона: ')
        if phone_number in contacts_db.get(id_user)[2]:
            return phone_number
        else:
            print('Нет такого телефона. Укажите корректный номер.')

# Заголовок
def show_title(div = '-', msg = ''):
    print('\n', div * len(msg), sep='')
    print(msg)
    print(div * len(msg))

# Просмотр телефонной книги
def show_contacts(contacts_db: dict, error_message: str):
    if not contacts_db:
        print(error_message)
    else:
        for id, user_info in contacts_db.items():
            print(f'{id}. {user_info[0]} {user_info[1]}')
            for phone, comment in user_info[2].items():
                print(f'- {phone} - {comment}')
            print()
