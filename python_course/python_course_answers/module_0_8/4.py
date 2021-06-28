print('Задача 4. Отрезок')
a = int(input("Введите число а"))
b = int(input("Введите число b"))
c = int(input("Введите число c"))
summa, count = 0, 0

for i in range(a, b+1):
  if i % c:
    count+=1
    summa+=i

print(f"Среднее арифметическое{summa/count}")
