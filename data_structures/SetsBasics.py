set1 = set()
print(set1)
print(type(set1))

set1.add(1)
print(set1)

set1.add(2)
print(set1)

set1.add(1)
print(set1)

list1 = [1, 2, 2, 4, 4, 5, 5, 5, 3, 3]
print(set(list1))

# clear set
set1.clear()
print(set1)

# copy
s = {1, 2, 3}
sc = s.copy()
print(s)
print(sc)
s.add(4)
print(s)
print(sc)

# difference
print(s.difference(sc))
print(sc.difference(s))

# difference update
s1 = {1, 2, 3}
s2 = {1, 4, 5}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

# discard => remove

s3 = {1, 2, 3, 4, 5}
s3.discard(3)
s3.discard(6)
print(s3)

# intersection

s4 = {1, 2, 3}
s5 = {2, 3, 6}
print(s4.intersection(s5))
print(s4)
s4.intersection_update(s5)
print(s4)

# is disjoint
s6 = {1, 2, 3}
s7 = {4, 5, 6}
s8 = {1, 2, 7}
print(s6.isdisjoint(s7))
print(s8.isdisjoint(s6))

# is subset
s9 = {1, 2, 3}
s10 = {1, 2}
print(s10.issubset(s9))

# is superset
print(s9.issuperset(s10))

# symmetric update
s11 = {1, 2, 3}
s12 = {3, 4, 5}
print(s11.symmetric_difference(s12))
print(s11)
print(s12)
s11.symmetric_difference_update(s12)
print(s11)
print(s12)

# union
s13 = {1}
s14 = {2}
print(s13.union(s14))

# update
s13.update(s14)
print(s13)
