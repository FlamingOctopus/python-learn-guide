print('Задача 10.')

N = int(input("Введите число "))
num_sum = 0

for i in range (1, N+1):
  num_sum += i
for i in range(N-1):
  num_sum -= int(input("Введите карточки которые не потеряны"))
print(f"Потерянная карточка: {num_sum}")