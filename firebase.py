import pyrebase
import time

config = {
  "apiKey": "AIzaSyA2gbZmPeu536huxGq6TWGFlwZYZSyo-P8",
  "authDomain": "project-1010073080742.firebaseapp.com",
  "databaseURL": "https://pruebafirebase-8f87b.firebaseio.com",
  "storageBucket": "project-1010073080742.appspot.com",
  #"serviceAccount": "C:\\Users\\L440\\Documents\\trash\\firebase.json"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.child("users")
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
users = db.child("users").get()
print(users.val()) 