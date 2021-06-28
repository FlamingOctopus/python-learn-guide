print('Задача 6. Успеваемость в классе')

N = int(input("Введите количество учеников "))
count_three, count_four, count_fifth = 0,0,0
for i in range(1, N):
  x = int(input(f"Введите оценку ученика{i}"))
  if x == 3:
    count_three+=1
  elif x == 4:
    count_four+=1
  else:
    count_fifth+=1
print(f"В классе {count_three} троечников, {count_four} хорошистов, {count_fifth} отличников")