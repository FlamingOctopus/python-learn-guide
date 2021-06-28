print('Задача 7. Наибольшая сумма цифр')

num_count = int(input("Введите количество чисел "))
max_sum = 0
pr_sum = 0
for nums in range(1,num_count+1):
  num = input("Введите число")
  summa = 0
  pr_sum = 0
  for i in num:
    summa+=int(i)
    pr_sum+=summa
  if pr_sum > max_sum:
    max_sum=summa
    max_num = int(num)
print(max_sum,max_num)