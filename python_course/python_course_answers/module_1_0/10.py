print('Задача 10. Яма ')

a = int(input("Введите число "))
for i in range(a):
  for left in range (a, a-i-1,-1):
    print(left, end="")
  print("." * (2*(a-i-1)),end="")
  for right in range (a-i,a+1):
    print(right, end="")
  print()