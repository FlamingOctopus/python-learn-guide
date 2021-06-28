print('Задача 6. Сумма факториалов')
sum_fact= 0
prod_fact,fact = 1,1
number = int(input("Введите число "))
for i in range(1,number+1):
  fact = 1
  for j in range(1,i+1):
    fact *= j
  sum_fact += fact

print("Сумма факториалов:",sum_fact)
