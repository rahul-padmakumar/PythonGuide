
# Placing keyword arguments ahead of positional arguments raises an exception:


def print_key_values(**kwargs):
    for key in kwargs:
        print("{} -> {}".format(key, kwargs[key]))


print_key_values(a=1, b=2)