print('Задача 2. Максимум из трёх чисел')

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третее число"))

if a >= b:
  max = a
else:
  max = b
if c >= max:
  max = c
print(max)
