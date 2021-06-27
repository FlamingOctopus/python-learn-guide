# Тут собраны примеры работы с различными библиотеками и прочее для себя


1. [Тесты  и логирование](#test)
2. [Асинхронность и многопоточность и т. д.](#async_n_threads)
3. [Парсинг](#scrap)
4. [Библиотеки](#lib)
    1.
## Тесты  и логирование <a name="test"></a>
### unittest(не рекомендуется, нарушает SOLID)

https://docs.python.org/3/library/unittest.html#re-using-old-test-code
https://ru.hexlet.io/courses/advanced_python/lessons/python_testing_unittest/theory_unit
https://pythonworld.ru/moduli/modul-unittest.html

### pytest

### logging

https://python-scripts.com/logging-python


## Асинхронность и многопоточность и т. д. <a name="async_n_threads"></a>
multithreading для парса 

В задачах, связанных с процессором, использование multithreading может понизить производительность. 

В задачах, связанных с процессором, использование multiprocessing может повысить производительность.

http://python-3.ru/page/multiprocessing

http://python-3.ru/page/import-threading 

https://python-scripts.com/threading 

https://www.tune-it.ru/web/myaut/home/-/blogs/%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F-threading-%D0%B2-python https://pythonru.com/uroki/potoki-i-mnogopotochnost-dlja-nachinajushhih

asyncio

https://docs.python.org/3/library/asyncio.html

https://habr.com/ru/post/337420/





## Парсинг <a name="scrap"></a>


https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers?hl=en&visit_id=637602093540037819-4103600971&rd=1
https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html

### Генерация юзерагента
* from user_agent import generate_user_agent
* headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
* page_response = requests.get(page_link, timeout=5, headers=headers)
* Опытные скрейперы могут попробовать установить свой агент на Googlebot User Agent — поисковый робот Google. Большинство веб-сайтов, очевидно, хотят попасть в выдачу Google и пропускают Googlebot.

###  Время ожидания запроса
page_response = requests.get(page_link, timeout=5, headers=headers)
* Используйте случайные задержки (например около 2–10 секунд), чтобы избежать блокировки. Особо щепетильным стоит проверить файл robots.txt (как правило, находится на http://<адрес сайта>/robots.txt). Иногда там можно найти параметр Crawl-delay, который говорит, сколько секунд нужно подождать между запросами, чтобы не вредить работе сервера.
###  Отлавливание исключний
try:
   page_response = requests.get(page_link, timeout=5)
   if page_response.status_code == 200:
   else:
       print(page_response.status_code)
except requests.Timeout as e:
   print("It is time to timeout")
   print(str(e))
except # other exception

###  Смена IP
proxies = {'http' : 'http://10.10.0.0:0000', 
         'https': 'http://120.10.0.0:0000'}
page_response = requests.get(page_link, proxies=proxies, timeout=5) 

###  honeypot
* Ловушки для хакеров — это средства для обнаружения сканеров или скреперов. 
Такими средствами могут быть «скрытые» ссылки, которые не видны пользователям, но могут быть извлечены скреперами и/или вэб-спайдерами. Такие ссылки будут иметь набор стилей CSS «display: none», «visibility: hidden» или «color: #fff;», их можно смешивать, задачая цвет фона или даже перемещаясь из видимой области страницы. Как только ваша программа посещает такую ссылку, ваш IP-адрес может быть помечен для дальнейшего расследования или даже мгновенно заблокирован.
* Другой способ обнаружить хакеров — это добавить ссылки с бесконечно глубокими деревьями директорий. В этом случае вам нужно ограничить количество загруженных страниц или ограничить глубину обхода.
###  Scrapy
* AutoThrottle - Это расширение для автоматического регулирования скорости обхода на основе нагрузки как сервера Scrapy, так и веб-сайта, на котором выполняется сканирование.
* scrapy-fake-useragent - Использовать случайный User-Agent, предоставляемый fake-useragent для каждого запроса IP-адреса
* scrapy-proxies - Настройка промежуточного ПО прокси-сервера Scrapy для каждого запроса
* https://pythonru.com/biblioteki/sozdanie-parserov-s-pomoshhju-scrapy-i-python
* https://python-scripts.com/scrapy-example
* https://pythonru.com/uroki/scrapy-parsing

###  Добавьте referer
* Referer — заголовок HTTP-запроса, который даёт понять, с какого сайта вы пришли. Неплохой вариант — сделать так, чтобы он показывал, будто вы перешли из Google:
* Referer: https://www.google.com/
* Стоит менять referer для веб-сайтов в разных странах: например для России использовать https://www.google.ru/, а не https://www.google.com/. Вместо Google можно подставить адреса соцсетей: Youtube, Facebook, ВКонтакте. Referer поможет сделать так, чтобы запросы выглядели как трафик с того сайта, откуда обычно приходит больше всего посетителей.

###  Используйте headless-браузер(обход отпечатков)
Он эмулирует поведение настоящего браузера и поддерживает программное управление. Чаще всего для этих целей выбирают Chrome Headless.

###  Подключите программу для решения CAPTCHA
Существуют веб-сайты, которые систематически просят вас подтвердить, что вы не робот, с помощью капч. Обычно капчи отображаются только для подозрительных IP-адресов, и с этим помогут прокси. В остальных же случаях используйте автоматический решатель CAPTCHA — скажем, 2Captcha или AntiCaptcha.

###  Аунтентификация по куки
* import 
* requests session = requests.Session() 
* params = {'username': 'username', 'password': 'password'} 
* s=session.post("http://pythonscraping.com/pages/cookies/welcome.php", params) 
* print("Cookie is set to:") 
* print(s.cookies.get_dict()) print("-----------") 
* print("Going to profile page...") 
* s = session.get("http://pythonscraping.com/pages/cookies/profile.php") 
* print(s.text) 


###  Извлечение текста скрытого за Ajax-стеной: 
* from selenium import webdriver 
* import time 
* driver = webdriver.PhantomJS(executable_path='') 
* driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html") 
* time.sleep(3) 
* print(driver.find_element_by_id("content").text) 
* driver.close() 

###  Простые заголовки
* import requests from bs4 import BeautifulSoup 
* session = requests.Session() 
* headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"} 
* url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending" 
* req = session.get(url, headers=headers) 
* bsObj = BeautifulSoup(req.text) 
* print(bsObj.find("table",{"class":"table-striped"}).get_text)

###  Selenium 
* подменга веб драйвера

* граббер тг
* https://github.com/andreyru02/telegram-grabber
* парсинг карт
* https://www.youtube.com/watch?v=DJysDXJLpM8
* чекер
* https://zismo.biz/topic/943273-kak-napisat-cheker-na-python-3-urovnia/

6. Pursue Different Scraping Patterns

A slow pace isn’t the only feature of human browsing activity. Humans skim websites uniquely. You should also consider different view time, random clicks when users visit a site. However, the bots follow the same browsing pattern. Websites can easily identify scrapers when they find repetitive and similar browsing actions. 

Therefore, you should apply various scraping patterns from time to time when extracting the data from the sites. Some sites may have improved anti-scraping mechanisms.

Consider combining several clicks, mouse movements or shuffle and combine random event activities to make your scraper look like a human.

Some example activities for a LinkedIn bot might include:

    Scrolling the news feed.
    Taking a break to ‘go to the toilet’.
    Commenting on someone’s post.
    Liking on someone’s post.
    Watching a video.

With the list above, you could create different combinations of activities such as:

    Scrolling Posts –> Break –> Liking Posts.

    Break –> Scrolling Posts –> Break.

To easily create the combinations, you can use a native package in Python. This ensures your web bots are less rule based and less deterministic.

from itertools import permutations 
  
Get all of the permutations of [2, 4, 6] 
perm_ = permutations([2, 4, 6]) 
  
Print all of the the permutations 
for i in list(perm_): 
    print(i) 

A Python program that prints all
combinations of given length 
from itertools import combinations 
  
Get all combinations of [2, 4, 6] 
with a length of length 2 
comb_ = combinations([2, 4, 6] , 2) 
  
Print all of the combinations 
for i in list(comb_): 
    print(i)




## Библиотеки <a name="lib"></a>

###  ftplib
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

###  json

* **Из json**
* import json
* x = '{"name":"Viktor", "age":30, "city":"Minsk"}'
* y = json.loads(x)
* print(y["age"])

* **в json**
* import json
* x = {
* "name": "Viktor",
* "age": 30,
* "city": "Minsk"
* }
* y = json.dumps(x)
* print(y)
* print(json.dumps(y, ensure_ascii=False))
* json.dumps(x, indent=4) 

### Время

pytz-для таймзон

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
 
Значение: datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
now = datetime.datetime.now()
 
then = datetime.datetime(2017, 2, 26)
 
Кол-во времени между датами.
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





### hash
hashlib
Для шифрования строк предназначен модуль hashlib. Прежде чем использовать функции из этого модуля, необходимо подключить модуль с помощью инструкции:
1
import hashlib

Модуль предоставляет следующие функции: md5(), sha1(), sha224(), sha256(), sha384 и sha512(). В качестве необязательного параметра функциям можно передать шифруемую последовательность байтов. Например:
1
2
>>> import hashlib
>>> h = hashlib.sha1(b"password")

Передать последовательность байтов можно также с помощью метода update(). В этом случае объект присоединяется к предыдущему значению:
1
2
>>> h = hashlib.sha1()
>>> h.update(b"password")

Получить зашифрованную последовательность байтов и строку позволяют два метода — digest() и hexdigest():
1
2
3
4
5
>>> h = hashlib.sha1(b"password")
>>> h.digest()
b'[\xaaa\xe4\xc9\xb9??\x06\x82%\x0b1\xf83\x1b~\xe6\x8f\xd9'
>>> h.hexdigest()
'5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

Наиболее часто применяемой функцией является функция md5(), которая шифрует строку с помощью алгоритма MD5. Она используется для шифрования паролей так как не существует алгоритма для дешифровки. Для сравнения введенного пользователем пароля с сохраненным в базе необходимо зашифровать введенный пароль, а затем произвести сравнение.
1
2
3
4
5
6
7
>>> import hashlib
>>> h = hashlib.md5(b"password")
>>> p = h.hexdigest()
>>> p    # Пароль, сохраненный в базе
'5f4dcc3b5aa765d61d8327deb882cf99'
>>> h2 = hashlib.md5(b"password")   # Пароль, введенный пользователем
>>> if p == h2.hexdigest(): print("Пароль правильный")

Программа выведет что пароль правильный.
hmac

Пример подписи URL секретным ключом.
>>> import hashlib, hmac
>>> secret = 'mysecret'.encode()
>>> url = 'https://docs-python.ru/standart-library/'.encode()
>>> signing = hmac.new(secret, url, hashlib.sha256)
>>> signing.digest()
# b'\xcf\xa4C\x1e\xd2,\x1eE\xedVW\x16\xd2\x86YdjJ\xbe\x83>;y \x94\xa3B-#\xa7\xe5M'
>>> signing.hexdigest()
# 'cfa4431ed22c1e45ed565716d28659646a4abe833e3b792094a3422d23a7e54d'
>>> signing.digest_size
# 32
>>> signing.block_size
# 64
>>> signing.name
# 'hmac-sha256'

base64
import base64
encoded_data = base64.b64encode("Encode this text")

print("Encoded text with base 64 is")
print(encoded_data)

import base64
decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")

print("decoded text is ")
print(decoded_data)

### jinja

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


####  наследование

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


#### вложенные блоки

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

#### Область видимости блоков

Давайте теперь, немного усовершенствуем базовый шаблон и добавим еще один блок для формирования элементов списка:
{% for li in list_table -%}
<li>{% block item %}{{ li }}{% endblock %}</li>
{% endfor -%}
Если теперь выполнить программу, то внутри тегов li не будет никакой информации. Дело в том, что внутри блока item доступ к внешней переменной li нет. Чтобы исправить эту ситуацию и разрешить оперировать переменными из внешней области видимости, после имени блока следует прописать ключевое слово scoped:
<li>{% block item scoped %}{{ li }}{% endblock %}</li>
Теперь при запуске программа будет работать также, как и ранее. Но мы же добавили этот блок item не просто так, значит, собираемся его переопределять в дочернем шаблоне. И это можно сделать следующим образом:
{% block item %}<p class="item">{{ super() }}</p>{% endblock %}

#### Вложенное наследование шаблонов

файл base.tpl – такой же как и ex_main.htm:
файл child1.htm: {% extends 'base.tpl' %} …
файл child2.htm: {% extends 'child1.htm' %} …


### прогресс выполнения в Python
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


### Сервер
#### wsgi

socket
сервер
![](https://imgur.com/a/eLxFFis)
![](https://imgur.com/a/WzOHnE3)
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

клиент
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print data

сокет с передачей картинки
![](https://imgur.com/a/T6XnanG)

#### курс крипты

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


### Работа с файлами 
#### csv
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

#### xml
парсинг
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


Python
1
2
3
4
5
obj_xml = etree.tostring(
    root,
    pretty_print=True,
    xml_declaration=True
)





#### pillow
https://www.youtube.com/watch?v=d7D2UuUqtgs&list=PLEYdORdflM3k2U6xicasFS3NXWwaZo8kw

from PIL import ImageOps
image = ImageOps.exif_transpose(image)
поворот по exif



#### pdf
 
https://python-scripts.com/create-pdf-pyfpdf
excel
https://www.youtube.com/watch?v=VQNV_oOdOqo
https://www.youtube.com/watch?v=d5jHpPSp5uI&t=4s
#### pickle
>>> import pickle
>>> data = {
...    'a': [1, 2.0, 3, 4+6j],
...    'b': ("character string", b"byte string"),
...    'c': {None, True, False}
... }
>>>
>>> with open('data.pickle', 'wb') as f:
...    pickle.dump(data, f)
...
>>> with open('data.pickle', 'rb') as f:
...    data_new = pickle.load(f)
...
>>> print(data_new)
{'c': {False, True, None}, 'a': [1, 2.0, 3, (4+6j)], 'b': ('character string', b'byte string')}
os
os.name - имя операционной системы. Доступные варианты: 'posix', 'nt', 'mac', 'os2', 'ce', 'java'.
os.environ - словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
os.getlogin() - имя пользователя, вошедшего в терминал (Unix).
os.getpid() - текущий id процесса.
os.uname() - информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.
os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True) - проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
os.chdir(path) - смена текущей директории.
os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).
os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True) - меняет id владельца и группы (Unix).
os.getcwd() - текущая рабочая директория.
os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True) - создаёт жёсткую ссылку.
os.listdir(path=".") - список файлов и директорий в папке.
os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.
os.remove(path, *, dir_fd=None) - удаляет путь к файлу.
os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.
os.renames(old, new) - переименовывает old в new, создавая промежуточные директории.
os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает из src в dst с принудительной заменой.
os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.
os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None) - создаёт символическую ссылку на объект.
os.sync() - записывает все данные на диск (Unix).
os.truncate(path, length) - обрезает файл до длины length.
os.utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True) - модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).
os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
os.system(command) - исполняет системную команду, возвращает код её завершения (в случае успеха 0).
os.urandom(n) - n случайных байт. Возможно использование этой функции в криптографических целях.
os.path - модуль, реализующий некоторые полезные функции на работы с путями.

os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.
os.path.abspath(path) - возвращает нормализованный абсолютный путь.
os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
os.path.dirname(path) - возвращает имя директории пути path.
os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.
os.path.getatime(path) - время последнего доступа к файлу, в секундах.
os.path.getmtime(path) - время последнего изменения файла, в секундах.
os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
os.path.getsize(path) - размер файла в байтах.
os.path.isabs(path) - является ли путь абсолютным.
os.path.isfile(path) - является ли путь файлом.
os.path.isdir(path) - является ли путь директорией.
os.path.islink(path) - является ли путь символической ссылкой.
os.path.ismount(path) - является ли путь точкой монтирования.
os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).
os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.
os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.
os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).
os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.
os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.




### аргументы командной строки
https://foxford.ru/wiki/informatika/analiz-argumentov-komandnoy-stroki-v-python


### Цикл разработки сайта

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