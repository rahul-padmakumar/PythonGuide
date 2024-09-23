from collections import namedtuple

Dog = namedtuple("Dog", ["age", "name"])

d1 = Dog(age=5, name="Test1")
print(d1)
print(d1.age)
print(d1.name)