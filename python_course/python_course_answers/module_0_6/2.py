print('Задача 2. Коллекторы')

name = input("Имя должника:")
sum_dolg = int(input("Сумма долга:"))
x = 0
while sum_dolg != x:
  print(f"{name}, ваша задолженность составляет {sum_dolg} рублей.")
  x = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?"))
  if x < sum_dolg:
    print(f"Маловато, {name}. Давайте ещё раз.")
  else:
    break
print(f"Отлично, {name}! Вы погасили долг. Спасибо!")