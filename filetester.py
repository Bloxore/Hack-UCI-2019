from pathlib import Path
try:
    from PIL import Image
except:
    def checker(my_file):
        if my_file.is_file():
            img = Image.open(my_file)
            img.show()
        else:
            print("file does not exist")