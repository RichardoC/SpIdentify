from PIL import Image
import os

folderNames = {"Spider", "NonSpider", "BigSpiders", "topdown"}
thresholdLow = 150
thresholdHigh = 255

for folderName in folderNames :
	if (not os.path.isdir('Edited' + folderName)) :
		os.makedirs('Edited' + folderName)

	for fileName in os.listdir( folderName) :
		try:
			image = Image.open(folderName + "/"+fileName)
			mask=image.convert("L")

			mask = mask.point(lambda i: i < thresholdLow and thresholdHigh)
			mask.save("Edited" + folderName +"/"+fileName)
		except:
			print "fucked",fileName
