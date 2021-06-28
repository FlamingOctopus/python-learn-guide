print('Задача 7. Великий и могучий')
phrase = input("Введите текст: ")
count,max_count = 0,0
for i in phrase:
  if i != " ":
    count+=1
    if count > max_count:
      max_count = count
  else:
    count = 0

print("Самое длинное слово:", max_count)