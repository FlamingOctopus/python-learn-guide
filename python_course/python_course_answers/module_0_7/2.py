print('Задача 2. Должники')

count = 0
for i in range(10):
  x = int(input("Введите число "))
  if x%2 == 0 and x > 0: count+=1
print(f"Подходящих чисел {count}")