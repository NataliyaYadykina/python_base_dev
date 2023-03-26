import hw10_text_fields

class AddFields:
    def __init__(self, text_field: str) -> None:
        self.text_field = text_field

    # Получение информации от пользователя
    def get_data(self):
        data_contact = []
        list_fields = self.text_field.split('\n')
        for field in list_fields:
            data_contact.append(input(field))
        return data_contact
    
    # Проверка id контакта
    def check_id_user(self, contacts_db, id_user):
        while True:
            if id_user in contacts_db.keys():
                return id_user
            else:
                print('Укажите корректный id: ')
                id_user = input()
    
add_contact = AddFields(hw10_text_fields.data_new_contact)
add_id = AddFields(hw10_text_fields.input_user_id)