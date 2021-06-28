print('Задача 8. Вклады')
x= int(input("Введите начальную сумму"))
y = int(input("Введите ожидаемую сумму"))
p = int(input("Введите процент"))
years = 0
while y >= x:
  x = int(x+(x * (p/100)))
  years += 1
print(f"Прошло {years} лет")