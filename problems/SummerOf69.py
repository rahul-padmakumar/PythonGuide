def summer_of_69(number_list):
    accumulator = 0
    dont_track = False
    for i in number_list:
        while not dont_track:
            if i != 6:
                accumulator = accumulator + i
                break
            else:
                dont_track = True
        while dont_track:
            if i != 9:
                break
            else:
                dont_track = False
                break
    return accumulator


print(summer_of_69([1, 3, 5]))
print(summer_of_69([4, 5, 6, 7, 8, 9]))
print(summer_of_69([2, 1, 6, 9, 11]))
print(summer_of_69([2, 9]))
print(summer_of_69([2, 6, 6, 9]))


