from PIL import Image
import os

for fileName in os.listdir('Spider') :
    image = Image.open("Spider/"+fileName)
    mask=image.convert("L")
    
    mask = mask.point(lambda i: i < 150 and 255)
    mask.save("Spider/"+fileName+"Edited.jpg")
