import os

def save_func(path_f,save_string):
    f = open(path_f, 'w')
    f.write(save_string)
    f.close()

save_string = input("Введите строку: ")
# /home/def/PycharmProjects/python_basic_15/Module22/05_save/
# home def PycharmProjects python_basic_15 Module22 05_save
path = "/" + os.path.join(input("Куда хотите сохранить документ? Введите последовательность папок (через пробел):").replace(" ", "/"))
file_name = input("Введите имя файла: ")

path_f = f"{path}/{file_name}.txt"


if os.path.exists(path_f):
    answer = input("Вы действительно хотите перезаписать файл? ")
    if answer == "да":
        save_func(path_f, save_string)
        print("Файл успешно перезаписан!")
    else:
        print("Ошибка!")
else:
    save_func(path_f, save_string)
    print("Файл успешно создан!")
