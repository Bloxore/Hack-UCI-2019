from pathlib import Path
from PIL import Image

def checker(my_file):
    if my_file.is_file():
        img = Image.open(my_file)
        img.show()
    else:
        print("file does not exist")