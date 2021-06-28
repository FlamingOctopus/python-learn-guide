print('Задача 7. Отрезок')

a = int(input("Введите число а"))
b = int(input("Введите число б"))
summa, count = 0, 0
for i in range(a,b+1,1):
  if i % 3 == 0:
    summa+=i
    count+=1

print(f"Среднее арифметическое {summa/count}")