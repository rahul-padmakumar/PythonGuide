print([x for x in range(10, 20)])

# squaring

print([x**2 for x in range(5, 10)])

print([x for x in range(10, 20) if x % 2 == 0])

print([x if x % 2 == 0 else 0 for x in range(10, 20)])

# double loop with list comprehension

print([x * y for x in range(1, 4) for y in [1, 10, 100]])
