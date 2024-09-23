
from collections import Counter

list_1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
c1 = Counter(list_1)
print(c1)
print(c1[1])
print(c1.keys())

print(list(c1))  # to get unique values from a list using counter

str_1 = "aaaaaaabbbccccccccccccdddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeee"
c2 = Counter(str_1)
print(c2)

print(sum(c2.values()))
print(len(str_1))

print(list(c2))

print(set(c2))

print(dict(c2))

print(c2.items())

print(c2.most_common())
print(c2.most_common()[::-1])

c2.clear()
print(c2)

dict_1 = {"a": 5, "b": 2, "c": 3}
print(Counter(dict_1))


