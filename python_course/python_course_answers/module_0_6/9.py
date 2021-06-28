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