import json
import os

path = 'hw8_contacts.json'

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
    print(type(max_id))
    print(contacts_db)
    contacts_db[str(max_id + 1)] = [data_contact[0], data_contact[1], {data_contact[2]:data_contact[3]}]
    print(max_id)
    print(contacts_db)

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

# Сохранение данных словаря в файл .json
def save_contact(data_contact):
    json.dump(data_contact, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
