print('Задача 5. Текстовый редактор')


def count_letters(text, number, letter):
  count_letter,count_number=0,0
  for i in text:
    if i == letter:
      count_letter+=1
    elif i == str(number):
      count_number+=1
    else:
      continue
  print(f"Количество цифр {number}: {count_number}\nКоличество букв {letter}: {count_letter}")

x = input("Введите текст")
y = input("Какую цифру ищем?")
z = input("Какую букву ищём?")

count_letters(x,y,z)