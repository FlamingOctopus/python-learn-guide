numbers_count = int(input("Введите максимальное число: "))
numbers_set = {str(dict_num) for dict_num in range(1, numbers_count + 1)}

while True:
    boris_phrase = input("Нужное число есть среди вот этих чисел: ")
    if boris_phrase == "Помогите!":
        print("Артём мог загадать следующие числа: ", end=" ")
        for number in sorted(numbers_set):
            print(number[0], end=" ")
        break
    else:
        boris_phrase = set(boris_phrase.split())
        artems_answer = input("Ответ Артёма: ")
        if artems_answer == 'Нет':
            numbers_set -= boris_phrase
        else:
            numbers_set &= boris_phrase
