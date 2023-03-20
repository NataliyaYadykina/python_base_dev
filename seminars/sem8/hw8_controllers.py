import hw8_views
import hw8_models
import hw8_text_fields

def process_func():
    contacts_db = hw8_models.load_contacts()
    check_new_data = False
    while True:
        if check_new_data:
            hw8_views.show_title(div = '*', msg = 'ВНИМАНИЕ! Сохраните внесенные изменения в файл!')
        action_type = hw8_views.get_action_type(hw8_text_fields.main_menu)
        match action_type:
            case 1:
                hw8_views.show_title(msg = 'Файл открыт.')
                print(contacts_db)
            case 2:
                hw8_models.save_contact(contacts_db)
                check_new_data = False
                hw8_views.show_title(msg = 'Телефонная книга успешно обновлена.')
            case 3:
                hw8_views.show_title(msg = 'Телефонная книга:')
                hw8_views.show_contacts(contacts_db, 'Телефонная книга пуста.')
            case 4:
                hw8_views.show_title(msg = 'Поиск контакта:')
                print('Функционал будет реализован в рамках следующего ДЗ.')
            case 5:
                hw8_views.show_title(msg = 'Добавление контакта в телефонную книгу:')
                data_contact = hw8_views.get_data_contact()
                check_contact = hw8_models.check_user_in_pb(contacts_db, data_contact)
                if check_contact:
                    hw8_views.show_title(msg = 'Такие контакты уже есть:')
                    hw8_views.show_contacts(check_contact, '')
                    choice = hw8_views.get_action_type(hw8_text_fields.add_or_update_contact)
                    if choice == 1:
                        id_user = hw8_views.get_id_user(contacts_db)
                        hw8_models.add_phone_in_contact(contacts_db, data_contact, id_user)
                        hw8_views.show_title(msg = 'Телефон успешно добавлен.')
                    elif choice == 2:
                        hw8_models.add_contact(contacts_db, data_contact)
                        hw8_views.show_title(msg = 'Контакт успешно добавлен.')
                else:
                    hw8_models.add_contact(contacts_db, data_contact)
                    hw8_views.show_title(msg = 'Контакт успешно добавлен.')
                check_new_data = True
            case 6:
                hw8_views.show_title(msg = 'Изменение контакта:')
                id_user = hw8_views.get_id_user(contacts_db)
                choice = hw8_views.get_action_type(hw8_text_fields.edit_contact_or_phone)
                phone = None
                if choice == 2:
                    phone = hw8_views.get_phone_number(contacts_db, id_user)
                hw8_views.show_title(msg = 'Введите новые данные или оставьте поле пустым:')
                new_data_contact = hw8_views.get_data_contact()
                if choice != 3:
                    hw8_models.change_contact(new_data_contact, contacts_db, id_user, phone_number = phone)
                    hw8_views.show_title(msg = 'Контакт успешно изменен.')
                    check_new_data = True
            case 7:
                hw8_views.show_title(msg = 'Удаление контакта:')
                print('Функционал будет реализован в рамках следующего ДЗ.')
            case 8:
                hw8_views.show_title(msg = 'Работа с телефонной книгой завершена.')
                return