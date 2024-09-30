from PIL import Image

image = Image.open("example.jpg")
print(image.format)

x = image.width / 2 - 200
w = x + 400
y = image.height / 2
h = image.height
cropped_image = image.crop((x, y, w, h))
image.paste(cropped_image, (0, 0))
image.show()
