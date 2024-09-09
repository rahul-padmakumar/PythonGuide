
def makes_twenty(a, b):
    if a == 20 or b == 20 or a + b == 20:
        return True
    else:
        return False


print(makes_twenty(18, 2))
print(makes_twenty(20, 10))
print(makes_twenty(2, 3))