import timeit

res_0: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res_0)

res_1: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(res_1)

res_2: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(round(res_2, 7))
