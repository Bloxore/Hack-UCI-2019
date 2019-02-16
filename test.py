from PIL import Image
img = Image.open('kirby.png')
img.show()
print(img.format)
print(img.mode)