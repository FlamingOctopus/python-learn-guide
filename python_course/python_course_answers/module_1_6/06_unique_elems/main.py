def remove_dupl(main_list):
    for number in main_list:
        count = main_list.count(number)
        count = int(count / 1)
        for number_remove in range(1, count):
            main_list.remove(number)
    return main_list


def main():
    main_list = [int(input(f"Первый список, {number} элемент: ")) for number in range(0, 3)]
    second_list = [int(input(f"Второй список, {number} элемент: ")) for number in range(0, 7)]
    print("Первый список: ", main_list, "\nВторой список: ", second_list)
    main_list.extend(second_list)
    remove_dupl(main_list)
    return main_list


print("Новый первый список с уникальными элементами:", main())
