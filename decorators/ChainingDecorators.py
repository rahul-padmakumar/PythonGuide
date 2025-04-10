
def decorator1(func):
    """
    A decorator that wraps a function and prints "Decorator 1" 
    before calling the original function.

    Args:
        func (callable): The function to be wrapped by the decorator.

    Returns:
        callable: The wrapped function with additional behavior.
    """
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