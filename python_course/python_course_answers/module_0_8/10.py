

print('Задача 10. Кинотеатр')

x = int(input("Введите количество мальчиков"))
y = int(input("Введите количество девочек"))
if x > 2*y or y > 2*x:
  print("нет решения")
elif x >= y:
  print("BGB"*(x-y), end="")
  print("BG"*(y-(x-y)),end="")
else:
  print("GBG"*(y-x), end="")
  print("GB"*(x-(y-x)),end="")




"""
print('Задача 10. Кинотеатр')

x = int(input("Введите количество мальчиков"))
y = int(input("Введите количество девочек"))
str_BG = []
if x > 2*y or y > 2*x:
  print("нет решения")
elif x >= y:
  for i in range(1,x-y):
    str_BG.append('BGB')
  for i in range(1,(y-(x-y))):
    str_BG.append('BG')
else:
  for i in range(1,y-x):
    str_BG.append('GBG')
  for i in range(1,(x-(y-x))):
    str_BG.append('GB')

for i in str_BG:
  print(i, end ='')
"""