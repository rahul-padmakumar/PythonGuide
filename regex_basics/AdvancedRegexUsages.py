import re

# Groups

match1 = re.search(r'(\d{3})-(\d{3})-(\d{4})', '123-123-1234')
print(match1.group())
print(match1.group(1))
print(match1.group(2))
print(match1.group(3))

# OR operator

match2 = re.search(r'man|woman', 'Super man is a comic hero')
print(match2)
match2 = re.search(r'man|woman', 'Super woman is a comic heroine')
print(match2)

# Wildcard operator
match3 = re.findall(r'.at', "The cat hit the hat with the bat")
print(match3)
match4 = re.findall(r'.ught', 'I brought the fish he caught')
print(match4)
match4 = re.findall(r'..ught', 'I brought the fish he caught')
print(match4)
match4 = re.findall(r'...ught', 'I brought the fish he caught')
print(match4)
match5 = re.findall(r'\S+ught', 'I brought the fish he caught')
print(match5)

# Starts or ends with
match6 = re.findall(r'\d$', '123 ends with 3')
print(match6)
match7 = re.findall(r'\d$', '123 ends with a')
print(match7)
match8 = re.findall(r'^\d', '123 ends with 3')
print(match8)
match9 = re.findall(r'^\d$', 'abc ends with c')
print(match9)

# Exclusion
match10 = re.findall(r'[^\d]', "My number is 1234")
print(match10)
match11 = re.findall(r'[^\d]+', "My number is 1234")
print(match11)

# punctuation removal with exclusion
match12 = re.findall(r'[^?!. ]+', 'How to remove punctuation from Alas! I. ?')
print(match12)
print(" ".join(match12))

# Brackets for grouping
match13 = re.findall(r'[\w]+-[\w]+', "I have long-word in my sentence")
print(match13)

# parenthesis for multiple option
for i in re.finditer(r'(basket|foot)ball', 'I play basketball, football and volleyball'):
    print(i.group())

print(re.findall(r'(basket|foot)ball', 'I play basketball, football and volleyball'))
