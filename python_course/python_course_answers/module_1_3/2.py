print('Задача 2. Функция максимума')


def maxi(a,b):
  maximum = ((a+b)+abs(a-b))/2
  return maximum

a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
c = float(input("Введите третее число "))
maximum = maxi(a,b)
maximum = maxi(maximum,c)
print(maximum)