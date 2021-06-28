print('Задача 8. Сумма ряда')

n = int(input("Введите число"))
b = 1
s = 0
for i in range(n + 1):
  s += b
  b *= -1/2
print(s)