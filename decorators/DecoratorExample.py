def decorated_func(function_to_be_decorated):
    def wrap_func():
        print("Starting !!!")
        function_to_be_decorated()
        print("Ending !!!")
    return wrap_func


def function_to_be_decorated():
    print("Hello all???")


function_to_be_decorated()