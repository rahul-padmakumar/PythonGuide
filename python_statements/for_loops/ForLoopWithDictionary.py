
dict1 = {"a": 1, "b": 2, "c": 3}

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for (k, v) in dict1.items():
    print("Key is {}, value is {}".format(k, v))
