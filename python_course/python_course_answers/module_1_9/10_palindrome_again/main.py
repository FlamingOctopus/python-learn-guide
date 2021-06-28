def is_polindrome(phrase):
    symbols_dict = dict()
    number_count = 0
    for sym in phrase:
        symbols_dict[sym] = symbols_dict.get(sym, 0) + 1
    for value in symbols_dict.values():
        if value % 2 != 0:
            number_count += 1
    return number_count <= 1


phrase = input("Введите строку: ")
validator = is_polindrome(phrase)
if validator:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
