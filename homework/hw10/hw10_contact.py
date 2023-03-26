class Contact:
    def __init__(self, data_contact: list) -> None:
        self.firstname = data_contact[0]
        self.lastname = data_contact[1]
        self.phone = data_contact[2]
        self.comment = data_contact[3]

    def __str__(self) -> str:
        return f'{self.firstname:<20} | {self.lastname:<20} | {self.phone:<20} | {self.comment:<20}'
    
# cont = Contact(['John', 'Smidt', '654', 'private'])
# print(cont)