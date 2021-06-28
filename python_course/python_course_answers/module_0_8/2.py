print('Задача 2. Долги')

count = 0
dolj = int(input("Введите количество должников "))
sum_d = 0
for i in range(0,dolj+1):
  if count%5 ==0 :
    print(f"Должник с номером {count}")
    x = int(input("Сколько должны?"))
    sum_d +=x
  count+=1

print(f"Общая сумма долга: {sum_d}")