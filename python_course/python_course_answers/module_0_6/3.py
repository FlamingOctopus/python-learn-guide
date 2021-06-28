print('Задача 3. Слишком большие числа')

number = int(input("Число:"))
count = 0

while int(number%10) != 0:
  count+=1
  number /= 10
print(count)