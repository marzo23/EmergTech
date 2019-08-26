from tkinter import *
import PIL
from PIL import Image, ImageDraw
import os
import uuid

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join(os.path.dirname(__file__),"key.json") 

def get_text():
    import os, io
    from google.cloud import vision

    vision_client = vision.ImageAnnotatorClient()   
    global image_number
    img = f'{image_number}.png'
    file_name = os.path.join(os.path.dirname(__file__),img) 

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description

def store_firebase(txt, img):
    import pyrebase
    import os

    config = {
    "apiKey": "AIzaSyA2gbZmPeu536huxGq6TWGFlwZYZSyo-P8",
    "authDomain": "project-1010073080742.firebaseapp.com",
    "databaseURL": "https://pruebafirebase-8f87b.firebaseio.com",
    "storageBucket": "pruebafirebase-8f87b.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child(img).put(img)
    img_url = storage.child(img).get_url(None)
    print(img_url)
    db = firebase.database()
    data = {"txt": txt, "img": img_url }
    db.child("raspberry").push(data)
    #users = db.child("raspberry").get()
    #print(users.val()) 

def save():
    global image_number
    filename = f'{image_number}.png'   # image_number increments by 1 at every save
    image1.save(filename)
    txt= get_text()
    store_firebase(txt, filename)

    image_number = str(uuid.uuid4())


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=5)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=5)
    lastx, lasty = x, y


root = Tk()

lastx, lasty = None, None
image_number = str(uuid.uuid4())

cv = Canvas(root, width=640, height=480, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()
