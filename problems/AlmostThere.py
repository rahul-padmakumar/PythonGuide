
def almost_there(number):
    return abs(number - 100) <= 10 or abs(number - 200) <= 10


print(almost_there(94))
print(almost_there(104))
print(almost_there(209))
print(almost_there(191))
print(almost_there(190))
print(almost_there(150))