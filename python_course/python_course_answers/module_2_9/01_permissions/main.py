from collections.abc import Callable
import functools


def check_permission(user: str) -> Callable:
    def check_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            except PermissionError as error:
                print(f'PermissionError: {error}')

        return wrapped

    return check_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
