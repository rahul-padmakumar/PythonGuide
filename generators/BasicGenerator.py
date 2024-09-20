
def gen_squares(n: int):
    for num in range(n):
        yield num ** 2


for x in gen_squares(25):
    print(x)