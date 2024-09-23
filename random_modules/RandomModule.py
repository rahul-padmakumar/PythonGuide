import random

random.seed(45)
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))
print(random.randint(0, 15))


list1 = list(range(1, 15))
print(list1)
print(random.choice(list1))
print(random.choices(population=list1, k = 10))
print(random.sample(population=list1, k = 10))
random.shuffle(list1)
print(list1)

print(random.uniform(0, 100))
print(random.gauss(mu=1.0, sigma=10.0))


