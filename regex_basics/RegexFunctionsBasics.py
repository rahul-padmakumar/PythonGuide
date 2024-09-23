import re

st1 = "Hello my land phone and other phones are not working"
match = re.search("phone", st1)
print(match)
print(match.string)
print(match.start())
print(match.end())
print(match.group())
print(match.span())


matches = re.findall("phone", st1)
print(matches)

for s in re.finditer("phone", st1):
    print(s.group())

st2 = "His phone number is 123-123-1234"
match1 = re.search(r'\d{3}-\d{3}-\d{4}', st2)
print(match1.group())

st2 = "His phone number is (123)-123-1234"
match1 = re.search(r'\(\d{3}\)-\d{3}-\d{4}', st2)
print(match1.group())
