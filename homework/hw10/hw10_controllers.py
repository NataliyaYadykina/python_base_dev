import hw10_menu
import hw10_pb
import hw10_search
import hw10_add

pb = hw10_pb.PhoneBook('hw10_contacts.json', 'hw10_phone_book.txt')

def process_func():
    check_new_data = False
    while True:
        if check_new_data:
            msg = 'ВНИМАНИЕ! Сохраните внесенные изменения в файл!'
            div = '*' * len(msg)
            print(div, msg, div, sep='\n')
        action = hw10_menu.main_menu.show_menu()
        match action:
            case 1:
                pb.save('\n\n' + '*' * 25 + '\n', ':\n- ', ' - ', '\n- ')
                check_new_data = False
                print('Телефонная книга успешно обновлена.')
            case 2:
                pb.show_contacts(pb.dict)
            case 3:
                choice = hw10_menu.search_menu.show_menu()
                search_text = hw10_search.Search(choice).show_what_search()
                search_result = pb.search_contact(choice, search_text)
                pb.show_contacts(search_result)
            case 4:
                data_contact = hw10_add.add_contact.get_data()
                check_contact = pb.check_user_in_pb(data_contact)
                if check_contact:
                    pb.show_contacts(check_contact)
                    choice = hw10_menu.add_menu.show_menu()
                    if choice == 1:
                        user_id = hw10_add.add_id.get_data()[0]
                        user_id = hw10_add.add_id.check_id_user(check_contact, user_id)
                        pb.add_phone_in_contact(data_contact, user_id)
                    elif choice == 2:
                        pb.add_contact(data_contact)
                else:
                    pb.add_contact(data_contact)
                check_new_data = True
            case 5:
                user_id = hw10_add.add_id.get_data()[0]
                user_id = hw10_add.add_id.check_id_user(pb.dict, user_id)
                choice = hw10_menu.edit_menu.show_menu()
                phone = None
                if choice == 2:
                    phone = hw10_search.Search(choice).show_what_search()
                    phone = pb.get_phone_number(user_id, phone)
                if choice != 3:
                    print('Введите новые данные или оставьте поле пустым: ')
                    new_data_contact = hw10_add.add_contact.get_data()
                    pb.change_contact(new_data_contact, user_id, phone)
                    check_new_data = True
            case 6:
                choice = hw10_menu.delete_menu.show_menu()
                if choice == 1:
                    user_id = hw10_add.add_id.get_data()[0]
                    user_id = hw10_add.add_id.check_id_user(pb.dict, user_id)
                    confirm = hw10_menu.confirm_delete_menu.show_menu()
                    if confirm == 1:
                        pb.delete_contact(user_id)
                        check_new_data = True
                elif choice == 2:
                    phone = hw10_search.Search(choice).show_what_search()
                    search_result = pb.search_contact(choice, phone)
                    pb.show_contacts(search_result)
                    user_id = None
                    if len(search_result) > 1:
                        user_id = hw10_add.add_id.get_data()[0]
                        user_id = hw10_add.add_id.check_id_user(pb.dict, user_id)
                    elif len(search_result) == 1:
                        user_id = list(search_result.keys())[0]
                    confirm = hw10_menu.confirm_delete_menu.show_menu()
                    if search_result and confirm == 1:
                        pb.delete_phone(phone, user_id)
                        check_new_data = True
            case 7:
                print('Работа с телефонной книгой завершена.')
                return