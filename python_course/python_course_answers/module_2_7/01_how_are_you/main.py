from functools import wraps
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """Функция-декоратор которая спрашивает "Как дела?"
           перед выполнением декорируемой функции"""
    @wraps(func)
    def wrap(*args, **kwargs) -> Any:
        input("Как дела?")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)

    return wrap


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def sq_generator(range: int, count=0) -> int:
    while True:
        count += 1
        if count >= range:
            return
        yield count ** 2


test()
gen = sq_generator(4)

for i in gen:
    print(i)
