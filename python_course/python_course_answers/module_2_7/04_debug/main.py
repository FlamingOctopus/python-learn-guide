
from typing import Callable, Any
from functools import wraps


def debug(func: Callable) -> Callable:
    """Декоратор для дебаггинга"""
    @wraps(func)
    def wrap(*args, **kwargs) -> Any:
        result = func(*args,**kwargs)
        print(f"Вызывается {func.__name__}{args,kwargs}\n"
              f"'{func.__name__}' вернула значение '{result}'")
        print(result)
    return wrap



@debug
def greeting(name, age=None):

    if age:

        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)

    else:

        return "Привет, {name}!".format(name=name)



greeting("Том")

greeting("Миша", age=100)

greeting(name="Катя", age=16)

