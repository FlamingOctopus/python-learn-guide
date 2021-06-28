print('Задача 8. Пирамидка')

a = int(input("Высота Пирамидки"))

for row in range(a):
  for space in range(a-row,0,-1):
    print(end=" ")
  for resh in range(row+1):
    print("#", end =" ")
  print()
