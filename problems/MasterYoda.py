
def master_yoda(data):
    data_splits = data.split(' ')
    return " ".join(data_splits[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready'))