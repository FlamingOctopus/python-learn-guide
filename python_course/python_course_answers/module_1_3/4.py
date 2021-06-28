print('Задача 4. Урок информатики 3')

def func(x):
  flag=True
  m = ""
  p = ""
  for a in x:
    if a == 'e':
      flag = False
    elif flag:
      m = m + a
    else:
      p = p + a
  print(f"Мантисса:{m}  Порядок:{p}")

x = input("Введите число в экспоненциальной форме ")
func(x)
