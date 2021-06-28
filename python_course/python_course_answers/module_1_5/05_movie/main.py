def add_film(films):
    film = str
    favorite_list = []
    while film != "Стоп":
        film = input("Введите название фильма")
        for current_film in films:
            if current_film == film:
                favorite_list.append(current_film)
            else:
                print("Ошибка, такого фильма нет")
    return favorite_list



films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

print("Теперь список ваших любимых фильмов состоит из: ", add_film(films))
