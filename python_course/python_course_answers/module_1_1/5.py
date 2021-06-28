print('Задача 5. Вот это объёмы!')
import math

x = float(input("Введите радиус случайной планеты: "))
v_earth = 10.8321 * 10 ** 11
v_planet = 4/3 *math.pi*x ** 3
if v_earth > v_planet:
  print(f"Объём планеты Земля больше в {round(v_earth/v_planet,3)}")
elif v_earth < v_planet:
  print(f"Объём планеты Земля меньше в {round(v_planet/v_earth,3)} раз")
else:
  print("Планеты равны по объему!")