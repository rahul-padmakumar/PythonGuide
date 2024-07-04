file = open('file1.txt', mode='w')
file.write("one line\n")
file.write("second line\n")
file.close()

file = open('file1.txt')
fileContent = file.read()
print(fileContent)
file.close()

file = open('file1.txt', mode='r')
fileContent = file.readline()
print(fileContent)
file.close()


# using with file closing not mandatory
with open('file1.txt', mode='r+') as file1:
    print(file1.readlines())
    file1.write('Third line')
    file1.seek(0)
    print(file1.readlines())


# using with file closing not mandatory
with open('file2.txt', mode='w+') as file2:
    print(file2.readlines())
    file2.write('Third line')
    file2.seek(0)
    print(file2.readlines())

# using with file closing not mandatory
with open('file2.txt', mode='a+') as file2:
    file2.write('\nFourth line')

# using with file closing not mandatory
with open('file2.txt') as file2:
    print(file2.readlines())

# iterating through lines n file
for lines in open('file2.txt'):
    print(lines)

