import json
import os
from hw10_contact import Contact

class PhoneBook:
    def __init__(self, path: str, export_path: str) -> None:
        self.path = path
        self.export_path = export_path
        self.error_message = 'Контакты не найдены.'
        self.dict = self.load()

    # Получение данных из файла .json в словарь
    def load(self):
        if os.stat(self.path).st_size == 0:
            contacts_db = {}
        else:
            contacts_db = json.load(open(self.path, 'r', encoding='utf-8'))
        return contacts_db
    
    # Просмотр телефонной книги
    def show_contacts(self, data_contacts):
        title = 'Телефонная книга'
        separ = '-' * len(title)
        print(separ, title, separ, sep = '\n')
        print()
        if not data_contacts:
            print(self.error_message)
        else:
            for id, user_info in data_contacts.items():
                print(f'{id}. {user_info[0]} {user_info[1]}')
                for phone, comment in user_info[2].items():
                    print(f'- {phone} - {comment}')
                print()

    # Добавление контакта в телефонную книгу
    def add_contact(self, data_contact):
        contact = Contact(data_contact)
        if self.dict:
            max_id = int(max(self.dict, key=int))
        else:
            max_id = 0
        self.dict[str(max_id + 1)] = [contact.firstname, contact.lastname, {contact.phone:contact.comment}]
        print(f'\nТелефон {contact.phone} контакта {contact.firstname} {contact.lastname} успешно добавлен!\n')

    # Обновление контакта, добавление номера телефона
    def add_phone_in_contact(self, data_contact, id_contact):
        contact = Contact(data_contact)
        self.dict[id_contact][2][contact.phone] = contact.comment
        print(f'\nТелефон {contact.phone} контакта {id_contact}. {contact.firstname} {contact.lastname} успешно добавлен!\n')

    # Проверка, есть ли указанный контакт в телефонной книге
    def check_user_in_pb(self, data_contact):
        contact = Contact(data_contact)
        found_contacts = {}
        for id, user_info in self.dict.items():
            if contact.firstname in user_info and contact.lastname in user_info:
                found_contacts[id] = user_info
                print('\nТакие контакты в книге уже есть.')
        return found_contacts

    # Поиск контакта
    def search_contact(self, choice: int, search_text: str):
        search_result = {}
        for id, user_info in self.dict.items():
            if choice == 1:
                for item in user_info:
                    if type(item) != dict:
                        if search_text.lower() in item.lower():
                            search_result[id] = user_info
            else:
                for key, value in user_info[2].items():
                    if search_text in key:
                        if not search_result.get(id, 0):
                            search_result[id] = [user_info[0], user_info[1], {key:value}]
                        else:
                            search_result[id][2][key] = value
        return search_result
    
    # Получение номера телефона 
    def get_phone_number(self, id_user, phone_number):
        while True:
            if phone_number in self.dict.get(id_user)[2]:
                return phone_number
            else:
                print('Нет такого телефона. Укажите корректный номер:')
                phone_number = input()

    # Изменение контакта
    def change_contact(self, new_data_contact, id_user, phone_number = None):
        contact = Contact(new_data_contact)
        if contact.firstname:
            self.dict[id_user][0] = contact.firstname
        if contact.lastname:
            self.dict[id_user][1] = contact.lastname
        if phone_number:
            if contact.phone:
                self.dict[id_user][2][contact.phone] = self.dict[id_user][2].pop(phone_number)
            else:
                contact.phone = phone_number
            if contact.comment:
                self.dict[id_user][2][contact.phone] = contact.comment
        print('Данные успешно изменены.')

    # Удаление контакта
    def delete_contact(self, id_user):
        if self.dict.get(id_user):
            self.dict.pop(id_user, None)
            print(f'Контакт с id = {id_user} успешно удален.')
        else:
            print('Такого контакта нет в телефонной книге.')

    # Удаление телефона
    def delete_phone(self, phone, id_user):
        phone = list(self.dict[id_user][2].keys())[0]
        self.dict[id_user][2].pop(phone, None)
        print(f'Телефон {phone} пользователя {self.dict[id_user][0]} успешно удален.')
    
    # Сохранение данных словаря в файл .json и экспорт в текстовый файл
    def save(self, sep_contacts: str, sep_after_name: str, sep_elements: str, sep_string: str):
        json.dump(self.dict, open(self.path, 'w', encoding='utf-8'), ensure_ascii=False)
        str_contact = ''
        for id, user_info in self.dict.items():
            str_contact += f'{id}. {user_info[0]} {user_info[1]}{sep_after_name}'
            for phone, comment in user_info[2].items():
                str_contact += f'{phone}{sep_elements}{comment}{sep_string}'
            str_contact += sep_contacts
        print(str_contact)
        with open(self.export_path, 'w', encoding = 'utf-8') as f:
            f.write(str_contact)

