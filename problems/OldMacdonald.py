
def mac_donald(name):
    if len(name) == 0:
        return ''
    altered_name = name[0].upper()
    if len(name) >= 4:
        altered_name = altered_name + name[1:3] + name[3].upper()
        if len(name) > 4:
            altered_name = altered_name + name[4:]
    else:
        altered_name = altered_name + name[1:]
    return altered_name


print(mac_donald('macdonald'))
print(mac_donald('abcd'))
print(mac_donald('cat'))
print(mac_donald('re'))
print(mac_donald('a'))
print(mac_donald(''))