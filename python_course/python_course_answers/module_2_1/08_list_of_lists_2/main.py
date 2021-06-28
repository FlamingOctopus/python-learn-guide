nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def adv_sum(temp_list):
    if not temp_list:
        return temp_list
    if isinstance(temp_list[0], list):
        return adv_sum(temp_list[0]) + adv_sum(temp_list[1:])
    return temp_list[:1] + adv_sum(temp_list[1:])


print(adv_sum(nice_list))
