def fib(num_pos):
    if num_pos == 1:
        return 0
    if num_pos == 2:
        return 1
    return fib(num_pos - 1) + fib(num_pos - 2)


num = int(input("Введите позицию числа в ряде Фибоначчи: ")) + 1
print("Число: ", fib(num))
