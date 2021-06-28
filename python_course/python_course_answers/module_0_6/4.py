print('Задача 4. Календари')
count = 0
x = int
while x != 0:
  x = int(input("Введите число: "))
  if x%2 != 0: count += 1
print("Количество четных чисел:", count)