from typing import Any, Iterable


class LinkedListMember:
    """Класс-узел связанного списка"""

    def __init__(self, current, next=None) -> None:
        self.current = current
        self.next = next

    def __str__(self) -> str:
        return f"--[{self.current}]--"


class LinkedList:
    """Класс односвязанного списка"""

    def __init__(self) -> None:
        self.begin = None
        self.length = 0
        self.__counter = 0

    def append(self, obj: Any) -> None:
        """Метод реализующий добавление объекта в список
        temp: узел списка
        tail:хвост списка"""
        temp = LinkedListMember(obj)
        if self.begin is None:
            self.begin = temp
            return
        tail = self.begin
        while tail.next:
            tail = tail.next
        tail.next = temp
        self.length += 1

    def remove(self, index: int) -> None:
        """Метод реализующий удаление объекта из списка
        current_data: текущий узел
        current_index: индекс текущего узла
        index: индекс узла который надо удалить
        IndexError: возбуждается если индекс больше длинны
        списка"""
        current_data = self.begin
        current_index = 0
        if self.length == 0 or self.length < index:
            raise IndexError
        if current_data is not None:
            if index == 0:
                self.begin = current_data.next
                self.length -= 1
                return
        while current_data is not None:
            if current_index == index:
                break
            temp = current_data
            current_data = current_data.next
            current_index += 1
        temp.next = current_data.next
        self.length -= 1

    def __next__(self) -> None:
        """Возвращает следующий элемент списка"""
        if self.__counter == 0:
            self.__counter += 1

            return self.begin

        elif self.length >= self.__counter:
            if self.__counter == 1:
                self.temp_for_iter = self.begin

            self.temp_for_iter = self.temp_for_iter.next
            self.__counter += 1
            return self.temp_for_iter

        else:
            raise StopIteration

    def __iter__(self) -> Iterable:
        """Возвращает итерируемый объект"""
        return self

    def get(self, index: int) -> None:
        """Метод реализующий получение объекта из списка
        __start_obj: узел с которого начинается перебор для поиска удаляемого узла
        __start_index: индекс с которого начинается перебор для поиска удаляемого узла
        index: переданный индекс
        """
        __start_obj = self.begin
        __start_index = 0
        while __start_index <= index:
            if __start_index == index:
                return __start_obj.current
            __start_index = __start_index + 1
            __start_obj = __start_obj.next

    def __str__(self) -> str:
        if self.begin is not None:
            current = self.begin
            values = [str(current.current)]
            while current.next is not None:
                current = current.next
                values.append(str(current.current))
            return f'[{values}]'
        return "[]"


my_list = LinkedList()

my_list.append(10)

my_list.append(20)

my_list.append(30)

my_list.append(40)

print("Итерируемся по списку:")

for i in my_list:
    print(i, end='')

print('\nТекущий список:', my_list)

print('Получение третьего элемента:', my_list.get(2))

print('Удаление 4 элемента.')

my_list.remove(3)

print('Новый список:', my_list)
