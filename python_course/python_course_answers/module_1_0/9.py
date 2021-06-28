print('Задача 9. Пирамидка 2')


a = int(input("Высота Пирамидки"))
num = 1
for row in range(a):
  for space in range(a-row,0,-1):
    print(end="   ")
  for resh in range(row+1):
    print(num, end ="    ")
    num+=2

  print()