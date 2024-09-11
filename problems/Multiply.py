from functools import reduce


def multiply(input_list): return reduce(lambda a, b: a * b, input_list)


print(multiply([1, 2, 3, -4]))
