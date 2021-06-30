# Оглавление

1. [Roadmap](#roadmap)
2. [База](#base)
    1. [Система контроля версий](#VCS)
    2. [Базовый фронтенд](#base_frontend)
    3. [Теория о работе интернета](#how_to_work_internet)
    4. [Базовая работа в linux](#base_linux)
3. [Начальные навыки](#begin)
    1. [Python](#python-base)
    2. [Базы данных](#databases)
4. [После прохождения данной части можно пробовать искать работу](#interview)
    1. [APIs](#apis)
    2. [Фреймворк Django](#django)
    3. [Кэширование](#cash)
5. [После прохождения данной части нужно пробовать искать работу](#interview-adv)
    1. [Инструменты для разработки](#Instruments)
    2. [Тестирование](#testing)
    3. [Практика](#practice)
6. [Нужные темы](#must_learn)
    1. [О современной разработке](#base_must_learn)
    2. [Безопасность веб-приложений](#security)
    3. [Качество кода](#code_qu)
    4. [Паттерны проектирования](#patterns)
    5. [Брокеры сообщений](#message_brokers)
7. [Дальнейшее развитие](#adv)
8. [Поиск работы](#work)

# Roadmap <a name="roadmap"></a>

<code>
  
                                                              BACKEND ROADMAP
                                                                     |
                                                   -----------------База-------------
                                                  |                  |              |
                                                  |                  |              |
                                                  |                  |              |
                                                  |                  |              |
                      Базовые знания о фронтенде _|       Как работает Интернет     |__Linux
                                                                     |
                                                                     |                                                 
                                                                     |
                                                        -----------Начало-----------
                                                       |             |              |
                                                       |             |              |
                                                       |             |              |
                                                       |             |              |
                                            VCS(Git) __|           Python           | __Базы данных
                                                                     |
                                                                     |
                                                                     |
                                                                     |                
                             -----------Можно начать ходить на собеседования(нужны проекты на гитхабе)-----------
                           |                                         |                                           |
                           |                                         |                                           |
                           |                                         |                                           | 
                           |                                         |                                           |
                      APIs_|                                       django                                        |__Кэширование
                                                                     |
                                                                     |
                                                                     |
                                                                     |
                                         Нужно начать ходить на собеседования(нужны проекты на гитхабе)-----------
                                              |                      |                                            |
                                              |                      |                                            |
                                              |                      |                                            | 
                                              |                      |                                            |
         Вебсерверы,инструменты(докер),CI/CD _|                Тестирование                                       |__Практика
                                                                     |
                                                                     |
                                                                     |
                                                                     |
                                          ----------------------Нужные темы------------------------------
                                          |              |           |       |                          |
                                          |              |           |       |                          |
                                          |              |           |       |                          |
                                          |              |           |       |                          |
       О современной разработке и прочее _| Безопасность_|           |       |__Паттерны проектирования |_Брокеры сообщений
                                                                     |
                                                                     |
                                                                     |
                                                                     |
                             ------------------------------Дальнейшее развитие_______
                             |          |                            |               |
                             |          |                            |               |
                             |          |                            |               |
                             |          |                            |               |
      Принципы написания кода|  GraphQt_|   Изучение JS и фреймворка(например реакт) |_Изучение фреймворкорков(flask и fastapi например)
  
</code>



# База <a name="base"></a>
### Frontend <a name="base_frontend"></a>


Необходимое:
* Css
* Html
* Позиционирование флекс, флоат. 
* Адаптивность media queries. 
* chrome developer tools, работа с DOM деревом в ней, с сетью, с JS консолью.

Углубленное изучение(пока пропустить):
* Less sass
* JavaScript и JavaScript API браузера. 
* Узнавать JQuery
* Document.querySelector, работа с CSS стилями из JavaScript, переменные, циклы, функции Javascript, работа с AJAX запросами (и на стороне фронтенда, то есть JS, и на стороне бэкенда, то есть Pythonа), модель асинхронности JavaScript. 
Одолженный фак https://github.com/acilsd/wrk-fet#javascript

### Как работает Интернет <a name="how_to_work_internet"></a>
Чеклист:
* Работа интернета, ip адреса и устройство глобальной сети. 
* DNS и как он работает, что происходит при переходе на интернет адрес. 
* Hosts файл. 
* Запуск чего-либо на своем домене 2-3 уровня, то есть как привязать к домену свой сервер. Причем это надо уметь настроить физически на линукс сервере, например, в nginx.
* HTTP и HTTPS уметь настроить на вашем домене  работу по защищенному HTTPS протоколу.
* Как работает HTTP. Виды HTTP запросов, чем они отличаются и когда целесообразно какие виды запросов применять. Основные HTTP статусы и что они означают, какие поля есть в HTTP запросах и за что они отвечают, хотя бы базовые.
* Как работают и для чего нужны Cookies, какие они бывают, как с ними работать из JavaScript c клиентской части и как с ними работать с серверной части.
* Как работают авторизация и аутентификация на веб-сайтах и в мобильных приложениях, которые хранят данные на сервере. Кстати, разницу между авторизацией и аутентификацией тоже надо понимать.
* В идеале вы должны уметь настроить механизм сессий без веб-фреймворков, просто чтобы понимать, как это всё работает под капотом вашего любимого фреймворка, того же Django. Чтобы у вас было настоящее понимание о том, что там никакой магии не происходит.
* Кэширование на стороне клиента

### Linux <a name="base_linux"></a>
Чеклист:
* Простые терминальные
* Терминальные утилиты Linux, необходимые в разработке grep, curl,se,lsof,,awk,wget,tail,head,less,find,ssh,kill,rip,htop
* управление процессами
* io управление
* управлению памятью
* взаимодействие между процессами
* posix basics(stdin,stdout,stderr,pipes)



# Начало <a name="begin"></a>
## VCS <a name="VCS"></a>
* Создать аккаунт гитхаб
* Выучить базовые команды и операции
* Ветки и слияние веток
* Интегрировать с IDE
* [1123](https://gitexplorer.com/)

## Python <a name="python-base"></a>

Сначала пролистать книгу: [Укус питона](http://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf), объем неочем 164, из которых часть вступление и эпилог.

**сделать тут что-нибудь**, в процессе использовать [этот сайт](https://proproprogs.ru/python) и гугл.

Можно глянуть [этот плейлист](https://www.youtube.com/c/%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9%D0%A5%D0%B8%D1%80%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2/playlists)

Также можно после курса пролистать книжку:[Книга рецептов](https://codernet.ru/books/python/python_kniga_receptov/)   


Очень опционально(не рекомендую тратить время):[Игра по основам языка](https://py.checkio.org/) [Кодворс](https://www.codewars.com/dashboard) [задачи](https://acmp.ru/index.asp?main=tasks)





## Базы данных. <a name="databases"></a>

* знать PostgreSQL, как ее поставить, минимально настроить, создавать там БД, таблицы, делать в них запросы. joinы с несколькими таблицами, со сложными группировками, having, оконными функциями и тд.
* Надо знать про индексы и про хотя бы минимальную их настройку, про внешние ключи и нормализацию и денормализацию БД, конечно, надо понимать, плюсы и минусы нормализованной и денормализованной БД.

* orm,acid
* транзакции
* проблема n+1
* теорема CAP
* Data replication
* sharding stratages

* Реляционные: mySQl, postgresql.
* Nosql: MongoDB

Книжки(для себя, не обязательно)
[Книга 1](https://codernet.ru/books/sql/sem_baz_dannyx_za_sem_nedel/) [Книга 2](https://ilshatpro.files.wordpress.com/2017/08/d0ba-d0b4d0b6-d0b4d0b5d0b9d182-d0b2d0b2d0b5d0b4d0b5d0bdd0b8d0b5-d0b2-d181d0b8d181d182d0b5d0bcd18b-d0b1d0b0d0b7-d0b4d0b0d0bdd0bdd18b.pdf) [Книга 3](https://psv4.userapi.com/c848428/u44301783/docs/d13/b0f96ba2e817/MySQL_po_maximumu.pdf?extra=ViMMYPVqhdY3EHwncPtkpyWylriSPBgvRQ4nmjzMXyJCQgjcIN2KrYJMtceC0joI2IjQsCOT5MRwPrPzHyrXkT7ZatOztnhAv4hqRm5oTMG3TwY1xAMUCh_yRURLW-VkGfttMOLSIRek3gSwNCto)
Ресурс для быстрого вката: [Клик](https://proproprogs.ru/modules/chto-takoe-subd-i-relyacionnye-bd)
***
***
***







# Можно начать ходить на собеседования(нужны проекты на гитхабе) <a name="interview"></a>

***
***
***

## APIs <a name="apis"></a>
* json
* soap
* rest
* json-rpc
* hateoas
* gRPC
* Swagger

## Django <a name="django"></a>
[О шаблонизаторе](https://proproprogs.ru/modules/chto-eto-ispolzovanie-v-shablonah)
[Быстрый вкат в django](https://proproprogs.ru/django/django-chto-eto-takoe-poryadok-ustanovki)
[Документация](https://djbook.ru/rel3.0/)

### Книжки
[Книга 1](https://vk.com/doc255577237_555736434?hash=958c0344b1ed45ebc3&dl=2dff05379401cb4001) [Книга 2](https://vk.com/doc183707182_490008703?hash=843b6e0736d10cab54&dl=782d42312e85a54b9e) [Книга 3](https://readthedocs.org/projects/django-orm-cookbook/downloads/pdf/latest/) [Книга 4](https://books.agiliq.com/_/downloads/django-admin-cookbook/en/latest/pdf/)

### Плейлисты
[Первый](https://www.youtube.com/playlist?list=PLrgHtaQ10vi3xalWI7q6Uzr7aZUNT0BJH) [Второй](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqwKfXqpgDKqjUDAe8qbCem) [Третий](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrTEtHA8zhIVeNIzXjmS8Vu) [Четвертый](https://www.youtube.com/playlist?list=PLF-NY6ldwAWpktIw6ailetqjXibKlOLY_) [Пятый](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C) [Шестой ](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq) [Седьмой](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrQz1aZB-gxR5WnP40RIJSj) [Восьмой](https://www.youtube.com/playlist?list=PLF-NY6ldwAWpjARuT4-IoL3cNLIGdF0RL) [Девятый](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F)

Чеклист:
* ![](https://sun9-57.userapi.com/impg/zhZRzgSzQIyr9hDlEHrTP6BePViZJF6ZiUf7SA/NOj6VI7rdoU.jpg?size=979x680&quality=96&sign=144b627ef5b06f3dc9485f45b442070d&type=album)
* Создание проекта и приложений
* модели и миграции, 
* создание роутов и контроллеров, которые называются Views в Django, 
* полезно знать тестирование в Django.
* Джанговый ORM
* джанговый язык темплейтов.
* Надо знать правильную структуру Django проектов, понимание, где писать бизнес-логику. 
* Как работать с джанговой админкой. 
* Как работать с юзерами, авторизацией и аутентификацией в Django. 
* Как работать со своими management  командами в Django.
* Аутентификация через социальные сети
* Сложные формы
* Deploy приложений
* ролевую модель в приложении и отслеживание прав пользователей
* Глубокое понимание MVC и ORM
* Работа с Middleware
* Полнотекстовый поиск
* В идеале еще знать DRF

## Кэширование <a name="cash"></a>
* Серверное(redis,memcached)
* CDN,на стороне клиента
***
***
***
# Нужно начать ходить на собеседования(нужны проекты на гитхабе) <a name="interview-adv"></a>

***
***
***
## Вебсерверы,инструменты(докер),CI/CD <a name="Instruments"></a>
* В качестве CI/CD гитлаю
* Работа с фоновыми задачами (celery)
* Запуск задач по расписанию(кронтаб)
* Вы должны уметь полностью настроить для себя сервер. Nginx, какой-нибудь gunicorn или uwsgi, django, celery, postgresql, redis. Вам должно быть абсолютно комфортно работать в командной строке, в консоли.

## Тестирование <a name="testing"></a>
* Какие бывают тесты, чем они отличаются, когда что использовать. Какие есть методологии разработки, связанные с тестированием и почему они хороши (TDD и тд).

## Практика <a name="practice"></a>
* Магазин, бронирование билетов или любая своя идея.
* Использовать максимальное количество фишек пушить на гитхаб
***
***
***
# Нужные темы <a name="must_learn"></a>

***
***
***
## О современной разработке и прочее <a name="base_must_learn"></a>
* масштабирование горизонтальное и вертикальное
* стратегии миграций
https://habr.com/ru/company/edison/blog/269789/
* [Структуры данных и вопросы на собесах](https://proglib.io/p/8-data-structures/)
* [Алгоритмы](https://www.youtube.com/watch?v=S2I0covkyMc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ)[Книга для ознакомления](https://vk.com/doc2036633_461668315?hash=9e4596e3a4e884a404&dl=75f266060bb1e7060e)
Особенно языка python 
[1](https://github.com/satwikkansal/wtfpython)
[2](https://habr.com/ru/company/mailru/blog/337364/)

## Безопасность <a name="security"></a>
* Хэш-алгоритмы
* https
* ssl/tls
* политика защиты контента csp
* cors
* owasp security risks
* security тактики
* Авторизация/аутентификация oauth/jwt/mfa
* SR
* content security policy

## Качество кода <a name="code_qu"></a>
* Следование стандартам разработки PEP8.
* Принципы написания качественного ПО. Про нейминг, про KISS, DRY, yagni про ООП и про Solid, про основные шаблоны проектирования, про чистый код. 
**Книги**
[Книга 1](https://www.livelib.ru/book/1001122709-sovershennyj-kod-masterklass-stiv-makkonnell) [Книга 2 ](https://www.livelib.ru/book/1000799728-struktura-i-interpretatsiya-kompyuternyh-programm-harold-abelson) [Книга 3](https://www.livelib.ru/book/1000020456-iskusstvo-programmirovaniya-tom-1-osnovnye-algoritmy-donald-e-knut) [Книга 4](https://www.livelib.ru/book/1000131747-iskusstvo-programmirovaniya-tom-2-poluchislennye-algoritmy-3e-izdanie-donald-e-knut) [Книга 5](https://www.livelib.ru/work/1002361405-priemy-obektnoorientirovannogo-proektirovaniya-patterny-proektirovaniya-erih-gamma-richard-helm-ralf-dzhonson-dzhon-vlissides) [Книга 6](https://www.livelib.ru/book/1000335711-refaktoring-uluchshenie-suschestvuyuschego-koda-dzhejn-roberts) [Книга 7](https://www.livelib.ru/book/1001581900-programmistpragmatik-put-ot-podmasterya-k-masteru-endi-hant) [Книга 8 ](https://www.livelib.ru/book/1000308145-ekstremalnoe-programmirovanie-razrabotka-cherez-testirovanie-kent-bek)

## Паттерны проектирования <a name="patterns"></a>
* SOA
* CQRS and Event sourcing
* serverless
* Монолитный
* микросервисы

## Брокеры сообщений <a name="message_brokers"></a>
* kafka
* rabbitmq
***
***
***


# Дальнейшее развитие <a name="adv"></a>

### FlaskFlask, fastapi, aiohttp.
[Быстрый вкат](https://proproprogs.ru/flask/flask-chto-eto-takoe-wsgi-prilozhenie)
### Fastapi
* [1](https://github.com/DJWOMS/FastAPI_ru)
* [2](https://www.youtube.com/channel/UCFCaz7mA2qNodfTh0x1ET5Q)


* https://github.com/adam-golab/react-developer-roadmap/blob/master/roadmap-ru.png
* https://github.com/vpavlenko/web-2020
* https://euler.jakumo.org/problems.html
* [Роадмапы](https://github.com/kamranahmedse/developer-roadmap)
* [Куча бесплатного материала](https://github.com/EbookFoundation/free-programming-books)
* [Университетская ИТ база](https://github.com/jwasham/coding-interview-university)
* [жс собес](https://habr.com/ru/post/486820/)

# Устройство на работу <a name="work"></a>
https://habr.com/ru/company/mailru/blog/350326/
[Статья на хабре](https://habr.com/ru/post/499394/)
* Площадки с вакансиями (hh, moikrug, linkedin)
* Чаты и каналы с вакансиями (telegram js_jobs, etc.)
* Нарисовать опыт, придумать историю, что интересного и необычного было, если что соглашение о неразглашении
* Составить резюме
* Выяснить вилку: у вас еще десяток предложений по другим вакансиям,что не хотите терять преиумещства называя желаемую зп,Чтобы назвать вилку вам сначала нужно подробнее узнать о фирме, команде, условиях работы, доп плюшках
* Спросить про
1. Тип оформления (нам нужен договор ТК РФ и белая зп на руки)
1. Какими системами баг-трекинга и учета рабочего времени пользуетесь (джира/трелло)
1. Наличие следящего ПО (наличие жесткого поминутного тайм трекинга и скринеров (hubstuff, time doctor) - красный флаг)
1. Размер команды разработки (без старших коллег вы практически не будете развиваться профессионально)
1. Наличие Тимлида/Сеньора (опять же вопрос вашего проф развития)
1. Частота пересмотра зарплаты (желательно полгода)
1. Какие бонусы имеются - скидка на курсы/участие в митапах/дмс
