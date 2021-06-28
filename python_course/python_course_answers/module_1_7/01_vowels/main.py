phrase = input("Введите текст: ")
list_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
new_list=[letter for letter in phrase if letter in list_letters ]
print("Список гласных букв: ",new_list,"\nДлина списка:", len(new_list))