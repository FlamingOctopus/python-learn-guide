print('Задача 10. Максимальное число (по желанию)')

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
