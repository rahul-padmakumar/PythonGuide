from PIL import Image

blue_image = Image.open("blue_color.png").convert("RGBA")
blue_image.putalpha(128)
blue_image.show()

red_image = Image.open("red_color.jpg").convert("RGBA")
red_image.putalpha(128)
blue_image.paste(red_image, (0, 0), red_image)
blue_image.convert("RGB").save("purple.jpg")