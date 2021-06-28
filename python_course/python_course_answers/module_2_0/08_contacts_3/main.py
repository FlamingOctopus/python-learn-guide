def add_contact(contacts_book):
    """Функция добавляет контакт в книгу"""
    name = tuple(input("Введите имя и фамилию: ").split())
    phone_number = input("Введите номер телефона: ")
    if not check_name_in_book(contacts_book, name):
        contacts_book[name] = phone_number
    else:
        print("Контакт уже есть в книге")
    return contacts_book


def check_name_in_book(contacts_book, surname):
    """Фунция проверяет наличие контакта в книге"""
    for key, value in contacts_book.items():
        return surname in key


def search(contacts_book, surname):
    """Функция ищет контакт в книге"""
    for key, value in contacts_book.items():
        if surname in key:
            print(key[0], key[1], value)


def menu():
    """Главное меню"""
    contacts_book = {}
    while True:
        request = input("Введите нужную операцию:").lower()
        if request == "добавить контакт":
            add_contact(contacts_book)
        elif request == "поиск человека по фамилии":
            surname = input("Введите фамилию контакта ")
            search(contacts_book, surname)
        else:
            print("Введите корректную операцию")


menu()
