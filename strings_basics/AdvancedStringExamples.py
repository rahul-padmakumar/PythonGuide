
# Casing

print("hello world".capitalize())

print("hello world".title())

print("hello world".upper())

print("hello world".lower())

# Location and counting

print("hello world".count('o'))

print("hello world".find('o'))

# Formatting

print("hello world".center(20, "*"))
print("hello\tworld".expandtabs())

# check

print("hello123".isalnum())
print("hello 123".isalnum())
print("hello123".isalpha())
print("hello".isalpha())
print("Hello World".istitle())
print("hello world".islower())
print("HELLO".isupper())
print("12345".isdigit())
print("    ".isspace())
print("Hello World".endswith('d'))

# Built in Regex

print("Hello world".split(' '))
print("Hello world".partition(' '))
