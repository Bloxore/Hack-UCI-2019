from PIL import Image

def user_name():
    return input("Insert user name?:  ")
def chat():
    return input("Enter message: ")
def emoji():
    return input("Insert an emoji: ")
def picture():
    img = Image.open(input("Insert an image: "))
    img.show()
def file():
    return input("Insert a file: ")
def nickname():
    return input("Insert nickname?: ")