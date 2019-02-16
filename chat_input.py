HELLO = None
try:
    from PIL import Image
except:
    HELLO = 'image failed.'

def user_name():
    return input("Insert user name?:  ")
def chat():
    return input("Enter message: ")
def emoji():
    return input("Insert an emoji: ")
def picture():
    if HELLO != 'image failed':
        img = Image.open(input("Insert an image: "))
        img.show()
def file():
    return input("Insert a file: ")
def nickname():
    return input("Insert nickname?: ")
