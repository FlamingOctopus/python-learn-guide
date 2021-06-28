site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find(site, key, deep):
    if key in site:
        return site[key]
    if deep > 1:
        for item in site.values():
            if isinstance(item, dict):
                result = find(item, key, deep - 1)
                if result:
                    break
        else:
            result = "Не найдено"
        return result


key = input("Введите ключ который нужно найти: ")
deep = int(input("Введите глубину поиска: "))
print(find(site, key, deep))
