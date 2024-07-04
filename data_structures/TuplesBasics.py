t1 = (1, 2, 3, 4, 5)
print(t1)
print(type(t1))

# len of tuples
print(len(t1))

t2 = ({"key1": "value1"}, [1, 2, 3], 1, True, 0.678)
print(t2)

# indexing
print(t2[0])
print(t2[-1])

# finding index of an element
print(t2.index([1, 2, 3]))
print(t2.index(True))

# count
print(t2)
print(t2.count([1, 2, 3]))

# slicing
print(t2[1:])
print(t2[:1])
print(t2[1::2])
print(t2[::-1])