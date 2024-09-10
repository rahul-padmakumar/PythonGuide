
def paper_doll(data):
    result = ''
    for ch in data:
        result = result + (ch * 3)
    return result


print(paper_doll('hello'))
print(paper_doll('Mississippi'))