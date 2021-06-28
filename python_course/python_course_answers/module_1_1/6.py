print('Задача 6. Метеостанция')

c = int(input("Нижняя граница: "))
a = int(input("Верхняя граница:"))
b = int(input("Шаг "))

print("C\t", "F")
while c != a or c < a:
    if c > a:
        c = a
        far = abs(c * 1.8) + 32
        print(c, "\t", int(far))
    else:
        far = abs(c * 1.8) + 32
        print(c, "\t", int(far))
        c += b

