from typing import Iterable


class SqGenerator:
    """Класс генератор генерирует последовательность квадратов чисел"""

    def __init__(self, range: int) -> None:
        self.__range = range
        self.__number = 0

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        self.__number += 1
        if self.__range <= self.__number:
            raise StopIteration
        return self.__number ** 2


def sq_generator(range_gen: int, count=0) -> Iterable:
    while True:
        count += 1
        if count >= range_gen:
            return
        yield count ** 2


range_number = 4

sq_gen = (number ** 2 for number in range(1, range_number))
generator_class = SqGenerator(4)
generator_func = sq_generator(4)

print("gen_comprehension")
for number_i in sq_gen:
    print(number_i)
print("gen_class")
for number_j in generator_class:
    print(number_j)
print("gen_func")
for number_k in generator_func:
    print(number_k)
