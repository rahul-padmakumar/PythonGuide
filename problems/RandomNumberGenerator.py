import random


def rand_num(low, high, limit):
    for i in range(limit):
        yield random.randint(low, high)


for num in rand_num(10, 100, 10):
    print(num)

