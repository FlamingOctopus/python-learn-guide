print('Задача 8. Новоселье')

S = int(input("Введите площадь "))
cost = int(input("Введите цену в млн руб. "))

if (S >= 100 and  cost <=10) or (S >= 80 and  cost <=7):
  print("Квартира подходит!")
else:
  print("Квартира не подходит")