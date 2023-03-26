import hw10_text_fields

class Search:
    def __init__(self, choice: int) -> None:
        self.choice = choice

    def show_what_search(self):
        if self.choice == 1:
            search_text = input(hw10_text_fields.search_contact)
        elif self.choice == 2:
            search_text = input(hw10_text_fields.search_phone)
        return search_text