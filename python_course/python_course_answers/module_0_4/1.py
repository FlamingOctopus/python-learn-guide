print('Задача 1. Датчик погоды')
try:
  rain = int(input("На улице идет дождь? "))
  if rain == 1:
    print("Пошёл дождь. Возьмите зонтик!")
  elif rain == 0:
    print("Дождя нет =)")
  else:
    print("Вы ввели что-то не то")
except ValueError:
  print("Вы ввели не число")