shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

find_thing = input("Название детали: ")
cost_sum, count_things = 0, 0
for thing in shop:
    if find_thing == thing[0]:
        cost_sum += thing[1]
        count_things += 1
print(f"Кол-во деталей - {count_things}\nОбщая стоимость - {cost_sum}")
