from PIL import Image
import os

folderName = "Spider"
thresholdLow = 150
thresholdHigh = 255

if (not os.path.isdir('Edited' + folderName)) :
	os.makedirs('Edited' + folderName)

for fileName in os.listdir( folderName) :
    image = Image.open(folderName + "/"+fileName)
    mask=image.convert("L")
    
    mask = mask.point(lambda i: i < thresholdLow and thresholdHigh)
    mask.save("Edited" + folderName +"/"+fileName)
