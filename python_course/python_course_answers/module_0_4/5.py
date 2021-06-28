print('Задача 5. Модуль числа')

number = int(input("Введите число"))
if number < 0:
  number_abs = -number
  print(f"Ввели {number}, ответ {number_abs}")
else:
  print(f"Ввели {number}, ответ {number}")