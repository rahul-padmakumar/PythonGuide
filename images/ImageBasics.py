from PIL import Image

image = Image.open("example.jpg")
print(image.format)
print(image.format_description)
print(image.size)
print(image.filename)

image.show()
