from datetime import time

t1 = time(1, 19, 28, 1234)
print(t1)

t2 = time(2)
print(t2)

print(t1.min)
print(t1.max)

print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)
t3 = t1.replace(3)
print(t3)
print(t1)
