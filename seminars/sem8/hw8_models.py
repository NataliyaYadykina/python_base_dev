import json
import os

path = 'hw8_contacts.json'
export_path = 'hw8_phone_book.txt'

# Получение данных из файла .json в словарь
def load_contacts():
    if os.stat(path).st_size == 0:
        contacts_db = {}
    else:
        contacts_db = json.load(open(path, 'r', encoding='utf-8'))
    return contacts_db

# Добавление контакта в телефонную книгу
def add_contact(contacts_db, data_contact):
    max_id = int(max(contacts_db, key=int))
    contacts_db[str(max_id + 1)] = [data_contact[0], data_contact[1], {data_contact[2]:data_contact[3]}]

# Поиск контакта
def find_contact(contacts_db, search_text):
    search_result = {}
    for id, user_info in contacts_db.items():
        for item in user_info:
            if type(item) != dict:
                if search_text.lower() in item.lower():
                    search_result[id] = user_info
    return search_result

# Поиск телефона
def find_phone(contacts_db, search_text):
    search_result = {}
    for id, user_info in contacts_db.items():
        for key, value in user_info[2].items():
            if search_text in key:
                if not search_result.get(id, 0):
                    search_result[id] = [user_info[0], user_info[1], {key:value}]
                else:
                    search_result[id][2][key] = value
    return search_result

# Проверка, есть ли указанный контакт в телефонной книге
def check_user_in_pb(contacts_db, data_contact):
    found_contacts = {}
    for id, user_info in contacts_db.items():
        if data_contact[0] in user_info and data_contact[1] in user_info:
            found_contacts[id] = user_info
    return found_contacts

# Обновление контакта, добавление номера телефона
def add_phone_in_contact(contacts_db, data_contact, id_contact):
    contacts_db[id_contact][2][data_contact[2]] = data_contact[3]

# Изменение контакта
def change_contact(new_data_contact, contacts_db, id_user, phone_number = None):
    if new_data_contact[0]:
        contacts_db[id_user][0] = new_data_contact[0]
    if new_data_contact[1]:
        contacts_db[id_user][1] = new_data_contact[1]
    if phone_number:
        if new_data_contact[2]:
            contacts_db[id_user][2][new_data_contact[2]] = contacts_db[id_user][2].pop(phone_number)
        if new_data_contact[3]:
            contacts_db[id_user][2][new_data_contact[2]] = new_data_contact[3]

# Удаление контакта
def delete_contact(contacts_db, id_user):
    if contacts_db.get(id_user):
        contacts_db.pop(id_user, None)
        print(f'Контакт с id = {id_user} успешно удален.')
    else:
        print('Такого контакта нет в телефонной книге.')

# Удаление телефона
def delete_phone(contacts_db, phone, id_user):
    phone = list(contacts_db[id_user][2].keys())[0]
    contacts_db[id_user][2].pop(phone, None)
    print(f'Телефон {phone} пользователя {contacts_db[id_user][0]} успешно удален.')

# Сохранение данных словаря в файл .json и экспорт в текстовый файл
def save_contact(data_contact, sep_contacts, sep_after_name, sep_elements, sep_string):
    json.dump(data_contact, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
    str_contact = ''
    for id, user_info in data_contact.items():
        str_contact += f'{id}. {user_info[0]} {user_info[1]}{sep_after_name}'
        for phone, comment in user_info[2].items():
            str_contact += f'{phone}{sep_elements}{comment}{sep_string}'
        str_contact += sep_contacts
    print(str_contact)
    with open(export_path, 'w', encoding = 'utf-8') as f:
        f.write(str_contact)
