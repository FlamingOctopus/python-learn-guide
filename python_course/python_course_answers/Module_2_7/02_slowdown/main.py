from time import sleep
from typing import Callable, Any
from functools import wraps


def slowing(func: Callable) -> Callable:
    """Декоратор который добавляет ожидание перед функцией 2 секунды"""
    @wraps(func)
    def wrap(*args, **kwargs) -> Any:
        sleep(2)
        return func(*args, **kwargs)

    return wrap


@slowing
def req_test_func(count: int) -> None:
    print(f"Осталось еще {count} раз")
    if count < 1:
        return
    req_test_func(count - 1)


req_test_func(4)
