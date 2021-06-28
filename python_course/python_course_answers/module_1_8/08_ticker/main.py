string, mod_string = input("Первая строка:"), input("Вторая строка:")
id_sym = mod_string.find(string[0])
number = len(mod_string[id_sym:])
new_string = mod_string[id_sym:] + mod_string[0:id_sym]
if new_string == string:
    print(f"Первая строка получается из второй со сдвигом {number}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
