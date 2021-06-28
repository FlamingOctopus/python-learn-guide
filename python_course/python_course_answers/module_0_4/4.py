print('Задача 4. Калькулятор скидки')
first_buy = int(input("Введите стоимость 1 товара:"))
second_buy = int(input("Введите стоимость 2 товара:"))
third_buy = int(input("Введите стоимость 3 товара:"))
total = first_buy+second_buy+third_buy
if (total) > 10000:
  total -= total*0.1
  print("Цена со скидкой", total)
else:
  print("Цена: ", total)