print('Задача 3. Посчитай чужую зарплату...')
count = 1
all_salary = 0
for i in range(12):
  salary = int(input(f"Введите зарплату за {count} месяц"))
  count+=1
  all_salary+=salary
print("Средняя зарплата:",all_salary/count)