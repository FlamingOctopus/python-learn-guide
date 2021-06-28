print('Задача 8. Яйца')
max_d = 4
min_d = 0

max_danger = float(input("Максимальный уровень опасности"))


if max_danger < 0:
  print("Повторите ввод")
else:
  x = min_d + (max_d - min_d)/2
  D = x**3 - 3 * x**2 - 12 * x + 10
  while abs(D) > max_danger:
    if D > 0:
      min_d = x
    else:
      max_d = x
    x = min_d + (max_d - min_d)/2
    D = x**3 - 3 * x**2 - 12 * x + 10

print("Приблизительная глубина безопасной кладки:", x,"м")