def validator(row):
    list_user = row.split(" ")
    if len(list_user) != 3:
        raise IndexError("Ошибка в количестве аргументов")
    if not list_user[0].isalpha():
        raise NameError("Ошибка в имени")
    # if not "."  in list_user[1] and not "@" in list_user[1]:
    #     raise SyntaxError("Ошибка в емейле")
    if not "." in list_user[1]:
        raise SyntaxError("Ошибка в емейле")
    if not  "@" in list_user[1]:
        raise SyntaxError("Ошибка в емейле")
    if not list_user[2].isdigit():
        if 10 > int(list_user[2]) or int(list_user[2])> 99:
            raise ValueError("Ошибка в возрасте")
    else:
        raise ValueError("Ошибка в возрасте,значение не целое число")
    return True


with open("registrations.txt", 'r') as file:
    with open("registrations_good.log ", 'w') as registrations_good:
        with open("registrations_bad.log ", 'w') as registrations_bad:
            for row in file:
                try:
                    if validator(row):
                        registrations_good.write(f"{row}")
                except Exception as exp:
                    registrations_bad.write(f"{row} - Ошибка  {exp} ")
