nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list = [number_deep for deep_list in nice_list for deep_deep_list in deep_list for number_deep in deep_deep_list]
print("Ответ: ", new_list)