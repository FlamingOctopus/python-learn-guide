def find_clone(main_tuple, tuple_element):
    """эта функция выводит срез в зависимости от указанных условий"""
    count_element = main_tuple.count(tuple_element)
    if count_element == 0:
        return tuple()
    elif count_element == 1:
        return main_tuple[main_tuple.index(tuple_element):]
    else:
        first_index = main_tuple.index(tuple_element)
        second_index = main_tuple.index(tuple_element, first_index + 1)
        return main_tuple[first_index:second_index + 1]


element = int(input("Введите число "))
new_tuple = (1, 2, 3, 4, 5, 3, 5, 4, 7, 1, 3)

print(find_clone(new_tuple, element))
