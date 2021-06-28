while True:
    password = input("Придумайте пароль:")
    count_digit, count_upper = 0, 0
    if len(password) > 8:

        for symbol in password:
            if symbol.isdigit(): count_digit += 1
            if symbol.isupper(): count_upper += 1
    if count_digit >= 3 and count_upper >= 1:
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")