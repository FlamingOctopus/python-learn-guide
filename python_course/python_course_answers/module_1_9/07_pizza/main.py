def orders_dict(count_orders):
    """Создает словарь"""
    orders = dict()
    for order in range(1, count_orders + 1):
        order_info = input(f"{order} заказ: ").split()
        if not order_info[0] in orders:
            orders[order_info[0]] = {order_info[1]: int(order_info[2])}
        else:
            if order_info[1] in orders[order_info[0]]:
                orders[order_info[0]][order_info[1]] += int(order_info[2])
            else:
                orders[order_info[0]].update({order_info[1]: order_info[2]})


def sort_orders(orders):
    """Сортирует и печатает"""
    for keys in orders.keys():
        print(keys, ":")
        for item in orders.values():
            sorted_dict = {}
            sorted_keys = sorted(item)
            for values in sorted_keys:
                sorted_dict[values] = item[values]
            for values in sorted_dict.items():
                print("\t", values[0], ": ", values[1])
            break


count_orders = int(input("Введите кол-во заказов:"))
orders_dict(count_orders)
