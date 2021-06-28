print('Задача 8. Колонтитул')
a = int(input("Длина колонтикула"))
b = int(input("Количество !"))
count = 0
for i in range(a):
    if (a - b) // 2 <= i and count < b:
        count += 1
        print("!", end="")
    else:
        print("~", end="")
