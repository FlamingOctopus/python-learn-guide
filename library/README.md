# Тут собраны примеры работы с различными библиотеками и прочее для себя


1. [Тесты  и логирование](#test)
1. [Aiogram](#Aiogram)
1. [Alembic](#Alembic)
1. [Асинхронность](#async)
1. [Sqlalchemy](#sqlalchemy)
   1. [Отправить в бд](#Отправитьвбд)
   1. [Типы данных для таблиц](#Типыданныхдлятаблиц)
   1. [Пример отправки транзакциями](#Примеротправкитранзакциями)
   1. [Вывод из бд](#Выводизбд)
   1. [Вывод из бд одного зкземпляра](#Выводизбдодногоэкземпляра)
   1. [Транзакции](#Транзакции)
   1. [Работа с запросами ForeignKey](#РаботасзапросамиForeignKey)
   1. [Методы](#Методы)
   1. [Основные степени ленивости](#Основныестепени)
   1. [Удаление и обновление](#Удалениеиобновление)
   1. [Пример отношения1 ко многим](#Примеротношения1комногим)
   1. [Пример инициализации базы](#Примеринициализациибазы)
   1. [Примеры разных запросов](#Примерыразныхзапросов)
   1. [Пример запросов без связывания с классами](#Примерзапросовбезсвязываниясклассами)
   1. [Пример со связываниями с классами](#Примерсосвязываниямисклассами)
   1. [Пример работы с классической орм](#Примерработысклассическойорм)
   1. [Пример запросов на классической версии](#Примерзапросовнаклассическойверсии)
   1. [Многие ко многим](#Многиекомногим)
1. [Парсинг](#scrap)
1. [Библиотеки](#lib)
    1. [ftplib](#ftplib)
    2. [json](#json)
    3. [Время](#time)
    4. [hash](#hash)
    5. [jinja](#jinja)
    6. [прогресс выполнения в Python](#progress)
    7. [Сервер](#server)
    8. [Работа с файлами](#work_with_files)
        1. [csv](#csv)
        2. [xml](#xml)
        3. [pillow](#pillow)
        4. [pdf](#pdf)
        5. [pickle](#pickle)
        6. [OS и OS.path](#os)
    9. [аргументы командной строки](#args)
1. [Цикл разработки сайта ](#site)

## Тесты  и логирование <a name="test"></a>
### unittest(не рекомендуется, нарушает SOLID)

https://docs.python.org/3/library/unittest.html#re-using-old-test-code
https://ru.hexlet.io/courses/advanced_python/lessons/python_testing_unittest/theory_unit
https://pythonworld.ru/moduli/modul-unittest.html

### pytest

### logging

https://python-scripts.com/logging-python


## Aiogram<a name="Aiogram"></a>
[Деплой бота на сервер](https://bitbucket.org/vkasatkin/tele_bot/src/master/ubuntu18/)
[Решение проблемы с распаковкой коллбэк даты](https://github.com/Abstract-X/tgbotcallback)
[Коннект бд](https://t.me/botfatherdev/218)
## Alembic<a name="Alembic"></a>
alembic init migrations(или другое название)
target_metadata = Base.metadata
url = config.get_main_option("sqlite:///tg.db")

alembic upgrade head
alembic revision --autogenerate -m ""
## Асинхронность <a name="async"></a>
import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

Представим 2 блокирующие задачи: gr1 и gr2, как будто они обращаются к неким сторонним сервисам, и, пока они ждут ответа, третья функция может работать асинхронно.

import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr1 ended work: {}'.format(tic()))


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 Ended work: {}'.format(tic()))


async def gr3():
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print("Done!")


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()


import random
from time import sleep
import asyncio


def task(pid):
    """Synchronous non-deterministic task.
    """
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


async def task_coro(pid):
    """Coroutine non-deterministic task
    """
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)


print('Synchronous:')
synchronous()

ioloop = asyncio.get_event_loop()
print('Asynchronous:')
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 1c-determinism-sync-async-asyncio-await.py
Synchronous:
Task 1 done
Task 2 done
Task 3 done
Task 4 done
Task 5 done
Task 6 done
Task 7 done
Task 8 done
Task 9 done
Asynchronous:
Task 2 done
Task 5 done
Task 6 done
Task 8 done
Task 9 done
Task 1 done
Task 4 done
Task 3 done
Task 7 done


import time
import urllib.request
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def fetch_sync(pid):
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    return datetime


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp.request('GET', URL)
    datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


print('Synchronous:')
synchronous()

print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()


import time
import random
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print('Fetch async process {} started, sleeping for {} seconds'.format(
        pid, sleepy_time))

    await asyncio.sleep(sleepy_time)

    response = await aiohttp.request('GET', URL)
    datetime = response.headers.get('Date')

    response.close()
    return 'Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start)


async def asynchronous():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print('{} {}'.format(">>" * (i + 1), result))

    print("Process took: {:.2f} seconds".format(time.time() - start))


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

Функция as_completed возвращает итератор, который выдаёт результаты корутин по мере их выполнения. 
Круто же, правда?! Кстати, и as_completed, и wait — функции из пакета concurrent.futures.

Ещё один пример — что если вы хотите узнать свой IP адрес. Есть куча сервисов для этого, но вы не знаете какой из них будет доступен в момент работы программы. Вместо того, чтобы последовательно опрашивать каждый из списка, можно запустить все запросы конкурентно и выбрать первый успешный.

Что ж, для этого в нашей любимой функции wait есть специальный параметр return_when. До сих пор мы игнорировали то, что возвращает wait, т.к. только распараллеливали задачи. Но теперь нам надо получить результат из корутины, так что будем использовать набор футур done и pending.

from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    response = await aiohttp.request('GET', service.url)
    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)

    print(done.pop().result())


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 2c-fetch-first-ip-address-response-await.py
Fetching IP from ip-api
Fetching IP from ipify
ip-api finished with result: 82.34.76.170, took: 0.09 seconds
Unclosed client session
client_session: <aiohttp.client.ClientSession object at 0x10f95c6d8>
Task was destroyed but it is pending!
task: <Task pending coro=<fetch_ip() running at 2c-fetch-first-ip-address-response.py:20> wait_for=<Future pending cb=[BaseSelectorEventLoop._sock_connect_done(10)(), Task._wakeup()]>>

Что же случилось? Первый сервис ответил успешно, но в логах какое-то предупреждение!

На самом деле мы запустили выполнение двух задач, но вышли из цикла уже после первого результата, в то время как вторая корутина ещё выполнялась. Asyncio подумал что это баг и предупредил нас. Наверно, стоит прибираться за собой и явно убивать ненужные задачи. Как? Рад, что вы спросили.


Состояния футур

ожидание (pending)
выполнение (running)
выполнено (done)
отменено (cancelled)

Всё настолько просто. Когда футура находится в состояние done, у неё можно получить результат выполнения. В состояниях pending и running такая операция приведёт к исключению InvalidStateError, а в случае canelled будет CancelledError, и наконец, если исключение произошло в самой корутине, оно будет сгенерировано снова (также, как это сделано при вызове exception). Но не верьте мне на слово.

Вы можете узнать состояние футуры с помощью методов done, cancelled или running, но не забывайте, что в случае done вызов result может вернуть как ожидаемый результат, так и исключение, которое возникло в процессе работы. Для отмены выполнения футуры есть метод cancel. Это подходит для исправления нашего примера.

from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    response = await aiohttp.request('GET', service.url)
    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)

    print(done.pop().result())

    for future in pending:
        future.cancel()


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 2c-fetch-first-ip-address-response-no-warning-await.py
Fetching IP from ipify
Fetching IP from ip-api
ip-api finished with result: 82.34.76.170, took: 0.08 seconds

Простой и аккуратный вывод — как раз то, что я люблю!

Если вам нужна некоторая дополнительная логика по обработке футур, то вы можете подключать коллбэки, которые будут вызваны при переходе в состояние done. Это может быть полезно для тестов, когда некоторые результаты надо переопределить какими-то своими значениями.


Обработка исключений

asyncio — это целиком про написание управляемого и читаемого конкурентного кода, что хорошо заметно при обработке исключений. Вернёмся к примеру, чтобы продемонстрировать.
Допустим, мы хотим убедиться, что все запросы к сервисам по определению IP вернули одинаковый результат. Однако, один из них может быть оффлайн и не ответить нам. Просто применим try...except как обычно:

from collections import namedtuple
import time
import asyncio
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
    Service('borken', 'http://no-way-this-is-going-to-work.com/json', 'ip')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    try:
        response = await aiohttp.request('GET', service.url)
    except:
        return '{} is unresponsive'.format(service.name)

    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, _ = await asyncio.wait(futures)

    for future in done:
        print(future.result())


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 3a-fetch-ip-addresses-fail-await.py
Fetching IP from ip-api
Fetching IP from borken
Fetching IP from ipify
ip-api finished with result: 85.133.69.250, took: 0.75 seconds
ipify finished with result: 85.133.69.250, took: 1.37 seconds
borken is unresponsive

Мы также можем обработать исключение, которое возникло в процессе выполнения корутины:

from collections import namedtuple
import time
import asyncio
import aiohttp
import traceback

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'this-is-not-an-attr'),
    Service('borken', 'http://no-way-this-is-going-to-work.com/json', 'ip')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    try:
        response = await aiohttp.request('GET', service.url)
    except:
        return '{} is unresponsive'.format(service.name)

    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done, _ = await asyncio.wait(futures)

    for future in done:
        try:
            print(future.result())
        except:
            print("Unexpected error: {}".format(traceback.format_exc()))


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 3b-fetch-ip-addresses-future-exceptions-await.py
Fetching IP from ipify
Fetching IP from borken
Fetching IP from ip-api
ipify finished with result: 85.133.69.250, took: 0.91 seconds
borken is unresponsive
Unexpected error: Traceback (most recent call last):
 File “3b-fetch-ip-addresses-future-exceptions.py”, line 39, in asynchronous
 print(future.result())
 File “3b-fetch-ip-addresses-future-exceptions.py”, line 26, in fetch_ip
 ip = json_response[service.ip_attr]
KeyError: ‘this-is-not-an-attr’

Точно также, как и запуск задачи без ожидания её завершения является ошибкой, так и получение неизвестных исключений оставляет свои следы в выводе:

from collections import namedtuple
import time
import asyncio
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'this-is-not-an-attr'),
    Service('borken', 'http://no-way-this-is-going-to-work.com/json', 'ip')
)


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    try:
        response = await aiohttp.request('GET', service.url)
    except:
        print('{} is unresponsive'.format(service.name))
    else:
        json_response = await response.json()
        ip = json_response[service.ip_attr]

        response.close()
        print('{} finished with result: {}, took: {:.2f} seconds'.format(
            service.name, ip, time.time() - start))


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    await asyncio.wait(futures)  # intentionally ignore results


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

$ python3 3c-fetch-ip-addresses-ignore-exceptions-await.py
Fetching IP from ipify
Fetching IP from borken
Fetching IP from ip-api
borken is unresponsive
ipify finished with result: 85.133.69.250, took: 0.78 seconds
Task exception was never retrieved
future: <Task finished coro=<fetch_ip() done, defined at 3c-fetch-ip-addresses-ignore-exceptions.py:15> exception=KeyError(‘this-is-not-an-attr’,)>
Traceback (most recent call last):
 File “3c-fetch-ip-addresses-ignore-exceptions.py”, line 25, in fetch_ip
 ip = json_response[service.ip_attr]
KeyError: ‘this-is-not-an-attr’

Вывод выглядит также, как и в предыдущем примере за исключением укоризненного сообщения от asyncio.



Таймауты

А что, если информация о нашем IP не так уж важна? Это может быть хорошим дополнением к какому-то составному ответу, в котором эта часть будет опциональна. В таком случае не будем заставлять пользователя ждать. В идеале мы бы ставили таймаут на вычисление IP, после которого в любом случае отдавали ответ пользователю, даже без этой информации.

И снова у wait есть подходящий аргумент:

import time
import random
import asyncio
import aiohttp
import argparse
from collections import namedtuple
from concurrent.futures import FIRST_COMPLETED

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
)

DEFAULT_TIMEOUT = 0.01


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    await asyncio.sleep(random.randint(1, 3) * 0.1)
    try:
        response = await aiohttp.request('GET', service.url)
    except:
        return '{} is unresponsive'.format(service.name)

    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    print('{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start))
    return ip


async def asynchronous(timeout):
    response = {
        "message": "Result from asynchronous.",
        "ip": "not available"
    }

    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, timeout=timeout, return_when=FIRST_COMPLETED)

    for future in pending:
        future.cancel()

    for future in done:
        response["ip"] = future.result()

    print(response)


parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--timeout',
    help='Timeout to use, defaults to {}'.format(DEFAULT_TIMEOUT),
    default=DEFAULT_TIMEOUT, type=float)
args = parser.parse_args()

print("Using a {} timeout".format(args.timeout))
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous(args.timeout))
ioloop.close()


Я также добавил аргумент timeout к строке запуска скрипта, чтобы проверить что же произойдёт, если запросы успеют обработаться. Также я добавил случайные задержки, чтобы скрипт не завершался слишком быстро, и было время разобраться как именно он работает.

$ python 4a-timeout-with-wait-kwarg-await.py
Using a 0.01 timeout
Fetching IP from ipify
Fetching IP from ip-api
{‘message’: ‘Result from asynchronous.’, ‘ip’: ‘not available’}

$ python 4a-timeout-with-wait-kwarg-await.py -t 5
Using a 5.0 timeout
Fetching IP from ip-api
Fetching IP from ipify
ipify finished with result: 82.34.76.170, took: 1.24 seconds
{'ip': '82.34.76.170', 'message': 'Result from asynchronous.'}

import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')

    print('DONE:', subreddit + '\n')

def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_reddit_top('python', client))
asyncio.ensure_future(get_reddit_top('programming', client))
asyncio.ensure_future(get_reddit_top('compsci', client))
loop.run_forever()


import asyncio

async def handle_tcp_echo(reader, writer):
    print('Connection from {}'.format(
        writer.get_extra_info('peername')
    ))
    while True:
        data = await reader.read(100)
        if data:
            message = data.decode()
            print("Echoing back: {!r}".format(message))
            writer.write(data)
            await writer.drain()
        else:
            print("Terminating connection")
            writer.close()
            break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(
            asyncio.start_server(handle_tcp_echo, '127.0.0.1', 7777),
            loop=loop
        )
    )
    loop.run_forever()


import signal  
import sys  
import asyncio  
import aiohttp  
import json

loop = asyncio.get_event_loop()  
client = aiohttp.ClientSession(loop=loop)

async def get_json(client, url):  
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):  
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')

    print('DONE:', subreddit + '\n')

def signal_handler(signal, frame):  
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_reddit_top('python', client))  
asyncio.ensure_future(get_reddit_top('programming', client))  
asyncio.ensure_future(get_reddit_top('compsci', client))  
loop.run_forever()






run()
create_task()
футуры
sleep
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )


async def Coro() :
    ...

# В Python 3.7+
задача = asyncio.create_task(Coro())
...

# Это работает во всех версиях Python, но менее читабельно
задача = asyncio.fecure_future(Coro())

gather
shield

asyncio.wait
async def foo():
    return 42

task = asyncio.create_task(foo())
done, pending = await asyncio.wait({task})

if task in done:
    # Everything will work as expected now.

wait_for

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
# timeout!


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54

asyncio.run_coroutine_threadsafe
# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
If an exception is raised in the coroutine, the returned Future will be notified. It can also be used to cancel the task in the event loop:

try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')

asyncio.current_task
get_running_loop()

asyncio.all_tasks

asyncio.Task
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
# cancel_me(): before sleep
# cancel_me(): cancel sleep
# cancel_me(): after sleep
# main(): cancel_me is cancelled now
cancelled()¶
Return True if the Task is cancelled.

The Task is cancelled when the cancellation was requested with cancel() and the wrapped coroutine propagated the CancelledError exception thrown into it.

done()¶
Return True if the Task is done.

A Task is done when the wrapped coroutine either returned a value, raised an exception, or the Task was cancelled.

result()¶
Return the result of the Task.

If the Task is done, the result of the wrapped coroutine is returned (or if the coroutine raised an exception, that exception is re-raised.)

If the Task has been cancelled, this method raises a CancelledError exception.

If the Task’s result isn’t yet available, this method raises a InvalidStateError exception.

exception()¶
Return the exception of the Task.

If the wrapped coroutine raised an exception that exception is returned. If the wrapped coroutine returned normally this method returns None.

If the Task has been cancelled, this method raises a CancelledError exception.

If the Task isn’t done yet, this method raises an InvalidStateError exception.

add_done_callback(callback, *, context=None)¶
Add a callback to be run when the Task is done.

This method should only be used in low-level callback-based code.

See the documentation of Future.add_done_callback() for more details.

remove_done_callback(callback)¶
Remove callback from the callbacks list.

This method should only be used in low-level callback-based code.

See the documentation of Future.remove_done_callback() for more details.

get_stack(*, limit=None)¶
Return the list of stack frames for this Task.

If the wrapped coroutine is not done, this returns the stack where it is suspended. If the coroutine has completed successfully or was cancelled, this returns an empty list. If the coroutine was terminated by an exception, this returns the list of traceback frames.

The frames are always ordered from oldest to newest.

Only one stack frame is returned for a suspended coroutine.

The optional limit argument sets the maximum number of frames to return; by default all available frames are returned. The ordering of the returned list differs depending on whether a stack or a traceback is returned: the newest frames of a stack are returned, but the oldest frames of a traceback are returned. (This matches the behavior of the traceback module.)

print_stack(*, limit=None, file=None)¶
Print the stack or traceback for this Task.

This produces output similar to that of the traceback module for the frames retrieved by get_stack().

The limit argument is passed to get_stack() directly.

The file argument is an I/O stream to which the output is written; by default output is written to sys.stderr.

get_coro()¶
Return the coroutine object wrapped by the Task.

New in version 3.8.

get_name()¶
Return the name of the Task.

If no name has been explicitly assigned to the Task, the default asyncio Task implementation generates a default name during instantiation.

New in version 3.8.

set_name(value)¶
Set the name of the Task.

The value argument can be any object, which is then converted to a string.

In the default Task implementation, the name will be visible in the repr() output of a task object.

New in version 3.8.

Concurrency and Multithreading
An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task.

To schedule a callback from another OS thread, the loop.call_soon_threadsafe() method should be used. Example:

loop.call_soon_threadsafe(callback, *args)
Almost all asyncio objects are not thread safe, which is typically not a problem unless there is code that works with them from outside of a Task or a callback. If there’s a need for such code to call a low-level asyncio API, the loop.call_soon_threadsafe() method should be used, e.g.:

loop.call_soon_threadsafe(fut.cancel)
To schedule a coroutine object from a different OS thread, the run_coroutine_threadsafe() function should be used. It returns a concurrent.futures.Future to access the result:

async def coro_func():
     return await asyncio.sleep(1, 42)

# Later in another OS thread:

future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
# Wait for the result:
result = future.result()
To handle signals and to execute subprocesses, the event loop must be run in the main thread.

The loop.run_in_executor() method can be used with a concurrent.futures.ThreadPoolExecutor to execute blocking code in a different OS thread without blocking the OS thread that the event loop runs in.

There is currently no way to schedule coroutines or callbacks directly from a different process (such as one started with multiprocessing). The Event Loop Methods section lists APIs that can read from pipes and watch file descriptors without blocking the event loop. In addition, asyncio’s Subprocess APIs provide a way to start a process and communicate with it from the event loop. Lastly, the aforementioned loop.run_in_executor() method can also be used with a concurrent.futures.ProcessPoolExecutor to execute code in a different process.

Running Blocking Code
Blocking (CPU-bound) code should not be called directly. For example, if a function performs a CPU-intensive calculation for 1 second, all concurrent asyncio Tasks and IO operations would be delayed by 1 second.

An executor can be used to run a task in a different thread or even in a different process to avoid blocking the OS thread with the event loop. See the loop.run_in_executor() method for more details.
Queues
Source code: Lib/asyncio/queues.py

asyncio queues are designed to be similar to classes of the queue module. Although asyncio queues are not thread-safe, they are designed to be used specifically in async/await code.

Note that methods of asyncio queues don’t have a timeout parameter; use asyncio.wait_for() function to do queue operations with a timeout.

See also the Examples section below.

Queue
class asyncio.Queue(maxsize=0, *, loop=None)
A first in, first out (FIFO) queue.

If maxsize is less than or equal to zero, the queue size is infinite. If it is an integer greater than 0, then await put() blocks when the queue reaches maxsize until an item is removed by get().

Unlike the standard library threading queue, the size of the queue is always known and can be returned by calling the qsize() method.

Deprecated since version 3.8, will be removed in version 3.10: The loop parameter.

This class is not thread safe.

maxsize
Number of items allowed in the queue.

empty()
Return True if the queue is empty, False otherwise.

full()
Return True if there are maxsize items in the queue.

If the queue was initialized with maxsize=0 (the default), then full() never returns True.

coroutine get()
Remove and return an item from the queue. If queue is empty, wait until an item is available.

get_nowait()
Return an item if one is immediately available, else raise QueueEmpty.

coroutine join()
Block until all items in the queue have been received and processed.

The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer coroutine calls task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, join() unblocks.

coroutine put(item)
Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.

put_nowait(item)
Put an item into the queue without blocking.

If no free slot is immediately available, raise QueueFull.

qsize()
Return the number of items in the queue.

task_done()
Indicate that a formerly enqueued task is complete.

Used by queue consumers. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.

If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).

Raises ValueError if called more times than there were items placed in the queue.

Priority Queue
class asyncio.PriorityQueue
A variant of Queue; retrieves entries in priority order (lowest first).

Entries are typically tuples of the form (priority_number, data).

LIFO Queue
class asyncio.LifoQueue
A variant of Queue that retrieves most recently added entries first (last in, first out).

Exceptions
exception asyncio.QueueEmpty
This exception is raised when the get_nowait() method is called on an empty queue.

exception asyncio.QueueFull
Exception raised when the put_nowait() method is called on a queue that has reached its maxsize.

Examples
Queues can be used to distribute workload between several concurrent tasks:

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())





## SQLALCHEMY <a name="sqlalchemy"></a>
[Внизу настройки для разных бд](https://coderlessons.com/tutorials/bazy-dannykh/sqlalchemy/sqlalchemy-kratkoe-rukovodstvo)

[Отношения в таблице](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)

В SQLALCHEMY есть три подхода декларативный, классический и связывания(mapping)


### Отправить в бд <a name="Отправитьвбд"></a>
```python
ins = users.insert().values(name='jack', fullname='Jack Jones')

conn.execute(address_table.insert(),
             [{"user_id": 1,
               "email_address": "ed@ed.com"},
              {"user_id": 1,
               "email_address": "ed@gmail.com"},
              {"user_id": 2,
               "email_address": "jack@yahoo.com"},
              {"user_id": 3,
               "email_address": "wendy@gmail.com"}, ])
```
### Типы данных для таблиц <a name="Типыданныхдлятаблиц"></a>
![](img.png)
### Пример отправки транзакциями <a name="Примеротправкитранзакциями"></a>
```python
author_one = Author(name="НеЛутц") 
s.add(author_one) 
s.commit()
book_one = Book(title="Чистый Python", author_id=1, genre="компьютерная литература", price=1500) 
s.add(book_one) 
s.commit()

s.add_all([Book(title="Чистый Чистый Python", author_id=1, genre="компьютерная литература", price=500),
           Book(title="НеЧистый Python", author_id=2, genre="компьютерная литература", price=2500),
           Book(title="Python как Питон", author_id=1, genre="компьютерная литература", price=2976)  
           ])
s.commit()
```

### Вывод из бд <a name="Выводизбд"></a>
```python
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Users
engine = create_engine('sqlite:///tg.db', echo=True)
conn = engine.connect()
s = select(Users)
result = conn.execute(s)
for i in result():
    print(i)
for id, name, fullname in result:
    print("name:", name, "; fullname: ", fullname)
for row in result:
    print("name:", row.name, "; fullname: ", row.fullname)

result = conn.execute(s)
row = result.fetchone()
print("name:", row._mapping['name'], "; fullname:", row._mapping['fullname'])
row = result.fetchone()
name, fullname = row["name"], row["fullname"]
row = result.fetchone()
print("name:", row[1], "; fullname:", row[2])
for row in conn.execute(s):
    print("name:", row._mapping[users.c.name], "; fullname:", row._mapping[users.c.fullname])
result.close()
```
    
### Вывод из бд одного экземпляра <a name="Выводизбдодногоэкземпляра"></a>
```python
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
session().query(Users).filter(Users.id == 1).one().id
emmployee = session().query(Users).all()

is_exists = session.query(exists().where(Department.name == department_name)).scalar()
```

### Транзакции <a name="Транзакции"></a>
```python
sqlalchemy.engine.Engine.execute() # автоматически подтверждает транзакцию в текущем соединении (выполняет COMMIT)
engine.execute("insert into employee_of_month (emp_name) values (:emp_name)", emp_name='fred')
```
Мы можем контролировать соединение используя метод 
```python
sqlalchemy.engine.Engine.connect()
```
```python
conn = engine.connect()
result = conn.execute("select * from employee")
result.fetchall()
conn.close()
```
Он также дает возможность управлять транзакциями. Транзакция является объектом класса sqlalchemy.engine.Transaction и содержит в себе следующие методы:
```python
sqlalchemy.engine.Transaction.close() # выполняет rollback
sqlalchemy.engine.Transaction.commit() # подтверждает транзакцию
sqlalchemy.engine.Transaction.rollback() # отменяет транзакцию
sqlalchemy.engine.Transaction.commit() # позволяет вам вручную подтвердить транзакцию.
```
Пример
```python
def dispatch_order(order_id):
    # проверка того, правильно ли указан order_id
    order = session.query(Order).get(order_id)

    if not order:
        raise ValueError("Недействительный order_id: {}.".format(order_id))

    try:
        for i in order.line_items:
            i.item.quantity = i.item.quantity - i.quantity

        order.date_placed = datetime.now()
        session.commit()
        print("Транзакция завершена.")

    except IntegrityError as e:
        print(e)
        print("Возврат назад...")
        session.rollback()
        print("Транзакция не удалась.")
dispatch_order(1)
```
### Работа с запросами ForeignKey <a name="РаботасзапросамиForeignKey"></a>
```python
# Используем join(), чтобы найти всех покупателей, у которых как минимум один заказ.
session.query(Customer).join(Order).all()session.query(Customer.id, Customer.username, Order.id).join(Order).all()

join_obj = user_table.join(address_table,
                           user_table.c.id == address_table.c.user_id)
join_obj = user_table.join(address_table)
print(join_obj)

session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()

# Создать FULL OUTER JOIN можно, передав в метод full=True. Например:
session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order, full=True).all()
# В этом запросе левой таблицей является customers. Это значит, что он вернет все записи из customers и только те, 
# которые соответствуют условию, из orders.

# Следующий запрос использует join() и group_by() для подсчета количества заказов, сделанных Dmitriy Yatsenko.
from sqlalchemy import func

session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'Dmitriy',
    Customer.last_name == 'Yatsenko',
).group_by(Customer.id).scalar()

c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
session.add(c1)
session.commit()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
   print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))

session.query(Customer).join(Invoice).filter(Invoice.amount == 8500).all()

result = session.query(Customer).join(Invoice).filter(Invoice.amount == 8500)
for row in result:
   for inv in row.invoices:
      print (row.id, row.name, inv.invno, inv.amount)

query.join (Счет, id == Address.custid)	явное условие
query.join (Customer.invoices)	указать отношения слева направо
query.join (Invoice, Customer.invoices)	то же самое, с явной целью
query.join (‘счета’)	то же самое, используя строку

s = session.query(Customer).filter(Invoice.invno.__eq__(12))
s = session.query(Customer).filter(Invoice.custid.__ne__(2))
s = session.query(Invoice).filter(Invoice.invno.contains([3,4,5]))
s = session.query(Customer).filter(Customer.invoices.any(Invoice.invno==11))
s = session.query(Invoice).filter(Invoice.customer.has(name = 'Arjun Pandit'))

from sqlalchemy.orm import subqueryload
c1 = session.query(Customer).options(subqueryload(Customer.invoices)).filter_by(name = 'Govind Pant').one()
print (c1.name, c1.address, c1.email)
for x in c1.invoices:
   print ("Invoice no : {}, Amount : {}".format(x.invno, x.amount))

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
x = session.query(Customer).get(2)
session.delete(x)
session.query(Customer).filter_by(name = 'Gopal Krishna').count()
session.query(Invoice).filter(Invoice.invno.in_([10,14])).count()
```

### Методы <a name="Методы"></a>
```python
all()	# Возвращает общее количество записей в запросе.
first()	# Возвращает первый результат из запроса или None, если записей нет.
scalar()	# Возвращает первую колонку первой записи или None, если результат пустой. Если записей несколько, то бросает исключение MultipleResultsFound.
one()	# Возвращает одну запись. Если их несколько, бросает исключение MutlipleResultsFound. Если данных нет, бросает NoResultFound.
get(pk)	# Возвращает объект по первичному ключу (pk) или None, если объект не был найден.
filter(*criterion)	# Возвращает экземпляр Query после применения оператора WHERE.
limit(limit)	# Возвращает экземпляр Query после применения оператора LIMIT.
offset(offset)	# Возвращает экземпляр Query после применения оператора OFFSET.
order_by(*criterion)	# Возвращает экземпляр Query после применения оператора ORDER BY. Чтобы сортировать по убыванию используйте функцию desc().
join(*props, **kwargs)	# Возвращает экземпляр Query после создания SQL INNER JOIN.
outerjoin(*props, **kwargs)	# Возвращает экземпляр Query после создания SQL LEFT OUTER JOIN.
group_by(*criterion) # Возвращает экземпляр Query после добавления оператора GROUP BY к запросу.
having(criterion)	# Возвращает экземпляр Query после добавления оператора HAVING.
count() # Считает количество подходящих экземпляров
exists() # Проверяет наличие значения в таблице
scalar() # возвращает объект или ноне если нет, если несколько исключение.
one() # возвращает объяект если есть, если нет исключение. 
distinct() # повторяющиеся записи
Метод like() выполняет поиск с учетом регистра. Для поиска совпадений без учета регистра используйте ilike().
sqlalchemy.sql.operators.ColumnOperators.__add__()	# add	+
sqlalchemy.sql.operators.ColumnOperators.__and__()	# and	&
sqlalchemy.sql.expression.ColumnElement.__eq__()	# equal	==
sqlalchemy.sql.operators.ColumnOperators.__ge__()	# greater equal	>=
sqlalchemy.sql.operators.ColumnOperators.__gt__()	# greater than	>
sqlalchemy.sql.expression.ColumnElement.__le__()	# less equal	<=
sqlalchemy.sql.expression.ColumnElement.__lt__()	# less than	<
sqlalchemy.sql.expression.ColumnElement.__ne__()	# not equal	!=
sqlalchemy.sql.operators.ColumnOperators.__or__()	# or	|
sqlalchemy.sql.operators.ColumnOperators.in_()	# in	in
sqlalchemy.sql.operators.ColumnOperators.notin_()	# not in	not in
cast() # приведение одного типа к другому
from sqlalchemy import cast, Date, distinct, union
session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all()

u = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com addresses.select().where(addresses.c.email_add.like('%@yahoo.com'))))
result = conn.execute(u)
result.fetchall()Функция union () # возвращает объект CompoundSelect из нескольких таблиц. Следующий пример демонстрирует его использование
u = union_all(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
# По умолчанию union() удаляет все повторяющиеся записи из результата. Для их сохранения используйте union_all().
u = except_(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))
# возвращает только те записи из таблицы адресов, которые имеют «gmail.com» в поле email_add, но исключают те, которые имеют «Pune» как часть поля postal_add.
u = intersect(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))
# Одна возвращает строки, содержащие «gmail.com», как часть столбца email_add, а другая возвращает строки, содержащие «Pune» как часть столбца postal_add. Результатом будут общие строки из обоих наборов результатов.

```
### Основные степени "ленивости" <a name="Основныестепени"></a>
* select — по умолчанию. ORM делает запрос только тогда, когда обращаются к данным. Осуществляется отдельным запросом.
* dynamic — позволяет получить объект запроса, который можно модифицировать по желанию. Получает данные из БД только после вызова all() или one() или любых других доступных методов.
* joined — в основной запрос добавляется с помощью LEFT JOIN. Выполняется сразу.
* subquery — похож на select, но выполняется как подзапрос.
* По умолчанию — select.

### Удаление и обновление <a name="Удалениеиобновление"></a>
```python
i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()
session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()

i = session.query(Item).filter(Item.name == 'Monitor').one()
session.delete(i)
session.commit()
session.query(Item).filter(
    Item.name.ilike("W%")
).delete(synchronize_session='fetch')
session.commit()
```
### Пример отношения 1 ко многим <a name="Примеротношения1комногим"></a>
```python
class Book(Base):  
    __tablename__ = 'Books'  
    
    id_book = Column(Integer, primary_key=True)  
    title = Column(String(250), nullable=False)  
    author_id = Column(Integer, ForeignKey("Authors.id_author"))  
    genre = Column(String(250))
    price = Column(Integer, nullable=False)
    Author = relationship("Author") 

class Author(Base):  
    __tablename__ = 'Authors'  
    
    id_author = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)  
    book = relationship("Book") # 1 ко многим

Base.metadata.create_all(engine)
```
### Пример инициализации базы <a name="Примеринициализациибазы"></a>
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_decl import Base, Book, Author
engine = create_engine("mysql+mysqlconnector://root:root@localhost/pylounge2", echo=True)
# Флаг echo включает ведение лога через стандартный модуль logging Питона.
# Когда он включен, мы увидим все созданные нами SQL-запросы. 
session = sessionmaker(bind=engine)
s = session()
author_one = Author(name="Лутц") 
s.add(author_one) 
s.commit()
```
### Примеры разных запросов <a name="Примерыразныхзапросов"></a>
```python
s.query(Book).first().title
for title, price in s.query(Book.title, Book.price).order_by(Book.title).limit(2):
    print(title, price)

for row in s.query(Book, Author).filter(Book.author_id == Author.id_author).filter(Book.price > 1000).group_by(Author.name):
    print(row.Book.title, ' ', row.Author.name)

print([(row.Book.title, row.Author.name) for row in s.query(Book, Author).join(Author).all()])

autor_query = s.query(Author).filter_by(Author.name == 'НеЛутц').one()
if autor_query != []:
    autor_query.name = 'Бизли' 
    s.add(autor_query)
    s.commit()

for row in session.query(Book).filter(Book.price > 1000): 
    print (row.title)
    
for row in session.query(Book, Author).filter(Book.author_id == Author.id_author).filter(Book.price > 1000):
    print(row.Book.title, ' ', row.Author.name)


second_book = session.query(Book).filter_by(id_book=3).one()
if second_book != []:
    second_book.price = 3000 
    session.add(second_book)
    session.commit()

second_book = session.query(Book).filter_by(id_book=2).one()
if second_book:
    print(second_book)
    # удаление
    session.delete(second_book)
    session.commit()

try:
    query_res = session.query(Book).filter_by(id_book=2).one()
except Exception as e:
    print(e)
else:
    print(query_res.price)
    

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')
session.add(c1)
session.commit())

session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
   Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)
session.commit()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Customers).all()
for row in result:
   print ("Name: ",row.name, "Address:",row.address, "Email:",row.email)

rows = [
   Customer(
      name = "Govind Kala", 
      address = "Gulmandi Aurangabad", 
      email = "kala@gmail.com", 
      invoices = [Invoice(invno = 7, amount = 12000), Invoice(invno = 8, amount = 18500)]),

   Customer(
      name = "Abdul Rahman", 
      address = "Rohtak", 
      email = "abdulr@gmail.com",
      invoices = [Invoice(invno = 9, amount = 15000), 
      Invoice(invno = 11, amount = 6000)
   ])
]
session.add_all(rows)
session.commit()


```
### Пример запросов без связывания с классами <a name="Примерзапросовбезсвязываниясклассами"></a>
```python
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_
engine = create_engine("mysql+mysqlconnector://root:root@localhost/pyloungedb", echo=True)
meta = MetaData(engine)

authors = Table('Authors', meta, autoload=True) 
books = Table('Books', meta, autoload=True)

conn = engine.connect()
s = select([books, authors]).where(and_(books.c.author_id == authors.c.id_author, books.c.price > 1200))
result = conn.execute(s)

for row in result.fetchall():
   print (row)

# удаление записи
delete_query = books.delete().where(books.c.id_book == 1) # DELETE Books WHERE BOKKS.ID_BOOK == 1;
conn.execute(delete_query)
# обновление записи
update_query=books.update().where(books.c.id_book==2).values(title='AnotherTitle') # UPDATE books SET title= al where books.id_book=3;
conn.execute(update_query)
```
### Пример со связываниями с классами <a name="Примерсосвязываниямисклассами"></a>
```python
from sqlalchemy.orm import mapper, relationship, sessionmaker

engine = create_engine("mysql+mysqlconnector://root:root@localhost/pyloungedb", echo=True)
meta = MetaData(engine)

authors = Table('Authors', meta, autoload=True) 
books = Table('Books', meta, autoload=True) 

class Book(object):
    def __init__(self, title, author_id, genre, price):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.price = price

    def __repr__(self):
        return "<Book('%s','%s', '%s', '%s')>" % (self.title, str(self.author_id), 
                                            self.genre, str(self.price))

class Author():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Author('%s')>" % (self.name)

mapper(Book, books)
mapper(Author, authors)
new_book = Book("NewBook", 1, "NewG", 2500)
```
### Пример работы с классической орм <a name="Примерработысклассическойорм"></a>
```python
from sqlalchemy import create_engine, select, Table, Column, Integer,   String, MetaData, ForeignKey
# Метаданные-это информация о данных в БД; например, информация о таблицах и столбцах, в которых мы храним данные.
meta = MetaData()
authors = Table('Authors', meta,
     Column('id_author', Integer, primary_key=True),
     Column('name', String(250), nullable = False)
)

books = Table('Books', meta,
     Column('id_book', Integer, primary_key=True),
     Column('title', String(250), nullable = False),
     Column('author_id', Integer, ForeignKey("Authors.id_author")),
     Column('genre', String(250)),
     Column('price', Integer)
)

print(books.c.author_id) # print(books.columns.author_id)
print(books.primary_key)

print(authors.c.name) # print(books.columns.author)
print(authors.primary_key)
print(authors.c)
# подключаемся к бд и заносим данные 
# субд+драйвер://юзер:пароль@хост:порт/база
engine = create_engine("mysql+mysqlconnector://root:root@localhost/pyloungedb", echo=True)
meta.create_all(engine) # или books.create(engine), authors.create(engine)

conn = engine.connect()

ins_author_query = authors.insert().values(name = 'Lutz')
conn.execute(ins_author_query)

ins_book_query = books.insert().values(title = 'Learn Python', author_id = 1, genre = 'Education', price = 1299)
conn.execute(ins_book_query)
ins_book_query2 = books.insert().values(title = 'Clear Python', author_id = 1, genre = 'Education', price =956)
conn.execute(ins_book_query2)

books_gr_1000_query = books.select().where(books.c.price > 1000) # SELECT * FROM Books WHERE Books.price > 1000;
result = conn.execute(books_gr_1000_query)

for row in result:
   print (row)

print()

s = select([books, authors]).where(books.c.author_id == authors.c.id_author)
result = conn.execute(s)

for row in result:
   print (row)
# 2021-01-27 10:27:59,575 INFO sqlalchemy.engine.base.Engine SELECT `Books`.id_book, `Books`.title, `Books`.author_id, `Books`.genre, `Books`.price, `Authors`.id_author, `Authors`.name
#FROM `Books`, `Authors`

```
### Пример запросов на классической версии <a name="Примерзапросовнаклассическойверсии"></a>
```python
fetchone()
select()
students.select().where(students.c.id>2)
for row in result:
   print (row)

s = select([users])
result = conn.execute(s)

from sqlalchemy import text
t = text("SELECT * FROM students")
result = connection.execute(t)

s = select([text("* from students")]) \
.where(
   and_(
      text("students.name between 😡 and :y"),
      text("students.id>2")
   )
)

conn = engine.connect()
stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()

conn = engine.connect()
stmt = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()

from sqlalchemy.sql import select
s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
result = conn.execute(s)
for row in result:
   print (row)

stmt = students.update().\
values({
   students.c.name:'xyz',
   addresses.c.email_add:'abc@xyz.com'
}).\
where(students.c.id == addresses.c.id)

stmt = table1.update(preserve_parameter_order = True).\
   values([(table1.c.y, 20), (table1.c.x, table1.c.y + 10)])
   
 stmt = users.delete().\
   where(users.c.id == addresses.c.id).\
   where(addresses.c.email_address.startswith('xyz%'))
conn.execute(stmt)

from sqlalchemy import join
from sqlalchemy.sql import select
j = students.join(addresses, students.c.id == addresses.c.st_id)
stmt = select([students]).select_from(j)
result = conn.execute(stmt)
result.fetchall()

from sqlalchemy import and_, or_
stmt = select([students]).where(and_(students.c.name == 'Ravi', students.c.id <3))
result = conn.execute(stmt)
print (result.fetchall())

stmt = select([students]).where(or_(students.c.name == 'Ravi', students.c.id <3))

from sqlalchemy import asc
stmt = select([students]).order_by(asc(students.c.name))
result = conn.execute(stmt)
for row in result:
   print (row)

from sqlalchemy import desc
stmt = select([students]).order_by(desc(students.c.lastname))

from sqlalchemy import between
stmt = select([students]).where(between(students.c.id,2,4))
print (stmt)


from sqlalchemy.sql import func
result = conn.execute(select([func.now()]))
print (result.fetchone())

result = conn.execute(select([func.max(employee.c.marks)]))
result = conn.execute(select([func.min(employee.c.marks)]))
result = conn.execute(select([func.avg(employee.c.marks)]))
print (result.fetchone())
result = conn.execute(select([func.max(students.c.lastname).label('Name')]))
print (result.fetchone())
```
### Многие ко многим <a name="Многиекомногим"></a>
```python
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///mycollege.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
class Department(Base):
   __tablename__ = 'department'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   employees = relationship('Employee', secondary = 'link')
   
class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   departments = relationship(Department,secondary='link')

class Link(Base):
   __tablename__ = 'link'
   department_id = Column(
      Integer, 
      ForeignKey('department.id'), 
      primary_key = True)

employee_id = Column(
   Integer, 
   ForeignKey('employee.id'), 
   primary_key = True)

Base.metadata.create_all(engine)
d1 = Department(name = "Accounts")
d2 = Department(name = "Sales")
d3 = Department(name = "Marketing")

e1 = Employee(name = "John")
e2 = Employee(name = "Tony")
e3 = Employee(name = "Graham")
e1.departments.append(d1)
e2.departments.append(d3)
d1.employees.append(e3)
d2.employees.append(e2)
d3.employees.append(e1)
e3.departments.append(d2)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
session.add(e1)
session.add(e2)
session.add(d1)
session.add(d2)
session.add(d3)
session.add(e3)
session.commit()
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

for x in session.query( Department, Employee).filter(Link.department_id == Department.id, 
   Link.employee_id == Employee.id).order_by(Link.department_id).all():
   print ("Department: {} Name: {}".format(x.Department.name, x.Employee.name))
```

## Парсинг <a name="scrap"></a>
Моменты на которые надо обратить внимание:
### Генерация юзерагента
Тут поможет user_agent и fake_useragent. Опытные скрейперы могут попробовать установить свой агент на Googlebot User Agent — поисковый робот Google. Большинство веб-сайтов, очевидно, хотят попасть в выдачу Google и пропускают Googlebot.

[О ботах гугла](https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers?hl=en&visit_id=637602093540037819-4103600971&rd=1)

[О ботах яндекс](
https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html)



### Время ожидания запроса
```python
page_response = requests.get(page_link, timeout=5, headers=headers) - requests
driver.implicity_wait() - selenium
time.sleep - python
```
* Используйте случайные задержки (например около 2–10 секунд), чтобы избежать блокировки. Особо щепетильным стоит проверить файл robots.txt (как правило, находится на http://<адрес сайта>/robots.txt). Иногда там можно найти параметр Crawl-delay, который говорит, сколько секунд нужно подождать между запросами, чтобы не вредить работе сервера.

### Смена IP
Смена айпи позволяет избежать бана, узнайте как это реализованно в библиотеке которую вы используете.
### honeypot
* Ловушки для хакеров — это средства для обнаружения сканеров или скреперов. 
Такими средствами могут быть «скрытые» ссылки, которые не видны пользователям, но могут быть извлечены скреперами и/или вэб-спайдерами. Такие ссылки будут иметь набор стилей CSS «display: none», «visibility: hidden» или «color: #fff;», их можно смешивать, задачая цвет фона или даже перемещаясь из видимой области страницы. Как только ваша программа посещает такую ссылку, ваш IP-адрес может быть помечен для дальнейшего расследования или даже мгновенно заблокирован.
* Другой способ обнаружить хакеров — это добавить ссылки с бесконечно глубокими деревьями директорий. В этом случае вам нужно ограничить количество загруженных страниц или ограничить глубину обхода.
### Добавьте referer
* Referer — заголовок HTTP-запроса, который даёт понять, с какого сайта вы пришли. Неплохой вариант — сделать так, чтобы он показывал, будто вы перешли из Google:
* Referer: https://www.google.com/
* Стоит менять referer для веб-сайтов в разных странах: например для России использовать https://www.google.ru/, а не https://www.google.com/. Вместо Google можно подставить адреса соцсетей: Youtube, Facebook, ВКонтакте. Referer поможет сделать так, чтобы запросы выглядели как трафик с того сайта, откуда обычно приходит больше всего посетителей.
### Используйте headless-браузер(обход отпечатков)
Он эмулирует поведение настоящего браузера и поддерживает программное управление. Чаще всего для этих целей выбирают Chrome Headless.
### Подключите программу для решения CAPTCHA
Существуют веб-сайты, которые систематически просят вас подтвердить, что вы не робот, с помощью капч. Обычно капчи отображаются только для подозрительных IP-адресов, и с этим помогут прокси. В остальных же случаях используйте автоматический решатель CAPTCHA — скажем, 2Captcha или AntiCaptcha.
### Используйте куки
Например аунтентификацию по куки, сохраняйте и используйте снова.
### Простые заголовки
Ставте простые хотя бы простые заголовки, узнайте как это реализованно в библиотеке которую вы используете.
### Извлечение текста скрытого за Ajax-стеной: 
* from selenium import webdriver 
* import time 
* driver = webdriver.PhantomJS(executable_path='') 
* driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html") 
* time.sleep(3) 
* print(driver.find_element_by_id("content").text) 
* driver.close() 
### Scrapy
* AutoThrottle - Это расширение для автоматического регулирования скорости обхода на основе нагрузки как сервера Scrapy, так и веб-сайта, на котором выполняется сканирование.
* scrapy-fake-useragent - Использовать случайный User-Agent, предоставляемый fake-useragent для каждого запроса IP-адреса
* scrapy-proxies - Настройка промежуточного ПО прокси-сервера Scrapy для каждого запроса
* https://pythonru.com/biblioteki/sozdanie-parserov-s-pomoshhju-scrapy-i-python
* https://python-scripts.com/scrapy-example
* https://pythonru.com/uroki/scrapy-parsing
### Selenium 
Используйте селениум, selenium wire для парсинга. selenium wire имеет поддержку драйвера который позволяет обходить антибот защиту.
### Разное
* граббер тг
* https://github.com/andreyru02/telegram-grabber
* парсинг карт
* https://www.youtube.com/watch?v=DJysDXJLpM8
* чекер
* https://zismo.biz/topic/943273-kak-napisat-cheker-na-python-3-urovnia/
* https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
* https://hussainaliakbar.github.io/restricting-tls-version-and-cipher-suites-in-python-requests-and-testing-with-wireshark/
* https://github.com/GH0st3rs/YoulaApi
### Применяйте разные паттерны
Применяйте разные паттерны парсинга для имитации живого человека, например разное время кликов, просмотров, лайков и т. д.

    Прокрутка сообщений -> Перерыв -> Сообщения "Нравится".

    Разрыв -> Прокрутка сообщений -> Разрыв.

Как делать комбинации:
```python
perm_ = permutations([2, 4, 6]) 

for i in list(perm_): 
    print(i) 

from itertools import combinations 

comb_ = combinations([2, 4, 6] , 2) 

for i in list(comb_): 
    print(i)
```



## Библиотеки <a name="lib"></a>

### ftplib <a name="ftplib"></a>
* import ftplib
* host = "ftp.ex.ru"
* ftp_user = "root"
* ftp_password = "python" 
* filename = "picture.png"
* con = ftplib.FTP(host, ftp_user, ftp_password)
* **Открываем файл для передачи в бинарном режиме**
* f = open(filename, "rb")
* **Передаем файл на сервер**
* send = con.storbinary("STOR "+ filename, f)
* **Закрываем FTP соединение**
* con.close

### json <a name="json"></a>

**Из json**
```python
import json 
  x = '{"name":"Viktor", "age":30, "city":"Minsk"}'
y = json.loads(x)
 print(y["age"])
```
**в json**
```python 
import json
x = {
"name": "Viktor",
"age": 30,
"city": "Minsk"
}
y = json.dumps(x)
print(y)
print(json.dumps(y, ensure_ascii=False))
json.dumps(x, indent=4) 
```
### Время <a name="time"></a>


pytz-для таймзон
```python
datetime
d = datetime.datetime(2017, 3, 5, 12, 30, 10)
print(d.year) # 2017
print(d.second) # 10
print(d.hour) # 12

import datetime
a = datetime.datetime.today()
print(a) # datetime.datetime(2017, 4, 5, 0, 16, 54, 989663)
b = datetime.datetime.now()
print(b) # datetime.datetime(2017, 4, 5, 0, 17, 8, 24239)

import datetime
a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'
today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/05/2017'
print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00

import datetime
datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
now = datetime.datetime.now()
then = datetime.datetime(2017, 2, 26)
delta = now - then
print(delta.days) # 38
print(delta.seconds) # 1131

time
import time
print(time.ctime()) # 'Wed Apr 5 00:02:49 2017'
print(time.ctime(1384112639)) # 'Sun Nov 10 13:43:59 2013'
import time
for x in range(5):
    time.sleep(2)
    print("Slept for 2 seconds")


import time
a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(a) # '2017-04-05-00.11.20'

import time
x = time.time()
print(x) # 1491340367.478385

import time
a = time.ctime(time.time())
print(a) # Wed Apr 5 00:13:47 2017
```

### hash <a name="hash"></a>
**hashlib**

Модуль предоставляет следующие функции: md5(), sha1(), sha224(), sha256(), sha384 и sha512(). В качестве необязательного параметра функциям можно передать шифруемую последовательность байтов. Например:
```python
import hashlib
h = hashlib.sha1(b"password")
```
Передать последовательность байтов можно также с помощью метода update(). В этом случае объект присоединяется к предыдущему значению:
```python
h = hashlib.sha1()
h.update(b"password")
```
Получить зашифрованную последовательность байтов и строку позволяют два метода — digest() и hexdigest():
```python
h = hashlib.sha1(b"password")
h.digest()
b'[\xaaa\xe4\xc9\xb9??\x06\x82%\x0b1\xf83\x1b~\xe6\x8f\xd9'
h.hexdigest()
'5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
```
Наиболее часто применяемой функцией является функция md5(), которая шифрует строку с помощью алгоритма MD5. Она используется для шифрования паролей так как не существует алгоритма для дешифровки. Для сравнения введенного пользователем пароля с сохраненным в базе необходимо зашифровать введенный пароль, а затем произвести сравнение.
```python
import hashlib
h = hashlib.md5(b"password")
p = h.hexdigest()
'5f4dcc3b5aa765d61d8327deb882cf99'
h2 = hashlib.md5(b"password")
if p == h2.hexdigest(): print("Пароль правильный")
```
**hmac**

Пример подписи URL секретным ключом.
```python
import hashlib, hmac
secret = 'mysecret'.encode()
url = 'https://docs-python.ru/standart-library/'.encode()
signing = hmac.new(secret, url, hashlib.sha256)
signing.digest()
# b'\xcf\xa4C\x1e\xd2,\x1eE\xedVW\x16\xd2\x86YdjJ\xbe\x83>;y \x94\xa3B-#\xa7\xe5M'
signing.hexdigest()
# 'cfa4431ed22c1e45ed565716d28659646a4abe833e3b792094a3422d23a7e54d'
signing.digest_size
# 32
signing.block_size
# 64
signing.name
# 'hmac-sha256'
```
**base64**
```python
import base64
encoded_data = base64.b64encode("Encode this text")
print("Encoded text with base 64 is")
print(encoded_data)

import base64
decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")
print("decoded text is ")
print(decoded_data)
```

### jinja <a name="jinja"></a>
```python


tpl = "Автомобиль: {{ (cs | max(attribute='price')).model  }}"

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''


html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}
 
{{ input('username') }}
{{ input('email') }}
{{ input('password') }}
'''


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]
<ul>
<li>Алексей 
    <ul>
    <li>age: 
    <li>weight: 78.5
    </ul>
<li>Николай 
    <ul>
    <li>age: 
    <li>weight: 82.3
    </ul>
<li>Иван 
    <ul>
    <li>age: 
    <li>weight: 94.0
    </ul>
</ul>


html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}
 
{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''


include and import

{% include 'header.htm' %}
Содержимое страницы
{% include 'footer.htm' %}

{% include "header.html" ignore missing %}
 


{% macro dialog_1(title, msg='') -%}
<div class="dialog">
<p class="title">{{title}}</p>
<p class="message">{{msg}}</p>
<input type="button" value="Закрыть"></p>
</div>
{%- endmacro %}


{% include 'header.htm' ignore missing %}
{% import 'dialogs.htm' as dlg %}
Содержимое страницы
{{ dlg.dialog_1('Внимание', 'Это тестовый диалог') }}
{% include 'footer.htm' %}
```

####  наследование
```html
<!DOCTYPE html>
<html>
<head>
        <meta charset="UTF-8">
        <title>{% block title %}{% endblock %}</title>
</head>
<body>
 
{% block content %}
{% endblock %}
 
</body>
</html>

{% extends 'ex_main.htm' %}
{% block title%}О сайте{% endblock %}
{% block content %}
<h1>О сайте</h1>
<p>Классный сайт, если его доделать.</p>
{% endblock %}

from jinja2 import Environment, FileSystemLoader
 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
 
template = env.get_template('about.htm')
 
output = template.render()
print(output)


{% extends 'layout/default.tpl' %}


{% extends 'layout/default.tpl' %}
 
{% block title%}О сайте{% endblock %}
 
{% block content %}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать.</p>
{% endblock %}

{% block content %}
{{ super() }}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать.</p>
{% endblock %}
```

#### вложенные блоки
```html
{% block content %}
        {% block table_contents %}
        <ul>
        {% for li in list_table -%}
        <li>{{li}}</li>
        {% endfor -%}
        </ul>
        {% endblock table_contents %}
{% endblock content %}


{% block content %}
{{ super() }}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать.</p>
{% endblock %}
```
#### Область видимости блоков

Давайте теперь, немного усовершенствуем базовый шаблон и добавим еще один блок для формирования элементов списка:
```html
{% for li in list_table -%}
<li>{% block item %}{{ li }}{% endblock %}</li>
{% endfor -%}
```
Если теперь выполнить программу, то внутри тегов li не будет никакой информации. Дело в том, что внутри блока item доступ к внешней переменной li нет. Чтобы исправить эту ситуацию и разрешить оперировать переменными из внешней области видимости, после имени блока следует прописать ключевое слово scoped:
```html
<li>{% block item scoped %}{{ li }}{% endblock %}</li>
```
Теперь при запуске программа будет работать также, как и ранее. Но мы же добавили этот блок item не просто так, значит, собираемся его переопределять в дочернем шаблоне. И это можно сделать следующим образом:
```html
{% block item %}<p class="item">{{ super() }}</p>{% endblock %}
```
#### Вложенное наследование шаблонов

    файл base.tpl – такой же как и ex_main.htm:
    файл child1.htm: {% extends 'base.tpl' %} …
    файл child2.htm: {% extends 'child1.htm' %} …


### прогресс выполнения в Python <a name="progress"></a>
```python
import time
from progress.bar import IncrementalBar

mylist = [1,2,3,4,5,6,7,8]

bar = IncrementalBar('Countdown', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(1)

bar.finish()

import time
from tqdm import tqdm

mylist = [1,2,3,4,5,6,7,8]

for i in tqdm(mylist):
    time.sleep(1)


from alive_progress import alive_bar
import time

mylist = [1,2,3,4,5,6,7,8]

with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar()
        time.sleep(1)

```
### Сервер <a name="server"></a>
#### wsgi

socket
сервер

![](https://imgur.com/a/eLxFFis)
![](https://imgur.com/a/WzOHnE3)
``` python
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
```
клиент
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print data

сокет с передачей картинки
![](https://imgur.com/a/T6XnanG)
```
#### курс крипты
```python
import websockets

import asyncio

import json

import time

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)

fig.show()

xdata = []

ydata = []

def update_graph():

   ax.plot(xdata, ydata, color='g')

   ax.legend([f"Last price: {ydata[-1]}$"])

   fig.canvas.draw()

   plt.pause(0.1)

async def main():

   url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"

   async with websockets.connect(url) as client:

       while True:

           data = json.loads(await client.recv())['data']

           event_time = time.localtime(data['E'] // 1000)

           event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"

           print(event_time, data['c'])

           xdata.append(event_time)

           ydata.append(int(float(data['c'])))

           update_graph()

if __name__ == '__main__':

   loop = asyncio.get_event_loop()

   loop.run_until_complete(main())

```
### Работа с файлами <a name="work_with_files"></a>
#### csv <a name="csv">csv</a>
```python
import csv
 
with open('example.csv', newline='') as File: 
    reader = csv.reader(File)
    for row in reader:
        print(row)
 
 
import csv
with open('name.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row['first_name'], row['last_name'])

import csv
 
with open('example4.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
print("Writing complete")

import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
```
#### xml <a name="xml"></a>
парсинг
```python


from lxml import etree
 
def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    
    root = etree.fromstring(xml)
 
    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)
            book_dict[elem.tag] = text
        
        if book.tag == "book":
            books.append(book_dict)
            book_dict = {}
    
    return books
 
 
if __name__ == "__main__":
    parseBookXML("books.xml")

парсинг с превращением в объект питона
from lxml import etree, objectify
 
def parseXML(xmlFile):
    """Parse the XML file"""
    with open(xmlFile) as f:
        xml = f.read()
    
    root = objectify.fromstring(xml)
    
    # возвращаем атрибуты как словарь.
    attrib = root.attrib
 
    # извлекаем данные данные.
    begin = root.appointment.begin
    uid = root.appointment.uid
    
    # в цикле выводим всю информацию про элементы (тэги и текст).
    for appt in root.getchildren():
        for e in appt.getchildren():
            print("%s => %s" % (e.tag, e.text))
        print()
    
    # пример как менять текст внутри элемента.
    root.appointment.begin = "something else"
    print(root.appointment.begin)
    
    # добавление нового элемента.
    root.appointment.new_element = "new data"
    
    # удаляем аннотации.
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True)
    print(obj_xml)
    
    # сохраняем данные в файл.
    with open("new.xml", "w") as f:
        f.write(obj_xml)
 
 
if __name__ == "__main__":
    f = r'path\to\sample.xml'
    parseXML(f)
создание
from lxml import etree, objectify
 
def create_appt(data):
    """
    Создаем изначальную структуру XML.
    """
    appt = objectify.Element("appointment")
    appt.begin = data["begin"]
    appt.uid = data["uid"]
    appt.alarmTime = data["alarmTime"]
    appt.state = data["state"]
    appt.location = data["location"]
    appt.duration = data["duration"]
    appt.subject = data["subject"]
    return appt
 
 
def create_xml():
    """
    Создаем XML файл.
    """

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <zAppointments>
    </zAppointments>
    '''
    
    root = objectify.fromstring(xml)
    root.set("reminder", "15")
    
    appt = create_appt({"begin":1181251680,
                        "uid":"040000008200E000",
                        "alarmTime":1181572063,
                        "state":"",
                        "location":"",
                        "duration":1800,
                        "subject":"Bring pizza home"}
                        )
    
    root.append(appt)
    
    uid = "604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800"
    appt = create_appt({"begin":1234360800,
                        "uid":uid,
                        "alarmTime":1181572063,
                        "state":"dismissed",
                        "location":"",
                        "duration":1800,
                        "subject":"Check MS Office website for updates"}
                        )
    root.append(appt)
    
    # удаляем все lxml аннотации.
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
 
    # конвертируем все в привычную нам xml структуру.
    obj_xml = etree.tostring(root,
        pretty_print=True,
        xml_declaration=True
    )
    
    try:
        with open("example.xml", "wb") as xml_writer:
        xml_writer.write(obj_xml)
    except IOError:
        pass

<?xml version="1.0" ?>
<zAppointments reminder="15">
    <appointment>
        <begin>1181251680</begin>
        <uid>040000008200E000</uid>
        <alarmTime>1181572063</alarmTime>
        <state></state>
        <location></location>
        <duration>1800</duration>
        <subject>Bring pizza home</subject>
    </appointment>
    <appointment>
        <begin>1234360800</begin>
        <duration>1800</duration>
        <subject>Check MS Office website for updates</subject>
        <location></location>
        <uid>604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800</uid>
        <state>dismissed</state>
    </appointment>
</zAppointments>

obj_xml = etree.tostring(
    root,
    pretty_print=True,
    xml_declaration=True
)
    
```


#### pillow <a name="pillow"></a>
https://www.youtube.com/watch?v=d7D2UuUqtgs&list=PLEYdORdflM3k2U6xicasFS3NXWwaZo8kw

    from PIL import ImageOps
    image = ImageOps.exif_transpose(image)
    поворот по exif



#### pdf <a name="pdf"></a>
 
https://python-scripts.com/create-pdf-pyfpdf
excel
https://www.youtube.com/watch?v=VQNV_oOdOqo
https://www.youtube.com/watch?v=d5jHpPSp5uI&t=4s
#### pickle <a name="pickle"></a>
```python
import pickle
data = {
   'a': [1, 2.0, 3, 4+6j],
   'b': ("character string", b"byte string"),
   'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
   pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)
{'c': {False, True, None}, 'a': [1, 2.0, 3, (4+6j)], 'b': ('character string', b'byte string')}
```
### OS и OS.path <a name="os"></a>
Библиотека для управления операций с файлами и файловой системой/системой


### аргументы командной строки <a name="args"></a>
https://foxford.ru/wiki/informatika/analiz-argumentov-komandnoy-stroki-v-python


## Цикл разработки сайта <a name="site"></a>

![](https://imgur.com/a/BL6eRl3)

1. Дизайн
* figma-блочная верстка(прототип сайта)
* Обсуждение с заказчиком
1. Верстка
* Верстка с использованием технологий напр. gulp+sass+js
* Адаптивность
* Обсуждение с заказчиком
1. Посадка на cms
* Логика - добавление услуг, галерея, заявки и т.д.
* Обсуждение с заказчиком
1. Домен
* ssl
* Залив
* Почта
* Доступ
* Метрика, google search console, вебмастер, sitemap, robots.txt, pagespeed,вту, лайтхаус.
![](https://i.imgur.com/8fu9wn0.jpg)
  

