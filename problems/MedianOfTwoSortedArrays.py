def median_0f_sorted_arrays(num1: list[int], num2: list[int]):
    temp_list: List[int] = num1
    temp_list.extend(num2)
    temp_list.sort()
    length_of_temp_list = len(temp_list)
    middle_index = int(length_of_temp_list / 2)
    if length_of_temp_list % 2 == 0:
        print((temp_list[middle_index] + temp_list[middle_index - 1]) / 2)
    else:
        print(temp_list[middle_index])


median_Of_sorted_arrays([1, 3], [2])
median_Of_sorted_arrays([1, 2], [3, 4])
