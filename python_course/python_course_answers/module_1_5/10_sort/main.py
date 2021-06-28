def sort_numbers(list_numbers):
    for i in range(len(list_numbers) - 1):
        for current_number in range(len(list_numbers) - i - 1):
            if list_numbers[current_number] > list_numbers[current_number + 1]:
                temp = list_numbers[current_number]
                list_numbers[current_number] = list_numbers[current_number + 1]
                list_numbers[current_number + 1] = temp
    print("Отсортированный список: ", list_numbers)


list = [1, 4, -3, 0, 10]
sort_numbers(list)
