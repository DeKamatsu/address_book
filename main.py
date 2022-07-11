"""
Задача
Создайте собственную программу «Адресная книга», работающую из командной строки и
позволяющую просматривать, добавлять, изменять, удалять или искать контактные
данные ваших знакомых. Кроме того, эта информация также должна сохраняться на диске
для последующего доступа.
"""

import abook
import contact


def create_contact():
    """
    Функция интерфейса: создает контакт на основании вводимой пользовательских данных.

    Возвращает объект класса 'Contact' или False
    """
    first_name = input("Введите имя контакта --> ")
    last_name = input("Введите фамилию контакта --> ")
    phone = input("Введите телефон контакта --> ")
    comment = input("Введите примечание (по необходимости) --> ")
    try:
        return contact.Contact(first_name, last_name, phone, comment)
    except ValueError:
        print("Не удалось создать новый контакт, так как не указаны ни имя, ни фамилия.")
        return False


def user_request():
    """
    Функция интерфейса: запрашивает у пользователя непустое поле для поиска контакта.

    Возвращает String
    """
    while True:
        request = input("Введите непустой запрос для подбора подходящих контактов --> ")
        if len(request.replace(' ', '')) != 0:
            return request
        print("Попробуйте еще раз. ", end="")


def select_contact(contact_list):
    """
    Функция интерфейса: уточняет выбор пользователя из списка объектов 'Contact', отвечающих пользовательскому запросу.
    :return:
    Объект 'Contact' или False
    """
    if len(contact_list) == 1:
        print(f"По запросу найден один контакт:\n{contact_list[0]}")
        return contact_list[0]
    else:
        print(f"В адресной книге найдены следующие контакты, отвечающие Вашему запросу:")
        for i in range(0, len(contact_list)):
            print(f"{i + 1}) {contact_list[i]}")
        no = 0
        while no < 1 or no > len(contact_list):
            try:
                no = input("Введите № контакта, с которым Вы хотите продолжить работу --> ")
                no = int(no)
            except:
                print("Попробуйте ввести номер еще раз.")
                no = -1
    return contact_list[int(no) - 1]


if __name__ == '__main__':
    """
    Пользовательский интерфейс для работы с адресной книгой
    """
    while True:
        book_name = input('Введите название адресной книги --> ')
        if len(str(book_name).replace(' ', '')) > 0:
            ab = abook.ABook(book_name)
            break

    while True:
        choice = input("""
Сделайте Ваш выбор:
1 - просмотреть все контакты в адресной книге (show all),
2 - добавить новый контакт (add),
3 - изменить контакт (modify),
4 - удалить контакт (delete),
0 - завершение работы с адресной книгой (quit)
--> """)
        if choice == '1':  # show all
            ab.show_all()
        elif choice == '2':  # add
            cont = create_contact()
            if cont is not False:
                ab.add(cont)
        elif choice == '3':  # modify
            request = user_request()
            contact_list = ab.find(request)
            if contact_list is not False:
                target_cont = select_contact(contact_list)
                new_cont = create_contact()
                if new_cont is not False:
                    ab.modify(target_cont, new_cont)
        elif choice == '4':  # delete
            request = user_request()
            contact_list = ab.find(request)
            if contact_list is not False:
                target_cont = select_contact(contact_list)
                ab.delete(target_cont)
        elif choice == '0':  # quit
            print('Завершение сеанса.')
            del ab
            break
        else:
            print('Повторите Ваш выбор, пожалуйста.')
