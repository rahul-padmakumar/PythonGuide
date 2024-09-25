import zipfile

with open('file_zip_1.txt', 'w+') as file1:
    file1.write("I am file one")

with open('file_zip_2.txt', 'w+') as file2:
    file2.write("I am file two")

zipfile1 = zipfile.ZipFile(file="Zip_1.zip", mode="w")
zipfile1.write('file_zip_1.txt', compress_type=zipfile.ZIP_DEFLATED)
zipfile1.write('file_zip_2.txt', compress_type=zipfile.ZIP_DEFLATED)
zipfile1.close()

extracted_file = zipfile.ZipFile(file="Zip_1.zip", mode="r")
extracted_file.extractall("extracted_contents")



