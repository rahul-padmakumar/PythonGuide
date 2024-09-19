
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator2
@decorator1
def print_hello():
    print("Hello")


print_hello()