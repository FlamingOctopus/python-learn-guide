def cesar(phrase, shift):
    cesar_list = [(alphabet[(alphabet.index(number) + shift) % 33] if number != " " else " ") for number in phrase]
    cesar_list ="".join(cesar_list)
    return cesar_list


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
phrase = input("Введите сообщение: ")
shift = int(input("Введите сдвиг:"))
print("Новая строка", cesar(phrase, shift))