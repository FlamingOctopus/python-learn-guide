def sort_tuple(new_tuple):
    for element in new_tuple:
        if not isinstance(element, int):
            return tuple()
    return tuple(sorted(new_tuple))


print(sort_tuple((1, 3, 4, 6, 5)))
print(sort_tuple((1, 3, 4.3, 6, 5)))
print(sort_tuple((1, 3, "4", 6, 5)))
