a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_five = 0
new_list = []
for number in a:
    if number == 5:
        count_five += 1
        continue
    new_list.append(number)

new_list.extend(c)
count_three = 0
for number in new_list:
    if number == 3:
        count_three += 1

print("Кол-во цифр 5 при первом объединении:", count_five, \
      "\nКол-во цифр 3 при первом объединении:", count_three, \
      "\nИтоговый список: ", new_list)
