print('Задача 4. Первая цифра')
x = float(input("Введите число"))
x = x%int(x)
x = x//0.1
print(int(x))