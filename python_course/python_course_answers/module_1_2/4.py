print('Задача 4. Число наоборот')


def func(x):
  number =""
  for i in x:
    if int(i) == 0:
      continue
    else:
      number = i+number
  print("Число наоборот:",number)

x = input("Введите число")
func(x)