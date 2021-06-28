first_class_list = [student for student in range(160, 176 + 1, 2)]
second_class_list = [student for student in range(162, 180 + 1, 3)]
first_class_list.extend(second_class_list)
print(sorted(first_class_list))
