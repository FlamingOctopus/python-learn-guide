print('Задача 6. Защита от дурака')

number = int(input("Введите число: "))

if (int(number/100) == 0 and int(number/10) > 0) or (int(number/-100) == 0 and int(number/-10) > 0):
  print("Число подходит")
else:
  print("Введите корректное число")