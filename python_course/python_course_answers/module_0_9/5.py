print('Задача 5. Марсоход 2')
x = 8
y = 10
while x>0 and x<=15 and y>0 and y<=20:
  button = input(f"Марсоход находится на позиции {x}, {y}, введите команду")
  if button == "w" and x<15:
    x+=1
  elif button == "s" and x>0:
    x-=1
  elif button == "d" and y<20:
    y+=1
  elif button == "a" and y>0:
    y-=1
  else:
    print("Вы не можете двигаться туда")