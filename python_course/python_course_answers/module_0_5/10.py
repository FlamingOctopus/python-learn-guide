x = int(input("Введите час "))

if (x>=8 and x <= 22) and (x<14 or x > 15) and (x<10 or x>=12) and (x<18 or x>=20):
  print("«Можно получить посылку»,")
else:
  print("Нельзя")





x = int(input("Введите час "))

if (x < 8 or x > 22) or (x>=14 and x < 15) or (x>=10 and x<12) or (x>=18 and x<20):
  print("Нельзя получить посылку")
else:
  print("Можно")
