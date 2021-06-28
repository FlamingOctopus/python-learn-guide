def running(K):
    numbers_list = [1, 2, 3, 4, 5]
    for current_number in range(1, K + 1):
        numbers_list.insert(0, (numbers_list.pop()))
    print(numbers_list)


K = int(input("Сдвиг: "))
running(K)
