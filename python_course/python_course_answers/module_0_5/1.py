print('Задача 1. Калькулятор опыта')

exp = int(input("Введите количество опыта:"))

if exp >= 1000 and exp < 2500:
  print("Ваш уровень: 2")
elif exp >= 2500 and exp < 5000:
  print("Ваш уровень: 3")
elif exp >= 5000:
  print("Ваш уровень: 4")
else:
  print("Ваш уровень 1")