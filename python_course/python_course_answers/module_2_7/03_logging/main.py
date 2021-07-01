from typing import Callable, Any
from functools import wraps
import datetime


def logging(func: Callable) -> Callable:
    """Декоратор который записывает ошибки в файл"""
    @wraps(func)
    def wrap(*args, **kwargs) -> Any:
        try:
            message = f"Название функции: {func.__name__}, это {func.__doc__}"
            print(message)
            func(*args, **kwargs)
        except Exception as e:
            with open('function_errors.log', 'a') as error_log_file:
                error_log_file.write(f"({datetime.datetime.now()}) : {message}. В ней возникла ошибка: {e}\n")

    return wrap


@logging
def test_func(count: int) -> None:
    """Рекурсивная функция счетчик"""
    if count > 10:
        raise Exception("Слишком большое число")
    if count < 0:
        return
    print(f"Осталось {count} раз")
    test_func(count - 1)


test_func(4)
test_func(11)
