# python_web_learning
Список материалов, информации, задания по которым я изучаю вебпрограммирование
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

# База

***
***
***
## Frontend
База:
* Css
* Html
* Позиционирование флекс, флоат. 
* Адаптивность media queries. 
* chrome developer tools, работа с DOM деревом в ней, с сетью, с JS консолью.

Углубленное изучение:
* Less sass
* JavaScript и JavaScript API браузера. 
* Узнавать JQuery
* Document.querySelector, работа с CSS стилями из JavaScript, переменные, циклы, функции Javascript, работа с AJAX запросами (и на стороне фронтенда, то есть JS, и на стороне бэкенда, то есть Pythonа), модель асинхронности JavaScript. 
* JSфреймворк (реакт или Vue)
Одолженный фак https://github.com/acilsd/wrk-fet#javascript

# Как работает Интернет 
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

## Linux
Чеклист:
* Простые терминальные
* Терминальные утилиты Linux, необходимые в разработке grep, curl,se,lsof,,awk,wget,tail,head,less,find,ssh,kill,rip,htop
* управление процессами
* io управление
* управлению памятью
* взаимодействие между процессами
* posix basics(stdin,stdout,stderr,pipes)
***
***
***










# Начало

***
***
***
## VCS
* Создать аккаунт гитхаб
* Выучить базовые команды и операции
* Ветки и слияние веток
* Интегрировать с IDE
* [1123](https://gitexplorer.com/)

## Python
Основы языка: [Укус питона](http://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf)

**Книги(пролистать, конспектировать то что покажется нужным)**
* [Лутц том 1](https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_1_mark_lutc/ ) углубленные основы, пролистать
* [Лутц том 2](https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_2_mark_lutc/)  ооп, пролистать
* [Справочник](https://codernet.ru/books/python/python_podrobnyj_spravochnik_devid_bizli/) основы и описание стандартных библиотек, пролистать
* [Книга рецептов](https://codernet.ru/books/python/python_kniga_receptov/)                Пролистать

**Не книги**
* [Курс яндекса](https://habr.com/ru/company/yandex/blog/498856/)
* [Ресурс с инфой по питону](https://proproprogs.ru/python )
* [Лекции препода МФТИ](https://www.youtube.com/c/%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9%D0%A5%D0%B8%D1%80%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2/playlists)

**Задачки**
* [Игра по основам языка](https://py.checkio.org/)
* [Кодворс](https://www.codewars.com/dashboard)
[1](https://acmp.ru/index.asp?main=tasks)

## Внешние библиотеки
* Pillow - работа с изображениями
* Requests -упрощенная работа с интернет протоколами
* Beautiful soup - одна из популярнейших библиотек для парсинга
* Simplejson - работа с json
* SQL Alchemy - работа с SQL
* telebot или другая библиотека для работы с телеграм ботами.

**Чеклист:**
* **Basic:**
* Переменные, условия, связанные условные выражения, операторы, условные операторы, циклы и итерации.
* Базовые структуры данных, функции, изменяемое против неизменяемого, общие методы, работа с файлами
* **Intermediate:***
* Базовое ООП
* Comprehensions
* Lambda функция
* Collections модуль
* Map, filter,zip
* *args and **kwargs
* Углубленное ООП
* Исключения
* PIP
* Environments(окружения)
* Модули и их создание
* Async IO(корутины и т.д.)
* Структуры данных
* **Advanced:**
* Декораторы
* Генераторы и итераторы
* Менеджеры контекста
* Метаклассы
* Конкурентность
* Параллелизм
* Тестирование
* Пакеты
* основные стандартные библиотеки
* Регулярные выражения. 
* Логирование
* Работа с pickle дампами, с JSON. 
* Работа с датами(там pytz и тд).
* Third-party библиотеки. Сюда входит например requests для работы с HTTP запросами. Aiohttp для отправки асинхронных запров и в качестве асинхронного веб-сервера. 
* Библиотеки для работы с Excel документами, PDF, XML, HTML (там beautiful soup тот же).

## Базы данных.

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








# Можно начать ходить на собеседования(нужны проекты на гитхабе)-

***
***
***

## APIs
* json
* soap
* rest
* json-rpc
* hateoas
* gRPC
* Swagger

## Django
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

## Кэширование
* Серверное(redis,memcached)
* CDN,на стороне клиента
***
***
***
# Нужно начать ходить на собеседования(нужны проекты на гитхабе)

***
***
***
## Вебсерверы,инструменты(докер),CI/CD
* В качестве CI/CD гитлаю
* Работа с фоновыми задачами (celery)
* Запуск задач по расписанию(кронтаб)
* Вы должны уметь полностью настроить для себя сервер. Nginx, какой-нибудь gunicorn или uwsgi, django, celery, postgresql, redis. Вам должно быть абсолютно комфортно работать в командной строке, в консоли.

## Тестирование
* Какие бывают тесты, чем они отличаются, когда что использовать. Какие есть методологии разработки, связанные с тестированием и почему они хороши (TDD и тд).

## Практика
* Магазин, бронирование билетов или любая своя идея.
* Использовать максимальное количество фишек пушить на гитхаб
***
***
***
# Нужные темы

***
***
***
## О современной разработке и прочее
* масштабирование горизонтальное и вертикальное
* стратегии миграций
* agile разработка
* [Структуры данных и вопросы на собесах](https://proglib.io/p/8-data-structures/)
* [Алгоритмы](https://www.youtube.com/watch?v=S2I0covkyMc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ)[Книга для ознакомления](https://vk.com/doc2036633_461668315?hash=9e4596e3a4e884a404&dl=75f266060bb1e7060e)
Особенно языка python 
[1](https://github.com/satwikkansal/wtfpython)
[2](https://habr.com/ru/company/mailru/blog/337364/)

## Безопасность
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

## Качество кода
* Следование стандартам разработки PEP8.
* Принципы написания качественного ПО. Про нейминг, про KISS, DRY, yagni про ООП и про Solid, про основные шаблоны проектирования, про чистый код. 
**Книги**
[Книга 1](https://www.livelib.ru/book/1001122709-sovershennyj-kod-masterklass-stiv-makkonnell) [Книга 2 ](https://www.livelib.ru/book/1000799728-struktura-i-interpretatsiya-kompyuternyh-programm-harold-abelson) [Книга 3](https://www.livelib.ru/book/1000020456-iskusstvo-programmirovaniya-tom-1-osnovnye-algoritmy-donald-e-knut) [Книга 4](https://www.livelib.ru/book/1000131747-iskusstvo-programmirovaniya-tom-2-poluchislennye-algoritmy-3e-izdanie-donald-e-knut) [Книга 5](https://www.livelib.ru/work/1002361405-priemy-obektnoorientirovannogo-proektirovaniya-patterny-proektirovaniya-erih-gamma-richard-helm-ralf-dzhonson-dzhon-vlissides) [Книга 6](https://www.livelib.ru/book/1000335711-refaktoring-uluchshenie-suschestvuyuschego-koda-dzhejn-roberts) [Книга 7](https://www.livelib.ru/book/1001581900-programmistpragmatik-put-ot-podmasterya-k-masteru-endi-hant) [Книга 8 ](https://www.livelib.ru/book/1000308145-ekstremalnoe-programmirovanie-razrabotka-cherez-testirovanie-kent-bek)

## Паттерны проектирования## 
* SOA
* CQRS and Event sourcing
* serverless
* Монолитный
* микросервисы

## Брокеры сообщений
* kafka
* rabbitmq
***
***
***


# Дальнейшее развитие

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

# Устройство на работу
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
