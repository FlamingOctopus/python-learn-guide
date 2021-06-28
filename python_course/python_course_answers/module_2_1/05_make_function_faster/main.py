# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result

def calculating_math_func(data, facts={}):
    if data in facts:
        result = facts[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        result /= data ** 3
        result **= 10
        facts[data] = result
    print(facts)
    return result


print(calculating_math_func(4))
print(calculating_math_func(5))
print(calculating_math_func(5))
