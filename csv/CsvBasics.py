import csv


data = open("example.csv", encoding="utf-8")
csv_file = csv.reader(data)
data_lines = list(csv_file)
print(list(map(lambda line: line[3], data_lines)))

write_file = open("example_1.csv", mode="w", newline="")
writer = csv.writer(write_file, delimiter=",")
writer.writerow(['a', 'b', 'c'])
writer.writerows([['1', '2', '3'], ['4', '5', '6']])
write_file.close()

write_file = open("example_1.csv", mode="a", newline="")
writer = csv.writer(write_file, delimiter=",")
writer.writerow(['7', '8', '9'])
write_file.close()




