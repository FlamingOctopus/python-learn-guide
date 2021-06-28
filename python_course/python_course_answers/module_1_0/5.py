print('Задача 5. Простые числа')

numbers = int(input("Введите количество чисел "))
simple_numbers = 0
for i in range(numbers):
  count = 0
  number = int(input("Введите число"))
  for j in range(1,number+1):
    print(number//j)
    if number%j != 0:
      continue
    else:
      count+=1
  if count == 2 :
    simple_numbers+=1

print("Количество простых чисел ",simple_numbers)
