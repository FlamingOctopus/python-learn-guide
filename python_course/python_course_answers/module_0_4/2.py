print('Задача 2. Поступление')
rus_count = int(input("Введите кол-во баллов по русскому языку:"))
math_count = int(input("Введите кол-во баллов по математике:"))
info_count = int(input("Введите кол-во баллов по информатике:"))
min = 270
if (rus_count+math_count+info_count) >= min:
  print("Поздравляю, ты поступил на бюджет!")
else:
  print("К сожалению, ты не прошёл на бюджет.")