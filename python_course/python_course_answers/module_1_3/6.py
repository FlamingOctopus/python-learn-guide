print('Задача 6. Недоделка 2')



def number(num,valid):
  num_count = 0
  for i in str(num):
    num_count += 1

  if num_count < valid:
    print(f"В  числе меньше {valid} цифр.")
  else:
    last_digit = num % 10
    first_digit = num // 10 ** (num_count - 1)
    between_digits = num % 10 ** (num_count - 1) // 10
    num = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return num


first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))

first_n = number(first_n,3)
second_n = number(second_n,4)

try:
  print(f'Изменённое первое число: {first_n }\nИзменённое второе число:{second_n}\nСумма чисел:', first_n + second_n)
except TypeError:
  print("повторите ввод")
