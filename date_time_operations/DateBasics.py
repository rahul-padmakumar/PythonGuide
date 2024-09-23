from datetime import date

d1 = date(2023, 3, 24)
print(d1)
d2 = date(2024, 3, 24)
print(d2)

print(d1.year)
print(d1.month)
print(d1.day)
print(d1.max)
print(d1.min)

print(d1.ctime())
print(d1.timetuple())
diff = d2 - d1
print(diff)
print(diff.days)
