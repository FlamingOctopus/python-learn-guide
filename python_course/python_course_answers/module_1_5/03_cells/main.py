def cells_list(list_length):
    list_for_cells = []
    for current_cell in range(1, list_length + 1):
        cell = int(input(f"Эффективность {current_cell} клетки: "))
        list_for_cells.append(cell)
    return list_for_cells


def update_cells_list_creator(list_cells):
    print("Неподходящие значения: ", end=" ")
    count = 0
    for current_cell in list_cells:
        if count > current_cell:
            print(current_cell, end=" ")
        count += 1


cells_count = int(input("Кол-во клеток: "))
update_cells_list_creator(cells_list(cells_count))
