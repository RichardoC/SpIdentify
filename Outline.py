from PIL import Image
import os

folderNames = {"Images/Spider", "Images/NonSpider", "Images/BigSpiders", "Images/topdown", "Images/Memes"}
thresholdLow = 150
thresholdHigh = 255

for folderName in folderNames :
	if (not os.path.isdir('EditedOutline' + folderName)) :
		os.makedirs('EditedOutline' + folderName)

	for fileName in os.listdir(folderName) :
		try:
			image = Image.open(folderName + "/"+fileName)
			mask=image.convert("L")

			mask = mask.point(lambda i: i < thresholdLow and thresholdHigh)
			mask.save("EditedOutline" + folderName +"/"+fileName)
		except:
			print "fucked",fileName
