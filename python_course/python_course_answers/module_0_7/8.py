print('Задача 8. Замечательные числа')


for i in range(1,100,1):
  number = ((i//10)*(i%10))*3
  if number == i: print(f"Это число подходит:{i}")