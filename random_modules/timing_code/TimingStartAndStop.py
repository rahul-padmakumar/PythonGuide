import time


def fun_one(n: int):
    return list(str(x) for x in range(n))


def fun_two(n: int):
    return list(map(str, range(n)))


def calculate_time(func, times: int):
    start_time = time.time()
    func(times)
    end_time = time.time()
    return end_time - start_time


print(calculate_time(fun_one, 1000000))
print(calculate_time(fun_two, 1000000))
