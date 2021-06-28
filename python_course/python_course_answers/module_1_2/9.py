print('Задача 9. Недоделка')

import random

def rock_paper_scissors():
  game = input("Введите камень, ножницы или бумага")
  rand = random.randint(1,3)
  if rand == 1:
    game_comp = "камень"
  elif rand == 2:
    game_comp = "ножницы"
  elif rand == 3:
    game_comp = "бумага"
  else:
    print("error")
  if (game == "камень" and game_comp == "ножницы") or (game == "ножницы" and game_comp == "бумага") or (game == "бумага" and game_comp == "камень"):
    print("Победа")
  else:
    print("Вы проиграли")

def guess_the_number():
  print('Задача 9. Игра «Угадай число»')
  number = 7
  x, count = 0, 0
  while number != x:
    x = int(input("Введите число"))
    count += 1
    if x > number:
      print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif x < number:
      print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
      break
  print("Вы угадали! Число попыток:", count)

def mainMenu():
  while True:
    select = input("Выберите игру в которую хотите поиграть \nКамень, ножницы, бумага - 1 ;Угадай число - 2")
    if select == "1":
      rock_paper_scissors()
    elif select =="2":
      guess_the_number()
    else:
      print("Повторите ввод корректно")

mainMenu()