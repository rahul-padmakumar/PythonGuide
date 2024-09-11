def is_even(num): return num % 2 == 0


print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))

print(list(filter(lambda num: num % 2 == 0, [1, 3, 6, 7, 10])))
