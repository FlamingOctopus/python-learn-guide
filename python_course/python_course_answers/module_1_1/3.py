print('Задача 3. Убийца Steam')
a = int(input("Укажите размер файла для скачивания:"))
b = int(input("Какова скорость вашего соединения?"))
if a <= 0 or b <= 0:
  print("Введите корректные данные")
else:
  dowl = 0
  timer = 1
  while dowl != a:
    dowl+=b
    if dowl >= a:
      dowl = a
    print(f"Прошло {timer} сек. Скачано {dowl} из {a} Мб ({round(dowl/(a/100))}%)")
    timer+=1
