import pypdf

reader = pypdf.PdfReader("Working_Business_Proposal.pdf")
print(len(reader.pages))
page1 = reader.get_page(0)
print(page1.extract_text())

pdf_writer = pypdf.PdfWriter()
pdf_writer.add_page(page1)
pdf_writer.add_page(reader.get_page(1))
output_file = open("pdf_example_1.pdf", "wb")
pdf_writer.write(output_file)
output_file.close()
