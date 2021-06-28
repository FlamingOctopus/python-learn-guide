print('Задача 1. Сумма чисел')

def summa_n(N):
  summa = 0
  for i in range(1,N+1):
    summa+=i
  print(f"Я знаю, что сумма чисел от 1 до {N} равна {summa}")

N = int(input("Введите число "))
summa_n(N)