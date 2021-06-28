print('Задача 8. НОД')

def evklid(a,b):
  while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
  print("НОД = ",a + b)


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
evklid(a,b)