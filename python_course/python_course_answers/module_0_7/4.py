print('Задача 4. С заботой о природе')

count = 0
for i in range(30, 36):
    x = int(input(f"Людей в {i} секторе "))
    if x > 10:
        print("Нарушение! Слишком много людей в секторе!")
        count += 1
    else:
        print("Всё спокойно")

print(f"Количество нарушений: {count}")