print('Задача 9. Плохой циферблат')
probeg = int(input("Введите пробег "))

if probeg//100 > 0 and probeg//100 < 10:
  sum_numbers = (probeg//100) +((probeg%100)//10)+(probeg%10)
  day_id = int(input("Введите номер дня"))
  if sum_numbers > day_id:
    probeg = 0
    print("Сброс пробега", probeg)
  else:
    print("Сегодня не сломался", probeg)
else:
  print("Вы ввели не трехзначное число.")