import timeit

smt_1 = """
fun_one(1000000)
"""

setup_1 = """
def fun_one(n: int):
    return list(str(x) for x in range(n))
"""

print(timeit.timeit(smt_1, setup_1, number=100))

smt_2 = """
fun_two(1000000)
"""

setup_2 = """
def fun_two(n: int):
    return list(map(str, range(n)))
"""

print(timeit.timeit(smt_2, setup_2, number=100))
