name_user = input("Введите свое имя: ")
while True:
    response = input("Выберите одно из действий:\n\
    1. Посмотреть текущий текст чата\n\
    2. Отправить сообщение")
    try:
        if response=="1":
            with open("chat.txt", 'r') as file:
                print(file.read())
        elif response=="2":
            message = input("Введите сообщение: ")
            with open("chat.txt", 'w') as file:
                file.write(f"{name_user}: {message}")
        else:
            print("Некорректное значение попробуйте снова.")
    except FileNotFoundError:
        print("Чат еще не создан")