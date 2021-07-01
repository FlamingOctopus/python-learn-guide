import datetime
from collections.abc import Callable
import functools, time, string


def timer(func: Callable, cls_name, date_format) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        date_time = datetime.datetime.now()
        date_time = date_time.strftime(date_format)
        print(f"- Запускается {cls_name}.{func.__name__}. Дата и время запуска: {date_time}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"- Завершение {cls_name}.{func.__name__}, время работы = {round(end - start, 3)}s")
        return result

    return wrapped


def log_methods(date_format) -> Callable:
    new_date_format = ""
    for i_sym in date_format:
        if i_sym in string.ascii_letters:
            new_date_format += ('%' + i_sym)
        else:
            new_date_format += i_sym

    @functools.wraps(timer)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                curr_method = getattr(cls, i_method_name)
                decorated_method = timer(curr_method, cls_name=cls.__name__, date_format=new_date_format)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
