list = [0, 1, 2, 0, 2, 3, 4]

new_list = [number for number in list if number != 0]
zeros_counter = len(list) - len(new_list)
new_list += [0] * zeros_counter
print(new_list)
new_list = [number for number in new_list if number != 0]
print(new_list)