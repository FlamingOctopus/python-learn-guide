from collections import Counter


def is_polindrome(string: str) -> bool:
    return len(list(filter(lambda x: x % 2 == 1, Counter(string).values()))) <= 1


print(is_polindrome('ababc'))
print(is_polindrome('abbbc'))
print(is_polindrome('aaab'))
print(is_polindrome('aaaa'))