
def spy_game(number_list):
    list_len = len(number_list)
    for index, item in enumerate(number_list):
        if (item == 0 and (index + 1) < list_len and (index + 2) < list_len
                and number_list[index + 1] == 0
                and number_list[index + 2] == 7):
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

