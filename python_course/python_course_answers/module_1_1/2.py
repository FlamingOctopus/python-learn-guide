print('Задача 2. Грубая математика')
import math

while True:
    x = float(input("Введите число: "))
    if x > 0:
        z = math.ceil(x)
        y = math.log(z)
        print(f"x = {z}   log(x) = {y}")
    else:
        z = math.floor(x)
        y = math.exp(z)
        print(f"x = {z}   exp(x) = {y}")

