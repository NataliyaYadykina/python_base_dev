import hw10_text_fields

class SelectMenu:
    def __init__(self, text_field: str) -> None:
        menu_strings = text_field.split('\n')
        self.title = menu_strings[0]
        self.items = '\n'.join(menu_strings[1:-1])
        self.question = menu_strings[-1]

    def show_menu(self):
        separ = '-' * len(self.title)
        print()
        print(separ, self.title, separ, self.items, self.question, sep = '\n')
        length = len(self.items.split('\n'))
        while True:
            choice = input()
            if choice.isdigit() and 0 < int(choice) <= length:
                return int(choice)
            else:
                print(f'ОШИБКА! Введите значения от 1 до {length}:')

main_menu = SelectMenu(hw10_text_fields.main_menu)
search_menu = SelectMenu(hw10_text_fields.find_contact_menu)
add_menu = SelectMenu(hw10_text_fields.add_or_update_contact)
edit_menu = SelectMenu(hw10_text_fields.edit_contact_or_phone)
delete_menu = SelectMenu(hw10_text_fields.delete_contact_menu)
confirm_delete_menu = SelectMenu(hw10_text_fields.confirm_delete_menu)
