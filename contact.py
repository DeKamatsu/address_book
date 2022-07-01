class Contact:
    """
    класс 'Contact' содержит информацию об одном контакте адресной книги: имя, фамилия, телефон, произвольное примечание.
    Обеспечивает создание непустой записи, возврат или изменение ее полей по запросу, удаление записи.
    """
    first_name: str
    last_name: str
    phone: str
    comment: str

    def __init__(self, first_name, last_name='', phone='', comment=''):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.comment = comment

    def __del__(self):
        print(f"Контакт '{self.first_name} {self.last_name}' удален.")
        # self.first_name = ''
        # self.last_name = ''
        # self.phone = ''
        # self.comment = ''

    def __str__(self):
        print(f"имя: '{self.first_name}, фамилия: {self.last_name}, телефон: {self.phone}, примечание: {self.comment}")

    def first_name_change(self, new_first_name):
        pass

    def last_name_change(self, new_last_name):
        pass

    def phone_change(self, phone_name):
        pass

    def comment_change(self, comment_name):
        pass
