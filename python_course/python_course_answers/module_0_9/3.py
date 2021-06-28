print('Задача 3. Кривой мессенджер')
phrase = input("Введите текст: ")
count = 0
for i in phrase:
  count+=1
  if i == "*":
    print(f"Символ ‘*’ стоит на позиции {count}")
    break