print('Задача 6. Монетка')

def func(x, y):
  if x**2 <= 1 and 1 >= y**2:
    print("Монетка где-то рядом")
  else:
    print("Монетки в области нет")

x = float(input("Введите x"))
y = float(input("Введите y"))

func(x,y)

