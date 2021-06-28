print('Задача 1. Урок информатики 2')


x = float(input("Введите число: "))
count = 0
a = x
if x > 0:
  while not(1 <= a <= 10):
    if a > 10:
      a /= 10
      count+=1
    else:
      a*=10
      count-=1
else:
  print("Введите положительное число")
print(f"Формат плавающей точки: x = {round(a,abs(count))} * 10 ** {count}")
