from typing import List


def numbers_list() -> List[int]:
    first_list = list()

    for num_0 in range(2, 1000):
        for num_1 in range(3, num_0 // 2, 2):
            if num_0 % num_1 == 0:
                break
        else:
            first_list.append(num_0)
    return first_list


second_list: list[int] = list(filter(lambda x: all(x % y != 0 for y in range(3, x // 2, 2)), (range(2, 1000))))
print(second_list)

print(numbers_list())
