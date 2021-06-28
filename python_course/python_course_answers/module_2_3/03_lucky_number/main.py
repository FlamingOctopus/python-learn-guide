import random

with open('file.txt', 'w') as file:
    count = 0
    while count <= 777:
        try:
            number = int(input("Введите число: "))
            rand = random.choice(["exc" if i == random.randint(1, 14) else i for i in range(1, 14)])
            if rand == "exc":
                raise Exception
            file.write(f"{number}\n")
            count += number
        except Exception:
            print("Рандомная ошибка, программа завершается")
            break
