site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iphone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_n_replace(site, deep=0):
    for key, value in site.items():
        if isinstance(value, dict):
            print("\t" * deep + f"'{key}':" + "{")
            find_n_replace(value, deep + 1)
            print('\t' * deep, '}')
        else:
            print('\t' * deep + f"'{key}':'{value}'")


def site_gen(site, count, phones_list=None):
    if phones_list is None:
        phones_list = []
    if count == 0:
        return
    phones_list.append(input('Введите название продукта для нового сайта: '))
    for name in phones_list:
        print('Сайт для', name, ':')
        site['html']['head']['title'] = f'Куплю/продам {name} недорого'
        site['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
        find_n_replace(site)
    site_gen(site, count - 1)


sites_qu = int(input('Сколько сайтов: '))
site_gen(site, sites_qu)
