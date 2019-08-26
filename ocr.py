import os, io
from google.cloud import vision

vision_client = vision.ImageAnnotatorClient()   

file_name = os.path.join(os.path.dirname(__file__),'image_1.png') 

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = vision_client.text_detection(image=image)
texts = response.text_annotations
print('Texts:'+texts[0].description)



