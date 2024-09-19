
def hello():
    print("Inside Hello")

    def inner_greet():
        print("Inside inner greet")

    return inner_greet


hello()()