<<<<<<< HEAD
HELLO = None
try:
    from PIL import Image
except:
    HELLO = 'image failed.'
=======
import filetester
>>>>>>> 1f355195d1875b182511c7bec29f88f4131628d6

def user_name():
    return input("Insert user name?:  ")
def chat():
    return input("Enter message: ")
def emoji():
    return input("Insert an emoji: ")
def picture():
<<<<<<< HEAD
    if HELLO != 'image failed':
        img = Image.open(input("Insert an image: "))
        img.show()
=======
    filetester.checker(input("Insert an image: "))
>>>>>>> 1f355195d1875b182511c7bec29f88f4131628d6
def file():
    return input("Insert a file: ")
def nickname():
    return input("Insert nickname?: ")
