import pickle
import contact


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
            print(f"Адресная книга {self.file_name}.data открыта.")
        except FileNotFoundError:
            file = open(self.file_name, 'wb')
            pickle.dump(self.address_book, file)
            print(f"Адресная книга {self.file_name}.data создана.")

    def __del__(self):
        """
        2) Автоматически сохраняет текущую адресную книгу в файл 'file_name' (расширение .data) в каталоге программы.
        """
        file = open(self.file_name, 'wb')
        pickle.dump(self.address_book, file)
        print(f"Завершение работы: Адресная книга сохранена в файл {self.file_name}.")

    def add(self):  # , cont):
        """
        3) Добавляет в адресную книгу новый объект 'Contact', если такой объект отсутствует в книге и отвечает требованиям.
        :return:
        информация об успешности добавления в виде True или False
        """
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        phone = input("Введите телефон: ")
        comment = input("Введите примечание: ")
        try:
            cont = contact.Contact(first_name, last_name, phone, comment)
            if cont in self.address_book:
                print('Такой контакт уже существует в адресной книге.')
                return False
            else:
                self.address_book.append(cont)
                print("Контакт добавлен.")
                self.address_book.sort(key=lambda x: x.first_name)
                return True
        except ValueError:
            print('Укажите корректное имя пользователя (имя или фамилия должны быть заполнены)!')
            return False

    def show_all(self):
        """
        4) Выводит на экран список или все записи 'Contact' из адресной книги.
        :return:
        вывод на печать форматированного списка объектов 'Contact'
        """
        if len(self.address_book) == 0:
            print("Адресная книга пуста.")

        else:
            for i in self.address_book:
                print(i)

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
            contact_list = [c for c in self.address_book if c.is_contain(str(request))]
            if len(contact_list) == 0:
                print("Ничего не найдено.")
                return False
            else:
                return contact_list

    def select(self, request):
        """
        6) Позволяет выбрать объект 'Contact', поле которого отвечает пользовательскому запросу.
        :return:
        Объект 'Contact' или False
        """
        contact_list = self.find(str(request))
        if contact_list is not False:
            if len(contact_list) == 1:
                return contact_list[0]
            else:
                print(f"В адресной книге '{self.file_name}' найдены следующие контакты, отвечающие Вашему запросу:")
                for i in range(0, len(contact_list)):
                    print(f"{i + 1}) {contact_list[i]}")
                no = 0
                while no < 1 or no > len(contact_list):
                    try:
                        no = input("Введите № контакта, с которым Вы хотите продолжить работу: ")
                        no = int(no)
                    except:
                        print("Попробуйте ввести номер еще раз.")
                        no = -1
            return contact_list[int(no) - 1]
        else:
            return False

    def modify(self, request):
        """
        7) Изменяет контактные данные 'Contact'
        :return:
        информация об успешности изменения в виде True или False
        """
        cont = self.select(str(request))
        if cont is not False:
            if self.add():
                self.address_book.remove(cont)
                self.address_book.sort(key=lambda x: x.first_name)
            else:
                print("Что-то пошло не так, попробуйте еще раз.")

    def delete(self, request):
        """
        8) Удаляет контактные данные 'Contact'
        :return:
        информация об успешности удаления в виде True или False
        """
        cont = self.select(str(request))
        if cont is not False:
            conf = input(f"Контакт '{cont.first_name}' '{cont.last_name}' будет удален. Для подтверждения введите 'Y'.")
            if conf.lower() == 'y':
                print("Контакт удален.")
                self.address_book.remove(cont)
            else:
                print("Операция отменена.")
