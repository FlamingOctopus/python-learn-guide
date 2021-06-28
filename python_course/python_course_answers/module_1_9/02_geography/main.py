country_count = int(input("Кол-во стран: "))
dict_citys = dict()
for country in range(1, country_count + 1):
    countries = input(f"{country} страна:").split()
    new_dict = {countries[city]: countries[0] for city in range(len(countries))}
    dict_citys.update(new_dict)
for city in range(1, 4):
    city_name = input(f"{city} город: ")
    city_return = dict_citys.get(city_name, False)
    if city_return:
        print(f"Город {city_name} расположен в стране {city_return}.")
    else:
        print(f"По городу {city_name} данных нет.")
