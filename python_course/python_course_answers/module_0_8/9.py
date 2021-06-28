print('Задача 9. Выражение')

x = int(input("Введите число "))

mult_first, mult_second = 1,1

for i in range(7):
  mult_x1 = x-2**i-1
  mult_first *= mult_x1
  mult_x2 = x-2**i
  mult_second *= mult_x2

print("Результат",mult_first/mult_second)
