
def pretty_print_decorator(func):
    def wrapper(self):
        print("*****************************************")
        func(self)
        print("******************************************")
    return wrapper


class Greet:

    def __init__(self, name):
        self.name = name

    @pretty_print_decorator
    def greet(self):
        print("Hello {}".format(self.name))


ex1 = Greet("Test")
ex1.greet()


