print('Задача 7. Обычный день на работе')

x, count_x, hours, count_y = 0, 0, 0, 0

print("Начался 8-часовой рабочий день")
while hours < 8:
    hours += 1
    print(f"{hours} час")
    x = int(input("Сколько задач решит Максим?"))
    count_x += x
    y = int(input("Звонит жена. Взять трубку?"))
    count_y += y

print(f"Рабочий день закончился. Всего выполнено задач: {count_x}")
if count_y > 0: print("Нужно зайти в магазин")
