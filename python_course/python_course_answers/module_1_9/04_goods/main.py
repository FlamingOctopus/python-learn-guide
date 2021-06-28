goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, value in goods.items():
    total_sum_items, total_sum_money = 0, 0
    for items in store[value]:
        temp_sum_items = items['quantity']
        total_sum_items += temp_sum_items
        total_sum_money += temp_sum_items * items['price']
    print(f"{key} - {total_sum_items} шт, стоимость {total_sum_money} руб")
