import pickle


class ABook:
    """
    Класс 'ABook' описывает объект 'Адресная книга', обеспечивающий сохранение в файле и манипуляции с контактными
    данными людей (имя, фамилия, телефон, произвольное примечание)

    1) При иницировании объекта класса 'ABook' по имени 'name' создается новая адресная книга либо открывается,
    если файл с таким именем был ранее создан.
    2) При завершении работы (удалении объекта класса 'ABook') автоматически сохраняет адресную книгу в рабочий
    каталог и уведомляет об этом пользователя.

    Объект 'Адресная книга' содержит список объектов класса 'Contact' и поддерживает следующие методы при работе из
    командной строки:
    3) add - добавлять контактные данные 'Contact',
    4) show_all - выводит на экран данные полей объектов 'Contact', содержащихся в объекте класса 'ABook',
    5) show - выводит на экран данные выбранного контакта (через декоратор поиска и выбора),
    6) find - находит объект 'Contact', поле которого отвечает пользовательскому запросу,
    7) modify - изменять контактные данные 'Contact' (через декоратор поиска и выбора),
    8) delete - удалять контактные данные 'Contact' (через декоратор поиска и выбора).

    """
    file_name: str
    address_book = []

    def __init__(self, name):
        """
        1) Создает новую или открывает существующую адресную книгу.
        :param name:
        имя адресной книги, соответствующее имени файла в каталоге программы (без указания расширения .data)
        """
        self.file_name = f"{name}.data"
        try:
            file = open(self.file_name, 'r+b')
            self.address_book = pickle.load(file)
            print(f"Адресная книга {self.file_name} открыта.")
        except FileNotFoundError:
            file = open(self.file_name, 'wb')
            pickle.dump(self.address_book, file)
            print(f"Адресная книга {self.file_name} создана.")

    def __del__(self):
        """
        2) Автоматически сохраняет текущую адресную книгу в файл 'file_name'.data в каталоге программы.
        """
        file = open(self.file_name, 'wb')
        pickle.dump(self.address_book, file)
        print(f"Адресная книга сохранена в файл {self.file_name}.")

    def add(self, cont):
        """
        3) Добавляет в адресную книгу новый объект 'Contact', если такой объект отсутствует в книге.
        :return:
        информация об успешности добавления в виде True или False
        """
        if cont in self.address_book:
            print('Такой контакт уже существует.')
            return False
        else:
            self.address_book.append(cont)
            print("Новый контакт добавлен.")
            self.address_book.sort(key=lambda c: c.first_name)
            return True

    def show_all(self):
        """
        4) Выводит на экран список или все записи 'Contact' из адресной книги.
        :return:
        вывод на печать форматированного списка объектов 'Contact'
        """
        if len(self.address_book) == 0:
            print("Адресная книга пуста.")
        else:
            no = 1
            for i in self.address_book:
                print(f"{no}) {i}")
                no += 1

    def show(self, request):
        """
        5) Выводит на экран список объектов 'Contact', отвечающих пользовательскому запросу.
        :return:
        вывод на печать форматированного списка объектов
        """
        cont = self.find(str(request))
        if cont is not False:
            print(cont)

    def find(self, request):
        """
        6) Находит группу объектов 'Contact', поле которых отвечает пользовательскому запросу.
        :return:
        Список объектов 'Contact' или False
        """
        if len(self.address_book) == 0:
            print("Адресная книга пуста.")
            return False
        else:
            contact_list = [c for c in self.address_book if c.is_contain(request)]
            if len(contact_list) == 0:
                print("Ничего не найдено.")
                return False
            else:
                return contact_list

    def modify(self, cont, new_cont):
        """
        7) Изменяет контактные данные 'Contact' путем замены на новый контакт
        :return:
        информация об успешности изменения в виде True или False
        """
        self.address_book.remove(cont)
        self.address_book.append(new_cont)
        self.address_book.sort(key=lambda c: c.first_name)

    def delete(self, cont):
        """
        8) Удаляет контактные данные 'Contact'
        :return:
        информация об успешности удаления в виде True или False
        """
        conf = input(f"Контакт '{cont.first_name}' '{cont.last_name}' будет удален. Для подтверждения введите 'Y'.")
        if conf.lower() == 'y':
            print("Контакт удален.")
            self.address_book.remove(cont)
        else:
            print("Операция отменена.")
