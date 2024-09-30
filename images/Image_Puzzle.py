from PIL import Image

word_image = Image.open("word_matrix.png").convert("RGBA")
mask_image = Image.open("mask.png").convert("RGBA")
mask_image.putalpha(200)
resized_mask = mask_image.resize((word_image.width, word_image.height))
word_image.paste(resized_mask, (0, 0), resized_mask)
word_image.show()
