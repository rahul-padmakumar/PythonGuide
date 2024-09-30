import csv
import pypdf
import re

ip_file = open("find_the_link.csv", "r")
content = list(csv.reader(ip_file))


link = ""
for i in range(len(content)):
    for j in range(len(content[i])):
        if i == j:
            link = link + content[i][j]

pdf_reader = pypdf.PdfReader("Find_the_Phone_Number.pdf")
for i in range(len(pdf_reader.pages)):
    match = re.search(r'\d{3}.\d{3}.\d{4}', pdf_reader.get_page(i).extract_text())
    if match:
        print(match.group())
        break
