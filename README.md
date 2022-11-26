# Оглавление

https://roadmap.sh/backend





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

### Roadmap <a name="roadmap"></a>


  
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
  



### База <a name="base"></a>
#### Frontend <a name="base_frontend"></a>
Тут необходимо изучить верстку на базовом уровне, т. е. вы должны уметь сверстать простую страницу используя css и html.

[Тут](https://github.com/acilsd/wrk-fet#javascript) хранится информация как и что учить.

#### Как работает Интернет <a name="how_to_work_internet"></a>
Вы должны знать базовые вещи:
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

#### Linux <a name="base_linux"></a>
Что нужно знать:
* Простые терминальные команды
* Терминальные утилиты Linux, необходимые в разработке grep, curl,lsof,awk,wget,tail,head,less,find,ssh,kill,htop [Моя шпаргалка](https://github.com/DefaultPerson/Linux_misc/tree/main/console_utils)
* управление процессами
* io управление
* управлению памятью
* взаимодействие между процессами
* posix basics(stdin,stdout,stderr,pipes)
***

### Начало <a name="begin"></a>
#### VCS <a name="VCS"></a>
* Создать аккаунт гитхаб
* Выучить базовые команды и операции
* Ветки и слияние веток
* Интегрировать с IDE
  
[Интерактивный курс по гиту](https://githowto.com/ru/setup)

[Тут вы можете потренироваться](https://gitexplorer.com/)

#### Python <a name="python-base"></a>

Сначала пролистать книгу: [Укус питона](http://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf), объем не о чем 164 страницы, из которых часть вступление и эпилог.

Потом можно пройти [курс](python_course), в процессе использовать [этот сайт](https://proproprogs.ru/python) и гугл.

Можно глянуть [этот канал](https://www.youtube.com/c/%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9%D0%A5%D0%B8%D1%80%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2/playlists)

Также можно после курса пролистать книжку:[Книга рецептов](https://codernet.ru/books/python/python_kniga_receptov/)   


Очень опционально(не рекомендую тратить время):
[Игра по основам языка](https://py.checkio.org/) 

[Кодворс](https://www.codewars.com/dashboard) 

[задачи](https://acmp.ru/index.asp?main=tasks)











#### Базы данных. <a name="databases"></a>

* знать PostgreSQL, как ее поставить, минимально настроить, создавать там БД, таблицы, делать в них запросы. joinы с несколькими таблицами, со сложными группировками, having, оконными функциями и тд.
* Надо знать про индексы и про хотя бы минимальную их настройку, про внешние ключи и нормализацию и денормализацию БД, конечно, надо понимать, плюсы и минусы нормализованной и денормализованной БД.

* orm,acid
* транзакции
* проблема n+1
* теорема CAP
* Data replication
* sharding stratages

* Реляционные: mySQl, postgresql, SQLite
* Nosql: MongoDB

Книжки(для себя, не обязательно)

[Книга 1](https://codernet.ru/books/sql/sem_baz_dannyx_za_sem_nedel/) 

[Книга 2](https://ilshatpro.files.wordpress.com/2017/08/d0ba-d0b4d0b6-d0b4d0b5d0b9d182-d0b2d0b2d0b5d0b4d0b5d0bdd0b8d0b5-d0b2-d181d0b8d181d182d0b5d0bcd18b-d0b1d0b0d0b7-d0b4d0b0d0bdd0bdd18b.pdf) 

[Книга 3](https://psv4.userapi.com/c848428/u44301783/docs/d13/b0f96ba2e817/MySQL_po_maximumu.pdf?extra=ViMMYPVqhdY3EHwncPtkpyWylriSPBgvRQ4nmjzMXyJCQgjcIN2KrYJMtceC0joI2IjQsCOT5MRwPrPzHyrXkT7ZatOztnhAv4hqRm5oTMG3TwY1xAMUCh_yRURLW-VkGfttMOLSIRek3gSwNCto)

[Сайт](https://proproprogs.ru/modules/chto-takoe-subd-i-relyacionnye-bd)
***


### Можно начать ходить на собеседования(нужны проекты на гитхабе) <a name="interview"></a>

#### APIs <a name="apis"></a>
* json
* soap
* rest
* json-rpc
* hateoas
* gRPC
* Swagger

#### Django <a name="django"></a>
[О шаблонизаторе](https://proproprogs.ru/modules/chto-eto-ispolzovanie-v-shablonah)
[Быстрый вкат в django](https://proproprogs.ru/django/django-chto-eto-takoe-poryadok-ustanovki)
[Документация](https://djbook.ru/rel3.0/)

**Книжки**

[Книга 1](https://vk.com/doc255577237_555736434?hash=958c0344b1ed45ebc3&dl=2dff05379401cb4001) [Книга 2](https://vk.com/doc183707182_490008703?hash=843b6e0736d10cab54&dl=782d42312e85a54b9e) [Книга 3](https://readthedocs.org/projects/django-orm-cookbook/downloads/pdf/latest/) [Книга 4](https://books.agiliq.com/_/downloads/django-admin-cookbook/en/latest/pdf/)

**Плейлисты**
[Первый](https://www.youtube.com/playlist?list=PLrgHtaQ10vi3xalWI7q6Uzr7aZUNT0BJH) [Второй](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqwKfXqpgDKqjUDAe8qbCem) [Третий](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrTEtHA8zhIVeNIzXjmS8Vu) [Четвертый](https://www.youtube.com/playlist?list=PLF-NY6ldwAWpktIw6ailetqjXibKlOLY_) [Пятый](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C) [Шестой ](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq) [Седьмой](https://www.youtube.com/playlist?list=PLF-NY6ldwAWrQz1aZB-gxR5WnP40RIJSj) [Восьмой](https://www.youtube.com/playlist?list=PLF-NY6ldwAWpjARuT4-IoL3cNLIGdF0RL) [Девятый](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F)

Чеклист:
* ![](https://sun9-57.userapi.com/impg/zhZRzgSzQIyr9hDlEHrTP6BePViZJF6ZiUf7SA/NOj6VI7rdoU.jpg?size=979x680&quality=96&sign=144b627ef5b06f3dc9485f45b442070d&type=album)

* полезно знать тестирование в Django.
* Надо знать правильную структуру Django проектов, понимание, где писать бизнес-логику.
* Как работать со своими management  командами в Django.
* Аутентификация через социальные сети
* ролевую модель в приложении и отслеживание прав пользователей
* Глубокое понимание MVC и ORM
* Работа с Middleware
* Полнотекстовый поиск
* В идеале еще знать DRF

#### Кэширование <a name="cash"></a>
* Серверное(redis,memcached)
* CDN,на стороне клиента
***

### Нужно начать ходить на собеседования(нужны проекты на гитхабе) <a name="interview-adv"></a>
#### Вебсерверы,инструменты(докер),CI/CD <a name="Instruments"></a>
* В качестве CI/CD гитлаю
* Работа с фоновыми задачами (celery)
* Запуск задач по расписанию(кронтаб)
* Вы должны уметь полностью настроить для себя сервер. Nginx, какой-нибудь gunicorn или uwsgi, django, celery, postgresql, redis. Вам должно быть абсолютно комфортно работать в командной строке, в консоли.

#### Тестирование <a name="testing"></a>
* Какие бывают тесты, чем они отличаются, когда что использовать. Какие есть методологии разработки, связанные с тестированием и почему они хороши (TDD и тд).

#### Практика <a name="practice"></a>
* Магазин, бронирование билетов или любая своя идея.
* Использовать максимальное количество фишек пушить на гитхаб
***
### Нужные темы <a name="must_learn"></a>
#### О современной разработке и прочее <a name="base_must_learn"></a>
* масштабирование горизонтальное и вертикальное
* стратегии миграций
https://habr.com/ru/company/edison/blog/269789/
* [Структуры данных и вопросы на собесах](https://proglib.io/p/8-data-structures/)
* [Алгоритмы](https://www.youtube.com/watch?v=S2I0covkyMc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ)[Книга для ознакомления](https://vk.com/doc2036633_461668315?hash=9e4596e3a4e884a404&dl=75f266060bb1e7060e)
Особенно языка python 
[1](https://github.com/satwikkansal/wtfpython)
[2](https://habr.com/ru/company/mailru/blog/337364/)

#### Безопасность <a name="security"></a>
Необходимо знать что пароли в БД нужно хранить в зашифрованном виде с помощью хэш-функций. Необходимо знать что такое протокол https, протоколы ssl/tls. Знать что такое “политика защиты контента csp”, она например реализована в django. Что такое CORS(Кроссдоменные запросы).

Знать разницу между авторизацией/аутентификацией. Знать что есть протокол авторизации oauth, стандарт jwt, mfa(Многофакторная аутентификация).

Базовые уязвимости https://developer.mozilla.org/ru/docs/Learn/Server-side/First_steps/Website_security

Топ 10 уязвимостей в этом году https://owasp.org/www-project-top-ten/

Список атак на веб ресурсы https://owasp.org/www-community/attacks/

Инструменты для сканирования на уязвимости https://owasp.org/www-community/Vulnerability_Scanning_Tools


#### Качество кода <a name="code_qu"></a>
* Следование стандартам разработки PEP8.
* Принципы написания качественного ПО. Про нейминг, про KISS, DRY, yagni про ООП и про Solid, про основные шаблоны проектирования, про чистый код. 
**Книги**
[Книга 1](https://www.livelib.ru/book/1001122709-sovershennyj-kod-masterklass-stiv-makkonnell) [Книга 2 ](https://www.livelib.ru/book/1000799728-struktura-i-interpretatsiya-kompyuternyh-programm-harold-abelson) [Книга 3](https://www.livelib.ru/book/1000020456-iskusstvo-programmirovaniya-tom-1-osnovnye-algoritmy-donald-e-knut) [Книга 4](https://www.livelib.ru/book/1000131747-iskusstvo-programmirovaniya-tom-2-poluchislennye-algoritmy-3e-izdanie-donald-e-knut) [Книга 5](https://www.livelib.ru/work/1002361405-priemy-obektnoorientirovannogo-proektirovaniya-patterny-proektirovaniya-erih-gamma-richard-helm-ralf-dzhonson-dzhon-vlissides) [Книга 6](https://www.livelib.ru/book/1000335711-refaktoring-uluchshenie-suschestvuyuschego-koda-dzhejn-roberts) [Книга 7](https://www.livelib.ru/book/1001581900-programmistpragmatik-put-ot-podmasterya-k-masteru-endi-hant) [Книга 8 ](https://www.livelib.ru/book/1000308145-ekstremalnoe-programmirovanie-razrabotka-cherez-testirovanie-kent-bek)

#### Паттерны проектирования <a name="patterns"></a>
* SOA
* CQRS and Event sourcing
* serverless
* Монолитный
* микросервисы

#### Брокеры сообщений <a name="message_brokers"></a>
* kafka
* rabbitmq
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

1. собрать ситуацию по вакансиям(мидл)
2. проверить технологии в вакансиях, выписать все что не знаю в эксель
3. резюме все технолгии которые нашли, технологии(с подтверждением), фотография в деловом стиле(в рф), оформление, проверить на чб печати, показать hrу, название фамилия имя профессия,пдф, отправить резюме во все компании с  сопроводительным писбмом " хочу работать у вас, ятакой то"
4. линкед ин+ищу работу+должность+наполнить чем-нибудь профиль+заполнить навыки, попросить всех кого знаю их подтвердить



# ру 
питон
алгоритмы и стругтуры данных
ооп
гит
технический английский
линукс
бд sql mysql postgresql
умегие разбираться в чужом коде
ВО
html css js
django flask tensorflow и пр.
тесты TDD
SOLID DRY KISS
Nosql(mongodb)
многопоточное асинхронное программирование
шаблоны проектирования
docker redis rabbitmq kafka celery jenkins ci/cd rest orm
опыт разработки опыт проектирования архитектуры

# us
питон
Тесты
Алгоритмы, структуры данных, КС
гит 
линукс
бд sql mysql postgresql
ВО
html css js
Agile - scrum kanban
django flask tensorflow и пр.
pytest unittest
mongodb
многопоточное ассинхронное программирование
шаблоны проектирования
docker redis rabbitmq kafka celery jenkins ci/cd rest orm jira cassandra spark
aws google cloud platform
Принципы построение архитектуры = клиент-сервер, микросервис, монолит
опыт разработки опыт проектирования архитектуры
https://github.com/timofurrer/awesome-asyncio
https://github.com/vinta/awesome-python
https://emacsway.github.io/ru/service-layer/#application-logic
https://habr.com/ru/company/yandex/blog/499534/


❄️, [17.05.2022 11:03]
[Переслано от ❄️]
В общем часть часть материала который я рекомендую из одного курса, аккаунт я дам, курсы обычно говно и трата денег, но этот норм, т.к. в нем нет воды, структурировано и куча заданий от простейших конструкций до чуть продвинутого ООП. Задания надо проходить честно(честно это когда не получилось решить задачу за несколько часов, откладываешь ее на след. день, не получилось решить на след. день- смотришь решение).

В общем чтобы как изучать питон:
0.Думаешь что хочешь написать, если ты хочешь просто изучить питон быстро бросишь, должна быть причина и цель, это ВАЖНО.

1. Первое с чего стоит начать это популярная книжка:
https://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf
Если ты интересовался изучением Python, скорее всего ты уже много рекомендации этой книги видел.
Там всего 140 страниц для чтения, написано неформальным языком(легко читается), поможет смотреть на конструкции в языке уже как на знакомые, поэтому можно просто пролистать за день-два, главное не запомнить что там написано(хотя желательно), а просто ознакомится с языком.

2.Проходишь тот курс который я упомянул
skillbox(да, у них есть что-то годное, я много курсов перелапатил, я знаю о чем говорю)
sweetpepper666@protonmail.com
Navarroarroyo2241

Правило! Не менять данные для входа, аккаунт не мой, уважай других людей. Также данные входа не раздавать.

Там нужен курс python basic(ведет молодой парень в очках), у него короткие ролики без водички, в конце каждого модуля задания. Делаешь задания ЧЕСТНО заглядывая в ответы в крайнем случае (не можешь решить задачу несколько часов, попробуй решить на след. день, не получилось, заглянул в ответ). Курс может занять у тебя много времени, месяц вполне или больше.

3. Ближе к концу курса берешь книгу Лутца по питону( та что в двух томах)
https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_1_mark_lutc/
https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_2_mark_lutc/
Ее НЕ надо читать, она написана в трудном для восприятия стиле, после 10 страниц тебе уже захочется бросить и книгу и программирование в целом.
Что нужно с ними делать:
1. Открываешь оглавление обоих книг и браузер
2. Все названия и термины которые ты видишь в первый раз гуглишь и читаешь что это такое только без душного описания на сотни страниц.
3. Чтобы понять что ты изучил тему или концепцию, объясни ее сам себе простыми словами(или кому-нибудь), это гарантирует то что ты запомнишь и поймешь что ты изучил.

3.5. Дополнительно:
Если нужно больше начальной теории https://proproprogs.ru/python оттуда бери только основы и ООП(но далее можешь брать все что хочешь, а пока рано). Можно еще пролистать книжку https://codernet.ru/books/python/python_kniga_receptov/ там просто примеры кода прикольные.

Это займет у тебя время месяца 2, но ты освоишь язык. Если есть вопросы или надо что-то объяснить-пишешь мне.






Далее:

4. Ты узнаешь как устроен современный веб(что такое API, frontend, backend и вообще в принципе в голове должно быть примерно как устроены и работают современные вебаппки). Ну и начинаешь смотреть и изучать что тебе из библиотек нужно для твоих целей, также можешь спросить меня. Сами библиотеки заучивать НЕ надо,  у них есть документация и примеры использования и библиотек очень много, можно просто запомнить что они делают и использовать по надобности, также когда мне будет не лень, скину чем список заметок свой по парсингу, ботам и пр., если не скину нужно мне напомнить.

5. Делаешь сам что хочешь(например идея из пункта 0), у тебя уже будет достаточно навыков, ты смело можешь брать любую библиотеку и применять(повторяю библиотеки не учат, их используют с документацией и примерами к ним). Их тысячи на любую тему.

6. Узнаешь всякие новые концепции и применяешь, например: асинхронность, кэширование, многопоточность и многопроцессорность.
Кстати хорошие каналы для новичков:
https://www.youtube.com/c/PythonToday
https://www.youtube.com/c/ZProgerIT
Много полезного.

❄️, [17.05.2022 11:03]
[Переслано от ❄️]
!Пункт дополнительный:
Можно изучить систему контроля версий  git и завести аккаунт на github, быстрое изучение гита:
https://githowto.com/ru
Можно изучить linux на базовом уровне, просто  гуглишь linux shell и тренируешься на виртуалке.
Изучить работу с бд(sqlite3) и что такое orm(начни с sqlalchemy или peewee).
Можешь подробнее рассмотреть этот ресурс:  https://proproprogs.ru
Можешь посмотреть требования к коду, что такое KISS, DRY, pep8...
Ну и в дополнение к концепциям, нужно бы знать что такое сериализация, брокеры сообщений, короче самому интересоваться и изучать новое.

7. Ну собственно все, далее ищешь и впитываешь инфу сам, в принципе ты в состоянии и другой ЯП выучить быстро если нужно, или самостоятельно углубится в бэкенд или что-то еще.

