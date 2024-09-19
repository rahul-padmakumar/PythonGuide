def repeat_decorator(times: int):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
        return wrapper
    return decorator


@repeat_decorator(7)
def print_hello():
    print("Hello")


print_hello()
