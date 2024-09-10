
def has33(number_list):
    for i, j in enumerate(number_list):
        if j == 3 and (i != len(number_list) - 1 and number_list[i + 1] == 3):
            return True
    else:
        return False


print(has33([1, 3, 3]))
print(has33([1, 3, 1, 3]))
print(has33([3, 1, 3]))
print(has33([3]))

