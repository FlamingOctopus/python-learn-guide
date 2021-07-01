from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorator):
    @functools.wraps(decorator)
    def wrapped(*args, **kwargs) -> Callable:
        return decorator(*args, **kwargs)

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*func_args, **func_kwargs) -> Any:
            print('Переданные арги и кварги в декоратор:', args, kwargs)
            result = func(*func_args, **func_kwargs)
            return result

        return wrapped

    return decorator


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)