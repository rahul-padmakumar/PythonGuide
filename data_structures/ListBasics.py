# list is a mutable-ordered sequence of elements

list1 = [2, 3, 4, 5, 6, 7]
print(list1)

# list can contain multiple type of elements

multipleElementList = [2, 3, 'Test', False, 4.5]
print(multipleElementList)

# length of list
print(len(multipleElementList))
print(len(list1))

# indexing
print(list1[0])
print(list1[-1])

# slicing
print(list1[:])
print(list1[1:])
print(list1[2:5])
print(list1[:3])
print(list1[::2])
print(list1[1:6:2])
print(list1[:4:2])
print(list1[::-1])
print(list1[-3:])
print(list1[-3::-1])
print(list1[-3:-1])

# slicing creates a new list
new_list = list1[:]
list1.append(8)
print(list1)
print(new_list)

# concatenation creates a new list
list2 = [9, 10, 11]
concatList = list1 + list2
print(concatList)
list2.append(12)
print(concatList)
print(list2)
print(list1)

# list are mutable
list1[0] = 1
print(list1)

# append function
list1.append(9)
print(list1)

# reverse list
list1.reverse()
print(list1)

# remove
list1.remove(9)
print(list1)

# pop
element = list1.pop()
print(element)
print(list1)
element1 = list1.pop(3)
print(element1)
print(list1)

# sort
list4 = [4, 3, 5, 10, 1, 6]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
stringList = ["Jan", "Feb", "Mar", "Apr"]
print(stringList.sort())
print(stringList)

# nesting of list
nestlist1 = [1, 2, 3]
nestlist2 = [4, 5, 6]
nestlist3 = [7, 8, 9]
list5 = [nestlist1, nestlist2, nestlist3]
print(list5)

# indexing nested list
print(list5[0])
print(list5[1][2])

# first comprehension - basic
firstCol = [row[0] for row in list5]
print(firstCol)

# count
print(firstCol.count(4))
print(firstCol.count(9))

# extend
list6 = [1, 2, 3]
list7 = [4, 5, 6]
list6.extend(list7)
print(list6)
list6.append(list7)
print(list6)

# index
print(list6.index(5))

# insert
list6.insert(4, 10)
print(list6)
