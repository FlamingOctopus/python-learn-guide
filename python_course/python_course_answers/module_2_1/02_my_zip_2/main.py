def shortener(first_item, second_item):
    return min(len(first_item), len(second_item))


def custom_zip(first_item_obj, second_iter_obj):
    zip_gen = ((first_item_obj[item], second_iter_obj[item]) for item in
               range(shortener(first_item_obj, second_iter_obj)))
    return zip_gen


# first = 'abcd'
# second = (10, 20, 30, 40)

first = ('abcd','lol')
second = [10, 20, 30, 40]


result = custom_zip(first, second)
print(result)
# print(list(result))
for item in result:
    print(item)
