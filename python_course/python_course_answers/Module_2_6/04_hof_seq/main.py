from typing import Iterable


class Sequence:
    def __init__(self, numbers_list: list) -> None:
        self.numbers_list = numbers_list

    def __next__(self) -> int:
        try:
            if not (self.numbers_list[1]== 1 and self.numbers_list[0] == 1):
                raise StopIteration("Неверные параметры, последовательность завершена")
            seq_hof = self.numbers_list[-self.numbers_list[-1]] + self.numbers_list[-self.numbers_list[-2]]
            self.numbers_list.append(seq_hof)
            return seq_hof
        except IndexError:
            raise StopIteration("Передано неправильное количество аргументов")

    def __iter__(self) -> Iterable:
        return self


first_sequence = Sequence([1, 1])

print("Первая последовательность")
for i in range(20):
    print(next(first_sequence))

print("Вторая последовательность")
second_sequence = Sequence([1, 2])
for i in range(20):
    print(next(second_sequence))
