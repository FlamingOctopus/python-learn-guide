print('Задача 2. Функция в функции')

def positive():
  print("Положительное")
def negative():
  print("Отрицательное")

def test():
  x = int(input("Введите число "))
  if x > 0:
    positive()
  elif x < 0:
    negative()
  else:
    print("Число равно 0")

test()