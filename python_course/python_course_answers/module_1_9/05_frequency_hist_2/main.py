phrase = "Здесь что-то написано"

sym_dict = {}
for sym in phrase:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1
print("Оригинальный словарь частот:")
for item in sym_dict.items():
    print(item[0], ":", item[1])

new_dict = {}
for values in sym_dict.items():
    if values[1] in new_dict:
        new_dict[values[1]] += [values[0]]
    else:
        new_dict[values[1]] = [values[0]]
print("Инвертированный словарь частот:")
for item in new_dict.items():
    print(item[0], ":", item[1])
