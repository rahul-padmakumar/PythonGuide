
def mac_donald(name):
    if len(name) > 3:
        altered_name = name[:3].capitalize() + name[3:].capitalize()
    else:
        altered_name = name.capitalize()
    return altered_name


print(mac_donald('macdonald'))
print(mac_donald('abcd'))
print(mac_donald('cat'))
print(mac_donald('re'))
print(mac_donald('a'))
print(mac_donald(''))