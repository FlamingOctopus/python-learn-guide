def reverse_list(list_nums):
    reverse_list_num = [list_nums[number] for number in range(len(list_nums) - 1, -1, -1)]
    if reverse_list_num == list_nums:
        return True
    else:
        return False


def main_func(list_nums):
    new_numbers = []
    add_numbers = []
    for number in range(0, len(list_nums)):
        for i in range(number, len(list_nums)):
            new_numbers.append(list_nums[i])
        if reverse_list(new_numbers):
            for number_add in range(0, number):
                add_numbers.append(list_nums[number_add])
            add_numbers.reverse()
            break
        new_numbers = []
    return add_numbers


N = int(input("Кол-во чисел: "))
list_nums = [int(input("Число:")) for number in range(1,N+1)]
add_numbers = main_func(list_nums)

print(f"Последовательность: {list_nums}\nНужно приписать чисел: {len(add_numbers)}\nСами числа: {add_numbers}")
