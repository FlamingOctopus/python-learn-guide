print('Задача 6. Спецшифр')
phrase = input("Введите строку: ")
count,max_count = 0,0
for i in phrase:
  if i == "s":
    count+=1
    if count > max_count:
      max_count = count
  else:
    count = 0

print("Самая длинная последовательность:", max_count)