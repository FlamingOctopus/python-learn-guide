1. [Парсинг](#scrap)
# завести новый репо
библиотеки
инструменты
что выбрать
стратегия парсинга
Методы обхода
капча с примерами
примеры парсинга токенов/пр

## Парсинг <a name="scrap"></a>
https://github.com/reanalytics-databoutique/webscraping-open-project
https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg
гезер должен вызывать 1 запрос а не 2
попробовать сохранять инфу в файл, а потом парсить
![img_6.png](img_6.png)
грубый парсинг пандас 
![img_7.png](img_7.png)
splash and puppeter , селен в крайнем случае(но для рендера жс, лучше использовать поддержку реквестов)
инсомния



![img_8.png](img_8.png)

![img_9.png](img_9.png)

requests html


![img_10.png](img_10.png)
grquests
Моменты на которые надо обратить внимание:
### Генерация юзерагента
Тут поможет user_agent и fake_useragent. Опытные скрейперы могут попробовать установить свой агент на Googlebot User Agent — поисковый робот Google. Большинство веб-сайтов, очевидно, хотят попасть в выдачу Google и пропускают Googlebot.
![img_11.png](img_11.png)

![img_12.png](img_12.png)

![img_13.png](img_13.png)
[О ботах гугла](https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers?hl=en&visit_id=637602093540037819-4103600971&rd=1)

[О ботах яндекс](
https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html)

meta:
    - new question system
    - stickers for sale
    - fan project review (projectreview@engineerman.org)

why:
    - create new interfaces
    - create new integrations
    - curiosity
    - security auditing
methods (in order of difficulty):
    web app:
        - super easy
        - watching chrome dev tools often enough
        - everything happening in plain sight
        - common with ip cameras
    mobile app (mitm):
        - sometimes super easy
        - mature software available, mitmproxy
        - on unrooted phones, pi in the middle might be necessary
        - involves hijacking https traffic in transit
        - can be thwarted by cert pinning and/or peer verification
    mobile app (mitm, pinned certs):
        - sometimes super easy
        - use objection to disable cert pinning
        - try previous again
    mobile app (above doesn't work):
        - hard
        - frida inspection & instrumentation
        - hook into various parts of the app to read output
        - much easier with a rooted phone
        - without root, only patched apk is possible
    examine firmware (freely available):
        - varying degree of difficulty
        - obfuscated/encrypted firmware adds new challenges
    examine firmware (get from device itself):
        - usually hard, sometimes impossible
        - must first break device out of case, usually ruining it
        - if successful, must locate uart pads
        - break out the solder gun

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




  

