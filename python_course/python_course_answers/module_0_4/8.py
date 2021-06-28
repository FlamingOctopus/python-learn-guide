print('Задача 8. Тяжёлая жизнь')

hours = int(input("Введите количество часов: "))
credit = int(input("Введите остаток по кредиту: "))
food = int(input("Введите расходы на еду: "))

salary = (200 * hours / 2 ** 3 + hours) - credit- food

if salary >= 0:
  print("Часов работы хватает.")
else:
  print("Часов не хватает. Придётся поработать!")