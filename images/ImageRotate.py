from PIL import Image

image = Image.open("example.jpg")
image.rotate(270).show()
