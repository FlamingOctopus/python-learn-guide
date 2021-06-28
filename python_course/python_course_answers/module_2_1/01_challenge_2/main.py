def numbers(counter, number):
    print(counter)
    if counter == number:
        return number
    return numbers(counter + 1, number)


number = int(input("Введите число"))

numbers(1, number)
