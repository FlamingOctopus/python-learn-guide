def reverse_this(word):
    word = list(word)
    current_symbol = 0
    for symbol in range(1, len(word)):
        if word[current_symbol] == word[-1 - current_symbol]:
            continue
        else:
            print("Слово не является палиндромом")
            return None
    print("Слово является палиндромом")


word = input("Введите слово: ")
reverse_this(word)
