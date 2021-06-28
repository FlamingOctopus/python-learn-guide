string = input("Введите строку: ")
string += ' '
new_string = ""
count = 0
prev_symbol = string[0]
for symbol in string:
    if prev_symbol == symbol:
        count += 1
    else:
        new_string += ''.join([prev_symbol, str(count)])
        count = 1
    prev_symbol = symbol

print(new_string)