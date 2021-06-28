print('Задача 9. Коровы')
phrase = input("Введите строку: ")
if len(phrase) == 10:
  milk, sum_milk = 0, 0
  for i in phrase:
    milk+=2
    if i == "a":
      continue
    else:
      sum_milk+=milk
  print(sum_milk)
else:
  print("Повторите ввод строки")