# Тут собраны примеры работы с различными библиотеками и прочее для себя


1. [Тесты  и логирование](#test)
2. [Асинхронность и многопоточность и т. д.](#async_n_threads)
3. [Парсинг](#scrap)
4. [Библиотеки](#lib)
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
5. [Цикл разработки сайта ](#site)

## Тесты  и логирование <a name="test"></a>
### unittest(не рекомендуется, нарушает SOLID)

https://docs.python.org/3/library/unittest.html#re-using-old-test-code
https://ru.hexlet.io/courses/advanced_python/lessons/python_testing_unittest/theory_unit
https://pythonworld.ru/moduli/modul-unittest.html

### pytest

### logging

https://python-scripts.com/logging-python


### sqlalchemy

>>> ins = users.insert().values(name='jack', fullname='Jack Jones')


Вывод из бд
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
...     print("name:", name, "; fullname: ", fullname)
for row in result:
...     print("name:", row.name, "; fullname: ", row.fullname)
>>> result = conn.execute(s)
>>> row = result.fetchone()
>>> print("name:", row._mapping['name'], "; fullname:", row._mapping['fullname'])
row = result.fetchone()
name, fullname = row["name"], row["fullname"]
>>> row = result.fetchone()
>>> print("name:", row[1], "; fullname:", row[2])
for row in conn.execute(s):
...     print("name:", row._mapping[users.c.name], "; fullname:", row._mapping[users.c.fullname])
result.close()


from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
session().query(Users).filter(Users.id == 1).one().id
emmployee = session().query(Users).all()

.count()
exists()

one()-возвращает объяект если есть, если нет исключение .scalar() - возвращает объект или ноне если нет, если несколько исключение

    is_exists = session.query(exists().where(Department.name == department_name)).scalar()

Основные степени "ленивости":


select — по умолчанию. ORM делает запрос только тогда, когда обращаются к данным. Осуществляется отдельным запросом.
dynamic — позволяет получить объект запроса, который можно модифицировать по желанию. Получает данные из БД только после вызова all() или one() или любых других доступных методов.
joined — в основной запрос добавляется с помощью LEFT JOIN. Выполняется сразу.
subquery — похож на select, но выполняется как подзапрос.

По умолчанию — select.

def get_employee_with_skills(session: DBSession, eid: int):
    employee = session.query(EmployeeWithSkills).filter(EmployeeWithSkills.id == eid).one()
    
class EmployeeWithDepartments(Employee):
    departments = relation(
        Department,
        # primaryjoin=EmployeeDepartments.employee_id == Employee.id,
        secondary=EmployeeDepartments.__tablename__,
        # secondaryjoin=EmployeeDepartments.department_id == Department.id,
    )

Созданный класс не является новой таблицей БД. Это все та же таблица Employee, только расширенная c помощью relation. Таким образом, вы можете обращаться к таблице Employee или EmployeeWithDepartments в запросах. Разница будет лишь в отсутствии/наличии relation.

Первый аргумент указывает к какой таблице мы будем создавать relation.
primaryjoin — это условие, по которому будет подключаться вторая таблица до её присоединения к объекту.
secondary — имя таблицы, содержащее foreign_keys для сопоставления. Используется в случае many-to-many.
secondaryjoin — условия сопоставления промежуточной таблицы с последней.
primaryjoin и secondaryjoin служат для явного указания соответствий в сложных ситуациях.

def has_in_relations(session: DBSession, reason: str):
    employees = session.query(EmployeeWithCadreMovements).filter(EmployeeWithCadreMovements.cadre_movements.any(CadreMovement.reason == reason)).all()
    return employees

output:
    [Steve Rogers, Tony Stark]
last_cadre_movement = relation(
    CadreMovement,
    primaryjoin=and_(
        CadreMovement.employee == Employee.id,
        uselist=False,
        CadreMovement.id == select([func.max(CadreMovement.id)]).where(CadreMovement.employee == Employee.id)
    )
)

  def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.address = address
        self.group = id_group

    def __repr__(self):
        info: str = f'Студент [ФИО: {self.surname} {self.name} {self.patronymic}, ' \
            f'Возраст: {self.age}, Адрес: {self.address}, ID группы: {self.group}]'
        return info
        
         student = session.query(Student).get(20)
        print(student)
        # student.age = 16
        session.query(Student).update({Student.age: Student.age + 1})
        print(student)
        session.query(Student).filter(Student.age <= 18).update({Student.age: Student.age + 1})
.delete()
session.rollback()
session.close()


conn.execute(addresses.insert(), [
   {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
   {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
])


ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)

row = result.fetchone()


s = students.select()
conn = engine.connect()
result = conn.execute(s)
for row in result:
   print (row)

s = students.select().where(students.c.id>2)
result = conn.execute(s)
for row in result:
   print (row)

from sqlalchemy.sql import select
s = select([users])
result = conn.execute(s)

from sqlalchemy import text
t = text("SELECT * FROM students")
result = connection.execute(t)

from sqlalchemy import and_
from sqlalchemy.sql import select
s = select([text("* from students")]) \
.where(
   and_(
      text("students.name between 😡 and :y"),
      text("students.id>2")
   )
)
conn.execute(s, x = 'A', y = 'L').fetchall()


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


u = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com addresses.select().where(addresses.c.email_add.like('%@yahoo.com'))))
result = conn.execute(u)
result.fetchall()Функция union () возвращает объект CompoundSelect из нескольких таблиц. Следующий пример демонстрирует его использование

u = union_all(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
По умолчанию union() удаляет все повторяющиеся записи из результата. Для их сохранения используйте union_all().
u = except_(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))возвращает только те записи из таблицы адресов, которые имеют «gmail.com» в поле email_add, но исключают те, которые имеют «Pune» как часть поля postal_add.

u = intersect(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))Одна возвращает строки, содержащие «gmail.com», как часть столбца email_add, а другая возвращает строки, содержащие «Pune» как часть столбца postal_add. Результатом будут общие строки из обоих наборов результатов.


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




c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
session.add(c1)
session.commit()


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
query.join ( ‘счета’)	то же самое, используя строку


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
Govind Pant Gulmandi Aurangabad gpant@gmail.com
Invoice no : 3, Amount : 10000
Invoice no : 4, Amount : 5000


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
x = session.query(Customer).get(2)
session.delete(x)
session.query(Customer).filter_by(name = 'Gopal Krishna').count()
session.query(Invoice).filter(Invoice.invno.in_([10,14])).count()

Многие ко многим

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

[Внизу настройки для разных бд](https://coderlessons.com/tutorials/bazy-dannykh/sqlalchemy/sqlalchemy-kratkoe-rukovodstvo)
[Отношения в таблице](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)
Есть 3 подхода декл не декл и связывания

### Alembic

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
Моменты на которые надо обратить внимание:
### Генерация юзерагента
Тут поможет user_agent и fake_useragent. Опытные скрейперы могут попробовать установить свой агент на Googlebot User Agent — поисковый робот Google. Большинство веб-сайтов, очевидно, хотят попасть в выдачу Google и пропускают Googlebot.

[О ботах гугла](https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers?hl=en&visit_id=637602093540037819-4103600971&rd=1)

[О ботах яндекс](
https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html)



### Время ожидания запроса
    page_response = requests.get(page_link, timeout=5, headers=headers) - requests
    
    driver.implicity_wait() - selenium
    
    time.sleep - python
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

    perm_ = permutations([2, 4, 6]) 
    
    for i in list(perm_): 
        print(i) 
    
    from itertools import combinations 
    
    comb_ = combinations([2, 4, 6] , 2) 
    
    for i in list(comb_): 
        print(i)




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

    import json 
      x = '{"name":"Viktor", "age":30, "city":"Minsk"}'
    y = json.loads(x)
     print(y["age"])

**в json**
  
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

### Время <a name="time"></a>


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





### hash <a name="hash"></a>
**hashlib**

Модуль предоставляет следующие функции: md5(), sha1(), sha224(), sha256(), sha384 и sha512(). В качестве необязательного параметра функциям можно передать шифруемую последовательность байтов. Например:

    import hashlib
    h = hashlib.sha1(b"password")

Передать последовательность байтов можно также с помощью метода update(). В этом случае объект присоединяется к предыдущему значению:

    h = hashlib.sha1()
    h.update(b"password")

Получить зашифрованную последовательность байтов и строку позволяют два метода — digest() и hexdigest():

    h = hashlib.sha1(b"password")
    h.digest()
    b'[\xaaa\xe4\xc9\xb9??\x06\x82%\x0b1\xf83\x1b~\xe6\x8f\xd9'
    h.hexdigest()
    '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

Наиболее часто применяемой функцией является функция md5(), которая шифрует строку с помощью алгоритма MD5. Она используется для шифрования паролей так как не существует алгоритма для дешифровки. Для сравнения введенного пользователем пароля с сохраненным в базе необходимо зашифровать введенный пароль, а затем произвести сравнение.

    import hashlib
    h = hashlib.md5(b"password")
    p = h.hexdigest()
    '5f4dcc3b5aa765d61d8327deb882cf99'
    h2 = hashlib.md5(b"password")
    if p == h2.hexdigest(): print("Пароль правильный")

**hmac**

Пример подписи URL секретным ключом.

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

**base64**

    import base64
    encoded_data = base64.b64encode("Encode this text")
    print("Encoded text with base 64 is")
    print(encoded_data)

    import base64
    decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")
    print("decoded text is ")
    print(decoded_data)


### jinja <a name="jinja"></a>

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


### прогресс выполнения в Python <a name="progress"></a>
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


### Сервер <a name="server"></a>
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


### Работа с файлами <a name="work_with_files"></a>
#### csv <a name="csv">csv</a>
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

#### xml <a name="xml"></a>
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

    obj_xml = etree.tostring(
        root,
        pretty_print=True,
        xml_declaration=True
    )
    



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
  

