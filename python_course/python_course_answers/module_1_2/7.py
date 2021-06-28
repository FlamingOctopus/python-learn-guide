print('Задача 7. Опять?')

def minimum(a,b):
  mini = ((a+b)-abs(a-b))/2
  print(int(mini))


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
minimum(a,b)