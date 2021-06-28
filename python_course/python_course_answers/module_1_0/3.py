print('Задача 3. Рамка')



a = int(input("Введите длину "))
b = int(input("Введите ширину "))
for columns in range(1,a+1):
  for rows in range(1, b+1):
    if rows == 1 or rows == b:
      print(" ","-"*b)
    else:
      print("|"," "*b,"|")