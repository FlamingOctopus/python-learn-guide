from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

first_list = list(map(lambda elem: round(elem ** 3, 3), floats))
print(first_list)

second_list = list(filter(lambda elem: len(elem) >= 5, names))
print(second_list)

third_list = reduce((lambda x, y: y * x), numbers)
print(third_list)
