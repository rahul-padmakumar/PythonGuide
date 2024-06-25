print("Python {}!".format("rocks"))

print("{} {}!".format("Python", "rocks"))

print("{1} {0}!".format("rocks", "Python")) # Inserted objects can be called by index position:

print("{b} {a}!".format(a="rocks", b="Python")) # Inserted objects can be assigned keywords:

print("{a}={a}".format(a="hello")) # inserted objects can be reused, avoiding duplication:

# Specify alignment with formatting default alignment left for strings, right for numbers
print("{0:8}|{1:12}".format("Label", "Value"))
print("{0:8}|{1:12}".format("x", 1))
print("{0:8}|{1:12}".format("y", 2))

# alignment can be specified with < for left, > for right, ^ for center
print("{0:<8}|{1:^12}".format("Label", "Value"))
print("{0:<8}|{1:^12}".format("x", 1))
print("{0:<8}|{1:^12}".format("y", 2))

# alignment can be specified with < for left, > for right, ^ for center
print("{0:^8}|{1:>12}".format("Label", "Value"))
print("{0:^8}|{1:>12}".format("x", 1))
print("{0:^8}|{1:>12}".format("y", 2))

# precede the alignment operator with a padding character
print("{0:=^8}|{1:.>12}".format("Label", "Value"))
print("{0:=^8}|{1:.>12}".format("x", 1))
print("{0:=^8}|{1:.>12}".format("y", 2))

# floating point number formatting
# {a:b.cf} -> a: number in format b: minimum number of digits c: number of digits after decimal point
print("{0:1.3f}".format(10.345678))
print("{a:10.4f}".format(a=10.3456789))





