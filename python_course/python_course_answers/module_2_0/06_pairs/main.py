from random import randint

rand_list = [randint(0, 20) for number in range(10)]
print("Оригинальный список: ", rand_list)
first_list, second_list = [], []
for index, number in enumerate(rand_list, 1):
    if index % 2 == 0:
        second_list.append(number)
    else:
        first_list.append(number)
print("Новый список: ", list(zip(first_list, second_list)))
