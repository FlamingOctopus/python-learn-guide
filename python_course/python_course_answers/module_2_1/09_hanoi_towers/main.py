def move(height, first_tower, second_tower):
    if height > 0:
        temp_tower = 2
        move(height - 1, first_tower, temp_tower)
        print(f"Переложить диск {height} со стержня номер {first_tower} на стержень номер {second_tower}")
        move(height - 1, temp_tower, second_tower)


height = int(input("Введите количество дисков: "))

move(height, 1, 3)
