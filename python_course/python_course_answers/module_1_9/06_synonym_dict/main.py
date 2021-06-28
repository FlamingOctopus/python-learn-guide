words_count = int(input("Введите количество пар слов: "))
new_dict = dict()
for item in range(1, words_count + 1):
    words = input(f"{item} пара: ").lower().split(" - ")
    new_dict[words[0]] = words[1]

while True:
    word = input("Введите слово: ").lower()
    if word in new_dict:
        print("Синоним:", new_dict[word])
        break
    else:
        print("Такого слова в словаре нет.")
