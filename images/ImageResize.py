from PIL import Image

image = Image.open("example.jpg")
resized_image = image.resize((3000, 500))
resized_image.show()
