class Contact:
    """
    Класс 'Contact' содержит информацию об одном контакте адресной книги: имя, фамилия, телефон, примечание.

    Методы класса беспечивают:
    1) создание нового контакта с обязательным наличием минимум одного из двух полей имени, 2) формат вывода контакта в
    виде текстовой строки, а также сравнения контактов, 3) проверку соответствия полей контакта поисковому запросу.
    """
    first_name: str
    last_name: str
    phone: str
    comment: str

    def __init__(self, first_name='', last_name='', phone='', comment=''):
        """
        1) Создание нового контакта с обязательным наличием минимум одного из двух полей имени.

        Принимает на входе параметры контакта как в виде значений 4 полей, так и в виде структуры данных типа кортеж
        или список (обрабатывается вместо первой переменной).
        """
        # проверяем, если на входе при создании объекта подается кортеж или список (попадет в первое поле first_name)
        if isinstance(first_name, tuple) or isinstance(first_name, list):
            data_set = list(first_name)
            first_name = data_set[0]
            last_name = data_set[1]
            phone = self.clear_number(data_set[2])
            comment = data_set[3]
        if first_name == '' and last_name == '':
            raise ValueError
        self.first_name = first_name
        self.last_name = last_name
        self.phone = self.clear_number(phone)
        self.comment = comment

    def __str__(self):
        """
        2) Определяет формат вывода контакта в виде текстовой строки.
        """
        return f"имя: {self.first_name}, фамилия: {self.last_name}, телефон: {self.phone}, примечание: {self.comment}"

    def is_contain(self, txt):
        """
        3) Проверка соответствия полей контакта поисковому запросу.
        """
        if txt in self.first_name or \
                txt in self.last_name or \
                self.clear_number(txt) in self.phone or \
                txt in self.comment:
            return True
        else:
            return False

    @staticmethod
    def clear_number(txt):
        """
        Удаляет возможные незначащие символы при различных формах записи телефона пользователем.
        """
        cleaned = str(txt)
        excluding = [' ', '+', '-', '(', '(']
        for e in excluding:
            cleaned = cleaned.replace(e, '')
        return cleaned
