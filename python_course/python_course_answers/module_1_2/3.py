print('Задача 3. Апгрейд калькулятора')

def summa(y):
  summa = 0
  for i in y:
    summa+=int(i)
    print("Сумма цифр", summa)

def maxi(y):
  max_current = 0
  for i in y:
    current = int(i)
    if current > max_current:
      max_current = current
  print("Наибольшая цифра", max_current)

def mini(y):
  min_current = 9
  for i in y:
    current = int(i)
    if current < min_current:
      min_current = current
  print("Наименьшая цифра", min_current)

while True:
  x = input("Введите операцию ")
  y = input("Введите число")
  if x =="сумма":
    summa(y)
  elif x == "макс":
    maxi(y)
  elif x == "мин":
    mini(x)
  else:
    print("Операция введена некорректно")