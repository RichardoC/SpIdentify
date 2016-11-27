from PIL import Image
import os
import matplotlib.pyplot as plt
%matplotlib inline

folderNames = {"Spider", "NonSpider", "BigSpiders", "topdown"}
thresholdLow = 150
thresholdHigh = 255

for folderName in folderNames :
    if (not os.path.isdir('Edited' + folderName)) :
        os.makedirs('Edited' + folderName)
    count = 0
    for fileName in os.listdir(folderName) :
        image = Image.open(folderName + "/"+fileName)
        lum_img = np.array(image)
        try:
            plt.imshow(lum_img[:,:,0],cmap='bwr')
            plt.savefig("Edited" + folderName +"/"+fileName,dpi=50)
        except Exception:
            print 'skip'