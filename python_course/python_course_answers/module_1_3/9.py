print('Задача 9. Сумма ряда')

def stepen(x,i):
  y=1
  for j in range(1,i+1):
    y*=x
  return y

def fact(i):
  if i == 0:
    return 1
  return fact(i-1) * i

precision = float(input("Введите точность: "))
x = int(input("Введите x: "))
count = 2
num = 1
current = 1
while abs(current) > precision:
  first = stepen(x,count)
  second = fact(count)
  current =  first / second
  count += 2
  if (count/2)%2 != 0:
    num+=current
  else:
    num-=current
print("Сумма ряда = ", num )