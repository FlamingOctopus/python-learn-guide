print('Задача 9. Уравнение')
from math import sqrt
a = int(input("Первое число "))
b =int(input("Второе число "))
c = int(input("Третее число "))


if a!=0:
  d =  b ** 2 - (4 * a * c)
  if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    if x1<x2:
      print("Два корня",x2,x1)
    else:
      print("Два корня",x1,x2)
  elif d == 0:
    x = (-b + sqrt(d))/(2*a)
    print("Один корень",x)
  else:
    pass
else:
  print("Введите КВАДРАТНОЕ уравнение")