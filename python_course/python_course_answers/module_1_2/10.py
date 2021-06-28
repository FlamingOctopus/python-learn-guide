print('Задача 10')

def spalnia():
  while True:
    x = input("Вы в спальне. Куда идем?\n1 - в ванну\n2 - в коридор")
    if x == "1":
      vanna()
    elif x == "2":
      coridor()
    else:
      print("Ошибка повторите ввод")
def kitchen():
  while True:
    x = input("Вы на кухне. Куда идем?\n1 - в окно\n2 - в коридор")
    if x == "1":
      print("Вы выпали из окна!")
      exit(0)
    elif x == "2":
      coridor()
    else:
      print("Ошибка повторите ввод")
def vanna():
  while True:
    x = input("Вы в ванной комнате. Куда идем?\n1 - в спальню\n2 - в коридор")
    if x == "1":
      spalnia()
    elif x == "2":
      coridor()
    else:
      print("Ошибка повторите ввод")
def coridor():
  while True:
    x = input("Вы в коридоре. Куда идем?\n1 - в спальню\n2 - в ванну\n3 - на кухню\n4 - в дверь")
    if x == "1":
      spalnia()
    elif x == "2":
      vanna()
    elif x == "3":
      kitchen()
    elif x == "4":
      print("Ура вы выбрались из квартиры!")
      exit(0)
    else:
      print("Ошибка повторите ввод")

spalnia()

