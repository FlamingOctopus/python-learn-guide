def is_prime(number):
    div_count = 0
    for div in range(1, number + 1):
        if number % div == 0: div_count += 1
    return div_count == 2


def crypto_alg(iter_item):
    return [item for index, item in enumerate(iter_item) if is_prime(index)]


print(crypto_alg('абвгдеё'))
