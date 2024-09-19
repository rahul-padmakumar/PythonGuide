
def decorator_for_sum(func):
    def wrapper_func(*args, **kwrgs):
        print("Starting of {}".format(func.__name__))
        print("Result = {}".format(func(*args, **kwrgs)))
    return wrapper_func


@decorator_for_sum
def sum_s1(num1, num2): return num1 + num2


sum_s1(9, 2)

