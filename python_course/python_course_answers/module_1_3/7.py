print('Задача 7. Маятник ')


x = float(input("Введите начальную амплитуду:"))
y = float(input("Введите амплитуду остановки:"))
count = 0
while x > y:
  x=x-(x*0.084)
  count+=1

print(f"Маятник считается остановившимся через {count} колебаний")