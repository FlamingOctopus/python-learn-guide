guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
left_or_enter = str
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек:", guests)
    left_or_enter = input("Гость пришел или ушел? ")
    person = input("Имя гостя: ")
    if left_or_enter == "пришел":
        if len(guests) < 6:
            print(f"Привет, {person}!")
            guests.append(person)
        else:
            print(f"Прости, {person}, но мест нет.")
    elif left_or_enter == "ушел":
        print(f"Пока, {person}!")
        guests.remove(person)
    elif left_or_enter == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    else:
        print("Ошибка, повторите ввод")