from typing import Callable, Any
from functools import wraps


# def counter(func: Callable, count=[0]) -> Callable:
#     """Декоратор который считает количество вызовов обернутых функций"""
#     @wraps(func)
#     def wrap(*args, **kwargs) -> Any:
#         count[0] += 1
#         print(f"Декоратор сработал {count[0]} раз.")
#         return func(*args, **kwargs), count[0]
#
#     return wrap

def counter(func: Callable) -> Callable:
    """Декоратор который считает количество вызовов обернутых функций"""

    @wraps(func)
    def wrap(*args, **kwargs) -> Any:
        wrap.count += 1
        print(f"Функция {func.__name__} была вызвана {wrap.count} раз.")
        return func(*args, **kwargs)

    wrap.count = 0
    return wrap


@counter
def test(count) -> None:
    for i in range(count):
        print("Счетчик внутри функции: ", i)


@counter
def another_test(count) -> None:
    for i in range(count):
        print("Счетчик внутри функции: ", i)


test(4)
test(4)
another_test(4)
