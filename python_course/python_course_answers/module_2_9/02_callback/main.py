import functools
from typing import Callable

app = dict()


def callback(elem: str) -> Callable:
    def call_wrapped(func: Callable) -> Callable:
        app[elem] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return call_wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
