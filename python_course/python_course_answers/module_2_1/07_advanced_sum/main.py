def adv_sum(temp_list):
    if not temp_list:
        return temp_list
    if isinstance(temp_list[0], list):
        return adv_sum(temp_list[0]) + adv_sum(temp_list[1:])
    return temp_list[:1] + adv_sum(temp_list[1:])


def sum(*args):
    for number in args:
        if isinstance(number, list):
            args = adv_sum(args[0])
    summa = 0
    for num in args:
        summa += num
    return summa


print(sum(1, 2, 3, 4, 5))
print(sum([[1, 2, [3]], [1], 3]))
