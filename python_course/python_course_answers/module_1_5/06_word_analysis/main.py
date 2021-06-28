def word_uni(word):
    word = list(word)
    checked_symbols_list = []
    count = 0
    for symbol in word:
        count_checked_symbols = 0
        for checking_symbol in checked_symbols_list:
            if symbol == checking_symbol:
                count -= 1
                break
            elif count_checked_symbols == len(checked_symbols_list):
                checked_symbols_list.append(symbol)
                count += 1
            else:
                count_checked_symbols += 1
                continue
        else:
            checked_symbols_list.append(symbol)
            count += 1
    print("Кол-во уникальных букв: ", count)


word = input("Введите слово: ")
word_uni(word)
