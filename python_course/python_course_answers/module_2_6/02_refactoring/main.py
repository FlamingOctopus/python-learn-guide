from typing import Iterable


def double_mult_func(first_obj: Iterable, second_obj: Iterable, number: int) -> Iterable:
    for x in first_obj:
        for y in second_obj:
            result = x * y
            if result == number:
                print('Found!!!')
                yield f"{result}, удалось получить заданное число из {x} и {y}"
            yield f"Неудача"


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
func = double_mult_func(list_1, list_2, to_find)

for i in func:
    print(i)
