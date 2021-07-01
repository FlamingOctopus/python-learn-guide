from collections.abc import Callable
import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapped() -> Callable:
        if not hasattr(cls, 'instance'):
            cls.instance = cls.__new__
        return cls.instance

    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)