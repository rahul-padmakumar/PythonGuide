from collections import defaultdict

def1 = defaultdict(lambda : -1)

print(def1)

def1["a"] = 10

print(def1)

print(def1["a"])

print(def1["b"])  # if key not present returns value returned from lambda
