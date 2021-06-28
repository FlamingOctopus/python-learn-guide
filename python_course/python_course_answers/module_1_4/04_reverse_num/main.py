def solution(x):
    sol = float(int_part(x)) + float(float_part(x))
    return sol


def int_part(x):
    x = int(x)
    first_num = ""
    for i in str(x):
        first_num = i + first_num
    return first_num


def float_part(x):
    number = round(x - int(x), 2)
    second_num = ""
    for i in str(number):
        if i == "0" or i == ".":
            continue
        else:
            second_num = i + second_num
    second_num = "0." + second_num
    return second_num


N, K = float(input("Введите первое число: ")), float(input("Введите второе число: "))

N = solution(N)
K = solution(K)
print(f"Первое число наоборот: {N}\nВторое число наоборот: {K}\nСумма: {N + K}")
