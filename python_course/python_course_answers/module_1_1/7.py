print('Задача 7. Ход конём')
x1 = float(input("Введите местоположение коня: "))
y1 = float(input())
x2 = float(input("Введите местоположение точки на доске:"))
y2 = float(input())

x1 = int(x1*10)
y1 = int(y1*10)
x2 = int(x2*10)
y2 = int(y2*10)

print(f"Конь в клетке ({x1}, {y1}). Точка в клетке ({x2}, {y2}).")
if x2 >= 0 and y2 >= 0:
  raz1 = abs(x1 - x2)
  raz2 = abs(y1 - y2)
  if (raz1 == 2 and raz2 == 2) or (raz1  == 1 and raz2 == 2):
    print ("Да, конь может ходить в эту точку.")
  else:
    print ("Нет, конь не может ходить в эту точку.")
else:
  print ("error")