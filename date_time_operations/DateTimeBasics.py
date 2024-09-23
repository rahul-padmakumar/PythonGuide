from datetime import datetime

dt1 = datetime(2024, 9, 24, 11, 53)
dt2 = datetime(2024, 9, 24, 17)

print(dt2)
print(dt1)
print(dt1.year)
print(dt1.month)
print(dt1.day)
print(dt1.date())
print(dt1.time())
print(dt1.timetuple())
print(dt1.today())
print(dt1.minute)
print(dt1.microsecond)
print(dt1.second)
print(dt1.hour)

dff = dt2 - dt1
print(dff)
print(type(dff))

print(datetime.timestamp(dt1))
